from django.db import models


class Location(models.Model):
    location= models.CharField(max_length=50)

    def __str__(self):
        return self.location

class Register(models.Model):
    #objects = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cleaned_date = None

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user_name=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=15)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    gender_male=models.BooleanField('Male',default=False)
    gender_female=models.BooleanField('Female',default=False)
    gender_other= models.BooleanField('Other',default=False)
    email_id=models.EmailField()
    profession=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    date_of_birth=models.DateField(max_length=10,default=False)

    def is_valid(self):
        pass



