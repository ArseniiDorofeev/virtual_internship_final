from django.db import transaction
from .models import User, Coords, PerevalAdded, PerevalImages


class DatabaseManager:
    @staticmethod
    @transaction.atomic
    def create_user(email, fam, name, otc, phone):
        return User.objects.create(email=email, fam=fam, name=name, otc=otc, phone=phone)

    @staticmethod
    @transaction.atomic
    def create_coords(latitude, longitude, height):
        return Coords.objects.create(latitude=latitude, longitude=longitude, height=height)

    @staticmethod
    @transaction.atomic
    def create_pereval_added(beauty_title, title, other_titles, connect, user, coords,
                             level_winter, level_summer, level_autumn, level_spring):
        return PerevalAdded.objects.create(
            beauty_title=beauty_title,
            title=title,
            other_titles=other_titles,
            connect=connect,
            user=user,
            coords=coords,
            level_winter=level_winter,
            level_summer=level_summer,
            level_autumn=level_autumn,
            level_spring=level_spring
        )

    @staticmethod
    @transaction.atomic
    def create_pereval_images(data, title, pereval):
        return PerevalImages.objects.create(data=data, title=title, pereval=pereval)
