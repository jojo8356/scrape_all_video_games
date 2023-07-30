from bs4 import BeautifulSoup as bs
import requests as r,time,requests
remove_duplicates = lambda original_list: list(set(original_list))
affiche = lambda liste: [print(i, element.text) for i, element in enumerate(liste)]
consoles_select = ['Dreamcast','Famicom','Game Boy','Game Boy Advance','Game Boy Color','GameCube','Linux','Master System','Mega Drive','par navigateur','Nintendo 3DS','Nintendo 64','Nintendo DS','Nintendo Entertainment System','Nintendo Switch','PlayStation','PlayStation 2','PlayStation 3','PlayStation 4','PlayStation 5','PlayStation Portable','PlayStation Vita','Super Famicom','Super Nintendo','Wii','Wii U','Windows (0-9)','Xbox','Xbox 360','Xbox One','Xbox Series']
start = time.time()
jeux = []
liens = []
response = r.get("https://fr.wikipedia.org/wiki/Liste_de_jeux_vid%C3%A9o")
soup = bs(response.content, 'lxml')
consoles = soup.find("div", {"id": "mw-content-text"}).find_all("ul")
console = []
indexes = [1, 6, 9]
for index in indexes:
    for x in consoles[index].find_all("li"):
        console.append(x.find("a"))
for x in console:
    liens.append(x["href"]) if ("title" in x and x["title"].replace("Liste de jeux ","") in consoles_select) else None
for x in range(len(liens)):
    if "/wiki/" in liens[x]:
        liens[x] = "https://fr.wikipedia.org"+liens[x]
urls = []
def dreamcast():
    response = r.get(liens[0])
    soup = bs(response.content, 'lxml')
    tr = soup.find_all("tbody")[2].find_all("tr")
    for x in tr:
        EU = x.find("td",{"bgcolor":"#bbbbff"})
        if EU != None:
            url = x.find("td").find("a")["href"]
            if "/wiki/" in url:
                urls.append("https://fr.wikipedia.org"+url)
def famicom():
    response = r.get(liens[1])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    for x in range(2,29):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            if " - J" not in (y.text):
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)

def GB():
    response = r.get(liens[2])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(2,28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            if " - J" not in (y.text):
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
def GBA():
    response = r.get(liens[3])
    soup = bs(response.content, 'lxml')
    tr = soup.find_all("tbody")[1].find_all("tr")
    del tr[0]
    for x in tr:
        try:
            EU = x.find_all("td")[6].text
            if EU == "✔\n":
                url = (x.find_all("td")[0].find("a")["href"])
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
        except:
            pass
def GBC():
    response = r.get(liens[4])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(2,29):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
def GC():
    response = r.get(liens[5])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(27):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)

def linux():
    response = r.get(liens[6])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(47):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
            except:
                pass

def Master_System():
    response = r.get(liens[7])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(27):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def Mega_Drive():
    response = r.get(liens[8])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text) or " - Ch" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def browser():
    response = r.get(liens[9])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(27):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def trois_DS():
    response = r.get(liens[10])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(29):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def N_six_quatre():
    response = r.get(liens[11])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text) or " - AUS" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
    del urls[urls.index("https://fr.wikipedia.org/wiki/Nintendo_64DD")]
    del urls[urls.index("https://fr.wikipedia.org/wiki/Japon")]
    del urls[urls.index("https://fr.wikipedia.org/wiki/Australie")]

def DS():
    response = r.get(liens[12])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(29):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
    del urls[urls.index("https://fr.wikipedia.org/wiki/Liste_de_jeux_DSiWare")]
    del urls[urls.index("https://fr.wikipedia.org/wiki/DSiWare")]
def NES():
    response = r.get(liens[13])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(27):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def switch():
    response = r.get(liens[14])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text) or " - AN" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def PS_un():
    response = r.get(liens[15])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(37):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
    del urls[urls.index("https://fr.wikipedia.org/wiki/Platinum_(Sony)")]
