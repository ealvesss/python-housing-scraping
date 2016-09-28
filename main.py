from bs4 import BeautifulSoup
import requests
import json
from util import HousingEncoder, HousingModel




url = 'http://www.au.dk/en/internationalcentre/housing/housingsite/housing-for-rent/?user=ichousing&pass=1qaz&submit=Login&logintype=login&pid=1425505&redirect_url=&tx_felogin_pi1%5Bnoredirect%5D=0'


response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
houses = soup.findAll("div", { "class" : "csc-default" })


i=1
total=1

houseList = []
h = HousingModel()

for house in houses:	
	title = house.findAll("h1")
	tbody = house.findAll("tbody")

	if title:	
		i+=1
		if i > 3:
			h.houseTitle = title[0].text
			
			if len(tbody) > 1:
				tds = tbody[1].findAll("td")
			else:
				tds = tbody[0].findAll("td")
				tds.pop(0)
			
			row=1
			
			for td in tds:
				if row % 2 == 0:
					#detailList.append(td.text)
					if row == 2:
						h.type = td.text
					elif row == 4:
					 	h.period = td.text
					elif row == 6:
						h.address = td.text
					elif row == 8:
					 	h.size = td.text
					elif row == 10:
					 	h.rooms = td.text
					elif row == 12:
					 	h.deposit = td.text
					elif row == 14:
					 	h.montlyRent = td.text
					elif row == 16:
					 	h.paymentOnAccount = td.text
					elif row == 18:
						h.furnished = td.text
					elif row == 20:
					 	h.smoking = td.text
					elif row == 22:
					 	h.tenants = td.text
					elif row == 24:
					 	h.additionalDescription = td.text
					elif row == 26:
					 	h.name = td.text	
					elif row == 28:
					 	h.phone = td.text	
					elif row == 30:
					 	h.email = td.text
				if not td.text == "Contact information":
					row+=1
					
			for img in house.findAll("li", {"class" : "csc-textpic-image csc-textpic-lastcol"}):
				h.images += "http://www.au.dk/" + str(img.find("a")["href"]) + ";"
			total+=1
		
			houseList.append(h)
			h = HousingModel()
			detailList = []
		
			

r = requests.put('https://aarhus-housing-5b057.firebaseio.com/housing.json',data=json.dumps(houseList,cls=HousingEncoder))
print r

