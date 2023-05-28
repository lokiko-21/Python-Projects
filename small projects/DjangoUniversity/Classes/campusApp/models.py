from django.db import models


# creates model manager model of University Campus
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # creates model manager
    object = models.Manager()

    # displays object output values in form of a string
    def __str__(self):
        # returns input value of the campus name
        # as a tuple to display in the browser
        display_campus = '{0.campus_name}'
        return display_campus.format(self)

    # removes 's' that django adds to the model name in browser
    class Meta:
        verbose_name_plural = "University Campus"
