import dgl
import numpy as np
import rdkit
import torch
from rdkit.Chem import GetPeriodicTable, MolFromSmiles
from rdkit.Chem.Crippen import MolLogP
from rdkit.Chem.Descriptors import MolWt
from rdkit.Chem.inchi import MolFromInchi
from rdkit.Chem.Lipinski import NumHDonors
from rdkit.Chem.rdMolDescriptors import CalcTPSA
from rdkit.Chem.rdmolops import AddHs
from torch.utils.data import Dataset

ATOM_TYPES = [
    "Ag","As","B","Br","C","Ca","Cl","F","H","I","K","Li","Mg","N","Na","O","P","S","Se","Si","Te","Zn","Sb","Pt","Gd","Sn",
]

CHIRALITY = [
    rdkit.Chem.rdchem.ChiralType.CHI_OTHER,
    rdkit.Chem.rdchem.ChiralType.CHI_TETRAHEDRAL_CCW,
    rdkit.Chem.rdchem.ChiralType.CHI_TETRAHEDRAL_CW,
    rdkit.Chem.rdchem.ChiralType.CHI_UNSPECIFIED,
]

HYBRIDIZATION = [
    rdkit.Chem.rdchem.HybridizationType.OTHER,
    rdkit.Chem.rdchem.HybridizationType.S,
    rdkit.Chem.rdchem.HybridizationType.SP,
    rdkit.Chem.rdchem.HybridizationType.SP2,
    rdkit.Chem.rdchem.HybridizationType.SP3,
    rdkit.Chem.rdchem.HybridizationType.SP3D,
    rdkit.Chem.rdchem.HybridizationType.SP3D2,
    rdkit.Chem.rdchem.HybridizationType.UNSPECIFIED,
]

BOND_TYPES = [
    rdkit.Chem.rdchem.BondType.SINGLE,
    rdkit.Chem.rdchem.BondType.DOUBLE,
    rdkit.Chem.rdchem.BondType.TRIPLE,
    rdkit.Chem.rdchem.BondType.AROMATIC,
]

BOND_STEREO = [
    rdkit.Chem.rdchem.BondStereo.STEREONONE,
    rdkit.Chem.rdchem.BondStereo.STEREOANY,
    rdkit.Chem.rdchem.BondStereo.STEREOZ,
    rdkit.Chem.rdchem.BondStereo.STEREOE,
]

def empty_graph():
    atom_scalar_dim = 11
    atom_feat_dim = len(ATOM_TYPES) + len(CHIRALITY) + len(HYBRIDIZATION) + atom_scalar_dim
    bond_scalar_dim = 2
    bond_feat_dim = len(BOND_TYPES) + len(BOND_STEREO) + bond_scalar_dim
    g = dgl.DGLGraph()
    g.set_n_initializer(dgl.init.zero_initializer)
    g.set_e_initializer(dgl.init.zero_initializer)
    g.ndata["feat"] = torch.empty((0, atom_feat_dim), dtype=torch.float32)
    g.edata["feat"] = torch.empty((0, bond_feat_dim), dtype=torch.float32)
    return g

