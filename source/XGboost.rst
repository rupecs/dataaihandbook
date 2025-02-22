Mathematical Explanation of XGBoost
===================================

XGBoost (Extreme Gradient Boosting) is a powerful gradient boosting algorithm that builds an ensemble of decision trees sequentially. The core idea is to combine weak learners (decision trees) into a strong learner. Each tree attempts to correct the errors made by the previous trees in the ensemble. This is achieved using gradient descent to minimize a loss function. Here's a detailed mathematical breakdown:

1. Additive Model
-----------------

The XGBoost model is an additive model, meaning it predicts the output by summing the predictions of individual trees:

.. math::

    \hat{y}_i = \sum_{k=1}^{K} f_k(x_i)

Where:

- :math:`\hat{y}_i`: Predicted value for instance :math:`i`.
- :math:`x_i`: Input features for instance :math:`i`.
- :math:`f_k(x_i)`: Prediction of the :math:`k`-th tree for instance :math:`i`. Each :math:`f_k` is a decision tree.
- :math:`K`: Total number of trees in the ensemble.

2. Objective Function
----------------------

The goal of XGBoost is to minimize the objective function. The objective function consists of two terms: a loss function and a regularization term.

.. math::

    Obj = \sum_{i} L(y_i, \hat{y}_i) + \sum_{k=1}^{K} \Omega(f_k)

Where:

- :math:`L(y_i, \hat{y}_i)`: Loss function that measures the difference between the actual value :math:`y_i` and the predicted value :math:`\hat{y}_i` for instance :math:`i`. Common loss functions for regression include Mean Squared Error (MSE) and Mean Absolute Error (MAE).
- :math:`\Omega(f_k)`: Regularization term that penalizes the complexity of the :math:`k`-th tree. This helps to prevent overfitting. A common form of regularization penalizes the number of leaves in the tree and the L2 norm of the leaf weights.

3. Loss Function (L)
---------------------

The loss function quantifies the error between the predicted and actual values. The tutorial uses Mean Squared Error (MSE).

.. math::

    MSE: L(y_i, \hat{y}_i) = (y_i - \hat{y}_i)^2

The goal is to find the :math:`f_k` that minimizes the overall objective function.

4. Regularization Term (Ω)
---------------------------

The regularization term penalizes complex trees. This prevents overfitting by discouraging trees that are too specific to the training data. A common regularization term is:

.. math::

    \Omega(f_k) = \gamma T + \frac{\lambda}{2} \sum_{j=1}^{T} w_j^2

Where:

- :math:`T`: Number of leaves in the tree.
- :math:`w_j`: Weight (value) of the :math:`j`-th leaf.
- :math:`\gamma`: Regularization parameter that penalizes the number of leaves. A higher :math:`\gamma` encourages simpler trees.
- :math:`\lambda`: Regularization parameter that penalizes the magnitude of leaf weights. A higher :math:`\lambda` encourages smaller leaf weights.

5. Training Process (Iterative)
-------------------------------

XGBoost trains the trees sequentially. At each iteration :math:`t`, a new tree :math:`f_t` is added to the ensemble. The prediction is updated as follows:

.. math::

    \hat{y}_i^{(t)} = \hat{y}_i^{(t-1)} + f_t(x_i)

Where:

- :math:`\hat{y}_i^{(t)}`: Predicted value for instance :math:`i` after adding :math:`t` trees.
- :math:`\hat{y}_i^{(t-1)}`: Predicted value for instance :math:`i` after adding :math:`t-1` trees.
- :math:`f_t(x_i)`: Prediction of the :math:`t`-th tree for instance :math:`i`.

The goal is to find the :math:`f_t` that minimizes the objective function, given the predictions from the previous trees.


6. Taylor Expansion Approximation
---------------------------------

To efficiently find the optimal :math:`f_t`, XGBoost uses a second-order Taylor expansion to approximate the loss function. The Taylor expansion approximates the loss function around the current prediction :math:`\hat{y}_i^{(t-1)}`:

.. math::

    L(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)) \approx L(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2} h_i f_t(x_i)^2

Where:

- :math:`g_i`: First derivative (gradient) of the loss function with respect to the prediction :math:`\hat{y}_i^{(t-1)}`.

  .. math::

      g_i = \frac{\partial L(y_i, \hat{y}_i^{(t-1)})}{\partial \hat{y}_i^{(t-1)}}

- :math:`h_i`: Second derivative (Hessian) of the loss function with respect to the prediction :math:`\hat{y}_i^{(t-1)}`.

  .. math::

      h_i = \frac{\partial^2 L(y_i, \hat{y}_i^{(t-1)})}{\partial \hat{y}_i^{(t-1)^2}}

