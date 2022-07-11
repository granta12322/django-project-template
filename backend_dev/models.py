from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(default = "My Fun Event", max_length= 100)
    venue = models.ForeignKey(to = "Venue", related_name= "events", on_delete= models.CASCADE,null = True)  # !!! Cascade for now but deleted venue shouldn't delete event
    organiser = models.ForeignKey(to = "users.User", related_name="events", on_delete = models.CASCADE, null = True)
    creation_date = models.DateField(auto_now_add = True)
    start_datetime = models.DateTimeField(null = False, default = "2022-12-07 12:00:00")

class Venue(models.Model):
    name = models.CharField(default = "My House", max_length= 100)
    address = models.CharField(default = "9 Bruce Street", max_length= 100)

class Ticket(models.Model):
    owner = models.ForeignKey(to = "users.User", related_name = "tickets", on_delete = models.CASCADE, null = True) # !!! Cascade for now but if user deletes account then ticket should be returned to owner
    event = models.ForeignKey(to = "Event", related_name = "tickets", on_delete = models.CASCADE)
    type = models.CharField(default = "Standard Entry", max_length = 100) # ! Needs changing to a foreignKey field



class TicketType(models.Model):
    name = models.CharField(default = "Basic Ticket Type", max_length= 50)
    event = models.ForeignKey(to = "Event", related_name = "ticket_types", on_delete = models.CASCADE)
    price = models.FloatField(default = 6.9)
    sale_date = models.DateTimeField(default = "2022-07-12 12:00:00")