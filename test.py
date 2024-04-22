"""GitHub Classroom autograding script."""

import os.path #Importa os.path a la libreria

import pandas as pd #Importa panda a la libreria

if not os.path.exists("train_dataset.csv"): #Si no existe el archivo train_dataset.csv
    raise FileNotFoundError("File 'train_dataset.csv' not found") #Muestra el mensaje de error

train_dataset = pd.read_csv("train_dataset.csv") #Lee el archivo train_dataset.csv

assert train_dataset.columns[0] == "phrase" #Comprueba que la columna 0 sea igual a "phrase"
assert train_dataset.columns[1] == "sentiment" #Comprueba que la columna 1 sea igual a "sentiment"

counts = train_dataset["sentiment"].value_counts()  #Cuenta los valores de la columna "sentiment"

assert counts["neutral"] == 1117 #Comprueba que el valor de "neutral" sea igual a 1117
assert counts["positive"] == 458 #Comprueba que el valor de "positive" sea igual a 458
assert counts["negative"] == 236    #Comprueba que el valor de "negative" sea igual a 236


if not os.path.exists("test_dataset.csv"): #Si no existe el archivo test_dataset.csv
    raise FileNotFoundError("File 'test_dataset.csv' not found") #Muestra el mensaje de error

test_dataset = pd.read_csv("test_dataset.csv") #Lee el archivo test_dataset.csv

counts = test_dataset["sentiment"].value_counts() #Cuenta los valores de la columna "sentiment"

assert counts["neutral"] == 274 #Comprueba que el valor de "neutral" sea igual a 274
assert counts["positive"] == 112 #Comprueba que el valor de "positive" sea igual a 112
assert counts["negative"] == 67 #Comprueba que el valor de "negative" sea igual a 67
