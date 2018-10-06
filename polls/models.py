from django.db import models

# Create your models here.
class Token(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=100)
    ttl = models.DateField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.token, self.ttl)

class Superadmin(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.token_id)

class Subadmin(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.token_id)

class Borrower(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.token_id)

class Facility(models.Model):
    name = models.CharField(max_length=70)
    status = models.IntegerField(max_length=1)
    borrower_id = models.ForeignKey(Borrower, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.status, self.borrower_id)