def mol_to_dgl(mol):
    if mol is None or mol.GetNumAtoms() == 0:
        return empty_graph()
    g = dgl.DGLGraph()
    g.add_nodes(mol.GetNumAtoms())
    g.set_n_initializer(dgl.init.zero_initializer)
    g.set_e_initializer(dgl.init.zero_initializer)
    atom_features = []
    pd = GetPeriodicTable()
    for atom in mol.GetAtoms():
        atom_feat = []
        atom_type = [0] * len(ATOM_TYPES)
        sym = atom.GetSymbol()
        if sym in ATOM_TYPES:
            atom_type[ATOM_TYPES.index(sym)] = 1
        chiral = [0] * len(CHIRALITY)
        tag = atom.GetChiralTag()
        if tag in CHIRALITY:
            chiral[CHIRALITY.index(tag)] = 1
        hybrid = [0] * len(HYBRIDIZATION)
        hyb = atom.GetHybridization()
        if hyb in HYBRIDIZATION:
            hybrid[HYBRIDIZATION.index(hyb)] = 1
        ex_valence = atom.GetExplicitValence()
        charge = atom.GetFormalCharge()
        degree = atom.GetDegree()
        valence = atom.GetImplicitValence()
        aromatic = int(atom.GetIsAromatic())
        ex_hs = atom.GetNumExplicitHs()
        im_hs = atom.GetNumImplicitHs()
        rad = atom.GetNumRadicalElectrons()
        ring = int(atom.IsInRing())
        try:
            mass = pd.GetAtomicWeight(sym)
        except Exception:
            mass = 0.0
        try:
            vdw = pd.GetRvdw(sym)
        except Exception:
            vdw = 0.0
        atom_feat.extend(atom_type)
        atom_feat.extend(chiral)
        atom_feat.append(ex_valence)
        atom_feat.append(charge)
        atom_feat.extend(hybrid)
        atom_feat.append(degree)
        atom_feat.append(valence)
        atom_feat.append(aromatic)
        atom_feat.append(ex_hs)
        atom_feat.append(im_hs)
        atom_feat.append(rad)
        atom_feat.append(ring)
        atom_feat.append(mass)
        atom_feat.append(vdw)
        atom_features.append(atom_feat)
    for bond in mol.GetBonds():
        g.add_edge(bond.GetBeginAtomIdx(), bond.GetEndAtomIdx())
    g.ndata["feat"] = torch.FloatTensor(atom_features)
    bond_features = []
    for bond in mol.GetBonds():
        bond_feat = []
        bond_type = [0] * len(BOND_TYPES)
        if bond.GetBondType() in BOND_TYPES:
            bond_type[BOND_TYPES.index(bond.GetBondType())] = 1
        bond_stereo = [0] * len(BOND_STEREO)
        if bond.GetStereo() in BOND_STEREO:
            bond_stereo[BOND_STEREO.index(bond.GetStereo())] = 1
        bond_feat.extend(bond_type)
        bond_feat.extend(bond_stereo)
        bond_feat.append(float(bond.GetIsConjugated()))
        bond_feat.append(float(bond.IsInRing()))
        bond_features.append(bond_feat)
    if len(bond_features) == 0:
        bond_scalar_dim = 2
        bond_feat_dim = len(BOND_TYPES) + len(BOND_STEREO) + bond_scalar_dim
        g.edata["feat"] = torch.empty((0, bond_feat_dim), dtype=torch.float32)
    else:
        g.edata["feat"] = torch.FloatTensor(bond_features)
    return g

def get_global_features(mol):
    if mol is None:
        return np.zeros(4, dtype=np.float32)
    mw = MolWt(mol)
    tpsa = CalcTPSA(mol)
    logp = MolLogP(mol)
    n_hdonors = NumHDonors(mol)
    desc = np.array([mw, tpsa, logp, n_hdonors], dtype=np.float32)
    return desc

class GraphData(Dataset):
    def __init__(self, strs, labels=None, mask=None, train=True, add_hs=True, inchi=True):
        self.strs = strs
        self.train = train
        if self.train:
            self.labels = np.array(labels, dtype=np.float32)
            self.mask = np.array(mask, dtype=np.bool_)
            assert len(self.strs) == len(self.labels)
        self.add_hs = add_hs
        if inchi:
            self.read_mol_f = MolFromInchi
        else:
            self.read_mol_f = MolFromSmiles

    def __getitem__(self, idx):
        mol = self.read_mol_f(self.strs[idx])
        if mol is None:
            g = empty_graph()
            gf = get_global_features(None)
            if self.train:
                return g, gf, self.labels[idx, :], self.mask[idx, :]
            else:
                return g, gf
        if self.add_hs:
            try:
                mol = AddHs(mol, addCoords=False)
            except Exception:
                g = empty_graph()
                gf = get_global_features(None)
                if self.train:
                    return g, gf, self.labels[idx, :], self.mask[idx, :]
                else:
                    return g, gf
        g = mol_to_dgl(mol)
        gf = get_global_features(mol)
        if self.train:
            return g, gf, self.labels[idx, :], self.mask[idx, :]
        else:
            return g, gf

    def __len__(self):
        return len(self.strs)

def collate_pair(samples):
    graphs_i, g_feats, labels, masks = map(list, zip(*samples))
    batched_graph_i = dgl.batch(graphs_i)
    return (
        batched_graph_i,
        torch.as_tensor(g_feats),
        torch.as_tensor(labels),
        torch.as_tensor(masks),
    )

def collate_pair_prod(samples):
    graphs_i, g_feats = map(list, zip(*samples))
    return dgl.batch(graphs_i), torch.as_tensor(g_feats)
