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
            num = 7
            if user.gender != self.gender_intrest:
                num -= 1
            # https://stackoverflow.com/questions/2864842/common-elements-comparison-between-2-lists
            common_food = list(set(user.favorite_food).intersection(self.favorite_food))
            if len(common_food) <= 0:
                num -= 1
            if user.favorite_show != self.favorite_show:
                num -= 1

            if user.profession != self.profession:
                num -= 1
        return True


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

user1.compare_users(user2)
