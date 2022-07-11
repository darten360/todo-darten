from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tags")

    def __str__(self):
        return f"{self.content}"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]