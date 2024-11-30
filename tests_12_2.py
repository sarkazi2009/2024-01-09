

import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name




class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers
Run1 = Runner("Усэйн", 10)
Run2 = Runner("Андрей", 9)
Run3 = Runner("Ник", 3)

# Запуск турниров
tournament1 = Tournament(90, Run1, Run3)
all_results1 = tournament1.start()
print("{", end=" ")
for place, participant in all_results1.items():
    print(f"{place}: {participant.name}", end=", ")
print("}")

tournament2 = Tournament(90, Run2, Run3)
all_results2 = tournament2.start()
print("{", end=" ")
for place, participant in all_results2.items():
    print(f"{place}: {participant.name}", end=", ")
print("}")

tournament3 = Tournament(90, Run2, Run1, Run3)
all_results3 = tournament3.start()
print("{", end=" ")
for place, participant in all_results3.items():
    print(f"{place}: {participant.name}", end=", ")
print("}")


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', speed=10)
        self.andrey = Runner('Андрей', speed=9)
        self.nick = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print("{", end="")
            for place, participant in result.items():
                print(f"{place}: {participant.name}", end=", ")
            print("}")

    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        all_results = tournament.start()
        self.__class__.all_results['usain_nick'] = all_results
        self.assertTrue(all_results[len(all_results)] == self.nick)

    def test_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        all_results = tournament.start()
        self.__class__.all_results['usain_nick'] = all_results
        self.assertTrue(all_results[len(all_results)] == self.nick)

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        all_results = tournament.start()
        self.__class__.all_results['usain_nick'] = all_results
        self.assertTrue(all_results[len(all_results)] == self.nick)

    def test_speed_issue(self):
        # Пример дополнительного теста для исправления логической ошибки
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        all_results = tournament.start()
        self.assertTrue(all_results[len(all_results)] == self.nick)


if __name__ == '__main__':
    Run1 = Runner("Усэйн", 10)
    Run2 = Runner("Андрей", 9)
    Run3 = Runner("Ник", 3)
    print(Run1)
    print(Run2)
    print(Run3)


    unittest.main()
