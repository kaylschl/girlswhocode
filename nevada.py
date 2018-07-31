import election
import matplotlib.pyplot as plt
import numpy as np
list_of_result = election.get_results()

data = []

for counties in list_of_result:
    states = (counties["Location"]["State"])
    if states == "Nevada":
        democrat = (counties["Vote Data"])
        county = (counties["Location"]["County"])
        for person, party in democrat.items():
        # if
            datas = county, party["Party"], party["Number of Votes"]
            data.append(party["Number of Votes"])



# print(data)
NUM_COUNTIES = 16

# setup the plot
fig, ax = plt.subplots()

# generate some random data
# x = [x for x in range(NUM_COUNTIES)]

# create the histogram
# ax.hist(x, align = 'right') # `align='left'` is used to center the labels

# now, define the ticks (i.e. locations where the labels will be plotted)
xticks = [i for i in range(NUM_COUNTIES)]

# also define the labels we'll use (note this MUST have the same size as `xticks`!)
xtick_labels = ["Carson City", "Churchill County", "Clark County", "Douglas County", "Elko County", "Esmeralda County", "Eureka County", "Humboldt County", "Lander County", "Lincoln County", "Lyon County", "Mineral County", "Nye County", "Pershing County", "Storey County", "Washoe County", "White Pine County"]

# add the ticks and labels to the plot
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels)

# plt.hist(data)
plt.hist(data,xticks) # Create a histogram
plt.title("Nevada counties in the 2016 Presidential Election")
plt.ylabel("Number of votes")
plt.xlabel("Counties")
plt.grid()
plt.show()
