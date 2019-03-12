from bs4 import BeautifulSoup
import urllib.request as request

path = r'C:\Users\PreNatal 2016\Documents\proyecto\imageScrapingPy\imagesResult' + '\\'
url = ('http://www.orangesmile.com/guia-turistica/guayaquil/galeria-fotos.htm',
       'https://sagacreativa.com/top-10-fotos-de-guayaquil/',
       'https://www.tripadvisor.co/LocationPhotos-g303845-w2-Guayaquil_Guayas_Province.html#66065654',
       'http://www.guayaquilesmidestino.com/para-conocer-su-historia',
       'http://www.guayaquilesmidestino.com/para-compartir-su-naturaleza',
       'http://www.guayaquilesmidestino.com/para-divertirse-y-gozar',
       'https://www.istockphoto.com/es/fotos/guayaquil',
       'https://www.minube.com/fotos/guayaquil-c1208',
       'https://www.suitesguayaquil.com/guayaquil-fotos.html',
       'https://turismoguayaquil.wordpress.com/fotos-guayaquil/'
       )

nameTemp = 1

def webScraping(URL):
    pagina = request.urlopen(URL)
    web = BeautifulSoup(pagina, 'html.parser')
    return web


for result in range(len(url)):
    try:
        resultScraping = webScraping(url[result])
        for img in resultScraping.find_all('img'):
            dirImage = img.get('src')
            try:
                if dirImage[:1] == '/':
                    image = url[result] + dirImage
                elif dirImage == None or dirImage == "":
                    notImage = url[result] + dirImage
                else:
                    image = dirImage

                nameImage = img.get('alt')
                if nameImage == None:
                    nameImage = str(nameTemp)
                    nameTemp = nameTemp + 1
                else:
                    nameImage = nameImage + str(nameTemp)

                folder = open(path + nameImage + '.jpg', 'wb')
                folder.write(request.urlopen(image).read())
                folder.close()
            except:
                print("imagen No definida")

    except:
        urlError = open("URLError.txt", 'w')
        urlError.write(url[result])
        urlError.close()


