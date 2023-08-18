# Python package for implementing ensemble methods of rank-based trees
* Available on PyPI.org: https://pypi.org/project/ranktreeEnsemble/
* The R version of this package is also available at R CRAN: https://CRAN.R-project.org/package=ranktreeEnsemble

## Authors
Ruijie Yin (ruijieyin428@gmail.com), Chen Ye (cxy364@miami.edu) and Min Lu (m.lu6@umiami.edu)

## Reference
Min Lu, Ruijie Yin and Steven X. Chen. Ensemble Methods of Rank-Based Trees for Single Sample Classification with Gene Expression Profiles. (Submitted)


## Getting Started

### Dependencies

#### For Python package:

* Prerequisites: pandas, sklearn, numpy, shap-hypetune, lightgbm
* Python (>= 3.6.0)

### Installation:
#### In a Python console, type:
pip install ranktreeEnsemble


### Examples:
* Build a Random Rank Forest with Variable Importance:
```
from ranktreeEnsemble.data.dataPrep import *
from ranktreeEnsemble.Method.ranktreeMethod import *
import pandas as pd

tnbc = pd.read_csv("data/tnbc.csv")

model = rforest(tnbc.drop(columns=['subtype']).head(100), tnbc["subtype"].head(100))
# get feature importance scores:
model.feature_importances_

# pair() to convert continuous variables to binary ranked pairs:
datp = pair(tnbc.iloc[100:111,:-1])
print(datp)
model.predict(datp)
```

* Build a Boosting with LogitBoost Cost model with Variable Importance:
```
model = rboost(tnbc.drop(columns=['subtype']).head(100), tnbc["subtype"].head(100))
# get feature importance scores:
model.feature_importances_
# Build a Boosting with LogitBoost Cost model with forward stepwise feature selection:
model_rfa = rboost_rfa(tnbc.drop(columns=['subtype']).head(100), tnbc["subtype"].head(100))
# Build a Boosting with LogitBoost Cost model with backward stepwise feature selection:
model_rfe = rboost_rfe(tnbc.drop(columns=['subtype']).head(100), tnbc["subtype"].head(100))
	
```


## Version History
* 0.1.3
    * Edited the description, and changed the structure of the package. 

* 0.1.2
    * Added functions for forward stepwise feature selection,  backward stepwise feature selection.

* 0.1.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details



