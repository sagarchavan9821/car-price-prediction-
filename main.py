from preprocessing import load_and_preprocess
from model import train_model

x, y = load_and_preprocess("ford.csv")
train_model(x, y)
