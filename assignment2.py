# SCENARIO:
# you have participated in your college level coding fest which was there for 6 days
# TASK:
# write a python program to give the final report which includes
# 1.activities for the including timeline
# 2.number of teams/participants for the day
# 3.Project names
# 4.technologies used
# 5.ppt demonstrations given
# 6.winner of the day
# 7.runner up of the day
# 8.best performer of the day
# 9.host of the program for that day

class CodingFestDay:
    def __init__(self, day, activities, participants, project_names,
                 technologies, ppts, winner, runner_up, best_performer, host):
        self.day = day
        self.activities = activities
        self.participants = participants
        self.project_names = project_names
        self.technologies = technologies
        self.ppts = ppts
        self.winner = winner
        self.runner_up = runner_up
        self.best_performer = best_performer
        self.host = host

    def display(self):
        print(f"\n Day {self.day} Report:")
        print(f"Activities and Timeline: {self.activities}")
        print(f"Number of Teams/Participants: {self.participants}")
        print(f"Project Names: {self.project_names}")
        print(f"Technologies Used: {self.technologies}")
        print(f"PPT Demonstrations Given: {self.ppts}")
        print(f"Winner of the Day: {self.winner}")
        print(f"Runner Up of the Day: {self.runner_up}")
        print(f"Best Performer of the Day: {self.best_performer}")
        print(f"Host of the Program: {self.host}")

coding_fest_data = []

for day in range(1, 7):
    print(f"\nEnter details for Day {day}:")
    activities = input("Activities and timeline: ")
    participants = int(input("Number of teams/participants: "))
    project_names = input("Project names (comma separated): ")
    technologies = input("Technologies used (comma separated): ")
    ppts = int(input("Number of PPT demonstrations given: "))
    winner = input("Winner of the day: ")
    runner_up = input("Runner up of the day: ")
    best_performer = input("Best performer of the day: ")
    host = input("Host of the program: ")

    fest_day = CodingFestDay(day, activities, participants, project_names,
                             technologies, ppts, winner, runner_up,
                             best_performer, host)
    coding_fest_data.append(fest_day)

print("\n\n========= 🏆 6-Day Coding Fest Final Report 🏆 =========")
for report in coding_fest_data:
    report.display()
