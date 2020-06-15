import numpy as np
import matplotlib.pyplot as plt

test_loss=[]
iterss=[]
for line in open("test_result.log"):
    if "loss = " in line:
        line_split= line.split(" ")
        index = line_split.index("=")
        test_loss.append(float(line_split[index+1]))
 
    if "Finetuning from models/" in line:
        line_split= line.split("_")
        index=len(line_split)
        iters=line_split[index-1]
        iter_num=iters.split(".")
        iter=iter_num[0]
        iterss.append(int(iter))
plt.plot(iterss,test_loss)
plt.show()
plt.savefig("test_loss.png")
print iterss
print test_loss