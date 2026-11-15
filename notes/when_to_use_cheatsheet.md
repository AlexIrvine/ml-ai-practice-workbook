# When to use what: DS / ML / stats / GenAI cheat sheet

For multiple-choice questions (MCQs), most questions are "which method fits this situation?" or "what's wrong with this approach?".
Every acronym is spelled out. **Bold = the bit to memorise.**

---

## 1. Picking a model

| Situation | First choice | Why | Main weakness |
|---|---|---|---|
| Predict a number, need to explain it | **Linear regression** | Each coefficient = effect of one feature | Only straight-line relationships; hurt by outliers and correlated features |
| Predict yes/no, need to explain it (credit risk!) | **Logistic regression** | Outputs a probability; coefficients → odds ratios; regulators like it | Only linear boundaries unless you engineer features |
| Tabular data, best accuracy | **Gradient boosting** (XGBoost, LightGBM) | Usually wins on tabular data | Easy to overfit, needs tuning, harder to explain |
| Tabular data, good accuracy with little tuning | **Random forest** | Robust, hard to overfit badly, gives feature importance | Big/slow, less accurate than tuned boosting |
| Need human-readable rules | **Decision tree** (shallow) | Can draw it as a flowchart | One deep tree overfits badly (high variance) |
| Small data, similarity-based | **k-NN (k-nearest neighbours)** | No training; predicts from the k closest points | Slow at prediction time; **needs scaling**; bad in high dimensions |
| Group customers with no labels | **k-means clustering** | Simple, fast | Must choose k; assumes round, similar-sized clusters; **needs scaling** |
| Too many features / visualise | **PCA (principal component analysis)** | Compresses correlated features into fewer components | Components are hard to interpret |
| Text, images, audio | **Neural networks / transformers** | Learn features themselves | Need lots of data and compute; black box |

**Supervised** = has labels (target column). **Unsupervised** = no labels (clustering, PCA).
**Classification** = predict a category. **Regression** = predict a number.

### Tree models: the classic MCQ

| | Decision tree | Random forest | Gradient boosting |
|---|---|---|---|
| How | One tree | **Many deep trees in parallel**, each on a random sample of rows + features, **average the votes** | **Many shallow trees in sequence**, each one **fixes the errors** of the ones before |
| Technique name | n/a | **Bagging** (bootstrap aggregating) | **Boosting** |
| Fixes | n/a | **Variance** (overfitting) | **Bias** (underfitting) |
| Overfit risk | High | Low | Medium (too many trees / too high learning rate) |

None of the tree models need feature scaling.

---

## 2. Metrics

### Confusion matrix (classification)

|  | Predicted fraud | Predicted not fraud |
|---|---|---|
| **Actually fraud** | TP (true positive) | FN (false negative): **missed fraud** |
| **Actually not fraud** | FP (false positive): **false alarm** | TN (true negative) |

