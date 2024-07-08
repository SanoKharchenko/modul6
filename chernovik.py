import time

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname  #имя пользователя
        self.password = password  #пароль
        self.age = age  #возраст

    def __hash__(self):
        return hash(self.password)

    def __eq__(self, other):
        return self.nickname == other.nickname

class Video:
    def __init__(self, title: str, duration, adult_mode: bool = False):
        self.title = title  #заголовок
        self.duration = duration  #продолжительность
        self.time_now = 0  #секунда остановки
        self.adult_mode = adult_mode  #ограничение по возрасту

class UrTube:
    def __init__(self):
        self.users = []  #список объектов User
        self.videos = []  #список объектов Video
        self.current_user = None  #текущий пользователь, User

    def log_in(self,login: str, password: str):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f'Пользователь {nickname} зарегистрирован и вошел в систему.')

    def log_out(self):
        self.current_user = None

    def add(self, *new_videos):
        for new_video in new_videos:
            if not any(video.title == new_video.title for video in self.videos):
                self.videos.append(new_video)

    def get_videos (self, search_word: str):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title_video: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title_video:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
            for second in range(video.time_now, video.duration + 1):
                print(f"{second + 1} ", end='')
                video.time_now += 1
                time.sleep(1)
            print("Конец видео")
            video.time_now = 0
            return
    print('Нет видео')




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
