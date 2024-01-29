import random



def testing_r(word_input, word_correct, grade, tf):  # функц проверки ответа и обновления рейтинга

    if word_input != word_correct:
        if grade == 0:
            print(False)
            return grade,
        else:
            print(False)
            return grade - 1,
    else:
        print(True)
        return grade + 1,


def testing_bool(word_input, word_correct, grade, tf):  # функц проверки ответа назначение tf

    if word_input != word_correct:
        return False
    else:
        return True


class for_test():
    def __init__(self, l1, l2, l3, r):
        self.ru = l1
        self.en = l2
        self.no = l3
        self.rating = r

    def quest(self):
        pass


class ru_en(for_test):
    def quest(self):
        question = self.ru
        correct = self.en
        r = self.rating
        language = "Английский"
        return correct, question, r, language


class ru_no(for_test):
    def quest(self):
        question = self.ru
        correct = self.no
        r = self.rating
        language = "Норвежский"
        return correct, question, r, language


class en_ru(for_test):
    def quest(self):
        question = self.en
        correct = self.ru
        r = self.rating
        language = "Русский"
        return correct, question, r, language


class en_no(for_test):
    def quest(self):
        question = self.en
        correct = self.no
        r = self.rating
        language = "Норвежский"
        return correct, question, r, language


class no_ru(for_test):
    def quest(self):
        question = self.no
        correct = self.ru
        r = self.rating
        language = "Русский"
        return correct, question, r, language


class no_en(for_test):
    def quest(self):
        question = self.no
        correct = self.en
        r = self.rating
        language = "Английский"
        return correct, question, r, language


def find_min_rating(data):
    min_rating = float('inf')  # Исходно устанавливаем минимальный рейтинг как бесконечность
    min_r_list = {}  # Создаем пустой словарь для хранения данных с минимальным рейтингом
    all_lists_with_3_rating = True

    for key, listt in data.items():
        rating = listt[3]
        if rating < min_rating:
            min_rating = rating
            min_r_list = {key: listt}
        elif rating == min_rating:
            min_r_list[key] = listt

        if rating != 3:
            all_lists_with_3_rating = False
    if all_lists_with_3_rating:
        return ["Словарь пройде!!", "Словарь пройде!!", "Словарь пройде!!", 0], 1

    if min_rating >= 3:
        return None
    random_key = random.choice(list(min_r_list.keys()))
    random_list = min_r_list[random_key]
    print(random_list, random_key)
    return random_list, random_key


def clear_dict(data):
    for k, value in data.items():
        if len(value) > 3:
            value[3] = 0
    return data