| Metric | Formula | Question it answers | Use when |
|---|---|---|---|
| Accuracy | (TP + TN) / all | How often right overall? | Classes balanced. **Misleading when imbalanced** |
| **Precision** | TP / (TP + FP) | Of the ones I flagged, how many were right? | **False alarms are costly** (e.g. blocking good customers' cards) |
| **Recall** (sensitivity, TPR = true positive rate) | TP / (TP + FN) | Of all the real positives, how many did I catch? | **Missing one is costly** (fraud, disease, default) |
| **F1 score** | 2 × P × R / (P + R) | Balance of precision and recall | Imbalanced data, one number needed |
| Specificity | TN / (TN + FP) | Of real negatives, how many cleared? | |
| **ROC-AUC** (receiver operating characteristic, area under the curve) | Area under TPR vs FPR (false positive rate) curve | How well does it **rank** positives above negatives, across all thresholds? 0.5 = random, 1 = perfect | Comparing models, threshold not chosen yet |
| **PR-AUC** (precision-recall area under the curve) | Area under precision vs recall | Same idea, focused on the rare class | **Very imbalanced data** (better than ROC-AUC here) |
| Log loss (cross-entropy) | | Are the **probabilities** good? | When you need calibrated probabilities |

**Classic trap:** 1% of transactions are fraud. A model that says "never fraud" gets **99% accuracy** and catches **0% of fraud** (recall = 0). → Use recall, precision, F1 or PR-AUC.

**Threshold:** lowering the probability cut-off (e.g. 0.5 → 0.2) → **recall up, precision down**. It's a trade-off you choose based on business cost.

### Regression metrics

| Metric | Meaning | Note |
|---|---|---|
| MAE (mean absolute error) | Average size of the error | Same units as target; **robust to outliers** |
| MSE (mean squared error) | Average squared error | **Punishes big errors**; units squared |
| RMSE (root mean squared error) | √MSE | Same units as target; punishes big errors |
| R² (R-squared, coefficient of determination) | Share of the variance explained, 0 to 1 | 0.7 = explains 70% of the variation. Always goes up when you add features → use **adjusted R²** to compare |

---

## 3. Overfitting, bias and variance

| | Underfitting | Overfitting |
|---|---|---|
| Also called | **High bias** | **High variance** |
| Signal | **Train error high AND test error high** | **Train error low, test error much higher** |
| Cause | Model too simple | Model too complex / too little data |
| Fix | More features, more complex model, less regularisation | **More data, regularisation, simpler model, cross-validation, early stopping, dropout** |

### Regularisation: penalise big coefficients

| | **L1 (Lasso)** | **L2 (Ridge)** |
|---|---|---|
| Penalty | Sum of \|coefficients\| | Sum of coefficients² |
| Effect | **Pushes some coefficients to exactly 0** → feature selection | **Shrinks all coefficients**, none to 0 |
| Use when | Many features, you suspect few matter | Correlated features (multicollinearity) |
| Both | **Elastic Net** | |

In sklearn, `C` in `LogisticRegression` = **1 / regularisation strength** → smaller C = stronger regularisation.

---

## 4. Preparing data

### Scaling (standardisation = mean 0, standard deviation 1)
- **Needs scaling:** anything using distances or gradients: **k-NN, k-means, SVM (support vector machine), PCA, linear/logistic regression with regularisation, neural networks**.
- **Doesn't need it:** **tree models** (decision tree, random forest, gradient boosting).

### Encoding categories
- **One-hot encoding**: one 0/1 column per category. Use for categories with no order (region, channel).
- **Ordinal encoding**: 1, 2, 3. Only when there's a real order (low < medium < high).
- High-cardinality (thousands of categories, e.g. postcode) → target encoding or grouping (watch for leakage).

### Missing values
- Drop rows: only if few and random.
- Fill: **median for skewed numbers** (income, amounts), mode for categories, or a model-based imputer.
- **Add a "was missing" flag column**: missingness itself can be predictive.

### Class imbalance (fraud, default)
1. **Use the right metric** (recall / precision / F1 / PR-AUC, not accuracy).
2. **Class weights**: `class_weight="balanced"`, making mistakes on the rare class cost more.
3. **Resampling**: undersample the majority, or oversample the minority. **SMOTE (synthetic minority over-sampling technique)** creates new synthetic minority examples. **Only on the training set!**
4. **Move the decision threshold.**
5. **Stratified split** so train and test have the same class ratio.

### Data leakage: information from the test set or the future gets into training
- **Fitting the scaler / imputer / encoder on all data before splitting.** → **Split first, fit on train only**, then transform test. A **`Pipeline`** does this automatically inside cross-validation.
- Features that are only known **after** the outcome (e.g. "days in collections" when predicting default).
- Random split on **time-series** data → future leaks into the past. Use a time-based split.
- Same customer in train and test → group split.
- **Signal:** suspiciously high accuracy.

---

## 5. Validation and tuning

| Method | Use when |
|---|---|
| **Train / test split** (e.g. 80/20) | Quick check. Test set touched **once**, at the end |
| Train / validation / test | Validation for tuning, test for final score |
| **k-fold cross-validation** (CV) | Small or medium data. Split into k parts, train on k−1, test on 1, rotate, average → more reliable score |
| **Stratified k-fold** | Classification, especially **imbalanced** data: keeps class ratios in each fold |
| **Time-series split** | Data has a time order: always train on the past, test on the future |
| **Grid search / random search** with CV | Tuning hyperparameters (settings you choose, e.g. tree depth, k, C). Random search is cheaper for many settings |

**Parameters** are learned (coefficients). **Hyperparameters** are set by you (k in k-NN, max_depth, learning rate).

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
pipe = Pipeline([("scale", StandardScaler()), ("model", LogisticRegression(class_weight="balanced"))])
print(cross_val_score(pipe, X_train, y_train, cv=5, scoring="f1").mean())
pipe.fit(X_train, y_train)
```

**Gradient descent** fails when: **learning rate too high** (diverges/bounces), **too low** (very slow), **features not scaled** (zig-zags), stuck in a local minimum (non-convex problems like neural networks).

---

## 6. Statistics

### Average and spread
- **Mean** = average. **Median** = middle value. **Mode** = most common.
- **Skewed data (income, transaction amounts, house prices) → use the median**: a few huge values drag the mean up.
- **Standard deviation** = typical distance from the mean. **SE (standard error)** = standard deviation / √n: how much the *mean* wobbles between samples.
- Outliers: **IQR (interquartile range) rule**: outside Q1 − 1.5×IQR or Q3 + 1.5×IQR. Prefer this to "3 standard deviations" on skewed data.

### Distributions

| Distribution | Models | Banking example |
|---|---|---|
| **Normal** (bell curve) | Continuous, symmetric values; averages of many things (CLT, central limit theorem) | Measurement error, average spend over many customers |
| **Binomial** | Number of successes in n yes/no trials | 1,000 loans, how many default? |
| **Poisson** | **Count of events in a fixed time** (rare, independent) | Fraud alerts per hour, complaints per day |
| **Exponential** | **Time between** Poisson events | Time until the next transaction |
| **Log-normal** | Positive, right-skewed | Income, transaction amounts |
| Uniform | Every value equally likely | Random number generator |

**CLT (central limit theorem):** the **mean of a large sample is roughly normal even if the data isn't**. That's why t-tests and confidence intervals work on skewed data with enough rows.

### Hypothesis testing
- **H0 (null hypothesis)** = no effect / no difference. **H1 (alternative hypothesis)** = there is one.
- **p-value = the probability of seeing data at least this extreme IF H0 were true.** Not the probability that H0 is true. Not the probability the result is due to chance.
- p < α (alpha, usually 0.05) → reject H0. p ≥ α → "not enough evidence", **not** "proved no difference".
- **Type I error** = false positive (reject a true H0). Rate = α. **Type II error** = false negative (miss a real effect). Rate = β.
- **Power** = 1 − β = chance of detecting a real effect. More data → more power.
- **CI (confidence interval)**: a 95% CI that **excludes 0** (for a difference) ⇔ significant at 5%.
- **Statistically significant ≠ important.** With huge n, tiny useless effects become significant → always report the **effect size**.

### Which test?

| Question | Data | Test |
|---|---|---|
| Is the mean different from a value? | 1 group, numeric | **One-sample t-test** |
| Do 2 groups have different means? | 2 independent groups, numeric | **Two-sample t-test** (Welch's if variances differ) |
| Same people measured twice (before/after) | Paired numeric | **Paired t-test** |
| 2 groups, numeric but **skewed / small / ranks** | | **Mann-Whitney U** (non-parametric = no normality assumption) |
| **3+ groups**' means | Numeric | **ANOVA (analysis of variance)**; Kruskal-Wallis if non-normal |
| Are two **categorical** variables related? (region vs default yes/no) | Counts in a table | **Chi-squared (χ²) test** |
| Two conversion rates (A/B test) | Proportions | **Two-proportion z-test** (or chi-squared) |
| Linear relationship between 2 numeric variables | | **Pearson correlation** |
| Monotonic (always up/down) relationship, or outliers / ranks | | **Spearman correlation** |

**Correlation ≠ causation.** A confounder (hidden third variable) can drive both. Only a randomised experiment (A/B test) shows causation cleanly.

### A/B testing traps
- **Peeking**: checking every day and stopping at the first p < 0.05 → false-positive rate far above 5%. **Fix the sample size in advance** (power calculation).
- **Multiple testing**: test 20 metrics → about 1 will be "significant" by luck. Fix: **Bonferroni correction** (use α / number of tests) or pick one primary metric up front.
- Sample size: to detect a **smaller effect you need much more data** (halve the effect → about 4× the sample).
- Randomise properly. Check groups are balanced. Run full weeks (weekday effects).

### Regression interpretation
- **Linear coefficient** = change in y for **+1 unit of x, holding the other features fixed**.
- **Logistic coefficient** = change in **log-odds**. **exp(coefficient) = odds ratio**. E.g. coefficient 0.7 → e^0.7 ≈ 2 → **odds of default double** per unit increase. Odds ratio > 1 = higher risk, < 1 = lower.
- **Linear regression assumptions (LINE):** Linear relationship, Independent errors, Normal residuals, Equal variance of residuals (**homoscedasticity**; a funnel shape in the residual plot = heteroscedasticity).
- **Multicollinearity** = features strongly correlated with each other → unstable coefficients, odd signs. Detect with **VIF (variance inflation factor)**: **above 5–10 = a problem**. Fix: drop/combine features, or use Ridge (L2).
- Residual = actual − predicted. A pattern in the residuals = the model is missing something.

### Bayes' theorem: the fraud alarm question
1% of transactions are fraud. The detector catches 95% of fraud (recall) and wrongly flags 5% of legit ones. **A transaction is flagged: what's the chance it's fraud?**
- Fraud and flagged: 0.01 × 0.95 = 0.0095
- Legit and flagged: 0.99 × 0.05 = 0.0495
- P(fraud | flagged) = 0.0095 / (0.0095 + 0.0495) ≈ **16%**

**Lesson: when the thing is rare, most alarms are false**, even with a good detector (base-rate fallacy).

---

## 7. GenAI, LLMs (large language models) and RAG (retrieval-augmented generation)

### Prompting vs RAG vs fine-tuning

| Approach | What it is | Use when | Cost |
|---|---|---|---|
| **Prompting** | Better instructions and examples in the prompt (few-shot) | **Always try first** | Cheapest |
| **RAG** | Search your documents, paste the relevant chunks into the prompt, answer from them | Model needs **your private or up-to-date facts**; you need **citations / audit trail** | Medium |
| **Fine-tuning** | Further-train the model on your examples | Change **style, format, tone or a narrow skill**, not to add facts | Expensive; facts go stale |
| **LoRA (low-rank adaptation)** | Cheap fine-tuning: train small add-on matrices, freeze the rest | Fine-tuning on a budget | |

**Banking default answer: RAG.** Facts can be updated without retraining, answers are grounded and **auditable** (you can show the source), which helps with regulation and reduces hallucination.

### RAG pipeline
**Chunk → embed → store → retrieve top-k → (rerank) → build prompt → generate → evaluate**

- **Chunking**: split documents into pieces, usually **fixed size with overlap** (overlap so sentences on a boundary aren't lost) or by sentence/paragraph. Too small = missing context; too big = noisy and uses up the context window.
- **Embedding** = a list of numbers (vector) representing meaning. Similar meaning → nearby vectors.
- **Cosine similarity** = angle between vectors (ignores length). **If vectors are normalised (length 1), cosine = dot product, and ranking by L2 (Euclidean) distance gives the same order.**
- **Vector search**: brute force for small sets; **ANN (approximate nearest neighbour)** indexes like **FAISS** or **HNSW (hierarchical navigable small world)** at scale: much faster, slightly less exact.
- **Sparse / keyword retrieval: TF-IDF (term frequency–inverse document frequency) and BM25 (Best Matching 25)**. **Beats embeddings on exact terms**: account numbers, product codes, names, acronyms.
- **Hybrid search** = keyword + semantic together, combined with e.g. **RRF (reciprocal rank fusion)**.
- **Reranking**: a **bi-encoder** embeds the query and documents separately (fast, used for the first search). A **cross-encoder** reads query and document together (slow, more accurate) → use it to **re-order the top ~50** results.
- **Prompt**: "Answer only from the context below; say you don't know if it isn't there; cite sources."

### RAG evaluation
| Stage | Metric | Meaning |
|---|---|---|
| Retrieval | **Recall@k** | Of the relevant documents, how many are in the top k? |
| Retrieval | **Precision@k** | Of the top k, how many are relevant? |
| Retrieval | **MRR (mean reciprocal rank)** | How high is the first correct result? (1st → 1, 2nd → 0.5...) |
| Retrieval | **nDCG (normalised discounted cumulative gain)** | Ranking quality with graded relevance |
| Generation | **Faithfulness / groundedness** | Is every claim supported by the retrieved context? |
| Generation | Answer relevance | Does it answer the question? |
| Both | **LLM-as-judge** | Another LLM scores answers against a rubric. Cheap and scalable but biased; check it against human labels |

### LLM concepts
- **Token** ≈ part of a word (~¾ of a word in English). Pricing and limits are in tokens.
- **Context window** = max tokens the model can read at once (prompt + answer).
- **Temperature**: **low (0–0.3) = focused, repeatable** (facts, extraction, banking). **High = more varied/creative.**
- **Top-p (nucleus sampling)**: only sample from the smallest set of words whose probabilities add up to p.
- **Hallucination** = confident, made-up answer. Reduce with RAG, "say I don't know", low temperature, citations, faithfulness checks.
- **Prompt injection** = text in a document or user input that tries to override instructions ("ignore previous instructions..."). Defend: treat retrieved text as data, limit tool permissions, filter inputs and outputs.
- **Agent** = **LLM + tools + loop**: the model decides on an action (call a tool / search / run code), sees the result, and repeats until done. Frameworks: LangChain, LangGraph, Google ADK (Agent Development Kit).
- **Guardrails** = checks around the model: block PII (personally identifiable information), toxic or off-topic output, enforce formats.
- **Attention** = each word looks at every other word and decides how much each matters for its meaning. **Transformers vs RNNs (recurrent neural networks):** transformers process all words **in parallel** and handle long-range context well; RNNs go word by word (slow, forget long context).

---

## 8. Responsible AI (big for a bank)

- **Fairness metrics:**
  - **Demographic parity** = each group gets approved at the **same rate**.
  - **Equal opportunity** = **equal true positive rate (recall)** across groups: qualified people approved equally.
  - **Equalised odds** = equal true positive rate AND equal false positive rate.
- Removing a protected attribute (e.g. gender) **doesn't remove bias**: **proxies** (postcode, job title) can carry it.
- **Explainability:**
  - **SHAP (SHapley Additive exPlanations)**: how much each feature pushed **this prediction** up or down; also works globally. Based on game theory.
  - **LIME (local interpretable model-agnostic explanations)**: fits a simple model around one prediction.
  - Why a bank cares: customers have a right to an explanation of decisions (e.g. a declined loan); regulators (FCA, Financial Conduct Authority; PRA, Prudential Regulation Authority) need to audit models.
- **Monitoring after deployment:**
  - **Data drift** = the **inputs** change (new customer mix). Detect: PSI (population stability index), KS (Kolmogorov–Smirnov) test.
  - **Concept drift** = the **relationship** between inputs and target changes (fraudsters change tactics, recession changes who defaults).
  - Fix: monitor, alert, retrain.
- **Model governance**: documentation (model cards), independent validation, approval before deployment, audit trails, human in the loop for high-impact decisions.

---

## 9. Big-O (time complexity) of common Python operations

| Operation | Cost |
|---|---|
| `x in list` | **O(n)**: scans the whole list |
| `x in set` / `key in dict` | **O(1)** average: hash lookup |
| `list.append(x)` | O(1) |
| `list.insert(0, x)` / `list.pop(0)` | O(n); use `collections.deque` for O(1) |
| `list.pop()` (from the end) | O(1) |
| `sorted(x)` / `list.sort()` | **O(n log n)** |
| `heapq.heappush` / `heappop` | O(log n) |
| Top k of n with a heap | O(n log k) |
| Binary search | O(log n) |
| String `+=` in a loop | O(n²) overall; use `"".join(parts)` |

**Rules:** keep only the biggest term (O(n) + O(1) = **O(n)**). One pass with O(1) work per step = O(n). A loop inside a loop is **not automatically O(n²)**: count how many times each pointer moves in total.

---

## 10. Quick MCQ traps

1. High accuracy on imbalanced data → probably meaningless; check recall and precision.
2. p-value ≠ probability the null hypothesis is true.
3. Fit the scaler on **train only**; scaling before the split = leakage.
4. Trees don't need scaling; k-NN, k-means, SVM, PCA and regularised regression do.
5. Random forest = bagging (reduces variance); gradient boosting = boosting (reduces bias).
6. L1 → some coefficients exactly 0 (feature selection); L2 → shrinks all.
7. Train error low + test error high = overfitting (high variance).
8. Skewed data → median and IQR, not mean and standard deviation.
9. Time-series → split by time, never shuffle.
10. Need private / changing facts in an LLM → RAG, not fine-tuning.
11. Exact codes / IDs → keyword search (BM25) beats embeddings.
12. Logistic regression coefficient → exp() → odds ratio.
13. Correlation ≠ causation; randomised experiment needed for causation.
14. Rare event + good detector → most alarms still false (Bayes).
15. Data drift = inputs change; concept drift = the input→output relationship changes.
