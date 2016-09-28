class HousingModel(object):
	def __init__(self):
		self._houseTitle = None
		self._type = None
		self._period = None
		self._address = None
		self._size = None
		self._rooms = None
		self._deposit = None
		self._monthlyRent = None
		self._paymentOnAccount = None
		self._furnished = None
		self._smoking = None
		self._tenants = None
		self._additionalDescription = None
		self._name = None
		self._phone = None
		self._email = None
		self._images = ""

	@property
	def period(self):
		return self._period

	@period.setter
	def period(self, value):
		self._period = value

	@period.deleter
	def period(self):
		del self._period

	@property
	def houseTitle(self):
		return self._houseTitle

	@houseTitle.setter
	def houseTitle(self, value):
		self._houseTitle = value

	@houseTitle.deleter
	def houseTitle(self):
		del self._houseTitle


	@property
	def type(self):
		return self._type

	@type.setter
	def type(self, value):
		self._type = value

	@type.deleter
	def type(self):
		del self._type

	@property
	def address(self):
		return self._address

	@address.setter
	def address(self, value):
		self._address = value

	@address.deleter
	def address(self):
		del self._address

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, value):
		self._size = value

	@size.deleter
	def size(self):
		del self._size

	@property
	def rooms(self):
		return self._rooms

	@rooms.setter
	def rooms(self, value):
		self._rooms = value

	@rooms.deleter
	def rooms(self):
		del self._rooms

	@property
	def deposit(self):
		return self._deposit

	@deposit.setter
	def deposit(self, value):
		self._deposit = value

	@deposit.deleter
	def deposit(self):
		del self._deposit

	@property
	def monthlyRent(self):
		return self._monthlyRent

	@monthlyRent.setter
	def monthlyRent(self, value):
		self._deposit = value

	@monthlyRent.deleter
	def monthlyRent(self):
		del self._monthlyRent

	@property
	def paymentOnAccount(self):
		return self._paymentOnAccount

	@paymentOnAccount.setter
	def paymentOnAccount(self, value):
		self._paymentOnAccount = value

	@paymentOnAccount.deleter
	def paymentOnAccount(self):
		del self._paymentOnAccount

	@property
	def furnished(self):
		return self._furnished

	@furnished.setter
	def furnished(self, value):
		self._furnished = value

	@furnished.deleter
	def furnished(self):
		del self._furnished

	@property
	def smoking(self):
		return self._smoking

	@smoking.setter
	def smoking(self, value):
		self._smoking = value

	@smoking.deleter
	def smoking(self):
		del self._smoking



	@property
	def tenants(self):
		return self._tenants

	@tenants.setter
	def tenants(self, value):
		self._tenants = value

	@tenants.deleter
	def tenants(self):
		del self._tenants

	@property
	def additionalDescription(self):
		return self._additionalDescription

	@additionalDescription.setter
	def additionalDescription(self, value):
		self._additionalDescription = value

	@additionalDescription.deleter
	def additionalDescription(self):
		del self._additionalDescription

	#NAME	
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@name.deleter
	def name(self):
		del self._name

	#Phone	
	@property
	def phone(self):
		return self._phone

	@phone.setter
	def phone(self, value):
		self._phone = value

	@phone.deleter
	def phone(self):
		del self._phone

	#EMAIL
	@property
	def email(self):
		return self._email

	@email.setter
	def email(self, value):
		self._email = value

	@email.deleter
	def email(self):
		del self._email
	
	#IMAGES
	@property
	def images(self):
		return self._images

	@images.setter
	def images(self, value):
		self._images = value

	@images.deleter
	def images(self):
		del self._images

	def __json__(self):
		return {
					'Title': self.houseTitle, 
					'Type': self.type, 
					'Period' : self.period,
					'Address' : self.address, 
					'Size' : self.size, 
					'Rooms' : self.rooms,
					'Deposit' : self.deposit,
					'MonthlyRent' : self.montlyRent,
					'paymentOnAccount' : self.paymentOnAccount,
					'Furnished' : self._furnished,
					'Smoking' : self._smoking,
					'Tenants' : self._tenants,
					'AddtionalDescription' : self._additionalDescription,
					'Name' : self._name,
					'Phone' : self._phone,
					'Email' : self._email,
					'Images' : self._images
				}




