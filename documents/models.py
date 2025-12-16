from django.db import models
from django.db.models import constraints

from workspaces.models import WorkSpace
from users.models import User

# Create your models here.


class Document(models.Model):

    class EmbeddingStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PROCESSING = 'PROCESSING', 'Processing'
        COMPLETED = 'COMPLETED', 'Completed'

    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    embeddings_status = models.CharField(max_length=10, choices=EmbeddingStatus.choices)
    meta_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['workspace', 'title'],
                name = 'unique_title_document_per_workspace'
            )
        ]



class DocumentChunk(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    content = models.TextField()
    chunk_index = models.IntegerField()
    token_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['document', 'chunk_index'],
                name = 'unique_chunkindex_per_doc'
            )
        ]