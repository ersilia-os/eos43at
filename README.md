# Coloring molecules for hERG blockade

Estimates blockade of the hERG potassium channel, a liability associated with QT prolongation and arrhythmia, on the pIC50 scale. Jimenez-Luna and co-workers trained message-passing graph neural networks across four ADME and safety endpoints, coupling them with integrated-gradients attribution so individual atoms can be coloured by their contribution to a prediction. This endpoint draws on 6,993 compounds with reported nanomolar IC50 values. The colouring explains what the network learned; it does not by itself establish that the prediction is correct.

This model was incorporated on 2021-10-19.Last packaged on 2025-09-17.

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
- **Interpretation:** Predicted pIC50 for hERG channel blockade, where higher values indicate stronger inhibition.

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
- **Environment Size (Mb):** `2431`
- **Image Size (Mb):** `2375.96`

**Computational Performance (seconds):**
- 10 inputs: `28.37`
- 100 inputs: `19.93`
- 10000 inputs: `192.97`

### References
- **Source Code**: [https://github.com/josejimenezluna/molgrad/](https://github.com/josejimenezluna/molgrad/)
- **Publication**: [https://doi.org/10.1021/acs.jcim.0c01344](https://doi.org/10.1021/acs.jcim.0c01344)
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
