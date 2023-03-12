import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

X = [-1, 0, 1, -3, -2, 3]
y = ['-1', '-1', '-1', '+1', '+1', '+1']
isSv = [True, False, False, False, True, False]

X2 = [x**2 for x in X]
sns.set(style="whitegrid", palette="muted")

colors = sns.color_palette("hls", 2)
svX = [-2, -1]
svX2 = [4, 1]

midpoint = [-1.5, 2.5]

#plt.scatter(x=midpoint[0], y=midpoint[1], color='black') # midpoint?
#plt.plot([-2, -1], [4, 1], linewidth=1, linestyle=':', color='gray');

#plt.plot([midpoint[0], 0], [midpoint[1], 3], linewidth=1, color='gray');


plt.plot([6, -6], [5, 1], linewidth=1, color='gray');
plt.plot([6, -6], [6.7, 2.7], linewidth=1, linestyle='--', color='gray');
plt.plot([6, -6], [5-1.7,1-1.7], linewidth=1, linestyle='--', color='gray');

plt.xlim(-6,6);
plt.ylim(-2,10);
plt.xlabel(r'$x$');
plt.ylabel(r'$x^2$');

sns.scatterplot(x=X, y=X2, hue=y, palette=colors, s=100);
#sns.scatterplot(x=svX, y=svX2, hue=[1, -1], palette=colors, edgecolor='black', s=150, legend=False);

plt.savefig("svm-sep.pdf")

