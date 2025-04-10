from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor


def rf_regressor(X_train, y_train):
    rf = RandomForestRegressor(n_estimators=300, random_state=42, max_depth=12)
    rf.fit(X_train, y_train.ravel())
    return rf

def boosting_regressor(X_train, y_train):
    gb = GradientBoostingRegressor(n_estimators=600, random_state=42, max_depth=12, learning_rate=0.9)
    gb.fit(X_train, y_train.ravel())
    return gb

def predict_salary(model, X_test):

    y_pred = model.predict(X_test.toarray())

    return y_pred