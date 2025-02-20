Statistical Inference
=====================

Statistical inference is the process of drawing conclusions about a population based on a sample of data. It involves estimating population parameters, testing hypotheses, and making predictions while accounting for uncertainty. The foundation of statistical inference is probability theory, which provides the framework for assessing the reliability and variability of estimates.

There are two main types of statistical inference:

- **Estimation:** Determining an unknown population parameter based on sample data. This includes point estimation (providing a single best guess) and interval estimation (providing a range of plausible values, such as confidence intervals).
- **Hypothesis Testing:** Making decisions about population parameters based on sample data by assessing the strength of evidence against a null hypothesis.

Statistical inference allows researchers to make probabilistic statements about populations and quantify uncertainty in decision-making.

Test Statistic
~~~~~~~~~~~~~~

A test statistic is a numerical value calculated from sample data that is used to decide whether to reject a null hypothesis in a hypothesis test. The test statistic is compared to a critical value or used to compute a p-value, which helps determine the significance of the result.

Mathematically, a test statistic is often expressed as:

.. math::

   T = \frac{\text{Sample Statistic} - \text{Null Hypothesis Value}}{\text{Standard Error}}

where:

- **Sample Statistic:** A measure obtained from the sample (e.g., sample mean, sample proportion).
- **Null Hypothesis Value:** The hypothesized value of the parameter under the null hypothesis.
- **Standard Error:** A measure of the variability of the sample statistic.

Different tests use different test statistics. Some common examples include:

- **Z-statistic:** Used when the population standard deviation is known and the sample size is large.
- **t-statistic:** Used when the population standard deviation is unknown and the sample size is small (Student’s t-distribution is applied).
- **Chi-square statistic:** Used in tests for variance and categorical data analysis.
- **F-statistic:** Used in ANOVA to compare variances across multiple groups.

Types of Inference Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Confidence Intervals
--------------------

A confidence interval provides a range of values within which a population parameter is likely to fall. It is computed using sample statistics and a margin of error based on the desired confidence level.

The general form of a confidence interval is:

.. math::

   \text{Estimate} \pm \text{Margin of Error}

Hypothesis Testing
------------------

Hypothesis testing is a procedure to assess whether there is enough statistical evidence to support a specific claim about a population parameter. The process includes:

1. Formulating the null hypothesis (:math:`H_0`) and the alternative hypothesis (:math:`H_a`).
2. Choosing an appropriate test statistic.
3. Determining the significance level (:math:`\alpha`), commonly set at 0.05.
4. Computing the test statistic from sample data.
5. Comparing the test statistic to the critical value or computing the p-value.
6. Making a decision: Reject or fail to reject :math:`H_0`.

Properties of Good Estimators
-----------------------------

A good estimator should satisfy the following properties:

- **Unbiasedness:** The expected value of the estimator equals the true parameter value.
- **Consistency:** As the sample size increases, the estimator converges to the true parameter value.
- **Efficiency:** The estimator has the smallest variance among all unbiased estimators.
- **Sufficiency:** The estimator captures all the information in the sample about the parameter.

Distributions in Statistical Inference
----------------------------------------

Statistical inference relies on various probability distributions to model data and derive test statistics for hypothesis testing and estimation. Below is a summary of the most commonly used distributions and their associated test statistics.

Normal Distribution
~~~~~~~~~~~~~~~~~~~

.. math::

   f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}

.. math::

   Z = \frac{X - \mu}{\sigma / \sqrt{n}}

Student’s t-Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   f(x) = \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi} \Gamma\left(\frac{\nu}{2}\right)} \left(1 + \frac{x^2}{\nu}\right)^{-\frac{\nu+1}{2}}

.. math::

   t = \frac{X - \mu}{s / \sqrt{n}}

Chi-Square Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   \chi^2 = \sum \frac{(O - E)^2}{E}

F-Distribution
~~~~~~~~~~~~~~

.. math::

   F = \frac{S_1^2}{S_2^2}

Binomial Distribution
~~~~~~~~~~~~~~~~~~~~~

.. math::

   P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}

.. math::

   Z = \frac{X - np}{\sqrt{np(1-p)}}

