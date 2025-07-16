
from ..models.manifacturation import Manifacturation, ManifacturationArticle
from ..models.article import Article
from rest_framework import serializers
from .manifacturationArticleSerializer import ManifacturationArticleSerializer
from ..models.stock import Stock
from ..models.user import User
from .userSerializer import UserSerializer
from ..services.availibilitieServices import is_fabriqueur_available
from rest_framework.exceptions import ValidationError


class ManifacturationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, required=False)
    project_leader = UserSerializer(read_only=True)
    project_leader_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, required=False)
    articles_with_quantity = serializers.ListField(
        child=serializers.DictField(child=serializers.CharField()), write_only=True , required=False
    )
    article_details = serializers.SerializerMethodField()
    #semaine = serializers.IntegerField(required=False)

    carte_acceptation = serializers.StringRelatedField()
    #, 'quantity_produced',
    class Meta:
        model = Manifacturation
        fields = [ 'id','product_name', 'status', 'user', 'user_id','status_admin','start_date','end_date', 'notes'
            ,'articles_with_quantity', 'article_details', 'carte_acceptation','project_leader', 'project_leader_id'
            , 'ref_frame', 'nombre_canaux', 'longeur', 'num_outillage', 'programme'
            , 'longeurFt1', 'longeurFt2' , 'longeurFt3', 'longeurFt4', 'tulipe']

    def append_suffix_to_nombrecanaux(self, nombre_canaux):
        if nombre_canaux and not str(nombre_canaux).endswith('C'):
            return f"{nombre_canaux}C"
        return nombre_canaux

    def get_article_details(self, obj):
        return ManifacturationArticleSerializer(ManifacturationArticle.objects.filter(manifacturation=obj), many=True).data

    def create(self, validated_data):
        articles_data = validated_data.pop('articles_with_quantity', [])
        user = validated_data.pop('user_id', None)
        project_leader = validated_data.pop('project_leader_id', None)
        nombre_canaux = validated_data.get('nombre_canaux')
        validated_data['nombre_canaux'] = self.append_suffix_to_nombrecanaux(nombre_canaux)
        instance = Manifacturation.objects.create(user=user,project_leader=project_leader , **validated_data)

        if articles_data:
            self.handle_articles_with_quantity(instance, articles_data)

        return instance

    def update(self, instance, validated_data):
        articles_data = validated_data.pop('articles_with_quantity', [])
        user = validated_data.pop('user_id', None)
        project_leader = validated_data.pop('project_leader_id', None)
        nombre_canaux = validated_data.get('nombre_canaux', instance.nombre_canaux)
        instance.nombre_canaux = self.append_suffix_to_nombrecanaux(nombre_canaux)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if user:
            instance.user = user
        if project_leader:
            instance.project_leader = project_leader
        instance.save()

        if articles_data:
            ManifacturationArticle.objects.filter(manifacturation=instance).delete()
            self.handle_articles_with_quantity(instance, articles_data)

        return instance

    def handle_articles_with_quantity(self, instance, articles_data):
        for item in articles_data:
            article = Article.objects.get(id=item['article'])
            #quantity_used = item['quantity_consume']
            quantity_used = int(item['quantity_consume'])
            ManifacturationArticle.objects.create(
                manifacturation=instance,
                article=article,
                quantite_consume=quantity_used
            )

            try:
                # stock = Stock.objects.get(article=article)
                # stock.total_quantity_used += quantity_used
                # stock.quantity = max(stock.quantity - quantity_used, 0)
                # stock.save()
                stock = Stock.objects.get(article=article)
                stock.total_quantity_used += quantity_used
                stock.virtual_stock = max(stock.virtual_stock - quantity_used, 0)
                stock.save()


            except Stock.DoesNotExist:
                print(f" stock not found for article {article.id}")

    # def validate(self, data):
    #     user = data.get('user_id', getattr(self.instance, 'user', None))
    #     sd = data.get('start_date', getattr(self.instance, 'start_date', None))
    #     ed = data.get('end_date', getattr(self.instance, 'end_date', None))
    #
    #     if user and sd and ed:
    #         if sd > ed:
    #             raise serializers.ValidationError({"end_date": "La date de fin doit être après la date de début."})
    #         if not is_fabriqueur_available(user, sd, ed):
    #             raise serializers.ValidationError({"user": "Ce Fabriquant n’est pas disponible pour cette période."})
    #
    #     return data

    def validate(self, data):
        sd = data.get('start_date', getattr(self.instance, 'start_date', None))
        ed = data.get('end_date', getattr(self.instance, 'end_date', None))

        if sd and ed and sd > ed:
            raise serializers.ValidationError({"end_date": "La date de fin doit être après la date de début."})

        return data
