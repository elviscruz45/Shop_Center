def total_cart_amount(request):
    total=0
    #for key,value in request.session["car"].items():
    #    total=total+(float(value["price"]))    
    
    if request.user.is_authenticated:
        for key,value in request.session["car"].items():
            total=total+(float(value["price"])*value["quantity"])
    
    #else:
    #    total="You have to login"
    return {"total_cart_amount":total}
