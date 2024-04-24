# import various dictionaries from this module and write print statements
from team_members import team_members
from pronouns import preferred_pronouns

print("Team Members:")
for name, info  in team_members.items():
    print("- Name:{}".format(name))
    print("  Position: {}".format(info["position"]))

print("Pronouns:")
for name, pronouns in preferred_pronouns.items():
    print("- Name: {}".format(name))
    print("  Pronouns: {}".format(pronouns))
