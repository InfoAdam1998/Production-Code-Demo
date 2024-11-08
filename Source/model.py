from preperation import prepare_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def build_model():

    #1. load preprocessed dataset
    df = prepare_data()

    #2. identify X and y
    X, y = get_X_y(df)

    #3. split dataset
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    #4. train the model
    rf = train_model(X_train, y_train)

    #5. evaluate the model
    score = evaluate_model(rf, X_test, y_test)

    print(score)
    #6. tune hyperparameters

    #7. save the model in a config file



def get_X_y(data,
            col_X =['area', 
                  'constraction_year', 
                  'bedrooms', 
                  'garden', 
                  'balcony_yes', 
                  'parking_yes', 
                  'furnished_yes', 
                  'garage_yes', 
                  'storage_yes'],
            col_y = "rent"):
    return data[col_X], data[col_y]

def split_train_test(X, y) :
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                         y,
                                                         test_size = 0.2)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)

    return rf

def evaluate_model(model, X_test, y_test):
    return model.score(X_test, y_test)
    

build_model()