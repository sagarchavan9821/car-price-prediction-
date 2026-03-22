
import pandas as pd
def load_and_preprocess(path):

 df=pd.read_csv(path)
 x=df.drop('price',axis=1)
 y=df['price']
 x=pd.get_dummies(x,columns=['model','transmission','fuelType',],drop_first=True)


 return x,y 

