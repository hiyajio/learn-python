class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f"{self.first} is {self.age}"

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th Birthday, {self.first}!"

class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active mods"

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"

u1 = User("Tom", "Garcia", 35)
u2 = User("Tom", "Garcia", 35)
u3 = User("Tom", "Garcia", 35)
jasmine = Moderator("Jasmine", "O' Conner", 61, "Piano")
jasmine2 = Moderator("Jasmine", "O' Conner", 61, "Piano")

print(User.display_active_users())
print(Moderator.display_active_mods())

# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())
# user3 = User("Joe", "Smith", 68)
# user4 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())

# print(User.active_users)
# print(user2.logout())
# print(User.active_users)

# print(user1.full_name())
# print(user2.full_name())

# print(user1.initials())
# print(user2.initials())

# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)

# tom = User.from_string("Tom,Jones,89")
# print(tom.first)
# print(tom.full_name())
# print(tom.birthday())
# print(tom)