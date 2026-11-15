"""Diagnostic maths assessment, Part I (Python): model answers.
Run with: python maths/assessment/assessment-python-solutions.py
"""

import numpy as np


# I1 [PY1] mean, population SD and sample SD of [2, 4, 6, 8]
x = np.array([2, 4, 6, 8])
print("I1 mean:", x.mean())                         # 5.0
print("I1 population SD:", np.std(x))               # 2.236 (divides by n)
print("I1 sample SD:", np.std(x, ddof=1))           # 2.582 (divides by n - 1)
# ddof=1 ("delta degrees of freedom") divides by n - 1 instead of n: the sample correction.


# I2 [PY2] simulate 10,000 die rolls, estimate P(even OR > 4)
rng = np.random.default_rng(0)
rolls = rng.integers(1, 7, size=10_000)
est = np.mean((rolls % 2 == 0) | (rolls > 4))
print("I2 simulated:", est, " exact: 2/3 =", 2 / 3)


# I3 [PY3] metrics from a confusion matrix
def metrics(tp, fp, fn, tn):
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    precision = tp / (tp + fp) if tp + fp else float("nan")   # undefined if no positive predictions
    recall = tp / (tp + fn) if tp + fn else float("nan")
    f1 = 2 * precision * recall / (precision + recall)
    return accuracy, precision, recall, f1

print("I3:", [round(m, 3) for m in metrics(40, 10, 20, 130)])   # [0.85, 0.8, 0.667, 0.727]


# I4 [PY4] gradient descent on f(w) = (w - 3)^2, derivative 2(w - 3)
w, lr = 0.0, 0.1
for _ in range(50):
    w = w - lr * 2 * (w - 3)
print("I4 final w:", w)                             # 2.99996, very close to the minimum at 3


# I5 [PY5] matrix product (F4) and cosine similarity (F3)
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 1]])
print("I5 A @ B:\n", A @ B)                         # [[4 2] [10 4]]

def cosine_similarity(a, b):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))

print("I5 cosine:", cosine_similarity([1, 0], [1, 1]))   # 0.7071
