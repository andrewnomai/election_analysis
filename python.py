counties_dict = {"Arapahoe county has": 422829, "Denver": 463353, "Jefferson": 432438}

# print each county and registered voter form so output looks like this
# Arapahoe county has 422829 registered voters.
# Denver county has 463353 registered voters.
# Jefferson county has 432438 registered voters.



voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]


for item in voting_data:
    print(f"{item['county']} has {item['registered_voters']:,} registered voters")


for county, voters in counties_dict.items():
    print(f'{county} has {voters:,} registered voters.')


for county_dict in voting_data:
    print(county_dict)


for i in range(len(voting_data)):
    print(voting_data[i]['county'])



    