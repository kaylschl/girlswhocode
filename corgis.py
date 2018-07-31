import school_scores
list_of_record = school_scores.get_all()

for s in list_of_record:
    print(s ["State"]["Code"], s["Year"])
    print(s ["GPA"]["B"]["Verbal"])
