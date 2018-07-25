from django.db import models

# Create your models here.
class Contact(models.Model):
    phone_number = models.CharField(max_length = 15)
    email = models.CharField(max_length = 100)
    location = models.CharField(max_length = 150)
    correspondence = models.CharField(max_length = 150)
    created_on = models.DateTimeField(auto_now_add = True)

    class Meta :
        ordering = ['-created_on']

# includes external users and emplyees of companies
class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'images', blank = True)
    session_id = models.IntegerField()
    user_type = models.CharField(max_length = 30)
    username = models.CharField(unique = True, max_length = 30)
    password = models.CharField(max_length = 128)
    date_created = models.DateTimeField()
    dob = models.DateField()
    contact = models.ForeignKey('Contact', on_delete = models.CASCADE)
    # company_id is the id of the manufacturer that the employee works for
    company_id = models.ForeignKey('Manufacturer', on_delete = models.CASCADE)
    pass

class Manufacturer(models.Model):
    name = models.CharField(max_length = 30)
    code = models.IntegerField(default = 0, blank = True, null = True, unique = True)
    industry = models.CharField(max_length = 100)
    modified = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = False)
    created_on = models.DateTimeField(auto_now_add = True)
    contact = models.ForeignKey('Contact', on_delete = models.CASCADE)

    class Meta :
        ordering = ['-created_on']

    def __unicode__(self) :
        return u'{} Code:{} industry:{}'.format(self.name, str(self.code), self.industry)

class Batch(models.Model):
    production_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    batch_number = models.IntegerField(unique = True, blank = True, null = True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE)
    origin = models.CharField(max_length = 50)
    created_on = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = False)
    manufacturer = models.ForeignKey('Manufacturer', on_delete = models.CASCADE)

    def __str__(self) :
        return "{}: {}".format(self.manufacturer.name, self.batch_number)

    class Meta :
        ordering = ['-created_on']

class ProductLine(models.Model):
    product_name = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    photo = models.ImageField(upload_to = 'images', blank = True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete = models.CASCADE, blank = True, null = True)
    quantity = models.IntegerField(default = 0, blank = True, null = True)
    production_date = models.DateTimeField(auto_now_add = True)
    created_on = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = False)

    def __str__(self) :
        return self.product_name

    class Meta :
        ordering = ['-created_on']

class Product(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    product_code = models.IntegerField(unique = True)
    product_line = models.ForeignKey(ProductLine, on_delete = models.CASCADE)
    is_active = models.BooleanField(default = False)
    batch_number = models.ForeignKey(Batch, on_delete = models.CASCADE)

    def __str__(self) :
        return str(self.product_code)

    def __unicode__(self) :
        return self.product_line_id

    class Meta :
        ordering = ['-created_on']

class ProductCode(models.Model):
    company_code = models.CharField(max_length = 4)
    product_line_code = models.CharField(max_length = 2)
    product_code = models.CharField(max_length = 10)

class Location(models.Model):
    name = models.CharField(max_length = 150)
    latitude = models.FloatField()
    longitude = models.FloatField()

#This represents data stored for each internal verification
# a
class FactoryCheck(models.Model):
    employee_id = models.ForeignKey('User', on_delete = models.CASCADE)
    date_checked = models.DateTimeField(auto_now = True)

#This will help us collect information about each external verification
#Including how many times a partivular code has been verified and by who where
class UserCheck(models.Model):
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    location_id = models.ForeignKey('Location', on_delete = models.CASCADE)
    date_checked = models.DateTimeField(auto_now = True)

# The following are options to be prepopulated and referenced from the Feedback Model (Table)
# 1.
# 2.
# 3.
# 4.
# 5.
class FeedbackOption(models.Model):
    option = models.IntegerField()
    message = models.CharField(max_length = 150)

# Feeeback from users
# Management may choose to reply a feeback
class Feedback(models.Model):
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    feeback_option = models.ForeignKey('FeedbackOption', on_delete = models.CASCADE)
    # ref = models.ForeignKey('self', null = True, blank = True)
    # pass



