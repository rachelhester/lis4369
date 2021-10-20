import datetime as dt 
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style

def get_requirements():
    print("\nData Analysis 1")
    print("Program Requirements:")
    print("1. Run demo.py.\n")
    print("2. If errors, more than likely missing installations.")
    print("3. Test Python Package Installer: pip freeze")
    print("4. Research how to do the following installations:")
    print("\ta. pandas (only if missing)")
    print("\tb. pandas-datareader (only if missing)")
    print("\tc. matplotlib (only if missing)")
    print("5. Create at least three functions that are called by the program:")
    print("\ta. main(): calls at least two other functions.")
    print("\tb. get_requirements(): displays the program requirements.")
    print("\tc. data_analysis_1(): displays the following data.")

def data_analysis_1():
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2018, 10, 15)

    df = pdr.DataReader("XOM", "yahoo", start, end)

    print("\nPrint number of records: ")
    print(len(df), sep='\n')

    print()
    print(df.columns)
    print("This shows you the columns of the data frame, which is important.")

    print("\nPrint data frame: ")
    print(df)

    print("\nPrint first five lines:")
    print(df.head())

    print("\nPrint last five lines:")
    print(df.tail())

    print("\nPrint first 2 lines:")
    print(df.head(2))

    print("\nPrint last 2 lines:")
    print(df.tail(2))

    style.use('ggplot')

    df["High"].plot()
    df['Adj Close'].plot()
    plt.legend()
    plt.show() 
