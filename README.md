# Coloring molecules for hERG blockade

By combining a Message-Passing Graph Neural Network (MPGNN) and a Forward fully connected Neural Network (FNN) with an integrated gradients explainable artificial intelligence (XAI) method, the authors developed MolGrad and tested it on a number of ADME predictive tasks. MolGrad incorporates explainable features to facilitate interpretation of the predictions.In this model, they train MolGrad with a dataset of hERG channel blockers/non-blockers to predict the cardiotoxicity of small molecules (IC50 in hERG blockade).

## Identifiers

* EOS model ID: `eos43at`
* Slug: `molgrad-herg`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Experimental value`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: pIC50 of hERG inhibition

## References

* [Publication](https://pubs.acs.org/doi/10.1021/acs.jcim.0c01344)
* [Source Code](https://github.com/josejimenezluna/molgrad/)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos43at)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos43at.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos43at) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://pubs.acs.org/doi/10.1021/acs.jcim.0c01344) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a AGPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!