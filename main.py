import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing

np.set_printoptions(threshold=sys.maxsize)


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def cse_cic_ids18():
    df = pd.read_csv("cse-cic-ids-slowloris.csv")

    # df = df[['Dst Port', 'Flow Duration', 'TotLen Fwd Pkts',
    #          'TotLen Bwd Pkts', 'Fwd Pkt Len Max', 'Bwd Pkt Len Mean',
    #          'Flow Pkts/s', 'Flow IAT Std', 'Flow IAT Max',
    #          'Bwd Header Len', 'Fwd Pkts/s', 'Bwd Pkts/s', 'Pkt Len Max',
    #          'Pkt Len Std', 'Bwd Seg Size Avg', 'Subflow Fwd Byts', 'Init Fwd Win Byts',
    #          'Init Bwd Win Byts', 'Label']]

    df = df[['Dst Port', 'Flow Pkts/s','Label']]

    # BINARY CLASSIFICATION  (Slowloris -> 1, Benign -> 0)
    df = df.replace('DoS attacks-Slowloris', 1)
    df = df.replace('Benign', 0)

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)

    return df


def cicids17():
    df = pd.read_csv("cicids-slowloris.csv")



    df = df[['Dst Port', 'Flow Duration', 'TotLen Fwd Pkts',
             'TotLen Bwd Pkts', 'Fwd Pkt Len Max', 'Bwd Pkt Len Mean',
             'Flow Pkts/s', 'Flow IAT Std', 'Flow IAT Max',
             'Bwd Header Len', 'Fwd Pkts/s', 'Bwd Pkts/s', 'Pkt Len Max',
             'Pkt Len Std', 'Bwd Seg Size Avg', 'Subflow Fwd Byts', 'Init Fwd Win Byts',
             'Init Bwd Win Byts', 'Label']]

    # BINARY CLASSIFICATION  (Slowloris -> 1, Benign -> 0)
    df = df.replace('DoS slowloris', 1)
    df = df.replace('BENIGN', 0)

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)

    return df


if __name__ == '__main__':
    df_slowloris = cse_cic_ids18()
    # df_slowloris = cicids17()



    # ------------------ Dataframe --------------------

    # Subset X, contains the selected columns except the 'Label' column
    X = df_slowloris.drop('Label', axis=1).to_numpy()

    # Subset y is assigned to the 'Label' column.
    y = df_slowloris['Label'].to_numpy()


    # # General Check for Infinte or NaN Values.
    # # Check for any infinite values
    # print(np.isinf(X).any())
    # print(np.isinf(y).any())
    #
    # # Check for any nan values
    # print(np.isnan(X).any())
    # print(np.isnan(y).any())

    # print(X[1][0])
    # print(y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    print("Decision Tree Classifier, accuracy score: ")
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print(accuracy_score(y_test, predictions))

    print("\nRandom Forest Classifier, accuracy score: ")
    clf1 = RandomForestClassifier()
    clf1.fit(X_train, y_train)
    predictions1 = clf1.predict(X_test)
    print(accuracy_score(y_test, predictions1))

    print("\nKNeighbors Classifier, accuracy score: ")
    clf2 = KNeighborsClassifier(n_neighbors=3)
    clf2.fit(X_train, y_train)
    predictions2 = clf2.predict(X_test)
    print(accuracy_score(y_test, predictions2))
    #
    # # Separate testing
    # print("\nKNeighbors Classifier, accuracy score: ")
    # clf2 = KNeighborsClassifier(n_neighbors=3)
    # clf2.fit(X_train, y_train)
    # for i in range(600, 1000):
    #     predictions2 = clf2.predict(X_test[i].reshape(1,-1))
    #     print(predictions2)
    #     print(y_test[i])
