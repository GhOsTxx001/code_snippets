#Used to manually count the number hours, minutes and seconds a playlist of videos would take
#I used this for video courses hence the name.
#So long as you know the lengths of the videos.
#A much better version 2 will be coming.


a = int(input("How many videos? "))

hours = 0
minutes = 0
seconds = 0

for i in range(a):
	print("For video ",i+1) 	
	hrs = int(input("hour length? "))
	if hrs>3:           #most videos aren't this long, so just to prevent any initial mistyping
		hrs=int(input("Is it really that long?"))

	mins = int(input("minute length "))
	if mins >59:
		mins = int(input("check again..."))

	secs = int(input("seconds length "))
	if secs>59:
		secs = int(input("check again...."))

	print("\n")
	print("--------------------------------------------------------------------------------")
	print("--------------------------------------------------------------------------------")
	print("\n")
	hours +=hrs
	minutes +=mins
	seconds +=secs

#for calculations up ahead
seconds_to_minutes = 0
modulo_seconds = 0 
minutes_to_hours = 0
modulo_minutes = 0
backup_min1 = 0
backup_min2 = 0

#seconds calculation
if seconds > 59:
	seconds_to_minutes = seconds//60
	modulo_seconds = seconds%60
	total_secs = modulo_seconds
else:
	total_secs = seconds
	#if the above were a function that would be easier to call in the results

if minutes > 59:
	minutes_to_hours = minutes//60
	modulo_minutes = minutes%60
else:
	print("just ",minutes_to_hours)

total_mins = seconds_to_minutes + modulo_minutes

total_hours = hours+ minutes_to_hours

if total_mins > 59:
	backup_min1 = total_mins//60
	backup_min2 = total_mins%60

	total_mins = backup_min2

	total_hours = hours + minutes_to_hours + backup_min1

else: 
	print("..................................")
	print("..................................")
	print("..................................")
	print("Minutes don't add up to 60 on the second part")
	print("..................................")
	print("..................................")
	print("..................................")
	print("That's a good thing")
print("Total course takes up ",total_hours," hours", total_mins," minutes", total_secs," seconds")