import json
survey = {
"What is your name? " : "name",
"What is your favorite city? " : "city",
"What is your favorite season? " : "season",
"What is your favorite color? " : "color",
"What is your favorite smell? " : "smell",
"What is your dream college? " : "college",
"Who is your favorite celebrity? " : "celeb",
"What is your current favorite song? " : "song"
}

contin = True
data = []

while contin:
    responses = {}
    for q in survey:
        responses[q] = input(q)
    data.append(responses)
    to_contin = input("Continue? Y/N ")
    if to_contin == "Y":
        contin == bool(True)
    else:
        break

if os.path.isfile("data.json"):
    file = open("data.json", "r+")
    old_data = json.load(file)
    old_data.extend(data)
    file.write(json.dumps(old_data))
    file.close()
else:
    file = open("data.json", "w")
    file.write(json.dumps(data))
    file.close()








import json
file = open("list_of_responses.json", "r")
a = "".join(file.readlines())
new_data = ",".join(a.split(']['))
file.close()

file = open("list_of_responses.json", "w")
file.write(json.dumps(new_data))
file.close()





import json


with open("data.json", "r") as f:
    # Load our json data into our json object
    data = json.load(f)

    # Loop through and print
    for d in data:
        print(d)
    print()

    # Find the most common college
    college_count = {} # hold the counts for each college
    for d in data:
        # Add 1 count for each college seen
        college_count[d["college"]] =  college_count.get(d["college"], 0) + 1
    print("College by percentage of participants")
    for college, count in college_count.items():
        print("{}: {}%".format(college, 100 * count/ len(data)))
    print()
#---------------------------------------------------------------
# WHAT TO DO IF YOU HAVE NEW DATA BUT YOU ALREADY HAVE A DATA.JSON FILE
# data2 = [{responses}]
# f2 = open("data.json")
# old_data = json.loads(f2) # return a list of data that was already in data.json
# old_data.extend(data2)
# f2.write(json.dumps(old_data))
# f2.close()
