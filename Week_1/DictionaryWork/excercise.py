# import various dictionaries from this module and write print statements
from team_members import team_members
from pronouns import names, pronouns

print("Team Members:")
for name, info  in team_members.items():
    print("- Name:{}".format(name))
    print("  Position: {}".format(info["position"]))

# Combine names and pronouns using a nested list comprehension
preferred_pronouns = {names[i]: pronouns[i] for i in range(len(names))}

# Print the names and their associated pronouns
print("Pronouns:")
for name, pronouns in preferred_pronouns.items():
    print("- Name: {}".format(name))
    print("  Pronouns: {}".format(pronouns))
