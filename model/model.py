from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

def train_and_evaluate(model, X_train, y_train, X_test, y_test):
    if model == "rf":
        model = RandomForestRegressor(n_estimators=300, random_state=42, max_depth=12)
    elif model == "gb":
        model = GradientBoostingRegressor(n_estimators=600, random_state=42, max_depth=12, learning_rate=0.9)
    else:
        raise ValueError("Model not supported. Choose 'rf' for Random Forest or 'gb' for Gradient Boosting.")
    with mlflow.start_run():
        mlflow.sklearn.autolog()
        model.fit(X_train, y_train.ravel())
        y_pred = model.predict(X_test)
        signature = infer_signature(X_test, y_pred)
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model_registry",
            signature=signature,
            registered_model_name="sk-learn-random-forest-reg-model")
        #mlflow.sklearn.save_model(model, path="./saved_models/rf_model")
        y_pred = model.predict(X_test.toarray())
        mlflow.log_metric("r2_score", r2_score(y_test, y_pred))
        mlflow.log_metric("mse", mean_squared_error(y_test, y_pred))
        print("Done")