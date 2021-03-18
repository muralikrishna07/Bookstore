from rest_framework import serializers
from .models import Book,Author
from rest_framework.response import Response

# from django.contrib.auth

class Authorserializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'author-detail',
        lookup_field = 'pk'
    )

    
    class Meta:
        model = Author
        fields  = ['id','name','url']



class BookSerializer(serializers.ModelSerializer):

    
    author=Authorserializer(many=True,read_only=True)
    
    class Meta:
        model = Book
        fields = ['id','title','description','publisher','release_date','author']

    def create(self, validated_data):
        author = validated_data.pop('author')
        book = Book.objects.create(**validated_data)
        for author in author:
            author, created = Author.objects.get_or_create(name=author['name'])
            book.author.add(author)
        book.save()
        return book

    def partial_update(self, instance, validated_data,partial=True):
        author = validated_data.pop('author')
        instance.title = validated_data['title']
        instance.description=validated_data['description']
        instance.publisher=validated_data['publisher']
        instance.release_date=validated_data['release_date']

        # instance.author = validated_data['author']
        # instance.publication_date = validated_data['publication_date']
        authors_list = []
        for author in author:
            author, created = Author.objects.get_or_create(name=author['name'])
            authors_list.append(author)
        instance.author.set(authors_list)
        instance.save()
        return instance 
    


    

