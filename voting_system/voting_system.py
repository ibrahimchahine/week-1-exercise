class System:
    def __init__(self):
        self.candidates = []
        self.voters = []
        self.votes = []
        self.positions = dict()
        self.voting_started = False

    def update_voting(self, flag):
        self.voting_started = flag

    def get_voter(self, voter_id):
        for voter in self.voters:
            if isinstance(voter, Citizen):
                if voter.id == voter_id:
                    return voter
        return

    def get_candatite(self, candidate_id):
        for candatatie in self.candidates:
            if isinstance(candatatie, Candidate):
                if candatatie.candidate_id == candidate_id:
                    return candatatie
        return

    def add_vote(self, voter, candidate_id, position):
        """Method for submiting a vote. If the submit is successful then returns True else returns False"""
        if self.voting_started:
            if voter not in self.voters:
                return False
            if isinstance(voter, Citizen) and (position in self.positions):
                self.voters.append(voter)
                candidate = self.get_candatite(candidate_id)
                self.votes.append(Vote(candidate.position, candidate, voter.id))
                self.positions["self.positions"] = 0
                return True
        return False

    def add_candidate(self, candidate):
        """
        Method for adding a candidate. If the submit is successful then returns True else returns False
        The method also adds the candatite to the position that he/she is submiting for.
        """
        if not self.voting_started:
            if candidate not in self.candidates:
                return False
            if isinstance(candidate, Candidate):
                self.candidates.append(candidate)
                self.positions[candidate.position] += 1
                return True
        return False

    # def counting_votes(self):


class Citizen:
    def __init__(self, id, name, age, addr):
        self.id = id
        self.name = name
        self.age = age
        self.addr = addr


class Candidate(Citizen):
    def __init__(self, position, candidate_id):
        self.candidate_id = candidate_id
        self.position = list(position)


class Vote:
    def __init__(self, position, candidate, voter_id):
        self.position = position
        self.candidate = candidate
        self.voter_id = voter_id


class Result:
    def __init__(self, candidate, voter_id):
        self.position = []
        self.candidate = candidate
        self.voter_id = voter_id
