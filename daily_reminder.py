#personal daily reminder
task = input("Enter the task you want to do")
priority = input("enter the priority leven(high,medium,low)")
time_bound = input("Is the task time bound(yes/no)")

match priority:
    case "high":
       if time_bound == "yes":
          print(priority,"is a high priority task  that requires immediate attention")
    case "medium":
       if time_bound == "yes":
          print(priority,"is a medium priority task that should be done soon")
    case "low":
        if time_bound == "no":
           print(priority,"is a low priority task. consider completing it when you have free time.")

