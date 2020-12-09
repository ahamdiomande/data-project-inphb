def parse_model(X, use_columns):
    if "Survived" not in X.columns:
        raise ValueError("target column survived should belong to df")
    target = X["Survived"]
    X = X[use_columns]
    return X, target

#model_cols1 =['SibSp', 'Parch', 'Fare']
#X, y = parse_model(X=train.copy(), use_columns=model_cols1)