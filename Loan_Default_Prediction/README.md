# Loan Default Prediction: Lend-or-Lose Project

## Project Overview

This project aims to predict loan defaults using a dataset of financial data. The main goal is to create a predictive model that can classify whether a loan will default based on various financial features.

### Files Included

1. train.csv: Contains the training data used for building the model. It includes features like loan amount, credit score, income, employment details, and a target variable `Default` (1 for default, 0 for no default).
2. test.csv: Contains the test data used for predicting loan defaults. The test data doesn't have the target variable `Default`, which is predicted using the model.
3. Lend-or-Lose-Final.ipynb: The main notebook containing the code for data preprocessing, feature engineering, model building, evaluation, and final prediction. This includes multiple machine learning models and their evaluation metrics.
4. Miscellaneous: A folder containing rough/experimental code in `.ipynb` files. These are intermediate steps and attempts used in the development of the final model.

## How to Use

### Step 1: Install Required Libraries

To run the code, you need to have Python installed along with the necessary libraries. You can install them via `pip`:

```bash
pip install pandas scikit-learn numpy
```

Additional libraries used in the project:

- pandas: For data manipulation.
- scikit-learn: For machine learning algorithms, data preprocessing, and model evaluation.
- numpy: For numerical operations.

### Step 2: Load the Data

The data is provided in the `train.csv` and `test.csv` files. These files contain the training and test data respectively. Make sure that the data files are in the same directory as the notebook, or specify the correct path.

```python
import pandas as pd

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
```

### Step 3: Run the Main Notebook

Open the `Lend-or-Lose-Final.ipynb` notebook in Jupyter or any compatible environment (such as Google Colab). This notebook includes:

- Data exploration and preprocessing
- Feature engineering
- Model training with Gradient Boosting Classifier and other ML models
- Hyperparameter tuning and evaluation
- Predictions on the test data

Run the cells in sequence to execute the entire pipeline. The notebook includes comments explaining each step.

### Step 4: Predictions

Once the model is trained, you can use it to make predictions on the test data. The predictions will be saved in a CSV file (`submission.csv`) which includes the predicted `Default` values for each loan in the test dataset.

```python
submission = sample_submission.copy()
submission['Default'] = test_predictions
submission.to_csv('submission.csv', index=False)
```

### Step 5: Explore Miscellaneous Notebooks

In the Miscellaneous folder, you will find various exploratory and rough codes that were tested during the project. These include different attempts for feature engineering, model evaluation, and visualization.

Feel free to explore and use these for reference or further improvement.

## Project Structure

```
Lend-or-Lose/
│
├── train.csv              # Training data
├── test.csv               # Test data
├── Lend-or-Lose-Final.ipynb  # Main notebook with ML models and code
└── Miscellaneous/         # Folder with rough codes in .ipynb format
```

## Model Evaluation

In the final notebook, the models were evaluated using accuracy and classification reports. Early stopping was used in the Gradient Boosting model to prevent overfitting. The final accuracy and the classification report are shown for the validation set.


## Acknowledgements

- Dataset: [Add any dataset source or acknowledgment here if necessary]
- Libraries: `scikit-learn`, `pandas`, `numpy`, `matplotlib`