7. Simplified Objective Function
--------------------------------

By removing constant terms (terms that don't depend on :math:`f_t`), we obtain a simplified objective function:

.. math::

    Obj^{(t)} \approx \sum_{i=1}^{N} \left[g_i f_t(x_i) + \frac{1}{2} h_i f_t(x_i)^2 \right] + \Omega(f_t)

Where:

- :math:`N`: Number of instances in the dataset.

8. Leaf Node Weights (:math:`w_j`)
-----------------------------------

For each leaf node :math:`j` in the tree :math:`f_t`, let :math:`I_j` be the set of instances that fall into that leaf. We can rewrite the objective function in terms of leaf node weights :math:`w_j`:

.. math::

    Obj^{(t)} \approx \sum_{j} \left[\left(\sum_{i \in I_j} g_i \right) w_j + \frac{1}{2} \left(\sum_{i \in I_j} h_i \right) w_j^2 \right] + \gamma T + \frac{\lambda}{2} \sum_{j} w_j^2

To find the optimal leaf weight :math:`w_j` that minimizes the objective function, we take the derivative with respect to :math:`w_j` and set it to zero:

.. math::

    \frac{\partial Obj^{(t)}}{\partial w_j} = \sum_{i \in I_j} g_i + \left(\sum_{i \in I_j} h_i \right) w_j + \lambda w_j = 0

Solving for :math:`w_j`, we get:

.. math::

    w_j = - \frac{\sum_{i \in I_j} g_i}{\sum_{i \in I_j} h_i + \lambda}

9. Gain Function (for Tree Splitting)
-------------------------------------

To determine the best way to split a node in the tree, XGBoost uses a gain function. The gain function measures the reduction in loss achieved by splitting a node.

.. math::

    Gain = \frac{1}{2} \left[\frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{G_P^2}{H_P + \lambda} \right] - \gamma

Where:

- :math:`G_L`: Sum of gradients for instances in the left child node. :math:`G_L = \sum_{i \in I_L} g_i`
- :math:`G_R`: Sum of gradients for instances in the right child node. :math:`G_R = \sum_{i \in I_R} g_i`
- :math:`G_P`: Sum of gradients for instances in the parent node. :math:`G_P = \sum_{i \in I_P} g_i = G_L + G_R`
- :math:`H_L`: Sum of Hessians for instances in the left child node. :math:`H_L = \sum_{i \in I_L} h_i`
- :math:`H_R`: Sum of Hessians for instances in the right child node. :math:`H_R = \sum_{i \in I_R} h_i`
- :math:`H_P`: Sum of Hessians for instances in the parent node. :math:`H_P = \sum_{i \in I_P} h_i = H_L + H_R`
- :math:`\lambda`: L2 regularization parameter on leaf weights.
- :math:`\gamma`: Regularization parameter for the number of leaves.

The split with the highest gain is chosen.

10. Learning Rate (:math:`\eta`)
---------------------------------

To prevent overfitting, XGBoost uses a learning rate (shrinkage). The learning rate scales the contribution of each tree.

.. math::

    \hat{y}_i^{(t)} = \hat{y}_i^{(t-1)} + \eta f_t(x_i)

Where:

- :math:`\eta`: Learning rate (:math:`0 < \eta \leq 1`). A smaller learning rate requires more trees but can lead to better generalization. Typical values are 0.01 to 0.3.

Summary
-------

In summary, the XGBoost algorithm iteratively adds trees to an ensemble. Each tree is trained to predict the gradients of the loss function with respect to the current predictions. The structure of each tree is determined by maximizing the gain function, which measures the reduction in loss achieved by splitting a node. Regularization terms and the learning rate are used to prevent overfitting.

Concrete Example Walkthrough
----------------------------

Let's walk through the concrete example provided in the tutorial, step by step, applying the mathematical concepts outlined above.

1. Dataset
----------

.. list-table::
   :header-rows: 1

   * - House Size (sq ft)
     - Actual Price ($1000s)
   * - 800
     - 150
   * - 1200
     - 220
   * - 1600
     - 280
   * - 2000
     - 350
   * - 2400
     - 420

2. Step 1: Initialize Predictions
---------------------------------

- Calculate the mean of the target variable (Actual Price):

  .. math::

      \hat{y}_i^{(0)} = \frac{150 + 220 + 280 + 350 + 420}{5} = 284

- The initial prediction for every house is $284,000.

3. Step 2: Compute the Gradient and Hessian
-------------------------------------------

- We are using the MSE loss function: 

  .. math::

      L(y_i, \hat{y}_i) = (y_i - \hat{y}_i)^2

- **Gradient (gᵢ):** 

  .. math::

      g_i = \frac{\partial L}{\partial \hat{y}_i} = 2 (\hat{y}_i - y_i)

  * House 1: :math:`g_1 = 2 (284 - 150) = 268`
  * House 2: :math:`g_2 = 2 (284 - 220) = 128`
  * House 3: :math:`g_3 = 2 (284 - 280) = 8`
  * House 4: :math:`g_4 = 2 (284 - 350) = -132`
  * House 5: :math:`g_5 = 2 (284 - 420) = -272`

- **Hessian (hᵢ):** 

  .. math::

      h_i = \frac{\partial^2 L}{\partial \hat{y}_i^2} = 2

  * :math:`h_1 = h_2 = h_3 = h_4 = h_5 = 2`

.. list-table::
   :header-rows: 1

   * - House Size
     - Actual Price
     - Prediction
     - Gradient (:math:`g_i`)
     - Hessian (:math:`h_i`)
   * - 800
     - 150
     - 284
     - 268
     - 2
   * - 1200
     - 220
     - 284
     - 128
     - 2
   * - 1600
     - 280
     - 284
     - 8
     - 2
   * - 2000
     - 350
     - 284
     - -132
     - 2
   * - 2400
     - 420
     - 284
     - -272
     - 2

4. Step 3: Build a Decision Tree (Stump)
----------------------------------------

- We consider a one-level decision tree (a stump). Let's examine two potential splits. We use :math:`\lambda = 0` and :math:`\gamma = 0` for simplicity.

- **Gain Function:**

  .. math::

      Gain = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{G_P^2}{H_P + \lambda} \right] - \gamma

