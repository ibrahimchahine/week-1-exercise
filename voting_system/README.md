# Voting System

This folder represents the Voting system homework code.
In this Markdown file, I detail the process of building this homework.

The approach that I took is using OOP in python because I saw that the homework includes different entities around the voting system, and most entities has relationship between them.

So let's detail the classes and relationships between the classes:

1. Citizen: This class represents the citizen in project, which includes the following properties (id, name, age, addr)
2. Candidate: This class represents the candidate in project, a canditate is also a citizen but it also includes the following properties (position, candidate_id) and the feild of the citizen.
3. Vote: This class represents a vote in the project, the feilds are (position, candidate, voter_id), we include the voter_id because we can an ability to find the voter of a vote without a reference.
