from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
n = int(input("Please enter n(int): "))
p = float(input("Please enter p(float): "))
size = int(input("Please enter size(int): "))
target = int(input("Please enter target(int): "))
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
print("Mean:", mean)
print("Probability of "+str(target)+":", binom.pmf(target, n, p)*100)
sns.displot(random.binomial(n=n, p=p, size=size))
plt.title("Binomial Simulation w/ n = "+str(n)+", p = "+str(p))
plt.show() 
