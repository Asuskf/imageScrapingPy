from bs4 import BeautifulSoup
import urllib.request as request

path = r'C:\Users\Asus\Documents\proyectos\imageScraping\imageScrapingPy\imagesScraping' + '\\'
url = ('http://www.orangesmile.com/guia-turistica/guayaquil/galeria-fotos.htm',
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
    resultScraping = webScraping(url[result])

    for img in resultScraping.find_all('img'):
        dirImage = img.get('src')
        try:
            if dirImage[:1] == '/':
                image = url[result]+dirImage
            elif dirImage == None or dirImage == "":
                notImage = url[result]+dirImage
            else:
                image = dirImage

            nameImage = img.get('alt')
            if nameImage == None:
                nameImage = str(nameTemp)
                nameTemp = nameTemp +1
            else:
                nameImage = nameImage + str(nameTemp)

            folder = open(path+nameImage+'.jpg', 'wb')
            folder.write(request.urlopen(image).read())
            folder.close()
        except:
            print("imagen No definida")

