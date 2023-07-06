# MAKING A SIMPLE LINE GRAPH
import matplotlib.pyplot as plt

playerName = ['A','B','C','D','E','F','G']
playerGoals = [100,130,125,90,20,50,70]
plt.plot(playerName, playerGoals, color=(0,0,1), marker='+', markersize=10, markeredgecolor=(1,0,0))
plt.title("Football Players Record")
plt.xlabel("Players Names")
plt.ylabel("Players Goals")
plt.show()