Poisson Distribution
~~~~~~~~~~~~~~~~~~~~

.. math::

   P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}

Exponential Distribution
~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   f(x) = \lambda e^{-\lambda x}, \quad x > 0

Probability Distributions and Their Applications
--------------------------------------------------

Normal Distribution
~~~~~~~~~~~~~~~~~~~

- **Probability Density Function (PDF):**

  .. math::

     f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}

- **Standard Normal Transformation:**

  .. math::

     Z = \frac{X - \mu}{\sigma / \sqrt{n}}

- **Properties:**
  
  - Symmetric about :math:`\mu`.
  - Mean: :math:`\mu`, Variance: :math:`\sigma^2`.
  - The empirical rule states that 68%, 95%, and 99.7% of data falls within 1, 2, and 3 standard deviations, respectively.

Statistical Inference (Revisited)
---------------------------------

### Introduction

Statistical inference is the process of drawing conclusions about a population based on a sample of data. It involves estimating population parameters, testing hypotheses, and making predictions while accounting for uncertainty. The foundation of statistical inference is probability theory, which provides the framework for assessing the reliability and variability of estimates.

There are two main types of statistical inference:

- **Estimation:** Determining an unknown population parameter based on sample data. This includes point estimation (providing a single best guess) and interval estimation (providing a range of plausible values, such as confidence intervals).
- **Hypothesis Testing:** Making decisions about population parameters based on sample data by assessing the strength of evidence against a null hypothesis.

Statistical inference allows researchers to make probabilistic statements about populations and quantify uncertainty in decision-making.

Test Statistic
~~~~~~~~~~~~~~

A test statistic is a numerical value calculated from sample data that is used to decide whether to reject a null hypothesis in a hypothesis test. The test statistic is compared to a critical value or used to compute a p-value, which helps determine the significance of the result.

Mathematically, a test statistic is often expressed as:

.. math::

   T = \frac{\text{Sample Statistic} - \text{Null Hypothesis Value}}{\text{Standard Error}}

where:

- **Sample Statistic:** A measure obtained from the sample (e.g., sample mean, sample proportion).
- **Null Hypothesis Value:** The hypothesized value of the parameter under the null hypothesis.
- **Standard Error:** A measure of the variability of the sample statistic.

Hypothesis Testing
~~~~~~~~~~~~~~~~~~

- **Null Hypothesis (:math:`H_0`):** A statement that there is no effect or no difference. It is assumed true until evidence suggests otherwise.
- **Alternative Hypothesis (:math:`H_a`):** A statement that contradicts the null hypothesis, indicating the presence of an effect or difference.
- **Significance Level (:math:`\alpha`):** The probability of rejecting the null hypothesis when it is actually true (Type I error).
- **p-value:** The probability of obtaining a test statistic as extreme as the observed one, assuming :math:`H_0` is true.

Worked Example
~~~~~~~~~~~~~~

**Problem:** A company claims that the average battery life of its smartphones is 20 hours. A sample of 30 smartphones has a mean battery life of 19.5 hours with a standard deviation of 1.5 hours. Test whether the claim is true at a 5% significance level.

**Solution:**

- **Step 1: Define Hypotheses**

  .. math::

     H_0: \mu = 20, \quad H_a: \mu \neq 20

- **Step 2: Compute the Test Statistic**

  .. math::

     t = \frac{19.5 - 20}{1.5 / \sqrt{30}} = \frac{-0.5}{0.273} \approx -1.83

- **Step 3: Determine the Critical Value**

  From the t-table with :math:`df = 29` at :math:`\alpha = 0.05`, the critical value for a two-tailed test is :math:`\pm 2.045`.

- **Step 4: Make a Decision**

  Since :math:`-1.83` falls within the acceptance region (:math:`-2.045, 2.045`), we fail to reject :math:`H_0`. There is no significant evidence to claim that the average battery life differs from 20 hours.

Applications of Hypothesis Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Medical Research:** Testing the effectiveness of new drugs.
- **Manufacturing:** Checking if a machine produces items within tolerance limits.
- **Finance:** Assessing if a new investment strategy yields higher returns.