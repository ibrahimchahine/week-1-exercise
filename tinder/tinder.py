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

    def compare_users(self, user):
        # https://www.programiz.com/python-programming/methods/built-in/isinstance
        if isinstance(user, User):
            print("true")

        return


user1 = User(
    "max", "male", 24, "doctor", "the big bang theory", ["pasta", "omlete"], "female"
)
user2 = User(
    "lucy", "female", 35, "engineer", "grey's anatomy", ["pizaa", "falafel"], "male"
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

user1.compare_users(user2)
