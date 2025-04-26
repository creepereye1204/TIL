import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle


with open('./gambling_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('./question.txt', 'rb') as f:
