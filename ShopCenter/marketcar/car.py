class Car:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        car=self.session.get("car")
        if not car:
            car=self.session["car"]={}
        else:
            self.car=car
    
    def add(self,product):
        if(str(product.id) not in self.car.keys()):
            self.car[product.id]={
                "product_id":product.id,
                "name":product.name,
                "price":str(product.price),
                "quantity":1,
                "image":product.image.url
            }
        else:
            for key,value in self.self.car.items():
                if key==str(product.id):
                    value["quantity"]=value["quantity"]+1
                    break
        
        self.save_car()
    
    def save_car(self):
        self.session["carro"]=self.car
        self.session.modified=True
    
    def delete(self,product):
        product.id=str(product.id)
        if product.id in self.carro:
            del self.car[product.id]
            self.save_car()
    
    def quit_product(self,product):
        for key,value in self.car.items():
            if key==str(product.id):
                value["quantity"]=value["quantity"]-1
                if value["quantity"]<1:
                    self.delete(product)
                break
        self.save_car()

    def clean_car(self):
        self.session["car"]={}
        self.session.modified=True
