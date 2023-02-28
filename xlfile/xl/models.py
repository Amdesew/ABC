from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description


class New_Students(models.Model):
    full_name = models.CharField(max_length=100)
    wanted_class = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=9)
    class Meta:
        pass

class Grade_One(models.Model):
    ተ_ቁ = models.CharField(max_length=500)
    ተማሪው_ዋ_ስም = models.CharField(max_length=500)
    ፆታ = models.CharField(max_length=15)
    አማርኛ = models.CharField(max_length=50)
    English  = models.CharField(max_length=50)
    Maths  =  models.CharField(max_length=50)
    G_science = models.CharField(max_length=50)
    ህ_ሰብ = models.CharField(max_length=50)
    ዜግነት = models.CharField(max_length=50)
    ጤናና_ሰ_ማጎ = models.CharField(max_length=50)
    ሥነጥበባት = models.CharField(max_length=50)
    ድምር = models.CharField(max_length=50)
    አማካይ = models.CharField(max_length=50)
    ደረጃ = models.CharField(max_length=50)
    ምርመራ = models.CharField(max_length=50) 
    class Meta:
        db_table = 'Grade_One'

class Grade_Two(models.Model):
    ተ_ቁ = models.CharField(max_length=500)
    ተማሪው_ዋ_ስም = models.CharField(max_length=500)
    ፆታ = models.CharField(max_length=15)
    አማርኛ = models.CharField(max_length=50)
    English  = models.CharField(max_length=50)
    Maths  =  models.CharField(max_length=50)
    G_science = models.CharField(max_length=50)
    ህ_ሰብ = models.CharField(max_length=50)
    ዜግነት = models.CharField(max_length=50)
    ጤናና_ሰ_ማጎ = models.CharField(max_length=50)
    ሥነጥበባት = models.CharField(max_length=50)
    ድምር = models.CharField(max_length=50)
    አማካይ = models.CharField(max_length=50)
    ደረጃ = models.CharField(max_length=50)
    ምርመራ = models.CharField(max_length=50) 
    class Meta:
        db_table = 'Grade_Two'

class Grade_Three(models.Model):
    ተ_ቁ = models.CharField(max_length=500)
    ተማሪው_ዋ_ስም = models.CharField(max_length=500)
    ፆታ = models.CharField(max_length=15)
    አማርኛ = models.CharField(max_length=50)
    English  = models.CharField(max_length=50)
    Maths  =  models.CharField(max_length=50)
    G_science = models.CharField(max_length=50)
    ህ_ሰብ = models.CharField(max_length=50)
    ዜግነት = models.CharField(max_length=50)
    ጤናና_ሰ_ማጎ = models.CharField(max_length=50)
    ሥነጥበባት = models.CharField(max_length=50)
    ድምር = models.CharField(max_length=50)
    አማካይ = models.CharField(max_length=50)
    ደረጃ = models.CharField(max_length=50)
    ምርመራ = models.CharField(max_length=50) 
    class Meta:
        db_table = 'Grade_Three'

class Grade_Four(models.Model):
    ተ_ቁ = models.CharField(max_length=500)
    ተማሪው_ዋ_ስም = models.CharField(max_length=500)
    ፆታ = models.CharField(max_length=15)
    አማርኛ = models.CharField(max_length=50)
    English  = models.CharField(max_length=50)
    Maths  =  models.CharField(max_length=50)
    G_science = models.CharField(max_length=50)
    ህ_ሰብ = models.CharField(max_length=50)
    ዜግነት = models.CharField(max_length=50)
    ጤናና_ሰ_ማጎ = models.CharField(max_length=50)
    ሥነጥበባት = models.CharField(max_length=50)
    ድምር = models.CharField(max_length=50)
    አማካይ = models.CharField(max_length=50)
    ደረጃ = models.CharField(max_length=50)
    ምርመራ = models.CharField(max_length=50) 
    class Meta:
        db_table = 'Grade_Four'

class Grade_Five(models.Model):
    ተ_ቁ = models.CharField(max_length=500)
    ተማሪው_ዋ_ስም = models.CharField(max_length=500)
    ፆታ = models.CharField(max_length=15)
    አማርኛ = models.CharField(max_length=50)
    English  = models.CharField(max_length=50)
    Maths  =  models.CharField(max_length=50)
    G_science = models.CharField(max_length=50)
    ህ_ሰብ = models.CharField(max_length=50)
    ዜግነት = models.CharField(max_length=50)
    ጤናና_ሰ_ማጎ = models.CharField(max_length=50)
    ሥነጥበባት = models.CharField(max_length=50)
    ድምር = models.CharField(max_length=50)
    አማካይ = models.CharField(max_length=50)
    ደረጃ = models.CharField(max_length=50)
    ምርመራ = models.CharField(max_length=50) 
    class Meta:
        db_table = 'Grade_Five'

class Grade_Six(models.Model):
    ተ_ቁ = models.CharField(max_length=50)
    ተማሪው_ዋ_ስም = models.CharField(max_length=50)
    ፆታ = models.CharField(max_length=15)
    አማርኛ = models.CharField(max_length=50)
    English  = models.CharField(max_length=50)
    Maths  =  models.CharField(max_length=50)
    G_science = models.CharField(max_length=50)
    ህ_ሰብ = models.CharField(max_length=50)
    ዜግነት = models.CharField(max_length=50)
    ጤናና_ሰ_ማጎ = models.CharField(max_length=50)
    ሥነጥበባት = models.CharField(max_length=50)
    ድምር = models.CharField(max_length=50)
    አማካይ = models.CharField(max_length=50)
    ደረጃ = models.CharField(max_length=50)
    ምርመራ = models.CharField(max_length=50) 
    class Meta:
        db_table = 'Grade_Six'

class Grade_Seven(models.Model):
    ተ_ቁ = models.CharField(max_length=50)
    ተማሪው_ዋ_ስም = models.CharField(max_length=50)
    ፆታ = models.CharField(max_length=15)
    አማርኛ = models.CharField(max_length=50)
    English  = models.CharField(max_length=50)
    Maths  =  models.CharField(max_length=50)
    G_science = models.CharField(max_length=50)
    ህ_ሰብ = models.CharField(max_length=50)
    ዜግነት = models.CharField(max_length=50)
    ጤናና_ሰ_ማጎ = models.CharField(max_length=50)
    ሥነጥበባት = models.CharField(max_length=50)
    ድምር = models.CharField(max_length=50)
    አማካይ = models.CharField(max_length=50)
    ደረጃ = models.CharField(max_length=50)
    ምርመራ = models.CharField(max_length=50) 
    class Meta:
        db_table = 'Grade_Seven'

class Grade_Eight(models.Model):
    ተ_ቁ = models.CharField(max_length=50)
    ተማሪው_ዋ_ስም = models.CharField(max_length=50)
    ፆታ = models.CharField(max_length=15)
    አማርኛ = models.CharField(max_length=50)
    English  = models.CharField(max_length=50)
    Maths  =  models.CharField(max_length=50)
    G_science = models.CharField(max_length=50)
    ህ_ሰብ = models.CharField(max_length=50)
    ዜግነት = models.CharField(max_length=50)
    ጤናና_ሰ_ማጎ = models.CharField(max_length=50)
    ሥነጥበባት = models.CharField(max_length=50)
    ድምር = models.CharField(max_length=50)
    አማካይ = models.CharField(max_length=50)
    ደረጃ = models.CharField(max_length=50)
    ምርመራ = models.CharField(max_length=50) 
    class Meta:
        db_table = 'Grade_eight'