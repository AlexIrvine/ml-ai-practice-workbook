# Diagnostic maths assessment

**Rules:** no notes, no internet, no AI. Basic calculator OK. Show working (partial credit).
Write **don't know** rather than guessing. Confidence: 1 = guessed, 2 = fairly sure, 3 = certain.
About 90–120 min; you can stop after any Part. Part I (Python) goes in `assessment-python.py`.

**Abbreviations used:** SD = standard deviation · TP / FP / FN / TN = true positives / false positives / false negatives / true negatives · F1 = F1 score · MSE = mean squared error · A/B test = experiment comparing version A with version B · PCA = principal component analysis · P(…) = probability of … · ∂ = partial derivative · ln = natural log (base e) · Σ = sum.

---

## Part A: Foundations

### A1 [F1]
Simplify 3(2x − 4) − 2(x − 5).

Working:

Answer:

Confidence (1–3):

### A2 [F2]
Solve for x: 2x + 7 = 19. Then rearrange y = mx + c to make x the subject.

Working:

Answer:

Confidence (1–3):

### A3 [F3]
Evaluate: (a) 2⁵ (b) 10⁻² (c) 9^(1/2) (d) write 0.00042 in scientific notation.

Working:

Answer:

Confidence (1–3):

### A4 [F4]
Evaluate: (a) log₁₀(1000) (b) ln(e³) (c) log(a × b) written as a sum of logs. (d) In one sentence: why might it help to work with logs of very small probabilities?

Working:

Answer:

Confidence (1–3):

### A5 [F5]
Calculate Σᵢ₌₁⁴ i². Then write "the mean of n values x₁ … xₙ" using Σ notation.

Working:

Answer:

Confidence (1–3):

### A6 [F6]
f(x) = x² − 3x. Find f(4). For g(x) = 1 / (1 + e⁻ˣ), what does g(x) approach as x becomes very large positive, and very large negative? What is g(0)?

Working:

Answer:

Confidence (1–3):

---

## Part B: Descriptive statistics

### B1 [S1]
For the data 2, 4, 4, 5, 7, 8, 12 find the mean, median, mode and range.

Working:

Answer:

Confidence (1–3):

### B2 [S2]
For the data 2, 4, 6, 8 calculate the population variance, population standard deviation, and sample variance.

Working:

Answer:

Confidence (1–3):

### B3 [S2]
In plain English, why does the sample variance divide by n − 1 instead of n?

Working:

Answer:

Confidence (1–3):

### B4 [S3]
A company's salaries include a few very high executive salaries. Should you report the mean or the median as "typical salary"? Why? Which way is the distribution skewed?

Working:

Answer:

Confidence (1–3):

### B5 [S4]
A test has mean 70 and standard deviation 10. A student scores 85. What is their z-score, and what does it mean?

Working:

Answer:

Confidence (1–3):

### B6 [S5]
Two variables have correlation r = −0.8. Describe the relationship. Then give an example where two things are correlated but one does not cause the other.

Working:

Answer:

Confidence (1–3):

---

## Part C: Probability

### C1 [P1]
A fair six-sided die is rolled. What is P(even number OR greater than 4)?

Working:

Answer:

Confidence (1–3):

### C2 [P1]
Two fair coins are tossed. What is P(at least one head)? Use the complement.

Working:

Answer:

Confidence (1–3):

### C3 [P2]
Explain the difference between "independent" and "mutually exclusive" events, with one example of each.

Working:

Answer:

Confidence (1–3):

### C4 [P3]
A disease affects 1% of people. A test detects it 90% of the time when present, and gives a false positive 5% of the time when absent. Someone tests positive. What is the probability they actually have the disease? Explain why the answer surprises most people.

Working:

Answer:

Confidence (1–3):

### C5 [P4]
A game costs nothing to play. You win £10 with probability 0.2, otherwise you lose £2. What is the expected value? Should you play many times?

Working:

Answer:

Confidence (1–3):

### C6 [P5]
A fair coin is flipped 10 times. What is the probability of exactly 3 heads? (Give the formula and, if you can, the number.)

Working:

Answer:

Confidence (1–3):

---

## Part D: Distributions & inference

### D1 [D1]
Adult heights are normally distributed with mean 170 cm and SD 10 cm. Roughly what percentage of people are between 150 cm and 190 cm?

Working:

Answer:

Confidence (1–3):

### D2 [D2]
Explain the Central Limit Theorem in plain English and why it matters.

Working:

Answer:

Confidence (1–3):

### D3 [D3]
A sample of 100 customers has mean spend £50 with SD £20. Calculate the standard error and an approximate 95% confidence interval for the true mean spend.

Working:

Answer:

Confidence (1–3):

### D4 [D4]
A test comparing two models gives p = 0.03 with significance level 0.05. (a) What is the null hypothesis likely to be? (b) What do you conclude? (c) What does the p-value actually mean? (d) Define Type I and Type II errors.

Working:

Answer:

Confidence (1–3):

### D5 [D5]
You run an A/B test: version A of a webpage converts 120 of 2,000 visitors, version B converts 150 of 2,000. Which statistical test would you use, and what would you need to check before declaring B the winner?

