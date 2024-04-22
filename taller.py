import os.path #Importa os.path a la libreria

import pandas as pd #Importa panda a la libreria

def read(directory): #Funcion read que recibe un directorio
    phrases = []
    sentiments = []

    for subdir in os.listdir(directory): #Bucle liste las carpetas en el directorio
        if os.path.isdir(os.path.join(directory, subdir)): #Si el archivo es un directorio existente
            for file in os.listdir(os.path.join(directory, subdir)): #Recorre los archivos del directorio
                if file.endswith(".txt"): #Si el archivo termina en .txt
                    with open(os.path.join(directory, subdir, file)) as f: #Abre el archivo
                        phrases.append(f.read()) #Agrega el contenido del archivo a la lista phrases
                        sentiments.append(subdir)
    return pd.DataFrame({"phrase": phrases, "sentiment": sentiments}) #Devuelve un DataFrame con las columnas "phrase" y "sentiment"

train_df = read("data/train") #Llama a la funcion read con el directorio "data/train"
test_df = read("data/test") #Llama a la funcion read con el directorio "data/test"

""" print(train_df) #Imprime el DataFrame train_df
print(test_df)  #Imprime el DataFrame test_df """

train_df.to_csv("train_dataset.csv", index=False) #Guarda el DataFrame train_df en un archivo csv
test_df.to_csv("test_dataset.csv", index=False) #Guarda el DataFrame test_df en un archivo csv

""" print(train_df['sentiment'].value_counts())
print(test_df['sentiment'].value_counts())
print(train_df.columns[0])
print(train_df.columns[1]) """