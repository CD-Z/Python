import pandas as pd
import matplotlib.pyplot as plt


def getting_started():
    mydataset = {
        'cars': ["BMW", "Volvo", "Ford"],
        'passings': [3, 7, 2]
    }

    myvar = pd.DataFrame(mydataset)

    print(myvar)
    end_function()


def series():
    a = [1, 7, 2]
    myvar = pd.Series(a)
    print(myvar)
    end_function()


def labels():
    a = [1, 7, 2]
    myvar = pd.Series(a, index=["x", "y", "z"])
    print(myvar)
    print(myvar["y"])
    end_function()


def key_value():
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pd.Series(calories, index=["day1", "day2"])
    print(myvar)
    end_function()


def data_frame():
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    myvar = pd.DataFrame(data)
    print(myvar)
    end_function()


def read_csv_data():
    df = pd.read_csv('Vornamen_2005-2020.csv', encoding='iso-8859-1', sep=';')
    print(df.head())
    # print(df.info())
    end_function()


def read_json_data():
    df = pd.read_json('data.json')
    print(df.head())
    # print(df.info())
    end_function()


def cleaning_empty_cells():
    df = pd.read_csv('dirtydata.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    new_df = df.dropna()

    print(new_df.to_string())
    end_function()


def change_data():
    df = pd.read_csv('dirtydata.csv')
    df.loc[7, 'Duration'] = 45
    print(df.to_string())
    end_function()


def remove_duplicates():
    df = pd.read_csv('dirtydata.csv')
    df.drop_duplicates(inplace=True)
    print(df.to_string())
    end_function()


def data_corr():
    df = pd.read_csv('data.csv')
    print(df.corr())
    df.corr().plot()
    df.plot(y=['Calories', 'Duration'])
    df.plot(y=['Pulse', 'Maxpulse'])
    plt.show()
    end_function()


def end_function():
    print("-----------------------------------------------------")


if __name__ == "__main__":
    # getting_started()
    # series()
    # labels()
    # key_value()
    # data_frame()
    # read_csv_data()
    # read_json_data()
    # cleaning_empty_cells()
    # change_data()
    # remove_duplicates()
    data_corr()
