from zombies.phrases import *
from zombies.models import Zombie
import random, datetime, radar

def generate_bio(name):
    return "{} is a {} zombie from {}. {} enjoys {}, {}, and eating brains.".format(
        name,
        random.choice(ZOMBIE_TYPES),
        random.choice(ZOMBIE_HOMETOWNS),
        name,
        random.choice(ZOMBIE_HOBBIES).lower(),
        random.choice(ZOMBIE_HOBBIES).lower()
    )

def generate_name():
    return random.choice(ZOMBIE_NAMES)

def generate_date_of_birth():
    return radar.random_date(
        start = datetime.date(1971,1,1),
        stop = Zombie.DATE_OF_OUTBREAK - datetime.timedelta(weeks=11*52)
    )

def generate_date_of_rebirth():
    return radar.random_date(
        start = Zombie.DATE_OF_OUTBREAK,
        stop = datetime.date.today()
    )

def generate_avatar():
    return '/media/zombies/{}.jpg'.format(
        random.randint(1,8)
    )