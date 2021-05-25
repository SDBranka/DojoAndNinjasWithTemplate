from django.db import models

# Create your models here.
class dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NinjaManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data["first_name"]) < 1:
            errors["first_name"] = "Please enter your first name"
        if len(post_data["last_name"]) < 1:
            errors["last_name"] = "Please enter your last name"
        if len(post_data["dojo_id"]) < 1:
            errors["dojo"] = "Please enter a dojo"
        return errors

class ninjas(models.Model):
    dojo = models.ForeignKey(dojos, related_name="ninja", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = NinjaManager()

# def __repr__(self):
        # return f"<users object: {self.first_name}, {self.last_name}, {self.email_address}, {self.age}>"