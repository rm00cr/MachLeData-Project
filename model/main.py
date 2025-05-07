from model import train_and_evaluate
from preprocessing import download_dataset, load_data, preprocess_data


def main():
    dataset_path = download_dataset()
    data = load_data(dataset_path)
    x_train, x_test, y_train, y_test = preprocess_data(data)
    train_and_evaluate("rf", x_train, y_train, x_test, y_test)


if __name__ == "__main__":
    main()
