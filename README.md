# fragmingham-pro
This is the Jupyter Notebook and the Dataset for the mentioned Classification Predictive Modeling
About the dataset:
The "Framingham" dataset is publically available on the Kaggle website, and it is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has 10-year risk of future coronary heart disease (CHD).The dataset provides the patients’ information. It includes over 4,240 records and 15 attributes.

Objective: To build a classification model that predicts Ten Year Coronary Heart Disease in a subject.
I have performed the following steps:
Read the file and displayed its columns.
Handled missing values, Outliers and Duplicate Data.
Calculated basic statistics of the data (count, mean, std, etc), did exploratory analysis and described my observations.
Resampled the imbalanced dataset by oversampling the positive cases.
Selected columns that will probably be important to predict heart disease.
Created training and testing sets (using 60% of the data for the training and reminder for testing) and scaled the data using MinMaxScaler.
Built 5 different machine learning models to predict TenYearCHD:
Logistic Regression - 67.56% Accuracy
