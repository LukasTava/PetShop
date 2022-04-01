from django.db import models


class Pet(models.Model):
    nome = models.CharField(max_length=100)
    dono = models.CharField(max_length=100)
    telefone = models.DecimalField(max_digits=12, decimal_places=0)
    lagradouro = models.CharField("Lagradouro", max_length=1024, default='Rua')
    numero = models.DecimalField("Numero", max_digits=5, decimal_places=0, default=0)
    bairro = models.CharField("Bairro", max_length=600, default='Centro')
    cidade = models.CharField("Cidade", max_length=1024, default='Cidade')
    estado = models.CharField("Estado", max_length=2, default='UF')

    def __str__(self):
        return self.nome


class Responsavel(models.Model):
    ATEDENDENTE = 'Atendente'
    VETERINARIO = 'Veterinário'
    TIPOS_RESPONSAVEL = [
        (ATEDENDENTE, 'Atendente'), (VETERINARIO, 'Veterinário'),
    ]
    nome = models.CharField(max_length=100, default="Nome")
    telefone = models.DecimalField(max_digits=12, decimal_places=0, default=0000)
    lagradouro = models.CharField("Lagradouro", max_length=1024, default='Rua')
    numero = models.DecimalField("Numero", max_digits=5, decimal_places=0, default=0)
    bairro = models.CharField("Bairro", max_length=600, default='Centro')
    cidade = models.CharField("Cidade", max_length=1024, default='Cidade')
    estado = models.CharField("Estado", max_length=2, default='UF')
    tipo = models.CharField(
        max_length=32,
        choices=TIPOS_RESPONSAVEL,
        default='Atendente',
    )

    def __str__(self):
        return self.nome


class Atendimento(models.Model):
    tipo = models.CharField(max_length=100)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=1000)
    data = models.DateTimeField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo