class System:
    def __init__(self):
        self.candidates = []
        self.voters = []
        self.votes = []
        self.positions = []
        self.voting_started = False

    def update_voting(self, flag):
        self.voting_started = flag

    def get_voter(self, voter_id):
        for voter in self.voters:
            if isinstance(voter, Citizen):
                if voter.id == voter_id:
                    return voter
        return

    def position_exists(self, position_name):
        for position_object in self.positions:
            if isinstance(position_object, Position):
                if position_object.position == position_name:
                    return True

        return False

    def get_candatite(self, candidate_id):
        for candatatie in self.candidates:
            if isinstance(candatatie, Candidate):
                if candatatie.candidate_id == candidate_id:
                    return candatatie
        return

    def add_vote(self, voter, candidate_id, position):
        """Method for submiting a vote. If the submit is successful then returns True else returns False"""
        if self.voting_started:
            if voter in self.voters:
                return False
            if isinstance(voter, Citizen) and self.position_exists(position):
                self.voters.append(voter)
                candidate = self.get_candatite(candidate_id)
                self.votes.append(Vote(position, candidate, voter.id))
                if self.update_positions(position, candidate, 1):
                    return True
        return False

    def add_candidate(self, candidate):
        """
        Method for adding a candidate. If the submit is successful then returns True else returns False
        The method also adds the candatite to the position that he/she is submiting for.
        """
        if not self.voting_started:
            if candidate in self.candidates:
                return False
            if isinstance(candidate, Candidate):
                self.candidates.append(candidate)
                for position in candidate.position:
                    self.update_positions(position, candidate, 0)
                if len(self.positions) == len(candidate.position):
                    return True

        return False

    def update_positions(self, position_name, candidate, vote):
        for position_object in self.positions:
            if isinstance(position_object, Position):
                if position_object.position == position_name:
                    position_object.update_candidate(candidate, vote)
                    return True
        temp_position = Position(position_name)
        temp_position.update_candidate(candidate, vote)
        self.positions.append(temp_position)
        return True

    def counting_votes(self):
        for pos in self.positions:
            print(str(pos))


class Citizen:
    def __init__(self, id, name, age, addr):
        self.id = id
        self.name = name
        self.age = age
        self.addr = addr


class Candidate(Citizen):
    def __init__(self, id, name, age, addr, position, candidate_id):
        Citizen.__init__(self, id, name, age, addr)
        self.candidate_id = candidate_id
        self.position = list(position)

    def __str__(self):
        return f"Candatite: {self.name}, Position: {self.position}"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Candidate):
            return __value.candidate_id == self.candidate_id
        return False


class Vote:
    def __init__(self, position, candidate, voter_id):
        self.position = position
        self.candidate = candidate
        self.voter_id = voter_id


class Position:
    def __init__(self, position):
        self.candidates = dict()
        self.position = position

    def update_candidate(self, candadate_id, vote):
        if candadate_id not in self.candidates:
            self.candidates[candadate_id] = 0
            return True
        self.candidates[candadate_id] += vote
        return True

    def __str__(self):
        position_str = []
        for candatite in self.candidates:
            position_str.append(
                [
                    "Candidate: " + candatite.name + " Position: " + self.position,
                    "Votes: " + str(self.candidates[candatite]),
                ]
            )
        return str(position_str)


system = System()
citizen1 = Citizen(name="ibra", addr="balala", age=24, id=33113)
citizen2 = Citizen(name="dsa", addr="das", age=24, id=3311121)
candidate = Candidate(
    name="asdasdas",
    addr="dsadasd",
    age=60,
    id=465456,
    position=["position1", "position2"],
    candidate_id=1213132123,
)

print(system.add_candidate(candidate=candidate))
system.update_voting(True)
print(system.add_vote(candidate_id=1213132123, voter=citizen1, position="position1"))
print(system.add_vote(candidate_id=1213132123, voter=citizen2, position="position2"))
print(system.counting_votes())