Working:

Answer:

Confidence (1–3):

### D6 [D6]
A coin lands heads 7 times in 10 flips. What is the maximum likelihood estimate of P(heads)? Explain the idea of "maximum likelihood" in one or two sentences.

Working:

Answer:

Confidence (1–3):

---

## Part E: Statistics for machine learning

### E1 [M1]
A fraud model's results on 200 transactions: TP = 40, FP = 10, FN = 20, TN = 130. Calculate accuracy, precision, recall and F1. Which metric matters most for fraud detection and why?

Working:

Answer:

Confidence (1–3):

### E2 [M2]
99% of emails in a dataset are not spam. A model predicts "not spam" for everything. What is its accuracy, and why is it useless?

Working:

Answer:

Confidence (1–3):

### E3 [M3]
A model scores 98% on training data and 70% on test data. What is happening? Name two ways to fix it.

Working:

Answer:

Confidence (1–3):

### E4 [M4]
Why do we keep a separate test set? What is k-fold cross-validation? Give one example of data leakage.

Working:

Answer:

Confidence (1–3):

### E5 [M5]
A model is ŷ = 3 + 2x. (a) Predict y when x = 4. (b) Interpret the slope. (c) For actual values [3, 4, 8] and predictions [2, 4, 6], calculate the MSE.

Working:

Answer:

Confidence (1–3):

### E6 [M6]
A classifier outputs probabilities [0.7, 0.2, 0.1] for classes [cat, dog, bird]. (a) What must these numbers add up to and why? (b) What function usually produces them? (c) If the true class is cat, what is the cross-entropy loss −ln(p_true)? (d) What happens to the loss as p_true → 0?

Working:

Answer:

Confidence (1–3):

---

## Part F: Linear algebra

### F1 [LA1]
a = [1, 2, 3], b = [4, 0, −1]. Find a + b and 2a.

Working:

Answer:

Confidence (1–3):

### F2 [LA2]
Find a · b (dot product) for the vectors above. Find the length of the vector [3, 4].

Working:

Answer:

Confidence (1–3):

### F3 [LA3]
Find the cosine similarity of [1, 0] and [1, 1]. Why do AI search systems compare embeddings with cosine similarity?

Working:

Answer:

Confidence (1–3):

### F4 [LA4]
Multiply [[1, 2], [3, 4]] × [[2, 0], [1, 1]]. Then: what shape is (3×2 matrix) × (2×4 matrix)? Can you multiply a 3×2 by a 3×2? Why/why not?

Working:

Answer:

Confidence (1–3):

### F5 [LA5]
What is the transpose of [[1, 2, 3], [4, 5, 6]]? What does the identity matrix do when you multiply by it?

Working:

Answer:

Confidence (1–3):

### F6 [LA6]
In plain English, what does PCA do, and why might you use it on a dataset with 500 features?

Working:

Answer:

Confidence (1–3):

---

## Part G: Calculus & optimisation

### G1 [C1]
Differentiate: (a) x³ (b) 5x² + 3x − 7 (c) eˣ.

Working:

Answer:

Confidence (1–3):

### G2 [C2]
What does a derivative tell you? At the minimum of a smooth curve, what is the derivative and why?

Working:

Answer:

Confidence (1–3):

### G3 [C3]
Differentiate (2x + 1)² using the chain rule. Why does the chain rule matter for neural networks?

Working:

Answer:

Confidence (1–3):

### G4 [C4]
For f(x, y) = x²y + 3y, find ∂f/∂x and ∂f/∂y. What is the gradient?

Working:

Answer:

Confidence (1–3):

### G5 [C5]
Minimise f(w) = w² using gradient descent. Start at w = 3 with learning rate 0.1. What is w after one step? After two steps?

Working:

Answer:

Confidence (1–3):

### G6 [C6]
What goes wrong if the learning rate is far too large? Far too small?

Working:

Answer:

Confidence (1–3):

---

## Part I: Python (answer in `maths/assessment/assessment-python.py`)

- **I1 [PY1]** Using NumPy, compute the mean, population SD and sample SD of [2, 4, 6, 8]. Explain what `ddof=1` does.  → answer in `assessment-python.py`. Confidence (1–3):

- **I2 [PY2]** Simulate 10,000 rolls of a fair die and estimate P(even OR > 4). Compare with your answer to C1.  → answer in `assessment-python.py`. Confidence (1–3):

- **I3 [PY3]** Write a function that takes TP, FP, FN, TN and returns accuracy, precision, recall and F1. Test it on E1's numbers.  → answer in `assessment-python.py`. Confidence (1–3):

- **I4 [PY4]** Write a gradient-descent loop that minimises f(w) = (w − 3)² starting at w = 0 with learning rate 0.1 for 50 steps. Print the final w.  → answer in `assessment-python.py`. Confidence (1–3):

- **I5 [PY5]** Using NumPy, multiply the matrices from F4 and write a `cosine_similarity(a, b)` function. Test it on F3's vectors.  → answer in `assessment-python.py`. Confidence (1–3):
