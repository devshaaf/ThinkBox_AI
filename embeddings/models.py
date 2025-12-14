from django.db import models
from documents.models import DocumentChunk

# Create your models here.


class Embeddings(models.Model):
    chunk = models.ForeignKey(DocumentChunk, on_delete=models.CASCADE)
    vector = models.JSONField()
    dimension = models.IntegerField()
    faiss_index_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)