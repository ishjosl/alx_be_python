task = input("Enter your task:")
time_bound = input("is it time bound? (yes/no)").lower() 
priority = input("Enter priority (high/ medium/ low)").lower()
match priority:
    case "high":
        reminder = "This task requires immediate attention"
    case "medium":
        reminder= "Make sure to complete this task soon"
    case "low":
        reminder= "Complete this task when you have time"
    
if time_bound == "yes":
    reminder = f"{reminder} Don't forget that it is urgent"


