from django.db import models


class Library(models.Model):
    # Basic Information
    name = models.CharField(max_length=200)
    number_of_books = models.IntegerField()
    number_of_members = models.IntegerField()

    # Contact Information
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    # Getter Methods
    def get_contact_info(self):
        return {
            "address": self.address,
            "phone_number": self.phone_number,
            "email": self.email,
        }

    def get_name(self):
        return self.name

    def get_number_of_books(self):
        return self.number_of_books

    def get_number_of_members(self):
        return self.number_of_members

    # Setter Methods
    def set_name(self, name):
        self.name = name
        self.save()

    def set_number_of_books(self, increment_or_decrement):
        if increment_or_decrement == "increment":
            self.number_of_books += 1
        elif increment_or_decrement == "decrement":
            self.number_of_books -= 1
        else:
            raise ValueError("Invalid increment_or_decrement value")

        self.save()

    def set_number_of_members(self, increment_or_decrement):
        if increment_or_decrement == "increment":
            self.number_of_members += 1
        elif increment_or_decrement == "decrement":
            self.number_of_members -= 1
        else:
            raise ValueError("Invalid increment_or_decrement value")

        self.save()

    def set_address(self, address):
        self.address = address
        self.save()

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
        self.save()

    def set_email(self, email):
        self.email = email
        self.save()

    def __str__(self):
        return self.name
