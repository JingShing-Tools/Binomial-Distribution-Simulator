from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
n, p = 10000, 0.1
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
print("Mean:", mean)
print("Probability of 120:", binom.pmf(120, n, p)*100)
sns.displot(random.binomial(n=n, p=p, size=10000))
plt.title("Binomial Simulation w/ n = 1000, p = 0.01")
plt.show() 
