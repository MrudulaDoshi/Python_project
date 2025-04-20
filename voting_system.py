def main():
    votes = {}

    print("Welcome to the Simple Voting System!")
    print("Enter the name of the candidate to vote for.")
    print("Type 'exit' to stop voting and see the results.\n")

    while True:
        name = "".join(input("Enter candidate name(or 'exit' to finish):").split())
        if name.lower() == 'exit':
            break
        if name == "":
            print("Candidate name cannot be empty.\n")
            continue

        if name in votes:
            votes[name] += 1
        else:
            votes[name] = 1

        print(f"Vote recorded for {name}. Total votes so far:\n")
        for candidate, count in votes.items():
            print(f"{candidate}: {count} vote(s)")
        print()

    print("\nVoting ended. Final Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} vote(s)")

# Run the program
main()