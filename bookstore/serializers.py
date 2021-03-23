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
        fields  = ['id','author_name','url']



class BookSerializer(serializers.ModelSerializer):

    
    author_name=Authorserializer(many=True)
    
    class Meta:
        model = Book
        fields = ['id','title','description','publisher','release_date','author_name']

    def create(self, validated_data):
        author_name = validated_data.pop('author_name')
        book = Book.objects.create(**validated_data)
        for author in author_name:
            author, created = Author.objects.get_or_create(author_name=author['author_name'])
            book.author_name.add(author)
        book.save()
        return book

    def update(self, instance, validated_data):
        author_name = validated_data.get('author_name',None)
        instance.title = validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        instance.publisher=validated_data.get('publisher',instance.publisher)
        instance.release_date=validated_data.get('release_date',instance.release_date)
        while author_name is not None:
            authors_list = []
            for author in author_name:
                author, created = Author.objects.get_or_create(author_name=author['author_name'])
                authors_list.append(author)
            instance.author_name.set(authors_list)
            break
        instance.save()
        return instance 

        # authors_list = []
        # try:
        #     author_name = validated_data.pop('author_name')
        #     for author in author_name:
        #         print(author)
        #         author, created = Author.objects.get_or_create(author_name=author['author_name'])
        #         authors_list.append(author)
    
        # except:
        #     authors_list = []
        #     for i in instance.author_name.all():
        #         authors_list.append(i)
        # instance.author_name.set(authors_list)
        # instance.title = validated_data.get('title', instance.title)
        # instance.description=validated_data.get('description', instance.description)
        # instance.publisher = validated_data.get('publisher', instance.publisher) 
        # instance.release_date = validated_data.get('release_date', instance.release_date)
        # instance.save()
        # return instance

