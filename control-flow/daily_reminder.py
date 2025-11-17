#personal daily reminder
task = input("Enter your task")
priority = input("Priority (high,medium,low)")
time_bound = input("Is it time bound?(yes/no)")

match priority:
    case "high":
       if time_bound == "yes":
          print(priority,"is a high priority task  that requires immediate attention")
       else :
          print(priority,"is a high priority task but not time bound. try to complete it soon")  
    case "medium":
       if time_bound == "yes":
          print(priority,"is a medium priority task that should be done soon")
       else :
            print(priority,"is a medium priority task. try to complete it when possible")
    case "low":
        if time_bound == "yes":
           print(priority,"is a low priority task. consider completing it as soon as possible.")
        else:
            print(priority,"is a low priority task. it can be done at your convenience.")