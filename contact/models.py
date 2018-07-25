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

class Employee(models.Model):
    pass

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    session_id = models.IntegerField()
    user_type = models.CharField(max_length = 30)
    contact = models.ForeignKey('Contact', on_delete = models.CASCADE)


class Batch(models.Model):
    batch_number = models.CharField(max_length = 100)
    production_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    origin = models.CharField(max_length = 50)
    created_on = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = False)

    class Meta :
        ordering = ['-created_on']

class ProductLine(models.Model):
    name = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to = 'images', blank = True)
    description = models.TextField(blank = True, null = True)
    production_date = models.DateTimeField(auto_now_add = True)
    quantity = models.IntegerField(default = 0, blank = True, null = True)
    manufacturer_id = models.ForeignKey('Manufacturer', on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = False)

    class Meta :
        ordering = ['-created_on']

class Product(models.Model):
    product_line_id = models.ForeignKey('ProductLine', on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = False)

    class Meta :
        ordering = ['-created_on']

    def __unicode__(self) :
        return self.product_line_id

class ProductCode(models.Model):
    company_code = models.CharField(max_length = 4)
    product_line_code = models.CharField(max_length = 2)
    product_code = models.CharField(max_length = 10)



#This represents data stored for each internal verification
# a
# class FactoryCheck(models.Model):
#     employee_id = models.ForeignKey('Employee', on_delete = models.CASCADE)
#     date_checked = models.DateTimeField(auto_now = True)

#This will help us collect information about each external verification
#Including how many times a partivular code has been verified and by who where
# class UserCheck(models.Model):
#     user_id = models.ForeignKey('User', on_delete = models.CASCADE)
#     location = models.CharField()
#     date_checked = models.DateTimeField(auto_now = True)


# The following are options to be prepopulated and referenced from the Feedback Model (Table)
# 1.
# 2.
# 3.
# 4.
# 5.
# class FeedbackOption(models.Model):
#     option = models.IntegerField()
#     message = models.CharField()

# Feeeback from users
# Management may choose to reply a feeback
# class Feedback(models.Model):
#     user_id = models.ForeignKey('User', on_delete = models.CASCADE)
#     feeback_option = models.ForeignKey('FeedbackOption', on_delete = models.CASCADE)
    # ref = models.ForeignKey('self', null = True, blank = True)
    # pass



