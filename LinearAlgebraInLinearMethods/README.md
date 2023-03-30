# TASK. Predicting gas production at wells

## Contents
[1. Deskription of task](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Deskription-of-task)
[2. What problem are we solving?](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#What-problem-are-we-solving?)
[3. Short information about data](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Short-information-about-data)
[4. Stages of work on the task](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Stages-of-work-on-the-task)
[5. Result](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Result)
[6. Conclusions](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Conclusions)

### Deskription of task
It's necessary to predict a gas production at wells.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Contents)

### What problem are we solving?
We need to build the best linear regression model predicting a gas production.

**What we practice**
- Linear regression models are built using the OLS;
- Features are searched for that are highly correlated with each other and with the target feature;
- Special attention is paid to overfitting models and how regularization eliminates overfitting of models.

### Short information about data
- MATH-ML. Practice.ipynb - notebook file with code;
- unconv.csv - dataset with data of wells.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Contents)

### Stages of work on the task
- reading data;
- linear regression by OLS;
- polynomial regression;
- regression by regularization on polynomial features.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Contents)

### Result
There were built 5 linear regression's models: usual linear regression, linear regression on polynomial features (polynomial regression), linear regression by Lasso-regularization (L1-regularization), linear regression by Ridge-regularization (L2-regularization) and linear regression by ElasticNet-regularization (L1-L2-regularization). Quality of models was measured by mean absolute procentile error and R2-score metrics. Results show that the best model is linear regression by ElaticNet-regularization.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Contents)

### Conclusions
- We understood the role of the OLS in building a linear regression model;
- We understood the difference between collinearity and multicollinearity;
- We found out what relationship exists between the determinant of a matrix built from features, the linear dependence of features among themselves, as well as with the target variable, and how they affect the prediction of the model;
- We saw what regularization does to prediction error from a mathematical point of view.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Contents)