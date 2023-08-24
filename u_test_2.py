import unittest

def pairs():
    boys = ['Иван', 'Василий', 'Александр', 'Владимир', 'Роман']
    girls = ['Мария', 'Екатерина', 'Валерия', 'Юлия', 'Елизавета']
    if len(boys) == len(girls):
        print('Идеальные пары:')
    boys.sort()
    girls.sort()
    names = zip(boys, girls)
    for name in names:
        return(f'{name[0]} и {name[1]}')
    else:
        return('Кто-то может остаться без пары')
    

class TestNames(unittest.TestCase):
    def test_list(self):
        first_pair = 'Александр и Валерия'
        second_pair = 'Петр и Владислава'
        my_list = pairs()
        self.assertIn(first_pair, my_list)
        self.assertNotIn(second_pair, my_list)


if __name__ == '__main__':
    unittest.main()