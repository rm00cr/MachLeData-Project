import kagglehub
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
import joblib


def download_dataset():
    """
    Download the dataset from Kaggle.
    """
    dataset_path = kagglehub.dataset_download("samithsachidanandan/the-global-ai-ml-data-science-salary-for-2025")
    return dataset_path


def load_data(dataset_path):
    data = pd.read_csv(dataset_path + "/salaries.csv")
    return data


def preprocess_data(data, debug=False):

    categorical_features = ["experience_level", "employment_type", "job_title", "company_size", "company_location", "employee_residence", "salary_currency"]

    categorical_transformer = ColumnTransformer([("onehot", OneHotEncoder(handle_unknown="ignore"), categorical_features)], remainder="passthrough")

    if debug:
        categorical_transformer = joblib.load("./categorical_transformer.pkl")
        return categorical_transformer.transform(data)
    
    data = data.query('job_title == "Data Scientist"')
    x_train, x_test, y_train, y_test = train_test_split(data.drop(columns=["salary", "salary_in_usd", "work_year"]), data["salary"],  test_size=0.15, random_state=42, shuffle=True)
    preprocessed_x_train = categorical_transformer.fit_transform(x_train)
    joblib.dump(categorical_transformer, "./categorical_transformer.pkl")
    preprocessed_x_test = categorical_transformer.transform(x_test)

    print(preprocessed_x_train.shape)
    print(preprocessed_x_train.shape)

    scaler = StandardScaler()   
    scaler.fit(y_train.values.reshape(-1, 1))
    # y_train = scaler.transform(y_train.values.reshape(-1, 1))
    # y_test = scaler.transform(y_test.values.reshape(-1, 1))
    print(y_train.shape)
    print(y_test.shape)

    return preprocessed_x_train, preprocessed_x_test, y_train.values.reshape(-1, 1), y_test.values.reshape(-1, 1)
