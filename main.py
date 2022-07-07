
# first we'll take a input of what we want to keep
nominee1 = input("Enter the name of 1st nominee: \n")
nominee2 = input("Enter the name of 2nd nominee: \n")

# intially vote count for both mustbe 0
nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]
no_of_voter = len(voter_id)

while True:
    if voter_id == []:# to check when voter list is completed
        print("Voting session is over!!")
        if nm1_votes >nm2_votes:
            percent = (nm1_votes/nm2_votes)*100
            print(nominee1,"has won the election with",percent,"% of votes")

        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/nm1_votes)*100
            print(nominee2, "has won the election with", percent, "% of votes")

        else:
            print("Both have equal number of votes !!! Government will decided who will rule") 
            break





    voter = int(input("Enter your voter id:"))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter) # We will remove so that again same voter can't vote
        print(".....................................")
        print("To give vote to", nominee1, "press 1")
        print("To give vote to", nominee2, "press 2")
        print(".....................................")

        vote = int(input("Enter your precious vote: "))
        
        if vote == 1:
            nm1_votes += 1
            print(nominee1,"Thank You to give your important vote to them !!")

        elif vote == 2:
            nm2_votes += 1
            print(nominee1,"Thank You to give your important vote to them !!")
            
        elif vote > 2:
            print("Check your pressed key!!")
        
        else:
            print("You are not voter Or You have already voted")