from django.test import TestCase
from games.models import games

class games_test(TestCase):
    def test_str(self):
        Games = games(ID_GAme ='GI',Name_of_Game =  'Genshin Impact', Description = 'гриндилка',Teg = '12')
        self.assertEqual(
            str(Games),
            ' '.join(['GI','Genshin Impact','гриндилка','12'])
        )
