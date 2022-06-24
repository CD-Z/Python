# https://pythonbasics.org/k-nearest-neighbors/
# notwendige Module importieren
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier


def main():
    # CSV lesen; nicht benötigte Spalten löschen
    # Mappen der Ja/Nein Spalte auf 0 und 1
    df = pd.read_csv('JoggingDaten.csv', sep=",")
    dict_map_ja_nein = {'Ja': 1, 'Nein': 0}
    temp_hum1 = df[["Temperatur", "Luftfeuchte", "Joggen"]]
    temp_hum = temp_hum1.replace({'Joggen': dict_map_ja_nein})
    print(temp_hum.info())
    print(temp_hum.head())

    # KNN
    model = KNeighborsClassifier(n_neighbors=3)
    data = temp_hum[['Temperatur', 'Luftfeuchte']].values
    target = temp_hum['Joggen'].values
    model.fit(data, target)

    def predict(temp, hum, display_distance_and_indices, label):
        predicted = model.predict([[temp, hum]])
        print(label, predicted)
        if display_distance_and_indices:
            distances, indices = model.kneighbors([[temp, hum]])
            print("Distances: ", distances)
            print("Indizes:", indices)

    predict(16, 60, True, "Tag 16")
    predict(25, 68, True, "Tag 17")
    predict(16, 56, True, "Tag 18")
    plt.scatter(temp_hum['Temperatur'], temp_hum['Luftfeuchte'],
                color=['r' if r == 0 else 'g' for r in temp_hum['Joggen']])
    plt.show()


if __name__ == "__main__":
    print("start")
    main()
