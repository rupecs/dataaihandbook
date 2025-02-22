
Mathematical Explanation of AdaBoost
======================================

AdaBoost (Adaptive Boosting) is an ensemble method that combines multiple weak classifiers to form a strong classifier. Rather than altering the structure of the model, AdaBoost adapts the weights of the training instances to focus more on the examples that are difficult to classify. This document provides a step-by-step mathematical breakdown of AdaBoost.

1. Additive Model
-----------------

AdaBoost builds an additive model in which the final classifier is a weighted sum of the predictions of individual weak learners:

.. math::

    F(x) = \sum_{t=1}^{T} \alpha_t\, h_t(x)

Where:

- :math:`F(x)` is the final ensemble prediction for the input :math:`x`.
- :math:`h_t(x)` is the prediction of the :math:`t`-th weak learner (typically outputting :math:`\pm1` for binary classification).
- :math:`\alpha_t` is the weight assigned to the :math:`t`-th weak learner.
- :math:`T` is the total number of weak learners in the ensemble.

2. Initialization of Instance Weights
---------------------------------------

Initially, all training instances are assigned equal weights. For :math:`N` training examples, the initial weight for each instance is:

.. math::

    w_i^{(1)} = \frac{1}{N} \quad \text{for } i = 1,2,\dots,N

3. Training Weak Learners and Calculating Error
-----------------------------------------------

At each iteration :math:`t`, AdaBoost trains a weak learner :math:`h_t(x)` using the current weights :math:`w_i^{(t)}`. The weighted error of this weak learner is computed as:

.. math::

    \epsilon_t = \sum_{i=1}^{N} w_i^{(t)}\, I\left( h_t(x_i) \neq y_i \right)

Where:

- :math:`\epsilon_t` is the weighted error at iteration :math:`t`.
- :math:`I(\cdot)` is the indicator function that equals 1 if its argument is true (i.e., when :math:`h_t(x_i)` misclassifies :math:`x_i`) and 0 otherwise.
- :math:`y_i` is the true label for the :math:`i`-th training instance.

4. Calculating the Weak Learner’s Weight
-----------------------------------------

The influence of the weak learner on the final model is determined by its weight, computed as:

.. math::

    \alpha_t = \frac{1}{2} \ln \left(\frac{1 - \epsilon_t}{\epsilon_t}\right)

A lower error :math:`\epsilon_t` yields a higher :math:`\alpha_t`, meaning that more accurate weak learners have a greater contribution to the final prediction.

5. Updating Data Point Weights in Each Learner
-----------------------------------------------

After calculating :math:`\alpha_t`, the weight of each data point is updated to emphasize the misclassified instances. The update rule is given by:

.. math::

    w_i^{(t+1)} = \frac{w_i^{(t)}\, \exp\left(-\alpha_t\, y_i\, h_t(x_i)\right)}{Z_t}

Where:

- :math:`y_i` is the true label of the :math:`i`-th instance.
- :math:`h_t(x_i)` is the prediction made by the weak learner for that instance.
- :math:`Z_t` is a normalization factor ensuring that the sum of weights remains 1, defined as:

  .. math::

      Z_t = \sum_{i=1}^{N} w_i^{(t)}\, \exp\left(-\alpha_t\, y_i\, h_t(x_i)\right)

The exponential factor :math:`\exp\left(-\alpha_t\, y_i\, h_t(x_i)\right)` behaves as follows:

- **For Correctly Classified Instances:**  
  If :math:`h_t(x_i)` correctly predicts :math:`y_i`, then :math:`y_i\, h_t(x_i)=1` and the factor becomes :math:`\exp\left(-\alpha_t\right)`, which is less than 1. This reduces the weight of correctly classified instances.

- **For Misclassified Instances:**  
  If the instance is misclassified (so that :math:`y_i\, h_t(x_i)=-1`), the factor becomes :math:`\exp\left(\alpha_t\right)`, which is greater than 1. This increases the weight of misclassified instances so that subsequent learners focus more on these harder cases.

6. Final Prediction
-------------------

After :math:`T` iterations, the final strong classifier is obtained by taking the sign of the weighted sum of the weak learners’ predictions:

.. math::

    H(x) = \text{sign}\left( \sum_{t=1}^{T} \alpha_t\, h_t(x) \right)

Where:

- :math:`H(x)` is the final predicted label for input :math:`x`.

7. Concrete Example Walkthrough
-------------------------------

Consider a binary classification task with labels :math:`y \in \{-1, +1\}` and three training instances. The process can be illustrated as follows:

**Iteration 1:**

- **Initialization:**  
  All instances are assigned equal weights:

  .. math::

      w_1^{(1)} = w_2^{(1)} = w_3^{(1)} = \frac{1}{3}

- **Train Weak Learner:**  
  Train the first weak learner :math:`h_1(x)` using the current weights.

- **Calculate Error:**  
  Suppose the weighted error is :math:`\epsilon_1 = 0.3`.

- **Compute Weight of Weak Learner:**

  .. math::

      \alpha_1 = \frac{1}{2} \ln \left(\frac{1 - 0.3}{0.3}\right)

- **Update Instance Weights:**  
  For each instance, update the weight as:

  .. math::

      w_i^{(2)} = \frac{w_i^{(1)}\, \exp\left(-\alpha_1\, y_i\, h_1(x_i)\right)}{Z_1}

  For example, if a data point was misclassified, its weight will increase due to :math:`\exp(\alpha_1)`, while a correctly classified point will have its weight decreased by a factor of :math:`\exp(-\alpha_1)`.

**Iteration 2:**

- **Train Weak Learner:**  
  Train the second weak learner :math:`h_2(x)` using the updated weights :math:`w_i^{(2)}`.

- **Calculate Error and Weight:**  
  Compute :math:`\epsilon_2` and then determine:

  .. math::

      \alpha_2 = \frac{1}{2} \ln \left(\frac{1 - \epsilon_2}{\epsilon_2}\right)

- **Update Weights:**  
  Update the instance weights for the next iteration:

  .. math::

      w_i^{(3)} = \frac{w_i^{(2)}\, \exp\left(-\alpha_2\, y_i\, h_2(x_i)\right)}{Z_2}

This process repeats for :math:`T` iterations.

8. Summary
----------

AdaBoost constructs a strong classifier by sequentially training weak learners. Initially, all training instances are given equal importance. In each iteration, the algorithm:

- Trains a weak learner using the current instance weights.
- Computes the learner’s weighted error and assigns it a weight :math:`\alpha_t`.
- Updates the instance weights—reducing the weight of correctly classified instances and increasing the weight of misclassified ones—so that the next learner focuses more on the challenging cases.

Finally, the strong classifier is the sign of the weighted sum of the weak learners’ predictions. This adaptive reweighting mechanism is central to AdaBoost's ability to improve classification performance over multiple iterations.