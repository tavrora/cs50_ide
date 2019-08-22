from cs50 import get_float

# request and input validation
while True:
    changeFl = get_float("Change owed: ")
    if changeFl > 0:
        break

centFl = changeFl * 100     # transfer to cents
centInt = round(centFl)     # convert number to integer
coinСounter = 0     # initialize the counter

# count the number of coins for change
if centInt >= 25:
    coinСounter = centInt // 25
    centInt = centInt % 25

if centInt < 25 and centInt >= 10:
    coinСounter = coinСounter + centInt // 10
    centInt = centInt % 10

if centInt < 10 and centInt >= 5:
    coinСounter = coinСounter + centInt // 5
    centInt = centInt % 5

if centInt < 5 and centInt >= 1:
    coinСounter = coinСounter + centInt

print(coinСounter)