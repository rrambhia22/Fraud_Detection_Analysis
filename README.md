# Application Link

https://share.streamlit.io/rrambhia22/rbs-ml-e2e-challenge/develop/model_deployment/FraudDetection_Deploy.py



# Problem Statement
Online Payments Fraud Detection.

The objective is to predict/detect the fraud transaction that happens through the online payment transactions. This would help in identifying the fraud transactions that are taking place over the online transactions.



# Dataset Source
https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset




# Initial Analysis
For the initial analysis of the dataset descriptive analysis, exploratory data analysis, statistical analysis, and data visualizations is performed which gives a better understanding of the data.

Data cleaning being an important step in the data analysis process, quality of data is analyzed before performing the model building phase. 

Data visualization is performed in Tableau in order to gain insights from the dataset and determine various trends and patterns.




# Model Training
Various machine learning models are implemented in order to identify the best fit model. In order to built the machine learning model, pre modeling steps are performed including correlation plot, feature selection, and label encoding. 

Correlation plot gives understanding about the relationship between each of the variables which helps in determining the important features or independent variables that need to be considered in order to predict the dependent variable. 

Automatic feature selection and extraction is performed that selects the important features from the dataset that can be provided for training of the model. 

The important features selected and extracted is done using the featurewiz library in Python and these features are then given to the model as the independent variables for model training. 

Label Encoding is performed on the categorical column to have a numerical data type as the column needs to be provided to the model for training.




# Model Overview
The various machine learning models implemented are Logistic Regression, Random Forest Classifier, XGBoost Classifier, and Decision Tree Classifier. 

Since the data was clean having no errors, the model accuracy was upto 100% but the confusion matrix displayed gave an overview of the correctly classified class and incorrectly classified class labels. Thus, based on the confusion matrix analysis, Random Forest Classifier and XGBoost Classifier could correctly classify the fraud detections majority of the time. 

Hence, the best fit model could be either Random Forest Classifer or XGBoost Classifier. 




# Model Packaging
For model packaging, Random Forest Classifier is considered for detecting the fraud transaction. The model is loaded and saved to a pickle file which will be used anytime while testing the data for fraud detection. 

After the model is saved using pickle library in Python, a GUI or app is developed to predict the fraud transaction for new input data. 

This is done using the Streamlit library in Python. An app is developed which predicts whether a particular transaction is a fraud transaction or not.




# Model Deployment
The model is deployed using the Streamlit Cloud.
