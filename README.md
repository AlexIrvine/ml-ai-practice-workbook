# ML / AI practice workbook

A self-study course for moving into **machine learning / AI engineering**: maths and
statistics lessons with worked examples, plus coding drills (LeetCode-style patterns,
pandas, SQL, statistics in code). Everything is a Jupyter notebook.

**Start with [`SETUP.md`](SETUP.md)** (once, about 10 minutes).

## How it works

- Every exercise file `x.ipynb` has a model-answer file **`x-solutions.ipynb`** right next
  to it, already run so you can see the expected output. Have a real attempt first, then
  compare.
- Lessons: read the notes (every number is shown with its working), answer in the ✏️
  cells (double-click to type, Shift+Enter to finish), then do the code tasks.
- If your output disagrees with a **Check:** line or `# expect` comment, stop and find out
  why. That habit matters more than speed.
- Write a confidence score (1 = guess, 2 = fairly sure, 3 = certain) where asked, so you
  can see later which topics you only guessed.
- Coding drills: set a timer, write the solution in the stub, run the test cell, then
  fill in "Explain it" (approach + time and space complexity).
- Labels like `[F5]` or `[P3]` are topic codes: F = foundations, S = descriptive
  statistics, P = probability, D = distributions and inference, M = ML statistics,
  LA = linear algebra, C = calculus, PY = Python for maths.

## Suggested order

| Step | File (in `maths/practice/` unless shown) | Topic |
|---|---|---|
| 0 | `maths/assessment/assessment.md` + `assessment-python.py` | Optional diagnostic test: find your gaps first |
| 1 | `01-sigma-notation` | Σ notation and the mean |
| 2 | `02-variance-sd` | Variance and standard deviation |
| 3 | `03-z-scores` | z-scores and outliers |
| 4 | `04-normal-distribution` | The normal distribution |
| 5 | `05-warmups` | Review set A |
| 6 | `06-clt` | Central limit theorem |
| 7 | `07-se-ci` | Standard error and confidence intervals |
| 8 | `08-warmups` | Review set B |
| 9 | `09-probability-rules` | Probability rules: not, or, at least one |
| 10 | `10-bayes` | Conditional probability and Bayes' theorem |
| — | `drills/01` → `drills/15` | Coding drills, in number order. Do `14_big_o_primer` early if Big-O notation is new to you. `11a` is a tutorial for `11`. |

Maths and coding can be done side by side. `data/loans_clean.csv` is the input for
drill 07 **and** the answer to drill 05, so do 05 before you open it.

## Layout

```
SETUP.md           one-time install steps
drills/            coding drills (NN_topic.ipynb) + NN_topic-solutions.ipynb
maths/practice/    lessons (NN-topic.ipynb) + NN-topic-solutions.ipynb
maths/assessment/  optional diagnostic test + model answers
data/              seed_bank_db.py (builds data/bank.db for the SQL drills), loans CSVs
notes/             "when to use which pattern" cheat sheet
```

## Redoing a notebook

Make a copy first (e.g. `10-bayes-attempt2.ipynb`), or reset it with
`git checkout -- <file>`.
