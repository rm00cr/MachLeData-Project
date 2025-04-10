from model import predict_salary, boosting_regressor
from preprocessing import download_dataset, load_data, preprocess_data
from metrics import evaluate_model

def main():
    dataset_path = download_dataset()
    data = load_data(dataset_path)
    x_train, x_test, y_train, y_test = preprocess_data(data)
    model = boosting_regressor(x_train, y_train)
    pred = predict_salary(model, x_train)
    print(evaluate_model(y_train, pred))
    pred = predict_salary(model, x_test)
    print(evaluate_model(y_test, pred))
if __name__ == "__main__":
    main()