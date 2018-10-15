from django.db import models

# Create your models here.

class Token(models.Model):
    # id = models.Autofield(primary_key=True)
    token = models.CharField(max_length=100)
    ttl = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.token, self.ttl)

class Superadmin(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Subadmin(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    # token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Borrower(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.token_id)

class Facility(models.Model):
    name = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    quantity = models.IntegerField()
    borrower_id = models.ForeignKey(Borrower, null=True, on_delete=models.CASCADE)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Equipment(models.Model):
    name = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    quantity = models.IntegerField()
    borrower_id = models.ForeignKey(Borrower, null=True, on_delete=models.CASCADE)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)
        # return "{0} - {1} - {2}".format(self.name, self.status, self.borrower_id)

class Reservation(models.Model):
    Reserver_ID = models.IntegerField()
    Status = models.IntegerField()
    Cancelled = models.IntegerField()
    Type = models.IntegerField()
    Name_reserved = models.CharField(max_length=50)
    Date_Resereved = models.DateField(auto_now_add=True)
    Date_Return = models.DateField()
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)
    #     return "{0} - {1} - {2}".format(self.Reserver_ID, self., self.,self.,self.,self.,self.)

class BorrowerLogs(models.Model):
    Borrower_ID = models.IntegerField()
    Approver_ID = models.IntegerField()
    Type = models.IntegerField()
    Name_Borrowed = models.CharField(max_length=50)
    Date_Borrowed = models.DateField()
    Date_Return = models.DateField()
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)
    #     return "{0} - {1} - {2}x".format(self.Borrower_ID, self.Approver_ID, self.Type,self.Name_Borrowed,self.Date_Borrowed,self.Date_Return)

class Logs(models.Model):
    User_ID = models.IntegerField()
    action = models.CharField(max_length=50)
    Date = models.DateField(auto_now_add=True)
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)
    #     return "{0} - {1} - {2}".format(self.User_ID, self.action, self.Date)
