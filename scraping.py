from bs4 import BeautifulSoup

f = open("recette.html", "r")
html_content = f.read()
f.close()

soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find('h1')
texte_titre = titre_h1.text
print("Titre page html : "+str(texte_titre))
print()
parag = soup.find('p', class_="description")
print("Description : \n",parag.text)
# ou encore 
lis_div_centre = soup.find_all('div', class_="centre")
description = lis_div_centre[1].find("p", class_="description")
print(description.text)

#Image
div_image = soup.find('div', class_="info")
image_info = div_image.find("img")
print("Le src de l'image est : ", image_info['src'])
