import numpy as np
import pylab as pl
n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Ysin = np.sin(1 * X)
Ycos = np.cos(2 * X)
# pl.axes([0.025, 0.025, 0.95, 0.95])
pl.plot(X, Ysin, color='blue', alpha=1.00)
pl.plot(X, Ycos, color='green', alpha=1.00)
pl.xlim([-np.pi, np.pi])
pl.ylim([-2.5, 2.5])
pl.show()
