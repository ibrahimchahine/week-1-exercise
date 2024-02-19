import random


class Delegation:
    def __init__(self, name, materials, suggested):
        self.name = name
        self.materials = materials
        self.suggested = suggested
        self.peace_achieved = False

    def get_suggested(self):
        return self.suggested

    def update_peace(self, peace_status):
        self.peace_achieved = peace_status

    def create_suggestion(self, length):
        suggestion_list = []
        for i in range(length):
            random_suggestion = random.randint(0, len(self.materials) - 1)
            suggestion_list.append(self.materials[random_suggestion])
        return suggestion_list

    def negotiation(self, other_delegation):
        if isinstance(other_delegation, Delegation):
            alien_suggested = other_delegation.get_suggested()
            suggestion_list = self.create_suggestion(len(alien_suggested))
            for needed_material in alien_suggested:
                if needed_material in suggestion_list:
                    other_delegation.update_peace(True)
                    return True
        return False

    def get_degotiations_details(self, other_delegation):
        if self.peace_achieved and isinstance(other_delegation, Delegation):
            return f"Peace achieved with {other_delegation.name}"
        return f"Peace degotiations failed with {other_delegation.name}"


humen_material = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
]


def delegation():
    humen_delegation = Delegation("Humens", humen_material, humen_material)
    klingon_delegation = Delegation("Klingon", ["A", "B", "R"], ["A", "B", "R"])
    vulcan_delegation = Delegation("Vulcan", ["F", "C", "K"], ["F", "C", "K"])
    brog_delegation = Delegation("Borg", ["Z", "D", "W"], ["Z", "D", "W"])
    vedala_delegation = Delegation("Vedala", ["C", "L", "X"], ["C", "L", "X"])
    delegations = [
        klingon_delegation,
        vedala_delegation,
        vulcan_delegation,
        brog_delegation,
    ]
    peace = []
    success_counter = 0
    for aliens in delegations:
        result = humen_delegation.negotiation(aliens)
        if result:
            success_counter += 1
        peace.append(aliens.get_degotiations_details(humen_delegation))
    if success_counter >= 0.7 * len(delegations):
        humen_delegation.update_peace(True)

    return peace, humen_delegation.peace_achieved


print(delegation())
