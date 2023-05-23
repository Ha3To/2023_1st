# 팩토리 메서드 패턴을 이용해 운동 클래스 생성
class Exercise:
    def create_exercise(self):
        raise NotImplementedError()


class AerobicExercise(Exercise):
    def create_exercise(self):
        return "유산소 운동"


class StrengthExercise(Exercise):
    def create_exercise(self):
        return "근력 운동"


class FlexibilityExercise(Exercise):
    def create_exercise(self):
        return "유연성 운동"

# 싱글턴 패턴을 이용한 사용자 정보 관리 클래스 생성


class UserInfoSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.preference = None

# 옵저버 패턴을 이용한 사용자 추천 운동 관리 클래스 생성


class ExerciseRecommendation:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def unsubscribe(self, user):
        self.subscribers.remove(user)

    def notify(self, exercise_type):
        for user in self.subscribers:
            user.update(exercise_type)


class User:
    def __init__(self, username):
        self.username = username

    def update(self, exercise_type):
        print(f"{self.username}님, 추천 운동은 {exercise_type.create_exercise()}입니다.")


def recommend_exercise(user_pref):
    if user_pref == "유산소":
        return AerobicExercise()
    elif user_pref == "근력":
        return StrengthExercise()
    elif user_pref == "유연성":
        return FlexibilityExercise()


class ExerciseFacade(ExerciseRecommendation):
    def __init__(self):
        super().__init__()

    def update_user_preference(self, user_preference):
        user_info = UserInfoSingleton()
        user_info.preference = user_preference

    def recommend_updated_exercise(self):
        user_info = UserInfoSingleton()
        recommended_exercise = recommend_exercise(user_info.preference)
        self.notify(recommended_exercise)


def recommend_exercise(user_pref):
    if user_pref == "유산소":
        return AerobicExercise()
    elif user_pref == "근력":
        return StrengthExercise()
    elif user_pref == "유연성":
        return FlexibilityExercise()
    else:
        raise ValueError("올바른 운동 선호를 입력해주세요: 유산소, 근력 또는 유연성")


def get_user_preference():
    print("선호하는 운동을 선택해주세요: 유산소, 근력, 유연성")
    user_input = input().strip()
    return user_input


def main():
    user1 = User("User1")
    user2 = User("User2")
    user3 = User("User3")

    exercise_facade = ExerciseFacade()
    exercise_facade.subscribe(user1)
    exercise_facade.subscribe(user2)
    exercise_facade.subscribe(user3)

    while True:
        try:
            user_preference = get_user_preference()
            if user_preference.lower() == 'exit':
                print("프로그램을 종료합니다.")
                break

            exercise_facade.update_user_preference(user_preference)
            exercise_facade.recommend_updated_exercise()

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
