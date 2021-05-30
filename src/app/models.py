from django.db import models

# Create your models here.
class Homepage(models.Model):
  
  name = models.CharField(max_length=255, help_text="Nome exibido na página inicial")
  subtitle = models.CharField(max_length=255, help_text="Subtitulo exibido abaixo do nome", blank=True, null=True)
  summary = models.TextField(help_text="Resumo", blank=True, null=True)
  
  background_image = models.ImageField(upload_to="background", help_text="Imagem do fundo da pagina", null=True, blank=True) 
  cover_image = models.ImageField(upload_to="cover", help_text="Imagem do card", null=True, blank=True) 
  profile_image = models.ImageField(upload_to="profile", help_text="Imagem de perfil", null=True, blank=True) 

  blog_button = models.BooleanField(default=True)
  portfolio_button = models.BooleanField(default=True)
  
  def __str__(self):
    return f"{self.name}" 

class HomepageLink(models.Model):
  class Meta:
    ordering = ['order']

  icon = models.CharField(max_length=255, help_text="Classe do icone do link")
  url = models.CharField(max_length=255, help_text="Url de destino do link")
  alt = models.CharField(max_length=255, help_text="Texto do link")
  
  order = models.DecimalField(max_digits=3, decimal_places=0)
  show = models.BooleanField(default=True)
  
  def __str__(self):
    return f"{self.order} - {self.alt} ({self.icon})"

class Post(models.Model):
  class Meta:
    ordering = ['-data_publicacao']

  title = models.CharField(max_length=255, help_text="Título da postagem")
  slug = models.CharField(max_length=255, help_text="Slug")
  data_publicacao = models.DateField(blank=True, null=True)
  plain_text = models.TextField(help_text="Conteúdo em texto", editable=False)
  markdown_text = models.TextField(help_text="Conteúdo em markdown")
  
  show = models.BooleanField(default=True)

  def __str__(self):
    return f"[{self.data_publicacao}] - {self.title}"

class Project(models.Model):
  name = models.CharField(max_length=255, help_text="Nome do projeto")
  description = models.TextField(max_length=2000, help_text="Descrição do projeto")
  image = models.ImageField(upload_to="projects", help_text="Imagem do projeto", null=True, blank=True) 
  technologies = models.CharField(max_length=255, help_text="Tecnologias utilizadas", blank=True, null=True)
  
  show = models.BooleanField(default=True)
  
  def __str__(self):
    return f"{self.name}"

class ProjectLink(models.Model):
  class Meta:
    ordering = ['-project']

  name = models.CharField(max_length=255, help_text="Texto do link")
  icon = models.CharField(max_length=255, help_text="Classe do icone do link")
  url = models.CharField(max_length=255, help_text="Url de destino do link")
  
  show = models.BooleanField(default=True)
  
  project = models.ForeignKey("Project", on_delete=models.CASCADE)
  
  def __str__(self):
    return f"[{self.project}] - {self.name} (Enable: {self.show})"
