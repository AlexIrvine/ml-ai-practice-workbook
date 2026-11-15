# Diagnostic maths assessment: model answers

Use this after attempting `assessment.md`. Scoring: **2** = fully correct · **1** = right idea with an error · **0** = wrong or blank. Total 94 (47 questions × 2). Part I (Python) is in `assessment-python-solutions.py`.

Topic codes in brackets (e.g. [F1]) match the lessons in `maths/practice/`.

## Part A: Foundations

| Q | Answer | Working / why |
|---|---|---|
| A1 [F1] | **4x − 2** | 3(2x − 4) − 2(x − 5) = 6x − 12 − 2x **+ 10** (−2 × −5 = +10) = 4x − 2. It's an expression, so there is nothing to "solve" |
| A2 [F2] | **x = 6**; **x = (y − c) / m** | 2x = 19 − 7 = 12 → x = 6. y − c = mx → divide by m |
| A3 [F3] | **32, 1/100 (0.01), 3, 4.2 × 10⁻⁴** | 2⁵ = 2·2·2·2·2; 10⁻² = 1/10²; 9^(1/2) = √9; move the decimal point 4 places right |
| A4 [F4] | **3, 3, log a + log b**; (d) see right | (d) Multiplying many tiny probabilities gives numbers too small for a computer to store (underflow). Logs turn the product into a **sum** of manageable numbers, e.g. log-likelihood |
| A5 [F5] | **30**; mean = (1/n) Σᵢ₌₁ⁿ xᵢ | 1 + 4 + 9 + 16 = 30 |
| A6 [F6] | **f(4) = 4**; g → **1** (large +x), → **0** (large −x), g(0) = **0.5** | 16 − 12 = 4. e⁻ˣ → 0 for large x, so g → 1/1; e⁻ˣ → ∞ for very negative x, so g → 0; g(0) = 1/(1 + 1). g is the **sigmoid**, which turns any number into a probability |

## Part B: Descriptive statistics

| Q | Answer | Working / why |
|---|---|---|
| B1 [S1] | mean **6**, median **5**, mode **4**, range **10** | Sum 42 / 7 = 6. Sorted 2, 4, 4, **5**, 7, 8, 12: the middle value. 4 appears twice. 12 − 2 = 10 |
| B2 [S2] | variance **5**, SD **2.24**, sample variance **6.67** | Mean 5; gaps −3, −1, 1, 3 → squares 9, 1, 1, 9 = 20. 20/4 = 5; √5 = 2.24; 20/3 = 6.67 |
| B3 [S2] | see right | The sample mean is worked out from the same data, so the data sits a bit closer to it than to the true mean, and the squared gaps come out slightly too small. Dividing by n − 1 corrects that underestimate |
| B4 [S3] | **Median**; **right (positive) skew** | A few huge salaries drag the mean up; the median is the typical employee |
| B5 [S4] | **z = 1.5** | (85 − 70) / 10 = 1.5: 1.5 SDs above the mean (roughly the top 7% if scores are normal) |
| B6 [S5] | Strong **negative** relationship; e.g. ice-cream sales and drownings | As one rises the other tends to fall, fairly consistently. Ice-cream sales and drownings both rise in hot weather: a **confounder** (the weather) drives both |

## Part C: Probability

| Q | Answer | Working / why |
|---|---|---|
| C1 [P1] | **2/3** | Even {2, 4, 6} or > 4 {5, 6} → {2, 4, 5, 6} = 4/6. By formula: 3/6 + 2/6 − 1/6 (the 6 is in both) |
| C2 [P1] | **3/4** | P(no heads) = ½ × ½ = ¼, so P(at least one) = 1 − ¼ |
| C3 [P2] | see right | **Independent:** one happening doesn't change the other's probability (two separate coin flips). **Mutually exclusive:** they can't both happen (rolling a 1 and a 6 on the same roll). Mutually exclusive events are **not** independent: if one happens, the other's probability drops to 0 |
| C4 [P3] | **≈ 15%** | P(disease \| positive) = 0.9 × 0.01 / (0.9 × 0.01 + 0.05 × 0.99) = 0.009 / 0.0585 = 0.154. Surprising because the disease is rare: false positives from the 99% who are healthy outnumber the true positives |
| C5 [P4] | **£0.40** per game; yes | EV = 0.2 × £10 − 0.8 × £2 = £2 − £1.60 = £0.40 > 0, so over many games you gain about 40p a game on average |
| C6 [P5] | **≈ 0.117** | Binomial: C(10, 3) × 0.5³ × 0.5⁷ = 120 / 1,024 = 0.117 |

## Part D: Distributions and inference

