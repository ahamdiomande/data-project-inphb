def convert_cast(df, categorical_cols):
    for col_name in categorical_cols:
        df[col_name] = df[col_name].astype("object")
    return df

categorical_cols = ["Survived", "Pclass"]
df= convert_cast(train, categorical_cols)
df.info()
