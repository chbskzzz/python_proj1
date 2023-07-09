#MULTI LINE GRAPH
import matplotlib.pyplot as plt

Aus_Overs = [5,10,15,20,25,30,35,40,45,50]
Eng_Overs = [5,10,15,20,25,30,35,40,45,50]
Aus_Scores = [45,90,130,165,190,210,240,290,320,370]
Eng_Scores = [30,76,129,155,188,209,239,286,210,371]

plt.xlabel("Overs")
plt.ylabel("Scores")
plt.title("Australian and English Batting Comparison")
plt.plot(Eng_Overs, Aus_Scores, color='y')
plt.plot(Aus_Overs, Eng_Scores, color='b')
plt.show()