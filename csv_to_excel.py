import pandas


read_file = pandas.read_csv("data.csv")

read_file.to_excel("data.xlsx", index=None, header=True)
