from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
import mlflow
import mlflow.sklearn


def rf_regressor(X_train, y_train):
    mlflow.set_experiment("RandomForest_regression")
    mlflow.sklearn.autolog()
    with mlflow.start_run():
        rf = RandomForestRegressor(n_estimators=300, random_state=42, max_depth=12)
        rf.fit(X_train, y_train.ravel())
        mlflow.sklearn.save_model(rf, path="./saved_models/rf_model")
    return rf

def boosting_regressor(X_train, y_train):
    mlflow.set_experiment("gradient_boosting_regression")
    mlflow.sklearn.autolog()
    with mlflow.start_run():
        gb = GradientBoostingRegressor(n_estimators=600, random_state=42, max_depth=12, learning_rate=0.9)
        gb.fit(X_train, y_train.ravel())
        mlflow.sklearn.save_model(gb, path="./saved_models/gb_model")
    return gb

def predict_salary(model, X_test):
    y_pred = model.predict(X_test.toarray())
    return y_pred