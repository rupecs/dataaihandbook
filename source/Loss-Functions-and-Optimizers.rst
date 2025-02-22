Loss functions are a crucial part of neural networks, guiding the optimization process by quantifying the difference between predicted and actual outputs. The choice of a loss function depends on the type of problem being solved (classification, regression, etc.). Below are the commonly used loss functions categorized by use case:

---

Regression Loss Functions
=========================
These loss functions are used when the output is a continuous variable.

Mean Squared Error (MSE)
------------------------
- **Formula:**

  .. math::
     MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2

- **Use Case:** Standard for regression problems where large errors should be penalized more than small ones.
- **Downside:** Sensitive to outliers.

Mean Absolute Error (MAE)
-------------------------
- **Formula:**

  .. math::
     MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|

- **Use Case:** Used when we want to minimize absolute deviations and avoid squaring large errors.
- **Downside:** Less sensitive to large errors compared to MSE.

Huber Loss
----------
- **Formula:**

  .. math::
     L(y, \hat{y}) = \begin{cases}
     \frac{1}{2} (y - \hat{y})^2, & \text{if } |y - \hat{y}| \leq \delta \\
     \delta (|y - \hat{y}| - \frac{1}{2} \delta), & \text{otherwise}
     \end{cases}

- **Use Case:** Used in regression when we want robustness against outliers (combines MSE and MAE).
- **Downside:** Requires tuning of the :math:`\delta` hyperparameter.

Log-Cosh Loss
-------------
- **Formula:**

  .. math::
     L(y, \hat{y}) = \sum_{i} \log (\cosh(y_i - \hat{y}_i))

- **Use Case:** Similar to Huber loss but smoother and differentiable everywhere.
- **Downside:** Computationally more expensive.

---

Classification Loss Functions
=============================
These loss functions are used when the output is categorical.

Cross-Entropy Loss
------------------
- **Binary Cross-Entropy (for Binary Classification)**

  - **Formula:**

    .. math::
       BCE = -\frac{1}{n} \sum_{i=1}^{n} y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)

  - **Use Case:** Used for binary classification problems.
  - **Downside:** Can be affected by imbalanced datasets.

- **Categorical Cross-Entropy (for Multi-class Classification)**

  - **Formula:**

    .. math::
       CCE = - \sum_{i=1}^{n} \sum_{j=1}^{k} y_{ij} \log(\hat{y}_{ij})

  - **Use Case:** Used when classes are mutually exclusive (one-hot encoded labels).
  - **Downside:** Can be unstable if probabilities are close to 0.

- **Sparse Categorical Cross-Entropy**
  - **Use Case:** Used for multi-class classification where labels are integers instead of one-hot encoded vectors.
  - **Benefit:** More memory-efficient than categorical cross-entropy.

Kullback-Leibler Divergence (KL-Divergence)
-------------------------------------------
- **Formula:**

  .. math::
     KL(P||Q) = \sum P(x) \log \frac{P(x)}{Q(x)}

- **Use Case:** Used when we want to measure how one probability distribution diverges from another.
- **Example:** Often used in Variational Autoencoders (VAEs).

Hinge Loss (for SVM)
---------------------
- **Formula:**

  .. math::
     Hinge(y, \hat{y}) = \sum \max(0, 1 - y \cdot \hat{y})

- **Use Case:** Used in Support Vector Machines (SVMs) and sometimes deep learning classifiers.
- **Downside:** Only works with margin-based classification.

Focal Loss
----------
- **Formula:**

  .. math::
     FL = -\alpha (1 - \hat{y})^\gamma y \log(\hat{y})

- **Use Case:** Used for imbalanced classification tasks (e.g., detecting rare diseases).
- **Benefit:** Reduces the loss contribution from well-classified examples, focusing on hard cases.

---

Loss Functions for Sequence Tasks
=================================
Used for NLP and time-series tasks.

Connectionist Temporal Classification (CTC) Loss
-------------------------------------------------
- **Use Case:** Used in speech recognition and handwriting recognition where the alignment between input and output sequences is unknown.
- **Example:** Speech-to-text models.

