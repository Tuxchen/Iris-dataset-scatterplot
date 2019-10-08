import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

fObj = open("iris.csv", "r")

xsetosa = []
xversicolor = []
xvirginica = []
ysetosa = []
yversicolor = []
yvirginica = []
csetosa = []
cversicolor = []
cvirginica = []

for line in fObj:
    l = line.rstrip().split(",")
    
    if len(l) != 5:
        continue
    
    if l[4] == 'Iris-setosa':
        xsetosa.append(l[2])
        ysetosa.append(l[3])
        csetosa.append('red')
    elif l[4] == 'Iris-versicolor':
        xversicolor.append(l[2])
        yversicolor.append(l[3])
        cversicolor.append('blue')
    elif l[4] == 'Iris-virginica':
        xvirginica.append(l[2])
        yvirginica.append(l[3])
        cvirginica.append('green')

plt.scatter(np.array(xsetosa), np.array(ysetosa), c=csetosa, label='Iris-setosa')
plt.scatter(np.array(xversicolor), np.array(yversicolor), c=cversicolor, label='Iris-versicolor')
plt.scatter(np.array(xvirginica), np.array(yvirginica), c=cvirginica, label='Iris-virginica')
plt.style.use("seaborn-whitegrid")
plt.xlabel("petal length")
plt.ylabel("petal width")
plt.title("iris.csv")
plt.legend(loc="lower right")
plt.show()
