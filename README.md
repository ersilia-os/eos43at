# Coloring molecules for hERG blockade

By combining a Message-Passing Graph Neural Network (MPGNN) and a Forward fully connected Neural Network (FNN) with an integrated gradients explainable artificial intelligence (XAI) method, the authors developed MolGrad and tested it on a number of ADME predictive tasks. MolGrad incorporates explainable features to facilitate interpretation of the predictions.In this model, they train MolGrad with a dataset of hERG channel blockers/non-blockers to predict the cardiotoxicity of small molecules (IC50 in hERG blockade).

This model was incorporated on 2021-10-19.


## Information
### Identifiers
- **Ersilia Identifier:** `eos43at`
- **Slug:** `molgrad-herg`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `hERG`, `Toxicity`, `Cardiotoxicity`, `Chemical graph model`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** pIC50 of hERG inhibition

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| pic50 | float | high | Inhibition of hERG |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos43at](https://hub.docker.com/r/ersiliaos/eos43at)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos43at.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos43at.zip)

### Resource Consumption
- **Model Size (Mb):** `6`
- **Environment Size (Mb):** `2430`
- **Image Size (Mb):** `2358.92`

**Computational Performance (seconds):**
- 10 inputs: `27.82`
- 100 inputs: `19.41`
- 10000 inputs: `771.39`

### References
- **Source Code**: [https://github.com/josejimenezluna/molgrad/](https://github.com/josejimenezluna/molgrad/)
- **Publication**: [https://pubs.acs.org/doi/10.1021/acs.jcim.0c01344](https://pubs.acs.org/doi/10.1021/acs.jcim.0c01344)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [AGPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos43at
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos43at
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
