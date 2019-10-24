from rest_framework import serializers
from items.models import Item
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name']

class ItemListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "item-detail",
		lookup_field = "id",
		lookup_url_kwarg = "item_id"
		)
	added_by = UserSerializer()

	favorites = serializers.SerializerMethodField()
	def get_favorites(self, obj):
		return len(obj.favoriteitem_set.all())
		# return obj.favoriteitem_set.all().count()


	class Meta:
		model = Item
		fields = ['image', 'name', 'description', 'id', 'added_by', 'favorites', 'detail']

class ItemDetailSerializer(serializers.ModelSerializer):
	
	favorites_name = serializers.SerializerMethodField()
	def get_favorites_name(self, obj):
		favorites = obj.favoriteitem_set.all()
		users=[]
		for fave in favorites:
	# 		users.append(User.objects.get(id=fave.user.id))
			users.append(fave.user)
		return UserSerializer(users, many=True).data

		# for fave in favorites.values_list("user"):
		# 	users.append(User.objects.get(id=fave[0]))

	class Meta:
		model = Item
		fields = ['image', 'name', 'description', 'id', 'favorites_name']
