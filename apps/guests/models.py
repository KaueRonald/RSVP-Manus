# from django.db import models

# # NOTE: These models seem redundant as similar models exist in apps.events
# #       which are correctly linked to the Event model. 
# #       Commenting these out to avoid conflicts. 
# #       Ensure these are not used elsewhere or update references.

# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     class Meta:
#         verbose_name = "Categoria"
#         verbose_name_plural = "Categorias"

#     def __str__(self):
#         return self.name

# class GuestGroup(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE,
#         related_name="groups"
#     )

#     class Meta:
#         verbose_name = "Grupo de Convidados"
#         verbose_name_plural = "Grupos de Convidados"

#     def __str__(self):
#         return f"{self.name} ({self.category.name})"

