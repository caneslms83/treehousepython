attendees = ["Ken", "luis", "treasurer"]
attendees.append("Ash")
attendees.extend(["James", "Gil"])
optional_invitees=(["Tom","Jerry"])
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendees currently in the meeting")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("CC: " + cc_line)