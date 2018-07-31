#Write a function "pretty_print_dict" that prints a given dict in sorted order

#def pretty_print_dict(dictionary):
    #for key, value in sorted(dictionary.items()):
        #print(key, value)

# Key = student name; value = disney character
#"Annamarie" : "Baymax",
#"Adriana" : "Rapunzel",
#"Sydney" : "Ariel",
#"Lisette" : "Mulan",
#}
#pretty_print_dict(students)

def translate_shorthand(dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

phrases = {
"imo" : "in my opinion",
"lol" : "league of legend",
"smh" : "shake my head",
"wow" : "world of warcraft",
"gwcsip" : "girls who code summer immersion program"
}
translate_shorthand(phrases)

story = """
Stacy was texting . She said lol noobs suck smh . imo wow is better .
are you going to gwcsip ?
"""

story_list = story.split()

new_story_list = []
# Go through each word of our story
for word in story_list:
    # The word is a shorthand
    if word in phrases.keys():
        new_story_list.append(phrases[word])
    # The word is NOT a shorthand
    else:
        new_story_list.append(word)
print(new_story_list)
print(" ".join(new_story_list))
