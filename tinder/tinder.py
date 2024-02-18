fields = {
    "Entertainment": ["singer", "musician"],
    "Med": ["doctor", "nurse"],
    "Goverment": ["police", "politician", "soldier"],
    "Tech": ["engineer", "it"],
}


class User:
    def __init__(
        self,
        name,
        gender,
        age,
        profession,
        favorite_show,
        favorite_food,
        gender_intrest,
    ):
        self.name = name
        self.gender = gender
        self.age = age
        self.profession = profession
        self.favorite_show = favorite_show
        self.favorite_food = favorite_food
        self.gender_intrest = gender_intrest
        for key, val in fields.items():
            if profession in val:
                self.feild = key
                break

    def compare_users(self, user):
        # https://www.programiz.com/python-programming/methods/built-in/isinstance
        if isinstance(user, User):
            num = 4
            if user.gender_intrest != self.gender:
                return False
            # https://stackoverflow.com/questions/2864842/common-elements-comparison-between-2-lists
            common_food = list(set(user.favorite_food).intersection(self.favorite_food))
            if len(common_food) <= 0:
                num -= 1
            if user.favorite_show != self.favorite_show:
                num -= 1
            if user.feild != self.feild:
                num -= 1
            if user.age not in range(self.age - 10, self.age + 10):
                num -= 1
            if num > 2:
                return True
        return False


user1 = User(
    "max", "male", 24, "doctor", "the big bang theory", ["pasta", "omlete"], "female"
)
user2 = User(
    "lucy", "female", 35, "police", "grey's anatomy", ["pizaa", "falafel"], "male"
)
user3 = User(
    "alex",
    "male",
    45,
    "singer",
    "How i met your mother",
    ["shawarma", "hummus"],
    "female",
)
user4 = User(
    "lucy",
    "female",
    35,
    "engineer",
    "grey's anatomy",
    ["indian", "asian"],
    "male",
)


def get_user():
    print("Enter your details:\n")
    name = input("Enter your name ")
    gender = input("Enter your gender ")
    print("profession list: \n")
    [print(values) for values in fields.values()]
    profession = input("Enter your profession ")
    age = int(input("Enter your age "))
    show = input("Enter your favorite show ")
    food = input("Enter your favorite food ")
    food = food.split(" ")
    print(food)
    gender_intrest = input("Enter your gender intrest ")

    user5 = User(
        name,
        gender,
        age,
        profession,
        show,
        food,
        gender_intrest,
    )
    if user1.compare_users(user5):
        print(f"Your match is {user1.name}")
        return
    elif user2.compare_users(user5):
        print(f"Your match is {user2.name}")
        return
    elif user3.compare_users(user5):
        print(f"Your match is {user3.name}")
        return
    elif user4.compare_users(user5):
        print(f"Your match is {user4.name}")
        return
    else:
        print("We didn't find a match for you, try again\n")
        get_user()


get_user()
