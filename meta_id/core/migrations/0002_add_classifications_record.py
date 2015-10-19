# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def insert_classifications(apps, schema_editor):
    data = [
        {
            "area": "Arquitetura e Urbanismo",
            "estilos": [
                "Arquitetura",
                "Urbanismo",
                "Design"
            ]
        },
        {
            "area": u"Artes Visuais",
            "estilos": [
                u"Exposição de Artes em geral"
            ]
        },
        {
            "area": u"Artesanato",
            "estilos": [
                u"Artesanato de Tradição",
                u"Artesanato Indígena",
                u"Artesanato de Referência Cultural",
                u"Artesanato Conceitual"
            ]
        },
        {
            "area": u"Audiovisual",
            "estilos": [
                u"Animação",
                u"Curta Metragem",
                u"Longa Metragem"
            ]
        },
        {
            "area": u"Artes Circenses",
            "estilos": [
                u"Artes cirsenses em geral",
                u"Mágicas"
            ]
        },
        {
            "area": u"Cultural Digital",
            "estilos": [
                u"Sites, Portais, Blogs",
                u"Redes Sociais",
                u"Outra Manifestação Cultural em meio digital"
            ]
        },
        {
            "area": u"Cultura dos Povos Indígenas",
            "estilos": [
                u"Dança",
                u"Música",
                u"Outra Manifestação da Cultura Indígena"
            ]
        },
        {
            "area": u"Culturas Afro-brasileiras",
            "estilos": [
                u"Artes",
                u"Dança",
                u"Música",
                u"Religiosa",
                u"Outra Manifestação da cultura Afro-brasileira"
            ]
        },
        {
            "area": u"Cultura Populares",
            "estilos": [
                u"Folclore",
                u"Música",
                u"Dança",
                u"Outra Manifestação da Cultura Popular"
            ]
        },
        {
            "area": u"Dança",
            "estilos": [
                u"Dança Clássica",
                u"Dança Moderna",
                u"Dança de Rua",
                u"Dança de Salão",
                u"Danças Brasileiras"
            ]
        },
        {
            "area": u"Design",
            "estilos": [
                u"Manifestação em Design Cultural"
            ]
        },
        {
            "area": u"Livro, Leitura e Literatura",
            "estilos": [
                u"Mediação de Leitura",
                u"Livro e Literatura",
                u"Literatura de Cordel",
                u"Literatura Infantil",
                u"Literatura Juvenil",
                u"Romance",
                u"Ensaio",
                u"Poesia",
                u"Crônica",
                u"Conto",
                u"Novela",
                u"Microconto",
                u"História em quadrinhos"
            ]
        },
        {
            "area": u"Moda",
            "estilos": [
                u"Expressão Artística da Moda",
                u"Pesquisa de Tendências (Cool hunting)",
                u"Styling",
                u"Produção de Moda",
                u"Estamparia",
                u"Estilismo",
                u"Fotografia",
                u"Figurinista",
                u"Jornalismo",
                u"Modelista",
                u"Pilotista",
                u"Web designer",
                u"Designer Gráfico"
            ]
        },
        {
            "area": u"Música e Ópera",
            "estilos": [
                u"Pop",
                u"Rock Nacional",
                u"Rock Internacional",
                u"Pagode",
                u"Samba",
                u"Forró",
                u"Sertanejo",
                u"MPB",
                u"Bossa Nova",
                u"Instrumental",
                u"Clássica",
                u"Rap",
                u"Hip-Hop",
                u"Funk",
                u"Jazz",
                u"Soul",
                u"Eletrônica",
                u"Gospel",
                u"Ópera",
                u"Regional/Popular Brasileira",
                u"Blues",
                u"Rap Gospel",
                u"Hip Hop Gospel",
                u"Rock Gospel",
                u"Pagode Gospel",
                u"Funk Gospel",
                u"Reggae Gospel",
                u"Axé / Swingueira",
                u"RnB",
                u"Reggae",
                u"Multiplicidade"
            ]
        },
        {
            "area": u"Patrimônio Material e Imaterial",
            "estilos": [
                u"Bens Culturais",
                u"Manifestações Culturais de Patrimônio Imaterial"
            ]
        },
        {
            "area": u"Teatro",
            "estilos": [
                u"Auto",
                u"Comédia",
                u"Drama",
                u"Farsa",
                u"Melodrama",
                u"Mimica",
                u"Monólogo",
                u"Musical",
                u"Revista",
                u"Stand-up Comedy",
                u"Tragédia",
                u"Infantil",
                u"Fantoches",
                u"Teatro de Rua",
                u"Circo"
            ]
        },
        {
            "area": u"Àreas Tranversais",
            "estilos": [
                u"Educação",
                u"Ciência",
                u"Comunicação",
                u"Cultura",
                u"Outras"
            ]
        },
        {
            "area": u"Outros",
            "estilos": [
                "Outros estilos não especificados"
            ]
        },
        {
            "area": u"Canto e Orquestra",
            "estilos": [
                u"Regente",
                u"Solista",
                u"Instrumentista",
                u"Coral Erudito",
                u"Coral Pupular",
                u"Maestro"
            ]
        },
        {
            "area": u"Arte Urbana",
            "estilos": [
                u"Rap",
                u"DJ",
                u"Grafite",
                u"Break"
            ]
        },
        {
            "area": u"Formação Cultural",
            "estilos": [
                u"Oficineiro",
                u"Palestrante/Expositor",
                u"Instrutor"
            ]
        }
    ]

    ClassificacaoArtistica = apps.get_model("core", "ClassificacaoArtistica")
    for classificacao in data:
        ClassificacaoArtistica.objects.create(**classificacao)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_classifications)
    ]
