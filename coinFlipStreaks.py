import random

numberOfStreaks = 0
highestStreak = 0

for experimentNumber in range(10000):
    streakCounter = 0
    previousFlip = ''
    
    for coinFlip in range(100):
        currentFlip = random.randint(0, 1)
        
        if currentFlip == previousFlip or coinFlip == 0:
            streakCounter += 1
            
            if streakCounter > highestStreak:
                highestStreak = streakCounter
                
            if streakCounter >= 6:
                numberOfStreaks += 1
                
        elif currentFlip != previousFlip:
            streakCounter = 0

        previousFlip = currentFlip

print(str(numberOfStreaks/10000) + ' %')
print(highestStreak)
