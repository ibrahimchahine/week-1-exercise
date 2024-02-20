# Voting System

This folder represents the Voting system homework code.
In this Markdown file, I detail the process of building this homework.

The approach that I took is using OOP in python because I saw that the homework includes different entities around the voting system, and most entities has relationship between them.

So let's detail the classes and relationships between the classes:

1. Citizen: This class represents the citizen in project, which includes the following properties (id, name, age, addr)
2. Candidate: This class represents the candidate in project, a canditate is also a citizen but it also includes the following properties (position, candidate_id) and the feilds of Citizen.
3. Vote: This class represents a vote in the project, the feilds are (position, candidate, voter_id), we include the voter_id because we can an ability to find the voter of a vote without a reference.
4. Position: This class represents a political position in the project, it includes (candidates, position name), we made the candidates as a dictitionary were the key is the candidate and the value is the votes for the partecular position
5. System: This class represents the main system we all the entities play a role. it includes the following proporties:
   5.1: candidates: a list of the candidates, every item is from type Candidate. There can't be any duplicates.
   5.2: voters: a list of the voters, of type Citizen. There can't be any duplicates.
   5.3: votes: a list of votes taken by citizens, every citizen is allowed one vote.
   5.4: positions: a list of the political positions, every item is from type Position.
   5.5: voting_started: This is a flag for the system, if True voting has begun and there can be no more canditdates added. If Flase then votes can't be submetted yet.