def PS_deux():
    response = r.get(liens[16])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(51):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def PS_trois():
    response = r.get(liens[17])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def PS_quatre():
    response = r.get(liens[18])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(29):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def PS_cinq():
    response = r.get(liens[19])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(38):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def PSP():
    response = r.get(liens[20])
    soup = bs(response.content, 'lxml')
    tr = soup.find_all("tbody")[2].find_all("tr")
    for x in tr:
        EU = x.find("td",{"bgcolor":"#bbbbff"})
        if EU != None:
            url = x.find("td").find("a")["href"]
            if "/wiki/" in url:
                urls.append("https://fr.wikipedia.org"+url)
def PS_vita():
    response = r.get(liens[21])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def Super_Famicom():
    response = r.get(liens[22])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def SNES():
    response = r.get(liens[23])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def Wii():
    response = r.get(liens[24])
    soup = bs(response.content, 'lxml')
    div = soup.find_all("tbody")[2]
    tr = div.find_all("tr")
    del tr[0]
    for x in tr:
        try:
            url = (x.find("td").find("a")["href"])
            if "/w/index.php?title=" not in url:
                urls.append("https://fr.wikipedia.org"+url)
        except:
            pass
url_windows = "https://fr.wikipedia.org/wiki/Liste_de_jeux_Windows_"
urls_windows = [url_windows + "(" + letter + ")" for letter in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
def PC():
    x = 0
    for url in urls_windows:
        response = r.get(url)
        soup = bs(response.content, 'lxml')
        div = soup.find("div",{"class":"mw-parser-output"})
        test = div.find_all("ul")
        while True:
            try:
                for y in test[x].find_all("li"):
                    lien = y.find("a")["href"]
                    if "/wiki/Liste" not in lien:
                        if "/wiki/" in lien:
                            urls.append("https://fr.wikipedia.org"+lien)
                x += 1
            except:
                break
def Wii_U():
    response = r.get(liens[25])
    soup = bs(response.content, 'lxml')
    body = soup.find_all("tbody")[2]
    tr = body.find_all("tr")
    for x in tr:
        try:
            EU = x.find_all("td")[6].text
            if "NC" not in EU:
                lien = x.find_all("td")[0].find("a")["href"]
                if "/wiki/" in lien:
                            urls.append("https://fr.wikipedia.org"+lien)
        except:
            pass
    
def Xbox():
    response = r.get(liens[27])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(27):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/wiki/" in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def Xbox_trois_six():
    response = r.get(liens[28])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(36):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/wiki/" in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass

def Xbox_one():
    response = r.get(liens[29])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/wiki/" in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def Xbox_series():
    response = r.get(liens[30])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(24):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/wiki/" in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def main():
    DS()
    GB()
    GBA()
    GBC()
    GC()
    Master_System()
    Mega_Drive()
    NES()
    N_six_quatre()
    PC()
    PSP()
    PS_cinq()
    PS_deux()
    PS_quatre()
    PS_trois()
    PS_un()
    PS_vita()
    SNES()
    Super_Famicom()
    Wii()
    Wii_U()
    Xbox()
    Xbox_one()
    Xbox_series()
    Xbox_trois_six()

main()
urls = remove_duplicates(urls)
with open("urls.txt","w") as f:
    for x in urls:
        f.write(x+"\n")

urls = open("urls.txt","r").readlines()
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

def scrap_data(lien):
    try:
        response = urlopen(lien)
        soup = bs(response.read(), 'lxml')
        titre = soup.find("head").find("title").text.replace(" — Wikipédia","")
        genre_element = soup.find('th', scope='row', text='Genre')
        genre = genre_element.find_next_sibling('td').text
        platforms_element = soup.find('th', scope='row', text='Plateforme')
        platforms = platforms_element.find_next_sibling('td').text
        jeu = [titre,platforms,genre,lien]
        for x in range(len(jeu)):
            jeu[x] = jeu[x].replace("\n","")
        jeux.append("#".join(jeu))
    except:
        pass

jeux = []
with ThreadPoolExecutor() as executor:
    urls.sort()
    for x in urls:
        lien = (x.replace("\n",""))
        executor.submit(scrap_data, lien)
end = time.time()
print(end-start)
