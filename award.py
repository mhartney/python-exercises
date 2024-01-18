"""This program determines what award a competitor in a
triathalon will receive, based on their time in each race."""

print("\n========Triathalon Awards========")
print("Note: Qualifying time is 100 minutes\n")

# Store times in Variables for each part of race.
print("Enter the participant's time (in minutes) for:")
swimming_time = int(input("Swimming: "))
cycling_time = int(input("Cycling: "))
running_time = int(input("Running: "))

# Calculate the total time taken in triathalon.
total_time = swimming_time + cycling_time + running_time
print(f"\nResults -\nTotal Time: {total_time} minutes")

# Below if statement uses logical operators to determine award given.
if total_time >= 111:
    print("Award Recieved: No award.")
    print("Qualifying Criteria: More than 10 minutes off qualifying time.")
elif total_time >= 106 and total_time <= 110:
    print("Award Recieved: Provincial scroll.")
    print("Qualifying Criteria: Within 10 minutes of qualifying time.")
elif total_time >= 101 and total_time <= 105:
    print("Award Recieved: Provincial Half Colours")
    print("Qualifying Criteria: Within 5 minutes of qualifying time.")
else:
    print("Award Recieved: Provincial Colours.")
    print("Qualifying Criteria: Within the qualifying time.")
print("\n")
