# CRUD excercise in a layout of possible future text game. More updates to come when I'll have some time (after finishing other projects).

import sys

MAX_WIDTH = 10 # terminal print width

class Sailor:
    def __init__(self, num = 0, name="", age=0, limbs=0, eyes=0, parrot=None, proffesion="", sailing=0, fighting=0, cost=0):
        self.num = num
        self.name = name
        self.age = age
        self.limbs = limbs
        self.eyes = eyes
        self.parrot = parrot
        self.proffesion = proffesion
        self.sailing = sailing
        self.fighting = fighting
        self.cost = cost

        self.crew_list = []
        self.ATTRS_ORDER = [key for key in self.__dict__ if key != "crew_list"] # self key's returned as list
    
    def __str__(self):
        values = "|".join(str(getattr(self, attr)).center(MAX_WIDTH) for attr in self.ATTRS_ORDER) # getattr pulls self values and sets it in order as in self.ATTRS_ORDER
        return f"{values}"
    
    def __repr__(self):
        return f"Sailor(num={self.num!r},name={self.name!r}, age={self.age!r}, limbs={self.limbs!r}, eyes={self.eyes!r}, parrot={self.parrot!r}, proffesion={self.proffesion!r}, sailing={self.sailing!r}, fighting={self.fighting}, cost={self.cost})"
    
    def update_numbers(self):
        """Updates crew members list numbers."""
        for index, member in enumerate(self.crew_list, start=1): # enumerate() returns pairs index-value
            member.num = index

    def add_crew_member(self):
        """Adds Sailor class instance."""
        name = get_input("Name: ", validate_name, "People of the sea must use names! Max. 10 signs!")
        age = get_input("Age: ", validate_age, "We really need a number between 5 and 75.")
        limbs = get_input("Limbs: ", validate_limbs, "This is amazing but actually people can have only max. 4 limbs and we do not hire people with less then 2 limbs.")
        eyes = get_input("Eyes: ", validate_eyes, "People can have max 2 eyes and min 1!")
        parrot = get_input("Parrot? 0-2: ", validate_parrot, "No parrot = 0. Max parrots = 2.")
        proffesion, sailing, fighting = get_proffesion_and_skills()

        num = len(self.crew_list) + 1
        cost = int((int(age)/4) + (int(limbs) * 2) + (int(eyes) * 2) + int(fighting) + int(sailing))

        new_sailor = Sailor(num, name, age, limbs, eyes, parrot, proffesion, sailing, fighting, cost)
        
        self.crew_list.append(new_sailor)
        self.update_numbers()

    def remove_crew_member(self, delete_person):
        """Removes Sailor class instance based on name parameter."""
        if delete_person.lower() in str(self.crew_list).lower():
            self.crew_list = [person for person in self.crew_list if person.name.lower() != delete_person.lower()]
            print("Person removed!")
        else:
            print("No such name on crew list!")
        self.update_numbers()
    
    def count_cost(self):
        """Counts total cost we have to spend on all crew members"""
        total_cost = sum(sailor.cost for sailor in self.crew_list)
        return total_cost
        

def get_input(promt, validation_func, error_message):
    """Validates input from a user."""
    while True:
        value = input(promt)
        if validation_func(value):
            return value
        else:
            print(error_message)


def validate_name(name: str) -> bool:
    return len(name) <= 10 and not name.isnumeric() and name != ""


def validate_parrot(parrot: str) -> bool:
    if not parrot.isnumeric():
        return False
    parrot_int = int(parrot)
    return 0 <= parrot_int <= 2


def validate_age(age: str) -> bool:
    if not age.isnumeric():
        return False
    age_int = int(age)
    return 5 <= age_int <= 75


def validate_limbs(limbs: str) -> bool:
    if not limbs.isnumeric():
        return False
    limbs_int = int(limbs)
    return 2 <= limbs_int <= 4


def validate_eyes(eyes: str) -> bool:
    if not eyes.isnumeric():
        return False
    eyes_int = int(eyes)
    return 1 <= eyes_int <=2