- **Split 1: House Size ≤ 1400**

  - Left Node: Houses 1 and 2
    - :math:`G_L = 268 + 128 = 396`
    - :math:`H_L = 2 + 2 = 4`

  - Right Node: Houses 3, 4, and 5
    - :math:`G_R = 8 + (-132) + (-272) = -396`
    - :math:`H_R = 2 + 2 + 2 = 6`

  - Parent Node: All Houses
    - :math:`G_P = 0` (Sum of all gradients)
    - :math:`H_P = 10` (Sum of all Hessians)

  - **Gain₁ Calculation:**

    .. math::

        Gain_1 = \frac{1}{2} \left[ \frac{396^2}{4} + \frac{(-396)^2}{6} - \frac{0^2}{10} \right]

        = \frac{1}{2} \left[ \frac{156816}{4} + \frac{156816}{6} \right]

        = \frac{1}{2} \left[ 39204 + 26136 \right] = 32670

- **Split 2: House Size ≤ 2200**

  - **Gain₂ Calculation:** 

    .. math::

        Gain_2 = \frac{1}{2} \left[ \frac{272^2}{8} + \frac{(-272)^2}{2} - \frac{0^2}{10} \right]

        = \frac{1}{2} \left[ \frac{73984}{8} + \frac{73984}{2} \right]

        = \frac{1}{2} \left[ 9248 + 36992 \right] = 23120

- Since :math:`Gain_1 > Gain_2`, **Split 1 (House Size ≤ 1400) is the best split.**

5. Step 4: Compute Leaf Node Weights
------------------------------------

.. math::

    w_j = - \frac{\sum g_i}{\sum h_i + \lambda}

- **Left Leaf (House Size ≤ 1400):**

  .. math::

      w_{\text{left}} = - \frac{268 + 128}{2 + 2} = -\frac{396}{4} = -99

- **Right Leaf (House Size > 1400):**

  .. math::

      w_{\text{right}} = - \frac{8 + (-132) + (-272)}{2 + 2 + 2} = -\frac{-396}{6} = 66

6. Step 5: Update Predictions
-----------------------------

- **Learning Rate:** :math:`\eta = 0.1`

.. list-table::
   :header-rows: 1

   * - House Size
     - Actual Price
     - Previous Prediction
     - Leaf Weight
     - Updated Prediction
   * - 800
     - 150
     - 284
     - -99
     - 274.1
   * - 1200
     - 220
     - 284
     - -99
     - 274.1
   * - 1600
     - 280
     - 284
     - 66
     - 290.6
   * - 2000
     - 350
     - 284
     - 66
     - 290.6
   * - 2400
     - 420
     - 284
     - 66
     - 290.6

7. Step 6: Repeat Until Convergence
-----------------------------------

- The process repeats, calculating new gradients based on the updated predictions, building a new tree, and updating the predictions again. This continues until a stopping criterion is met (e.g., a maximum number of trees is reached, or the improvement in the loss function falls below a threshold).

This detailed walkthrough provides a clear understanding of how XGBoost works both mathematically and practically, using the provided example. The real power of XGBoost comes from building many trees and handling more complex datasets with numerous features.
