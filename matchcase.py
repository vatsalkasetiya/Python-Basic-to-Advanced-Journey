# DAY=3

# match DAY:
#     case 1 | 2 | 3 | 4 | 5:
#         print("weekday")
#     case 6 | 7:
#         print("weekend")

light=input("enter traffic light color:")

match light:
    case "red":
        print("stop")
    case "yellow":
        print("get ready")
    case "green":
        print("go")
    case _:
        print("invalid color")