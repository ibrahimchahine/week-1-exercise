import random


class Delegation:
    def __init__(
        self,
        name,
        materials,
        suggested,
    ):
        self.name = name
        self.materials = materials
        self.suggested = suggested

    def get_suggested(self):
        return self.suggested

    def create_suggestion(self, length):
        suggestion_list = []
        for i in range(length):
            random_suggestion = random.randint(0, len(self.materials) - 1)
            suggestion_list.append(self.materials[random_suggestion])
        return suggestion_list

    def negotiation(self, alien_delegation):
        if isinstance(alien_delegation, Delegation):
            alien_suggested = alien_delegation.get_suggested()
            suggestion_list = self.create_suggestion(len(alien_suggested))
            for needed_material in alien_suggested:
                if needed_material in suggestion_list:
                    return True
        return False


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
    humen_delegation = Delegation("Humen", humen_material, humen_material)
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
    positive = 0
    for aliens in delegations:
        if humen_delegation.negotiation(aliens):
            peace.append(aliens.name)
    return peace


print(delegation())
