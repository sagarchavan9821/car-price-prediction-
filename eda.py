import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(path):
    df = pd.read_csv(path)

    print(df.head())
    print(df.shape)
    print(df.info())
    print(df.isnull().sum())

    sns.histplot(df["price"], bins=50, kde=True)
    plt.show()

    plt.figure(figsize=(6,4))
    sns.boxplot(data=df, x='year', y='price')
    plt.show()

    
    sns.scatterplot(data=df, x="mileage", y="price")
    plt.show()

    
    sns.boxplot(data=df, x="engineSize", y="price")
    plt.show()
     
    sns.boxplot(data=df, x="transmission", y="price")
    plt.show()

    
    sns.boxplot(data=df, x="fuelType", y="price")
    plt.show()

    sns.boxplot(data=df, x="model", y="price")
    plt.show()



if __name__ == "__main__":
    perform_eda("ford.csv")
