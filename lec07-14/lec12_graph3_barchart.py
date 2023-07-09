#Bar Chart
import matplotlib.pyplot as plt

std_marks=[97,43,69,56]
test_no=[1,2,3,4]
plt.bar(test_no, std_marks,color='r',width=0.5,edgecolor='y',
        linewidth=3,xerr=0.5,ecolor='g',capsize=5,alpha=1,align='edge')
# plt.barh(test_no, std_marks)
plt.xlabel("Test NO")
plt.ylabel("Student Marks")
plt.show()