import json
import pandas as pd 

def top_tweets(datos):
    df = datos.nlargest(10, "retweetCount")
    return print(df["content"].to_markdown())

def top_usuarios(datos):
    pass

def top_dias(datos):
    pass

def top_hashtags(datos):
    pass


def main():
    f = open("farmers-protest-tweets-2021-03-5.json")
    datos = pd.read_json("farmers-protest-tweets-2021-03-5.json")
    
    top_tweets(datos)
    top_usuarios(datos)
    top_hashtags(datos)
    top_dias(datos)

    f.close()

main()