Sequence-to-Sequence (Seq2Seq) Loss
-----------------------------------
- Typically uses **Cross-Entropy Loss** with **teacher forcing**.
- **Use Case:** Used in machine translation, text summarization.

BLEU/ROUGE Scores
-----------------
- Not directly used as a loss function but often used to evaluate NLP models.

---

Generative Model Loss Functions
===============================

Adversarial Loss (GANs)
------------------------
- **Used in Generative Adversarial Networks (GANs).**
- **Generator Loss:** Encourages the generator to create realistic images.
- **Discriminator Loss:** Ensures the discriminator can distinguish between real and fake images.

Variational Autoencoder (VAE) Loss
-----------------------------------
- **Combination of:**
  - **Reconstruction Loss (MSE or Cross-Entropy)**
  - **KL Divergence**

---

Summary Table
=============

.. list-table::
   :widths: 25 30 45
   :header-rows: 1

   * - Task Type
     - Loss Function
     - Use Case
   * - **Regression**
     - MSE, MAE, Huber, Log-Cosh
     - Predicting continuous values
   * - **Binary Classification**
     - Binary Cross-Entropy
     - Spam detection, sentiment analysis
   * - **Multi-class Classification**
     - Categorical Cross-Entropy, Sparse Cross-Entropy
     - Image classification, text classification
   * - **Imbalanced Data**
     - Focal Loss
     - Rare event classification
   * - **Sequence Tasks**
     - CTC Loss, Seq2Seq Loss
     - Speech recognition, machine translation
   * - **Generative Models**
     - Adversarial Loss, VAE Loss
     - GANs, VAEs, Image generation




Optimizers in machine learning help adjust model parameters (like weights and biases) to minimize a loss function. They are crucial for training algorithms efficiently.

Common Optimizers in Machine Learning
=====================================

1. **Gradient Descent (GD)**
   
   - **Batch Gradient Descent**: Computes the gradient using the entire dataset.
   - **Stochastic Gradient Descent (SGD)**: Updates weights after each training example.
   - **Mini-batch Gradient Descent**: Uses a small batch of data per update.

2. **Momentum-based Optimizers**
   
   - **Momentum**: Adds a fraction of the past update to the current gradient.
   - **Nesterov Accelerated Gradient (NAG)**: Looks ahead before computing the gradient.

3. **Adaptive Learning Rate Optimizers**
   
   - **Adagrad**: Adjusts learning rates based on past gradients; suitable for sparse data.
   - **RMSprop**: Divides gradients by a running average of their recent magnitudes.
   - **Adam (Adaptive Moment Estimation)**: Combines momentum and RMSprop, widely used in deep learning.
   - **AdamW**: A variation of Adam that decouples weight decay from learning rate updates.

4. **Second-Order Methods**
   
   - **Newton’s Method**: Uses second-order derivatives for faster convergence.
   - **Quasi-Newton Methods (L-BFGS)**: Approximates Hessian without computing it explicitly.

---

Optimizers Used in Different ML Methods
=======================================

Decision Trees & Ensemble Methods
---------------------------------

- **Greedy Splitting (Gini, Entropy, MSE, MAE)**
- **Pruning Techniques**
- **Gradient Boosting**
- **XGBoost (Optimized Gradient Boosting)**
- **LightGBM (Histogram-based Gradient Boosting)**
- **CatBoost (Categorical Feature Boosting)**

Neural Networks (Shallow Networks)
----------------------------------

- **SGD**
- **Momentum**
- **Adam**
- **RMSprop**
- **L-BFGS** (for small networks)

Deep Neural Networks (DNNs)
---------------------------

- **Adam (most widely used)**
- **AdamW (better regularization than Adam)**
- **RMSprop (especially for RNNs)**
- **NAG (for accelerated convergence)**
- **LARS (Layer-wise Adaptive Rate Scaling for large-scale models)**
- **LAMB (Layer-wise Adaptive Moments, used in BERT, large NLP models)**
- **Lookahead Optimizer (improves stability in deep networks)**

