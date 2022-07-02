from django.db import models

# Create your models here.

class customer(models.Model):
    cust_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    Email=models.EmailField( max_length=250)
    password=models.IntegerField()
    phone=models.CharField(max_length=11)
    address=models.CharField( max_length=150)

    def __str__(self)->str :
        return self.name

class order(models.Model):
    order_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    total_price=models.IntegerField()
    cust_id=models.ForeignKey(customer, on_delete=models.CASCADE)

    def __str__(self) ->str :
        return self.name


class cart(models.Model):
    pro_id=models.IntegerField(primary_key=True)
    order_id=models.ForeignKey(order, on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self) ->str :
        return self.pro_id


class product(models.Model):
    pro_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='proImg/')
    price=models.IntegerField()
    description=models.TextField(null=True)
    create_date=models.DateTimeField( auto_now_add=True, null=True)

    def __str__(self) ->str :
        return self.name




class sign_up(models.Model):
    user_name=models.CharField( max_length=50)
    Email=models.EmailField( max_length=250)
    password=models.IntegerField()
    phone=models.CharField(max_length=11)

    def __str__(self) ->str :
        return self.user_name



class payment(models.Model):
    pay_id=models.IntegerField(primary_key=True)
    order_id=models.ForeignKey(order, on_delete=models.CASCADE)
    Date=models.DateTimeField( auto_now_add=True, null=True)

    def __str__(self) ->str :
        return self.pay_id


class contactus(models.Model):
    name=models.CharField(max_length=50)
    Email=models.EmailField( max_length=250)
    massege=models.CharField(max_length=150)

    def __str__(self) ->str :
        return self.name



