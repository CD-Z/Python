import pandas as pd
import matplotlib.pyplot as plt


def start():
    df = pd.read_csv('absence_4cWI_2022.csv', sep=";")
    p_head(df)
    df = df.drop('Klasse', 1)
    print(df.corr())
    #df.groupby(['Fach']).plot(kind='hist',y=['Fehlstd.','Unentsch. Fehlstd.'])
    dff= df.groupvy("Fach")["Fehlstd."].sum().plot(kind='hist')

    plt.show()


def p_head(data):
    print(data.head())


if __name__ == "__main__":
    start()
