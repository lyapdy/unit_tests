import unittest


def exst_courses():
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "count": duration}
        courses_list.append(course_dict)
    min_duration = min(durations)
    max_duration = max(durations)
    max_values = []
    min_values = []
    for index1, index2 in enumerate(durations):
        if index2 == max_duration:
            max_values.append(index1)
        elif index2 == min_duration:
            min_values.append(index1)
    courses_min = []
    courses_max = []
    for id in min_values:
        courses_min.append(courses_list[id]["title"])
    for id in max_values:
        courses_max.append(courses_list[id]["title"])
    return(f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_duration} месяца(ев)\n Самый длинный курс(ы): {", ".join(courses_max)} - {max_duration} месяца(ев)')

class TestNames(unittest.TestCase):
    def test_list(self):
        first_course = 'Python-разработчик с нуля'
        second_course = 'Fullstack-разработчик на Python'
        my_list = exst_courses()
        self.assertIn(first_course, my_list)
        #self.assertNotIn(second_course, my_list)


if __name__ == '__main__':
    unittest.main()