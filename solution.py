"""
Spring 2026 Kaggle Linear Regression Challenge -- solution
==========================================================
Metric: R^2 on the RAW target.

KEY DIAGNOSTIC FINDINGS (drive every modeling choice below):
  1. The target is a MONOTONIC NONLINEAR transform of a linear combination of
     features: signed-log(target) is tame (skew ~0, kurtosis ~ -1.4) and a
     linear fit there reaches Pearson 0.80 / Spearman 0.88 with the target.
     Raw Pearson correlations are ~0 only because the transform's explosive
     tails destroy linear correlation while preserving rank.
  2. The RAW target is extraordinarily heavy-tailed (kurtosis ~707). A SINGLE
     point is ~50% of the total sum-of-squares; the top 10 points are ~88%.
     Those extremes are largely NOISE-driven, hence unpredictable.
  3. Consequence: raw R^2 is dominated by a handful of unpredictable points and
     is therefore high-variance. The linear-signal raw-R^2 ceiling is only
     ~0.012. Inverting a signed-log fit explodes tail error (CV R^2 = -72).
     Public and private sets contain DIFFERENT extreme points, so the public
     leaderboard is near-pure luck -- exactly as the organizers warned.

STRATEGY:
  Predict the conditional mean E[target | x] with a regularized gradient-boosted
  tree on the RAW target (squared loss = conditional mean, native NaN handling),
  then SHRINK predictions toward the train mean. Shrinkage is the crucial knob:
  it trades a tiny bit of signal for a large reduction in catastrophic tail
  overshoot, which is what actually maximizes EXPECTED R^2 on this metric.
  Seed-averaging further reduces prediction variance.

  Chosen by repeated 6x5-fold CV (averaging out the outlier-driven noise):
    alpha (shrinkage) = 0.40, min_samples_leaf = 80, seed-averaged x8.
    -> expected raw R^2 ~ +0.031, typical (median) fold ~ +0.035.
  Adding the linear predictor as a feature gave no lift (GBM recovers it).
"""
import pandas as pd, numpy as np
from sklearn.ensemble import HistGradientBoostingRegressor

FEATS = [f"x{i}" for i in range(15)]
ALPHA = 0.40          # shrinkage toward the train mean
SEEDS = range(8)      # seed-averaging to cut prediction variance

def main(train_path, test_path, sample_path, out_path="submission.csv"):
    tr = pd.read_csv(train_path)
    te = pd.read_csv(test_path)
    samp = pd.read_csv(sample_path)

    Xtr, y, Xte = tr[FEATS], tr["target"].values, te[FEATS]
    mu, ymin, ymax = y.mean(), y.min(), y.max()

    # Seed-averaged regularized GBM on the RAW target (conditional mean).
    preds = []
    for s in SEEDS:
        model = HistGradientBoostingRegressor(
            max_iter=250, learning_rate=0.03, max_depth=3,
            min_samples_leaf=80, l2_regularization=5.0, random_state=s,
        ).fit(Xtr, y)            # HistGBR handles missing values natively
        preds.append(model.predict(Xte))
    raw = np.mean(preds, axis=0)

    final = mu + ALPHA * (raw - mu)      # shrink -> controls outlier overshoot
    final = np.clip(final, ymin, ymax)   # safety vs. test-time extrapolation

    sub = pd.DataFrame({"Id": te["Id"].values, "target": final})
    sub = samp[["Id"]].merge(sub, on="Id", how="left")   # exact required order
    assert sub["target"].isna().sum() == 0
    sub.to_csv(out_path, index=False)
    print(f"Wrote {out_path} ({len(sub)} rows)")

if __name__ == "__main__":
    main(
        "spring2026_kaggle_linear_regression_challenge_train.csv",
        "spring2026_kaggle_linear_regression_challenge_test.csv",
        "spring2026_sampleSubmission.csv",
    )
