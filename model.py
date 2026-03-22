from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

def train_model(x, y):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

    
    numerical_cols = ['year','mileage','mpg','engineSize']
    scaler = StandardScaler()

    X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
    X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    print("R2:", r2)

    n = X_test.shape[0]
    p = X_test.shape[1]

    adjusted_r2 = 1 - ((1 - r2) * (n - 1)) / (n - p - 1)
    print("Adjusted R2:", adjusted_r2)