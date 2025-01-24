from django.db import models

class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True
    )  # save data when object "created"
    updated_at = models.DateTimeField(
        auto_now=True,
    )  # save data when object "saved"

    class Meta:
        abstract = True  # Django will not add this model to database

