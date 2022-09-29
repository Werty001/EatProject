from ssl import SSLSession

class Cart:
	def __init__(self, request):
		self.request=request
		self.session=request.session
		cart=self.session.get("cart")
		if not cart:
			cart=self.session["cart"]={}
		#else:
		self.cart=cart
		
	def addItem(self, Item):
		if(str(Item.id) not in self.cart.keys()):
			self.cart[Item.id]={
				"Item_id":Item.id,
				"name":Item.name,
				"price":str(Item.price),
				"unit":1,
				"image": Item.image.url
				}
		else:
			for key, value in self.cart.items():
				if key==str(Item.id):
					value["unit"]=value["unit"]+1
					value["price"]=float(value["price"])+Item.price
					break
		self.save_cart()
		
	def save_cart(self):
		self.session["cart"]=self.cart
		self.session.modified=True

	def removeItem(self, Item):
		Item.id=str(Item.id)
		if Item.id in self.cart:
			del self.cart[Item.id]
	
	def subtractItem(self, Item):
		for key, value in self.cart.items():
				if key==str(Item.id):
					value["unit"]=value["unit"]-1
					value["price"]=float(value["price"])-Item.price
					if value["unit"]<1:
						self.removeItem(Item)
					break
		self.save_cart()

	def cleanCart(self):
		self.session["cart"]={}
		self.session.modified=True


