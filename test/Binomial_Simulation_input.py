from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
from math import floor

n = int(input("Please enter n(int): "))
p = float(input("Please enter p(float): "))
size = int(input("Please enter size(int): "))
target = int(input("Please enter target(int): "))
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
fixed_mean = floor((n+1)*p)
print("Mean:", mean)
print("fixed mean:", fixed_mean)
print("Probability of "+str(target)+":", binom.pmf(target, n, p)*100)
plt.figure(1)
sns.displot(random.binomial(n=n, p=p, size=size))
plt.title("Binomial Simulation w/ n = "+str(n)+", p = "+str(p))
plt.tight_layout()
plt.savefig('plot.png')
# plt.show()
