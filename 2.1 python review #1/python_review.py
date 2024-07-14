import random
temperatures=[]
for i in range(7):
	temperatures.append(random.randint(26,40))
days_of_the_week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

even_temps = [temp for temp in temperatures if temp % 2 == 0]
good_days = [days_of_the_week[i] for i in range(7) if temperatures[i] % 2 == 0]
good_days_count = len(good_days)

highest_temp = max(temperatures)
highest_temp_day = days_of_the_week[temperatures.index(highest_temp)]
lowest_temp = min(temperatures)
lowest_temp_day = days_of_the_week[temperatures.index(lowest_temp)]

normal_average = sum(temperatures) / len(temperatures)
above_average = [temp for temp in temperatures if temp > normal_average]

for x in range(7):
	print(days_of_the_week[x], ":", temperatures[x])



print("Temperatures For The Weeek: ", temperatures)
print("Shelly Had " ,good_days, "Good Days")
print("The Hottest Temperuters: " ,highest_temp, "On Days: ", highest_temp_day)
print("The Lowest Temperatures: " ,lowest_temp, "On Days: ", lowest_temp_day)
print("The Normal Average: ", normal_average)
print("The Days With Temperuters Above The Average: ", above_average)