def validate_skill(skill: str) -> bool:
    if not skill.isnumeric():
        return False
    skill_int = int(skill)
    return 1 <= skill_int <=5


def validate_yes_no(yes_no: str) -> bool:
    while True:
        if yes_no.lower() == "y":
            return True # no need of "break" becouse "return" automatically stops function
        elif yes_no.lower() == "n":
            return False
        else:
            print('Only "Y" or "N" answers!')
            yes_no = input("Please type Y/N: ")


def get_proffesion_and_skills():
    while True:
        profession = input("What is profession of crew member? (S)ailor or (W)arrior? S/W?: ")
        if profession.lower() == "s":
            sailing_skills = get_input("What is the level of sailing skills (1-5): ", validate_skill, "Please provide number: 1-5.")
            return "sailor", int(sailing_skills), 0
        elif profession.lower() == "w":
            fighting_skills = get_input("What is the level of fighting skills (1-5): ", validate_skill, "Please provide number: 1-5.")
            return "warrior", 0, int(fighting_skills)
        else:
            print("Please type: W or S.")
            continue
	    

def show_introduction():
    """Game intro - can be skipped."""
    user_reply = input("Do you wish to see game introduction? Y/N ")
    return validate_yes_no(user_reply)


def instructions(first_question: bool) -> None:
    """Game instructions."""
    if first_question == True:
        print("\nYou are a captain of a ship and you need to recruit a whole crew anew.\nYou have to hire both sailros and warriors.\nBeware that both STORMS and PIRATES threathens to your precious wares.\nOnly SAILORS can fight with STORMS and only WARRIORS can fight with PIRATES.\nThe better crew member the higher the pay - and you have only 100 coins to pay for the crew!\nChoose wisely before embarking to your journey.\n")


def show_menu_one():
    """Game menu - allows user only to provide '1', '2', '3', '4', '5' or '6' answers and returns the user choice."""
    while True:
        print("\nMenu:\n1 - Add a crew member.\n2 - Remove a crew member.\n3 - Show your crew.\n4 - Check your gold.\n5 - Start sailing.\n6 - End game.")
        user_reply = input("Type: 1, 2, 3, 4, 5 or 6: ")
        
        if user_reply.isnumeric() and 1 <= int(user_reply) <= 6:
            return user_reply
        else:
            print('Only 1, 2, 3, 4, 5 or 6 answers!')
            continue

 
def sailor_list(self: list) -> None:
    """Prints all crew members."""
    names = "|".join(attr.center(MAX_WIDTH) for attr in self.ATTRS_ORDER) # joins each element of list using "|" and centering with "max_width"
    print (f"{len(names) * '-'}\n{names}\n{len(names) * '-'}")
    for sailor in self.crew_list:
        print(sailor)
    print(len(names) * "-")
    total_cost = self.count_cost()
    print(f"{(len(names) - MAX_WIDTH) * ' '}{str(total_cost).center(MAX_WIDTH)}")


def main():
    sailor_manager = Sailor() # class instance variable
    first_question = show_introduction()
    instructions(first_question)

    menu_actions = {
        '1': sailor_manager.add_crew_member, # no () - we do not want to call function but only to save a call to function for future use
        '2': lambda: sailor_manager.remove_crew_member(input("Who do you wish to remove from the crew? Type name: ")), # lambda has built in return function
        '3': lambda: sailor_list(sailor_manager),
        '4': lambda: print("\nCheck your gold - work in progress."),
        '5': lambda: print("\nStart sailing - will be available in a full version."),
        '6': lambda: print("\nThanks for playing!!!") or sys.exit(0), # "or" in python, returns the value of the first expression that is True. First is print(), which returns None - and None is treated as False. Becaouse of this second second part is executed: sys.exit. If we would used "and", python would expect that both parts of expression must be True to execute sys.exit(0) - and it finally won't be excecuted. 
    }

    while True:
        second_question = show_menu_one() # returns 1-6
        action = menu_actions.get(second_question) # ".get" takes value of given key (from selected dictionary)

        if action:
            action() # () - function is called at this stage
        else:
            print('1, 2, 3, 4, 5 or 6 answers!')

if __name__ == "__main__":
    main()