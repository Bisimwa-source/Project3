from django.db import models

# Create your models here.
class Meta:
    managed = False
    db_table = 'Companies'



from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=150, unique=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    website = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Companies'

    def __str__(self):
        return self.company_name


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='company_id')
    title = models.CharField(max_length=150)
    salary_range = models.CharField(max_length=100, null=True, blank=True)
    job_type = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    posted_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Jobs'

    def __str__(self):
        return self.title


class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, db_column='job_id')
    status = models.CharField(max_length=100)
    applied_date = models.DateField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Applications'

    @property
    def days_since_applied(self):
        from datetime import date
        return (date.today() - self.applied_date).days

    def __str__(self):
        return f"{self.job.title} - {self.status}"



