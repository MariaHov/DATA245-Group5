# DATA245-Group5
# Air Quality Prediction in Beijing
This project aims to predict the air quality in Beijing using machine learning techniques. The target column used for prediction is PM2.5, which is a measure of the concentration of fine particulate matter in the air. High levels of PM2.5 are harmful to human health, so predicting the PM2.5 levels can help individuals plan their outdoor activities and take necessary precautions.

## Data
The dataset used for this project is the (https://archive.ics.uci.edu/ml/datasets/Beijing+Multi-Site+Air-Quality+Data#) from the UCI Machine Learning Repository. It contains hourly measurements of various air pollutants, including PM2.5, from 12 monitoring stations in Beijing from 2010 to 2015.

## Approach
The project uses machine learning algorithms to predict the PM2.5 levels based on historical data. The following steps are involved:

1. Data preprocessing: The raw data is cleaned, preprocessed, and transformed to prepare it for machine learning algorithms.

2. Feature engineering: Additional features are created from the raw data to improve the performance of machine learning algorithms.

3. Model selection: Various machine learning algorithms are evaluated, and the best-performing model is selected for further tuning.

4. Hyperparameter tuning: The hyperparameters of the selected model are tuned to optimize its performance.

5. Model evaluation: The performance of the final model is evaluated on a test set to estimate its generalization error.

## Requirements
The project requires the following packages to be installed:

- Python 3.6 or above
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- jupyter notebook

## Usage
To run the project, follow these steps:

1. Clone the repository to your local machine.

2. Open a command prompt or terminal and navigate to the project directory.

3. Create a virtual environment and activate it:

```
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate  # Windows
```

4. Install the required packages:

```
pip install numpy
pip install pandas
```

5. Launch Jupyter Notebook:

```
jupyter notebook
```

6. Open the `air_quality_prediction.ipynb` notebook and run the cells.

## Conclusion
The project demonstrates how machine learning can be used to predict the air quality in Beijing based on historical data. The final model achieves a high level of accuracy in predicting the PM2.5 levels, which can be used to help individuals make informed decisions about their outdoor activities.
