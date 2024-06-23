from ..models import User

class UserRepository:
    def get_user_by_discord_id(self, discord_id):
        return User.objects.get(discord_id=discord_id)

    def create_user(self, validated_data):
        return User.objects.create(**validated_data)

    def get_all_users(self):
        return User.objects.all()
