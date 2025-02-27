.. _random_forests:

######################################
Comprehensive Guide to Random Forests
######################################

.. contents:: Table of Contents
   :local:

Introduction to Decision Trees
===============================

A **Decision Tree** is a supervised learning algorithm used for **classification and regression** tasks. It consists of:

- **Internal nodes** representing decisions based on a feature.
- **Branches** representing outcomes of those decisions.
- **Leaf nodes** representing final class (classification) or value (regression).

How Decision Trees Work
------------------------

1. **Select the Best Feature to Split** at each node using a **splitting criterion**.
2. **Recursively Split** the dataset until a stopping condition is met.
3. **Assign Class or Value** at the leaf nodes.

Splitting Criteria in Decision Trees
=====================================

At each node, the best feature for splitting is selected using one of the following criteria:

Gini Impurity (for Classification)
------------------------------------

Measures the impurity of a node:

.. math::
   Gini = 1 - \sum p_i^2

where :math:`p_i` is the proportion of class :math:`i` in the node.

- **Lower Gini Impurity = Better Split**
- **Range**: 0 (pure node) to 0.5 (worst case for two classes)

Entropy & Information Gain (for Classification)
------------------------------------------------

Entropy measures disorder in a node:

.. math::
   Entropy = -\sum p_i \log_2(p_i)

**Information Gain (IG)** is computed as:

.. math::
   IG = Entropy(parent) - \sum (\text{weighted entropy of children})

- **Higher IG = Better Split**
- **Computationally expensive than Gini Impurity**

Mean Squared Error (MSE) (for Regression)
-----------------------------------------

Measures variance reduction:

.. math::
   MSE = \frac{1}{n} \sum (y_i - \bar{y})^2

Mean Absolute Error (MAE) (for Regression)
------------------------------------------

Alternative criterion for regression:

.. math::
   MAE = \frac{1}{n} \sum |y_i - \bar{y}|

- **More robust to outliers than MSE**

Stopping Criteria for Decision Trees
=====================================

To prevent overfitting, stopping criteria include:

- **Max Depth**: Limits tree depth.
- **Min Samples per Leaf**: Minimum number of samples per leaf.
- **Min Samples per Split**: Minimum samples required to split a node.
- **Impurity Threshold**: Stops if further splitting does not significantly reduce impurity.
- **Max Number of Leaves**: Limits the number of leaf nodes.

Random Forests: Ensemble of Decision Trees
==========================================

**Random Forest** is an ensemble learning method that builds multiple decision trees and aggregates their results.

- **Classification**: Uses majority voting.
- **Regression**: Averages predictions of all trees.

How Random Forests Work
------------------------

1. **Bootstrap Sampling (Bagging)**:
   - Draw random subsets **with replacement**.
   - Each tree is trained on a different **bootstrapped dataset**.

2. **Feature Randomization**:
   - Instead of considering all features at each split, only a **random subset of features** is considered.

3. **Grow Multiple Decision Trees**:
   - Each tree is trained independently.

4. **Aggregate Predictions**:
   - **Classification**: Majority voting.
   - **Regression**: Average of all tree predictions.

Hyperparameters in Random Forests
==================================

- **Number of Trees (`n_estimators`)**: More trees = More stable predictions.
- **Number of Features per Split (`max_features`)**: Controls how many random features are considered.
- **Maximum Depth (`max_depth`)**: Limits tree depth.
- **Minimum Samples per Split (`min_samples_split`)**: Minimum number of samples required to split.
- **Minimum Samples per Leaf (`min_samples_leaf`)**: Minimum number of samples per leaf.
- **Bootstrap Sampling (`bootstrap`)**: Uses bootstrapped samples if True.

Early Stopping in Random Forests
=================================

Although Random Forests **do not naturally support early stopping**, it can be simulated by:

1. Monitoring **Out-of-Bag (OOB) error**.
2. Using **cross-validation** to find optimal `n_estimators`.
3. Limiting **tree depth**.

Advantages of Random Forests
============================

- ✅ **Handles high-dimensional data well**
- ✅ **Resistant to overfitting**
- ✅ **Works for both classification & regression**
- ✅ **Handles missing values & outliers**
- ✅ **Feature importance scores available**

Disadvantages of Random Forests
================================

- ❌ **Computationally expensive**
- ❌ **Memory-intensive**
- ❌ **Less interpretable than single decision trees**

Feature Importance in Random Forests
=====================================

- **Gini Importance**: Measures decrease in Gini impurity when using a feature.
- **Permutation Importance**: Shuffles feature values and observes change in accuracy.

Implementing Random Forest in Python
=====================================

Here’s how to use `RandomForestClassifier` in **Scikit-Learn**:

.. code-block:: python

   from sklearn.ensemble import RandomForestClassifier
   from sklearn.datasets import load_iris
   from sklearn.model_selection import train_test_split
   from sklearn.metrics import accuracy_score

   # Load data
   data = load_iris()
   X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

   # Train Random Forest
   rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
   rf.fit(X_train, y_train)

   # Predict and evaluate
   y_pred = rf.predict(X_test)
   print("Accuracy:", accuracy_score(y_test, y_pred))

Conclusion
==========

Random Forests are a **powerful and versatile** machine learning algorithm that balances **accuracy, robustness, and interpretability** while reducing overfitting compared to single decision trees.

