def sanitize(time_string):
    if ":" in time_string:
        splitter = ":"
    elif "-" in time_string:
        splitter = "-"
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return (mins + "." + secs)


class AthleteList(list):

    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])


def get_coach_data(filename):

    try:
        with open(filename) as file:
            data = file.readline()

        temp1 = data.strip().split(",")

        return AthleteList(temp1.pop(0), temp1.pop(0), temp1)

    except IOError as err:
        print("File error: " + str(err))

# Invoking the get_coach_data with the filename attribute

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

# Printing the athletes name and there respective names

print(james.name + " 's Fastest times are " + str(james.top3()))

print(julie.name + " 's Fastest times are " + str(julie.top3()))

print(mikey.name + " 's Fastest times are " + str(mikey.top3()))

print(sarah.name + " 's Fastest times are " + str(sarah.top3()))

print("--checking the new functionality--")

vera = AthleteList('Vera Vi')

vera.append("1.31")

print(vera.top3())

vera.extend(["2.22", "1.52", "1.62"])

print(vera.top3())
