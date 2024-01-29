from django.db import transaction
from .models import PerevalAdded, User, Coords


class DataManager:
    @staticmethod
    @transaction.atomic
    def add_pereval(data):
        user_data = data['user']
        coords_data = data['coords']

        user, created = User.objects.get_or_create(
            email=user_data['email'],
            defaults={'fam': user_data['fam'], 'name': user_data['name'], 'otc': user_data['otc'],
                      'phone': user_data['phone']}
        )

        coords, _ = Coords.objects.get_or_create(
            latitude=coords_data['latitude'],
            longitude=coords_data['longitude'],
            height=coords_data['height']
        )

        pereval = PerevalAdded.objects.create(
            beauty_title=data['beauty_title'],
            title=data['title'],
            other_titles=data['other_titles'],
            connect=data['connect'],
            user=user,
            coords=coords,
            level_winter=data['level']['winter'],
            level_summer=data['level']['summer'],
            level_autumn=data['level']['autumn'],
            level_spring=data['level']['spring']
        )

        return pereval.id
