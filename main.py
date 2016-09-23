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
			detailList.append({'Title':title[0].text})
			
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
						detailList.append({'Type': td.text})
					elif row == 4:
						detailList.append({'Period': td.text})
					elif row == 6:
						detailList.append({'Address': td.text})
					elif row == 8:
						detailList.append({'Size': td.text})
					elif row == 10:
						detailList.append({'Rooms': td.text})
					elif row == 12:
						detailList.append({'Deposit': td.text})
					elif row == 14:
						detailList.append({'MontlyRent': td.text})
					elif row == 16:
						detailList.append({'PaymentOnAccount': td.text})
					elif row == 18:
						detailList.append({'Furnished': td.text})	
					elif row == 20:
						detailList.append({'Smoking': td.text})	
					elif row == 22:
						detailList.append({'Tenants': td.text})	
					elif row == 24:
						detailList.append({'AdditionalDescription': td.text})	
					elif row == 26:
						detailList.append({'Name': td.text})	
					elif row == 28:
						detailList.append({'Phone': td.text})	
					elif row == 30:
						detailList.append({'Email': td.text})		
				if not td.text == "Contact information":
					row+=1
					
			for img in house.findAll("li", {"class" : "csc-textpic-image csc-textpic-lastcol"}):
				imgList.append("http://www.au.dk/" + str(img.find("a")["href"]))
			total+=1
			detailList.append(imgList)
			houseList.append(detailList)
			detailList = list()
			imgList = list()


r = requests.put('https://aarhus-housing-5b057.firebaseio.com//aarhus-housing.json',data=str(json.dumps(houseList)))
print r