| Q | Answer | Working / why |
|---|---|---|
| D1 [D1] | **≈ 95%** | 150 and 190 are 2 SDs either side of 170 → the 68–95–99.7 rule |
| D2 [D2] | see right | Take many random samples and average each: the averages form an approximately normal curve, centred on the true mean with spread σ/√n, **whatever the shape of the original data**, once n is large enough. It's why we can build confidence intervals and run A/B tests on non-normal data |
| D3 [D3] | SE **£2**; CI **£46.08 to £53.92** | SE = 20 / √100 = 2. 50 ± 1.96 × 2 = 50 ± 3.92 |
| D4 [D4] | see right | (a) H0: there's no difference between the two models. (b) p = 0.03 < 0.05, so reject H0: the difference is statistically significant at 5%. (c) If there were really no difference, a result at least this extreme would happen only 3% of the time; it is **not** the probability that H0 is true. (d) Type I = false positive (finding an effect that isn't there); Type II = false negative (missing a real effect) |
| D5 [D5] | **Two-proportion z-test** (or chi-square); B is **not** significant | p_A = 6%, p_B = 7.5%; pooled 6.75%; z ≈ 1.89, p ≈ 0.059 > 0.05. Before declaring a winner, check: the sample size was planned in advance, users were randomly assigned, no peeking/early stopping, the test ran full weeks, and the effect is big enough to matter |
| D6 [D6] | **0.7** | MLE (maximum likelihood estimation) = choose the parameter value that makes the data you saw most probable. 7/10 heads is most likely when P(heads) = 0.7 |

## Part E: Statistics for ML

| Q | Answer | Working / why |
|---|---|---|
| E1 [M1] | accuracy **0.85**, precision **0.80**, recall **0.67**, F1 **0.73** | (40 + 130)/200; 40/(40 + 10); 40/(40 + 20); 2 × 0.8 × 0.667 / (0.8 + 0.667). **Recall** usually matters most for fraud: each missed fraud costs money, while a false alarm costs a quick check (but precision still matters for workload) |
| E2 [M2] | **99%**; useless | It never catches any spam: recall = 0. Accuracy is misleading on imbalanced data |
| E3 [M3] | **Overfitting** (high variance) | Fixes: simpler model, more training data, regularisation, early stopping, dropout. Never "fix" it by changing the test set |
| E4 [M4] | see right | Test set = an honest estimate of performance on unseen data. k-fold cross-validation: split the data into k parts, train on k − 1 and test on the remaining one, rotate k times, average the scores. Leakage example: scaling with the whole dataset's mean/SD before splitting, or a feature that is only known after the outcome (e.g. "account closed" when predicting churn) |
| E5 [M5] | (a) **11** (b) see right (c) **MSE = 1.67** | (a) 3 + 2 × 4. (b) Each +1 in x increases the predicted y by 2. (c) Errors 1, 0, 2 → squares 1, 0, 4 → 5/3 |
| E6 [M6] | (a) **1** (b) **softmax** (c) **0.357** (d) **→ ∞** | (a) Exactly one class is true, so the probabilities cover all outcomes. (c) −ln 0.7 = 0.357. (d) −ln(p) grows without limit as p → 0: confident wrong answers are punished very hard |

## Part F: Linear algebra

| Q | Answer | Working / why |
|---|---|---|
| F1 [LA1] | a + b = **[5, 2, 2]**; 2a = **[2, 4, 6]** | Add element by element; multiply each element by 2 |
| F2 [LA2] | a · b = **1**; length **5** | 1×4 + 2×0 + 3×(−1) = 4 + 0 − 3. √(3² + 4²) = √25 |
| F3 [LA3] | **≈ 0.707** | (1·1 + 0·1) / (1 × √2) = 1/√2. Cosine similarity compares **direction** (meaning) and ignores length (e.g. document length), so similar texts score high even if one is longer |
| F4 [LA4] | **[[4, 2], [10, 4]]**; **3×4**; **no** | Row × column: [1·2 + 2·1, 1·0 + 2·1] = [4, 2]; [3·2 + 4·1, 3·0 + 4·1] = [10, 4]. (3×2)(2×4) → 3×4. 3×2 by 3×2: the inner numbers (2 and 3) must match, and they don't |
| F5 [LA5] | **[[1, 4], [2, 5], [3, 6]]**; identity leaves it unchanged | Rows become columns. Multiplying by the identity matrix is like multiplying by 1 |
| F6 [LA6] | see right | PCA (principal component analysis) finds new axes along the directions of greatest variance and keeps the top few. With 500 features: faster training, less noise and redundancy (many features are correlated), less overfitting, and the ability to visualise the data in 2–3 dimensions |

## Part G: Calculus and optimisation

| Q | Answer | Working / why |
|---|---|---|
| G1 [C1] | **3x²**, **10x + 3**, **eˣ** | Bring the power down and reduce it by 1; constants vanish; eˣ is its own derivative |
| G2 [C2] | slope; **0** at a minimum | A derivative is the slope (rate of change). At a minimum the curve is flat |
| G3 [C3] | **8x + 4** | Outer: 2(2x + 1); times the inner derivative 2 → 4(2x + 1). Backpropagation is the chain rule applied layer by layer |
| G4 [C4] | ∂f/∂x = **2xy**, ∂f/∂y = **x² + 3**; gradient **[2xy, x² + 3]** | Treat the other variable as a constant |
| G5 [C5] | **2.4**, then **1.92** | f′(w) = 2w. w = 3 − 0.1 × 6 = 2.4; then 2.4 − 0.1 × 4.8 = 1.92 |
| G6 [C6] | see right | Too large: steps overshoot the minimum, bounce around or diverge. Too small: very slow progress, may stall before reaching the minimum |
