from conncector.connector import get_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from conf. conf import logging
import pickle 
from util.util import save.model

logging.info('extracting df')

df = get_data("https://raw.githubusercontent.com/5x12/ml-cookbook/master/supplements/data/cars.csv")
print(df)

def train_test_split(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        random_state = 2
                                                    )
return X_train, X_test, y_train, y_test

logger.info('Df is extracted')

save.model ('model/conf/linear_regression.pkl', model=rg)

df = get_data("https://raw.githubusercontent.com/5x12/ml-cookbook/master/supplements/data/cars.csv")
print(df)


def training()

reg = LinearRegression()

reg.fit(X_train, y_train)

reg = Ridge(alpha=4.0, max_iter = 10000)

reg.fit(X_train, y_train)