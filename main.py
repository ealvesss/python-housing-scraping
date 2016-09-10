from bs4 import BeautifulSoup
import requests
import json

url = 'http://www.au.dk/en/internationalcentre/housing/housingsite/housing-for-rent/?user=ichousing&pass=1qaz&submit=Login&logintype=login&pid=1425505&redirect_url=&tx_felogin_pi1%5Bnoredirect%5D=0'


response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
houses = soup.findAll("div", { "class" : "csc-default" })


i=1
total=1

houseList = list()
detailList = list()
imgList = list()

for house in houses:	
	title = house.findAll("h1")
	tbody = house.findAll("tbody")

	if title:	
		i+=1
		if i > 3:
			detailList.append(title[0].text)
			
			if len(tbody) > 1:
				tds = tbody[1].findAll("td")
			else:
				tds = tbody[0].findAll("td")
				tds.pop(0)
			
			row=1
			
			for td in tds:
				if row % 2 == 0:
					detailList.append(td.text)
				
				if not td.text == "Contact information":
					row+=1
					
			for img in house.findAll("li", {"class" : "csc-textpic-image csc-textpic-lastcol"}):
				imgList.append("http://www.au.dk/" + str(img.find("a")["href"]))
			total+=1
			detailList.append(imgList)
			houseList.append(detailList)
			detailList = list()
			imgList = list()


r = requests.put('https://aarhus-housing.firebaseio.com/aarhus-housing.json',data=str(json.dumps(houseList)))
print r