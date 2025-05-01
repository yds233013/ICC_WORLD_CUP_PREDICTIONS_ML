# ICC_World_Cup_2023_Prediction🏏
## Course Project 3 of Data Mining Course

* This Project aims to predict:
  1. Predicting the batsman who will score most runs/ hit most sixes/ make most centuries in the tournament.
  2. Predicting the target run scored by the team bats first in semi finals.
  3. Predicting the Finalist Teams and Players
  4. Predict the Winner of ICC Cricket World Cup 2023

## First things first : What are our predictions?
* Finalist Teams : India and Australia

* World Cup Winners :
  1. By FinalistAndWinnerPrediction: Australia
  2. By WC_pred: India
  [Let's all remain optimistic and hope that our prediction comes true on the 19th of November, with India emerging as the victorious team in the competition.]

* Semi-final Targets :
  1. Semi-Final 1 : India bats first : Target = 320
  2. Semi-Final 1 : New Zealand bats first : Target = 292
  3. Semi-Final 2 : South Africa bats first : Target = 359
  4. Semi-Final 2 : Australia bats first : Target = 338

* India Playing 11 for the 2 games :
 * V. Kohli
 * R. Sharma
 * KL Rahul
 * S. Iyer
 * R. Jadeja
 * S. Gill
 * K. Yadav
 * M. Shami
 * SN Thakur
 * J. Bumrah
 * M. Siraj

* Prediction of top 3 highest run Scorers in 2023:
  1. V Kohli --> 659 Runs
  2. Q de Kock --> 647 Runs
  3. RG Sharma --> 587 Runs
  

## Basic Flow of the Event:
* Data Scraping/ Collection: We collected the data required in all the predictions. We considered the ODI data ranging from past 1 year to 50 years.
  1. Major data columns used:
     * Team1 Name
     * Team2 Name
     * Score
     * Batsman information
     * Baller information
     * Venue(Ground)
     * Result
     * Date
    
* Data Preprocessing: To ensure the quality and preparation of the input data, We preprocessed every dataset used in our model as per the requirements.
    1. Data Cleaning: Cleaned the data scrapped as per the requirements. handled missing values by removing rows or replacing it with 0/mean and removing the duplicate values.
    2. Data Integration: Data files coming from different sources and in different formats, we need to merge them appropriately.
    3. Encoding Categorical data: Machine learning works on numeric data hence categorical data which are not of the type float/int has to be converted into numeric values. We done it by LabelEncoding/OnehotEncoding.
    4. Splitting the Dataset into the Training set and Test set: Splitted the data into training set and testing set as per the standard ratios.
    5. Feature Scaling: It helps ensure that all features contribute equally to the model training process. We used StandardScaler class of sklearn.preprocessing
   
* Feature Selection: Used EDA stats, correlations to extract the necessary features and removed redundant, noisy and irrelevant features. it plays crucial role on optimizing and enhancing model performance and reducing computational complexity.

* Data Analysis: As the World Cup is now reaching to its end, we analysed the data of last 5 year including current year's and figured the form of batsmen and bowler by [this](https://www.researchgate.net/publication/323611656_Predicting_Players'_Performance_in_One_Day_International_Cricket_Matches_Using_Machine_Learning) research paper. Now by the form rating of the batsmen and bowlers playing in WCC, we extracted top 6 batsmen and top 5 bowlers.

  1. Batsmen Rating Formula: 0.4262*Ave + 0.2566*Inns + 0.1510*SR + 0.0787*Centuries + 0.0556*Fifties - 0.0328*Zeros
  2. Bowlers Rating Formula: 0.3269*Overs + 0.2846*Inns + 0.1877*SR + 0.1210*Ave

* Model Training:
    1. Performed Deep neural network model considering activation function, class weight, batch normalization, kernel initializer, kernel regularizer, batch size and early stopping. We tried out many different configurations of the network architecture and settled on the one which gave us better accuracy and less overfitting.
    2. We also used RandomForestClassifier and RandomForestRegressor and tried different hyperparamer values - especially max_depth which affected the extent of overfitting. We observed that this model was giving pretty good results on almost all the datasets.
    3. We tried out XGB as well, as expected it was performing good on the datasets with small number of instances.

* Model Evaluation:
   1. In the multi-class classification problems, the loss function used is categoriacal cross-entropy. We had to use different nomenclatures according to the specific model that we are using. For example - XGB class reffered to the same loss as 'mlogloss'. The models were judged based on accuracy and the loss functions were used to train the models.
   2. For regression problems, the usual mean square error was used as the loss function and the models were trained and judged based on the same.
  
* Prediction:
    Finally, the input data for which we wanted to predict was fed to the trained classifiers/regressors and the desired predictions were obtained.
     
For Highest Run scorer prediction-
Took all odi matches data of top 5 players in the ranking currently(before semis), and considering ground, date, and opponent as factors, ran a neural network model to predict the runs the batsman will hit in the semis and finals. Then added the predicted semis/finals runs with the current runs, and predicted the highest run scorer of the tournament.

# Contributions :
 * Finalist and WinnerPrediction - Dhruvi Gohel(202101188) and Varun Vyas(202101468)
 * Score Prediction - Dhruvi Gohel(202101188) and Varun Vyas(202101468)
 * Finalist_prediction_2- Ayush Patel(202101439)
 * Players Prediction - Dhruvil Thakor(202101462) and Dhruvi Gohel(202101188)
 * Highest Run Scorer Prediction, API- Aayush Patel(202101452)
