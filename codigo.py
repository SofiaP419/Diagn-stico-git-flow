import json

def top_tweets(datos):
    pass

def top_usuarios(datos):
    pass

def top_dias(datos):
    pass

def top_hashtags(datos):
    pass


def main():
    f = open("farmers-protest-tweets-2021-03-5.json")
    datos = json.load(f)
    
    top_tweets(datos)
    top_usuarios(datos)
    top_hashtags(datos)
    top_dias(datos)

    f.close()