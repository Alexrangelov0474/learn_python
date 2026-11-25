from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    username = 'test hero'
    level = 5
    health = 18.9
    damage = 24.3


    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.damage, self.hero.damage)

    def test_attr_types(self):
        self.assertIsInstance(self.username, str)
        self.assertIsInstance(self.health, float)
        self.assertIsInstance(self.damage, float)
        self.assertIsInstance(self.level, int)

    def test_battle_enemy_hero_has_the_same_name(self):
        enemy_hero = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_hero_health_not_enough(self):
        self.hero.health = 0
        enemy_hero = Hero('enemy', self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle_enemy_hero_health_not_enough(self):

        enemy_hero = Hero('enemy', self.level, 0, self.damage)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('You cannot fight enemy. He needs to rest', str(ex.exception))

        enemy_hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('You cannot fight enemy. He needs to rest', str(ex.exception))

    def test_draw(self):
        enemy_hero = Hero('enemy', self.level, self.health, self.damage)
        result = self.hero.battle(enemy_hero)
        self.assertEqual('Draw', result)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(-102.6, self.hero.health)
        self.assertEqual(24.3, self.hero.damage)

    def test_hero_win(self):
        enemy_hero = Hero('enemy', 1, 1, 1)
        result = self.hero.battle(enemy_hero)
        self.assertEqual('You win', result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(22.9, self.hero.health)
        self.assertEqual(29.3, self.hero.damage)

    def test_enemy_hero_win(self):
        self.hero.damage = 5
        enemy_hero = Hero('enemy', self.level + 10, self.health + 100, self.damage + 100)
        result = self.hero.battle(enemy_hero)

        self.assertEqual('You lose', result)
        self.assertEqual(16, enemy_hero.level)
        self.assertEqual(98.9, enemy_hero.health)
        self.assertEqual(129.3, enemy_hero.damage)

    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"

        self.assertEqual(expected, str(self.hero))


if __name__ == '__main__':
    main()