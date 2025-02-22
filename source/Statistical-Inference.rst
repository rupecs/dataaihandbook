Statistical Inference: A Comprehensive Guide
=============================================

Statistical inference is a fundamental concept in statistics, allowing us to draw conclusions about populations based on sample data. This guide provides a comprehensive overview of the key principles and techniques involved.

Statistical Inference
---------------------

Statistical inference is the process of drawing conclusions about a population based on a sample of data. It involves estimating population parameters, testing hypotheses, and making predictions while accounting for uncertainty. The foundation of statistical inference is probability theory, which provides the framework for assessing the reliability and variability of estimates.

There are two main types of statistical inference:

1. **Estimation:** Determining an unknown population parameter based on sample data. This includes point estimation (providing a single best guess) and interval estimation (providing a range of plausible values, such as confidence intervals).

2. **Hypothesis Testing:** Making decisions about population parameters based on sample data by assessing the strength of evidence against a null hypothesis.

Statistical inference allows researchers to make probabilistic statements about populations and quantify uncertainty in decision-making.

Test Statistic
--------------

A test statistic is a numerical value calculated from sample data that is used to decide whether to reject a null hypothesis in a hypothesis test. The test statistic is compared to a critical value or used to compute a p-value, which helps determine the significance of the result.

Mathematically, a test statistic is often expressed as:

.. math::
   T = \frac{\text{Sample Statistic} - \text{Null Hypothesis Value}}{\text{Standard Error}}

where:

* **Sample Statistic:** A measure obtained from the sample (e.g., sample mean, sample proportion).
* **Null Hypothesis Value:** The hypothesized value of the parameter under the null hypothesis.
* **Standard Error:** A measure of the variability of the sample statistic.

Different tests use different test statistics. Some common examples include:

* **Z-statistic:** Used when the population standard deviation is known and the sample size is large.
* **t-statistic:** Used when the population standard deviation is unknown and the sample size is small (Student’s t-distribution is applied).
* **Chi-square statistic:** Used in tests for variance and categorical data analysis.
* **F-statistic:** Used in ANOVA to compare variances across multiple groups.

Types of Inference Methods
--------------------------

Confidence Intervals
^^^^^^^^^^^^^^^^^^^^

A confidence interval provides a range of values within which a population parameter is likely to fall. It is computed using sample statistics and a margin of error based on the desired confidence level.

The general form of a confidence interval is:

.. math::
   \text{Sample Statistic} \pm \text{Margin of Error}

where the margin of error depends on the standard error and a critical value from the chosen probability distribution (e.g., Z-distribution or t-distribution). A higher confidence level will result in a wider interval, reflecting greater certainty that the true parameter lies within the range.

Hypothesis Testing
^^^^^^^^^^^^^^^^^^^^

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

1. **Unbiasedness:** The expected value of the estimator equals the true parameter value.
2. **Consistency:** As the sample size increases, the estimator converges to the true parameter value.
3. **Efficiency:** The estimator has the smallest variance among all unbiased estimators.
4. **Sufficiency:** The estimator captures all the information in the sample about the parameter.

Distributions in Statistical Inference
---------------------------------------

Statistical inference relies on various probability distributions to model data and derive test statistics for hypothesis testing and estimation. Below is a summary of the most commonly used distributions and their associated test statistics.

Normal Distribution
^^^^^^^^^^^^^^^^^^^^

.. math::
   f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}

.. math::
   Z = \frac{X - \mu}{\sigma / \sqrt{n}}

Student’s t-Distribution
^^^^^^^^^^^^^^^^^^^^^^^^

.. math::
   f(x) = \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi} \Gamma\left(\frac{\nu}{2}\right)} \left(1 + \frac{x^2}{\nu}\right)^{-\frac{\nu+1}{2}}

.. math::
   t = \frac{\bar{X} - \mu}{s / \sqrt{n}}

Chi-Square Distribution
^^^^^^^^^^^^^^^^^^^^^^

.. math::
   \chi^2 = \sum \frac{(O - E)^2}{E}

Where *O* represents the observed frequency and *E* represents the expected frequency.

F-Distribution
^^^^^^^^^^^^^^^^

.. math::
   F = \frac{S_1^2}{S_2^2}

Where :math:`S_1^2` and :math:`S_2^2` are the variances of two independent samples.

Binomial Distribution
^^^^^^^^^^^^^^^^^^^^^

.. math::
   P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}

.. math::
   Z = \frac{X - np}{\sqrt{np(1-p)}}

Poisson Distribution
^^^^^^^^^^^^^^^^^^^^

.. math::
   P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}

Exponential Distribution
^^^^^^^^^^^^^^^^^^^^^^^

.. math::
   f(x) = \lambda e^{-\lambda x}, \quad x > 0



Probability Distributions and Their Applications
================================================



Understanding the Normal Distribution and Hypothesis Testing
------------------------------------------------------------


Definition and Properties
~~~~~~~~~~~~~~~~~~~~~~~~~

The normal distribution is a continuous probability distribution characterized by its bell-shaped curve. It is widely used in statistics due to the Central Limit Theorem, which states that the distribution of sample means approaches normality as the sample size increases.

The probability density function (PDF) of a normal distribution with mean :math:`\mu` and standard deviation :math:`\sigma` is given by:

.. math::
   f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}


Standard Normal Distribution and Transformation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A standard normal distribution is a special case where :math:`\mu = 0` and :math:`\sigma = 1`. Any normal variable :math:`X` can be transformed into the standard normal variable :math:`Z` using:

.. math::
   Z = \frac{X - \mu}{\sigma}

Key Properties
~~~~~~~~~~~~~~

* Symmetry: The normal distribution is symmetric about its mean :math:`\mu`.
* Mean and Variance: Mean = :math:`\mu`, Variance = :math:`\sigma^2`.
* Empirical Rule:

  * 68% of data lies within 1 standard deviation.
  * 95% of data lies within 2 standard deviations.
  * 99.7% of data lies within 3 standard deviations.

Real-World Applications
~~~~~~~~~~~~~~~~~~~~~~~

* Human characteristics (e.g., height, weight distribution)
* Stock market returns approximations
* Measurement errors in experiments
* Signal processing in engineering


Worked Example: Testing a Claim About Battery Life
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem Statement
^^^^^^^^^^^^^^^^^

A smartphone company claims that the average battery life of its devices is 20 hours. A sample of 30 smartphones shows an average battery life of 19.5 hours with a standard deviation of 1.5 hours. Test this claim at a 5% significance level.

Step 1: Define Hypotheses
^^^^^^^^^^^^^^^^^^^^^^^^^

* Null Hypothesis (:math:`H_0`): :math:`\mu = 20` (The true mean battery life is 20 hours)
* Alternative Hypothesis (:math:`H_a`): :math:`\mu \neq 20` (The true mean battery life is different from 20 hours)

Step 2: Compute the Test Statistic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the population standard deviation is unknown, we use the t-statistic:

.. math::
   t = \frac{\bar{x} - \mu}{s / \sqrt{n}}

Substituting the given values:

.. math::
   t = \frac{19.5 - 20}{1.5 / \sqrt{30}} = \frac{-0.5}{0.273} = -1.83

Step 3: Determine the Critical Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a two-tailed test with :math:`\alpha = 0.05` and 29 degrees of freedom (df = n - 1), the critical values from the t-table are :math:`\pm 2.045`.

Step 4: Make a Decision
^^^^^^^^^^^^^^^^^^^^^^^^

The computed test statistic :math:`t = -1.83` falls inside the acceptance region :math:`[-2.045, 2.045]`.

Since :math:`|t| < 2.045`, we fail to reject :math:`H_0`.

Conclusion
^^^^^^^^^^

There is not enough statistical evidence to conclude that the true mean battery life differs from 20 hours.





Understanding the Student’s t-Distribution and Hypothesis Testing
----------------------------------------------------------------

The Student’s t-distribution is a continuous probability distribution used primarily when the sample size is small, and the population standard deviation is unknown. It is similar in shape to the normal distribution but has heavier tails, meaning it gives more probability to extreme values.

The probability density function (PDF) of the t-distribution with degrees of freedom :math:`v` is given by:

.. math::
   f(t) = \frac{\Gamma \left(\frac{v+1}{2} \right)}{\sqrt{v\pi} \Gamma \left(\frac{v}{2} \right)} \left(1 + \frac{t^2}{v} \right)^{-\frac{v+1}{2}}

where:

* :math:`v` is the degrees of freedom (:math:`df = n - 1`)
* :math:`\Gamma(x)` is the gamma function

Properties of the t-Distribution
---------------------------------

* **Symmetry:** The t-distribution is symmetric about zero, similar to the normal distribution.

* **Mean and Variance:**

  * Mean = 0
  * Variance = :math:`\frac{v}{v-2}` for :math:`v > 2`

* **Shape Dependence:**

  * For small degrees of freedom, the distribution has heavier tails (higher kurtosis).
  * As :math:`v \to \infty`, the t-distribution approaches the standard normal distribution.

* **Application in Small Samples:** Used when :math:`n < 30` and the population standard deviation :math:`\sigma` is unknown.

Applications of the Student’s t-Distribution
----------------------------------------------

* Confidence intervals for small sample means
* Hypothesis testing for population means with unknown variance
* Regression analysis when estimating coefficients
* Medical and psychological studies with limited data

Problem Statement
-----------------

A company claims that a new drug reduces blood pressure by 10 mmHg on average. A sample of 15 patients shows an average reduction of 8.5 mmHg with a standard deviation of 3 mmHg. Test this claim at a 5% significance level.

Step 1: Define Hypotheses
-------------------------

* Null Hypothesis (:math:`H_0`): :math:`\mu = 10` (The true mean reduction is 10 mmHg)
* Alternative Hypothesis (:math:`H_1`): :math:`\mu \neq 10` (The true mean reduction is different from 10 mmHg)

Step 2: Compute the Test Statistic
-----------------------------------

Since the population standard deviation is unknown, we use the t-statistic:

.. math::
   t = \frac{\bar{x} - \mu}{s / \sqrt{n}}

Substituting the given values:

.. math::
   t = \frac{8.5 - 10}{3 / \sqrt{15}}

.. math::
   t = \frac{-1.5}{0.7746} = -1.937

Step 3: Determine the Critical Value
--------------------------------------

For a two-tailed test with :math:`\alpha = 0.05` and :math:`df = 15 - 1 = 14`, the critical values from the t-table are:

.. math::
   t_{\text{critical}} = \pm 2.145

Step 4: Make a Decision
------------------------

The computed test statistic :math:`t = -1.937` falls inside the acceptance region :math:`(-2.145, 2.145)`.

Since :math:`|t| < t_{\text{critical}}`, we fail to reject :math:`H_0`.

Conclusion
----------

There is not enough statistical evidence to conclude that the true mean reduction in blood pressure differs from 10 mmHg.



Understanding the Chi-Square Distribution and Hypothesis Testing
--------------------------------------------------------------

The Chi-Square (χ²) distribution is a continuous probability distribution that arises in hypothesis testing, particularly in tests of variance and categorical data analysis. It is used when dealing with sample variances and independence tests.

The probability density function (PDF) of the Chi-Square distribution with *k* degrees of freedom is:

.. math::
   f(x) = \frac{x^{k/2 - 1} e^{-x/2}}{2^{k/2} \Gamma(k/2)}, \quad x > 0

where:

* *k* is the degrees of freedom (df)
* Γ(x) is the gamma function

Properties of the Chi-Square Distribution
-----------------------------------------

* **Non-Negativity:** The chi-square distribution is defined only for non-negative values (:math:`x \geq 0`).
* **Shape Dependence:**

  * For small *k*: The distribution is right-skewed.
  * As :math:`k \to \infty`: It approximates a normal distribution.
* **Mean and Variance:**

  * Mean = *k*
  * Variance = 2*k*

Applications of the Chi-Square Distribution
------------------------------------------

* Testing variance in normally distributed populations
* Chi-Square Goodness-of-Fit Test (to check if data follows a specific distribution)
* Chi-Square Test of Independence (to test relationships between categorical variables)
* Statistical genetics, quality control, and machine learning feature selection

Problem Statement
-----------------

A university claims that the variance in students' final exam scores is 225. A random sample of 20 students gives a variance of 300. Test whether the variance is significantly different from 225 at a 5% significance level.

Step 1: Define Hypotheses
--------------------------

* Null Hypothesis (H₀): :math:`\sigma^2 = 225` (The true variance is 225)
* Alternative Hypothesis (H₁): :math:`\sigma^2 \neq 225` (The true variance is different from 225)

Step 2: Compute the Test Statistic
-----------------------------------

For variance testing, we use the Chi-Square test statistic:

.. math::
   \chi^2 = \frac{(n - 1) s^2}{\sigma^2}

Substituting the given values:

.. math::
   \chi^2 = \frac{(20 - 1) (300)}{225}

.. math::
   \chi^2 = \frac{19 \times 300}{225} = \frac{5700}{225} = 25.33

Step 3: Determine the Critical Values
-------------------------------------

For a two-tailed test with :math:`\alpha = 0.05` and *df* = 20 - 1 = 19, the critical values from the Chi-Square table are:

.. math::
   \chi^2_{\text{critical lower}} = 10.117, \quad \chi^2_{\text{critical upper}} = 32.852

Step 4: Make a Decision
------------------------

The computed :math:`\chi^2 = 25.33` lies within the acceptance region (10.117, 32.852).

Since :math:`\chi^2` does not exceed the critical values, we fail to reject H₀.

Conclusion
----------

There is not enough statistical evidence to conclude that the variance of exam scores is significantly different from 225.




Understanding the F-Distribution and Hypothesis Testing
--------------------------------------------------------

The F-distribution is a continuous probability distribution used primarily in variance comparison tests, such as the ANOVA (Analysis of Variance) test and the F-test for equality of variances. It is defined as the ratio of two independent chi-square distributed variables, each divided by its respective degrees of freedom.

The probability density function (PDF) of the F-distribution with degrees of freedom :math:`d_1` and :math:`d_2` is:

.. math::

   f(x) = \frac{\Gamma \left(\frac{d_1 + d_2}{2} \right)}{\Gamma \left(\frac{d_1}{2} \right) \Gamma \left(\frac{d_2}{2} \right)} \left(\frac{d_1}{d_2}\right)^{d_1/2} \frac{x^{(d_1/2 - 1)}}{\left(1 + \frac{d_1}{d_2} x \right)^{(d_1 + d_2)/2}}, \quad x > 0

where:

* :math:`d_1` and :math:`d_2` are the degrees of freedom for the two sample variances.
* :math:`\Gamma(x)` is the gamma function.

Properties of the F-Distribution
---------------------------------

* **Non-Negativity:** The F-distribution is only defined for non-negative values (:math:`x \geq 0`).
* **Right-Skewed:** The distribution is always skewed to the right, regardless of degrees of freedom.
* **Mean and Variance:**

  * Mean = :math:`\frac{d_2}{d_2 - 2}` for :math:`d_2 > 2`
  * Variance = :math:`\frac{2 d_2^2 (d_1 + d_2 - 2)}{d_1 (d_2 - 2)^2 (d_2 - 4)}` for :math:`d_2 > 4`
* **Used for Comparing Variances:** The F-distribution is used to test whether two population variances are equal.

Applications of the F-Distribution
------------------------------------

* **F-Test for Variance Comparison:** Determines if two population variances are significantly different.
* **ANOVA (Analysis of Variance):** Compares means across multiple groups to determine if at least one differs.
* **Regression Analysis:** Assesses the overall significance of a regression model.

Problem Statement
-----------------

Two manufacturing plants claim that their production variances in the number of defective products are equal. A sample of 25 products from Plant A has a variance of 4.5, while a sample of 30 products from Plant B has a variance of 2.0. Test the claim at a 5% significance level.

Step 1: Define Hypotheses
--------------------------

* Null Hypothesis (:math:`H_0`): :math:`\sigma_A^2 = \sigma_B^2` (The two population variances are equal).
* Alternative Hypothesis (:math:`H_1`): :math:`\sigma_A^2 > \sigma_B^2` (The variance of Plant A is significantly greater than that of Plant B).

Step 2: Compute the Test Statistic
-----------------------------------

The F-test statistic is calculated as:

.. math::

   F = \frac{s_A^2}{s_B^2}

Substituting the given values:

.. math::

   F = \frac{4.5}{2.0} = 2.25

The degrees of freedom (df) are:

.. math::

   d_1 = n_A - 1 = 25 - 1 = 24

.. math::

   d_2 = n_B - 1 = 30 - 1 = 29

Step 3: Determine the Critical Value
-------------------------------------

For a one-tailed test with :math:`\alpha = 0.05`, :math:`d_1 = 24`, and :math:`d_2 = 29`, the critical F-value from the F-table is:

:math:`F_{\text{critical}} = 2.03`

Step 4: Make a Decision
------------------------

The computed :math:`F = 2.25` is greater than the critical value :math:`F_{\text{critical}} = 2.03`, meaning we are in the rejection region.

Since :math:`F > F_{\text{critical}}`, we reject :math:`H_0`.

Conclusion
----------

There is enough statistical evidence to conclude that the variance in defective products at Plant A is significantly greater than at Plant B.



Understanding the Binomial Distribution and Hypothesis Testing
---------------------------------------------------------------

The Binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of independent Bernoulli trials, where each trial has only two possible outcomes: success or failure.

The probability mass function (PMF) of the Binomial distribution is given by:

.. math::
   P(X=k) = \binom{n}{k} p^k (1 - p)^{n - k}

where:

* :math:`X` is the number of successes in :math:`n` trials
* :math:`n` is the total number of trials
* :math:`k` is the number of successes
* :math:`p` is the probability of success in a single trial
* :math:`\binom{n}{k} = \frac{n!}{k!(n-k)!}` is the binomial coefficient

Properties of the Binomial Distribution
---------------------------------------

* Discrete Distribution: The binomial distribution only takes integer values from 0 to :math:`n`.

* Mean and Variance:

  * Mean = :math:`E(X) = np`

  * Variance = :math:`Var(X) = np(1 - p)`

* Symmetry & Skewness:

  * The distribution is symmetric if :math:`p = 0.5`.

  * It is right-skewed if :math:`p < 0.5` and left-skewed if :math:`p > 0.5`.

* As :math:`n` increases, the binomial distribution approximates the normal distribution (by the Central Limit Theorem).

Applications of the Binomial Distribution
-----------------------------------------

* Modeling pass/fail outcomes in exams
* Quality control (e.g., defective vs. non-defective products)
* Predicting election outcomes (success = candidate wins a vote)
* Modeling medical treatment success rates

Problem Statement
-----------------

A medical trial is conducted for a new vaccine, and the manufacturer claims that it has a 90% success rate in preventing infection. A random sample of 100 patients receives the vaccine, and 82 patients successfully develop immunity. Test whether the true success rate is lower than 90% at a 5% significance level.

Step 1: Define Hypotheses
--------------------------

* Null Hypothesis (:math:`H_0`): :math:`p = 0.9` (The vaccine is 90% effective).

* Alternative Hypothesis (:math:`H_1`): :math:`p < 0.9` (The vaccine is less effective than claimed).

Step 2: Compute the Test Statistic
-----------------------------------

Since :math:`n` is large, we use the normal approximation to the binomial (i.e., the z-test for proportions):

.. math::
   Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1 - p_0)}{n}}}

where:

* :math:`\hat{p} = \frac{82}{100} = 0.82` (sample proportion)

* :math:`p_0 = 0.9` (claimed proportion)

* :math:`n = 100`

Substituting the values:

.. math::
   Z = \frac{0.82 - 0.9}{\sqrt{\frac{0.9(1 - 0.9)}{100}}}

.. math::
   Z = \frac{-0.08}{\sqrt{\frac{0.09}{100}}}

.. math::
   Z = \frac{-0.08}{\frac{0.03}{1}} = -2.67

Step 3: Determine the Critical Value
-------------------------------------

For a one-tailed test at :math:`\alpha = 0.05`, the critical value from the standard normal table is:

.. math::
   Z_{\text{critical}} = -1.645

Step 4: Make a Decision
------------------------

The computed :math:`Z = -2.67` is less than the critical value :math:`Z_{\text{critical}} = -1.645`, meaning we are in the rejection region.

Since :math:`Z < Z_{\text{critical}}`, we reject :math:`H_0`.

Conclusion
----------

There is enough statistical evidence to conclude that the true effectiveness of the vaccine is lower than the claimed 90%.





Understanding the Poisson Distribution and Hypothesis Testing
--------------------------------------------------------------

The Poisson distribution is a discrete probability distribution that models the
number of events occurring in a fixed interval of time or space, where the
events occur independently and at a constant average rate. It is often used
in situations where events happen rarely or sporadically.

The probability mass function (PMF) of the Poisson distribution is:

.. math::
   P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \dots

where:

* :math:`X` is the number of events in the fixed interval
* :math:`k` is the number of occurrences (non-negative integer)
* :math:`\lambda` is the mean number of events (also the variance) in the interval
* :math:`e` is Euler’s number, approximately equal to 2.71828

Properties of the Poisson Distribution
---------------------------------------

* **Discrete Distribution:** The Poisson distribution takes non-negative
  integer values.
* **Mean and Variance:**

  * Mean = :math:`E(X) = \lambda`
  * Variance = :math:`Var(X) = \lambda`
* **Skewness:** The distribution is right-skewed when :math:`\lambda` is small,
  and it becomes more symmetric as :math:`\lambda` increases.
* **Approximates Normal Distribution:** For large :math:`\lambda`, the Poisson
  distribution approximates a normal distribution due to the Central Limit
  Theorem.

Applications of the Poisson Distribution
----------------------------------------

* Modeling rare events: For example, the number of accidents at an
  intersection or the number of calls to a call center per minute.
* Queuing theory: Modeling the arrival of customers at a service facility.
* Natural phenomena: Modeling occurrences like radioactive decay, meteorite
  impacts, or the number of emails received.

Problem Statement
-----------------

A restaurant claims that on average, 3 customers arrive per minute during peak
hours. A sample of 60 minutes shows that, on average, 200 customers arrive in
total during the 60-minute period. Test whether the average customer arrival
rate is different from 3 per minute at a 5% significance level.

Step 1: Define Hypotheses
--------------------------

* Null Hypothesis (:math:`H_0`): :math:`\lambda = 3` (The average arrival rate is 3 customers per minute).
* Alternative Hypothesis (:math:`H_1`): :math:`\lambda \neq 3` (The average arrival rate is different from 3 customers per minute).

Step 2: Compute the Test Statistic
-----------------------------------

For large sample sizes, we can use the z-test for Poisson distributions.
The test statistic is given by:

.. math::
   Z = \frac{\hat{\lambda} - \lambda_0}{\sqrt{\frac{\lambda_0}{n}}}

where:

* :math:`\hat{\lambda} = \frac{200}{60} = 3.33` (sample mean arrival rate)
* :math:`\lambda_0 = 3` (claimed mean arrival rate)
* :math:`n = 60` (sample size in minutes)

Substituting the values:

.. math::
   Z = \frac{3.33 - 3}{\sqrt{\frac{3}{60}}}

.. math::
   Z = \frac{0.33}{\sqrt{0.05}} = \frac{0.33}{0.2236} = 1.48

Step 3: Determine the Critical Value
-------------------------------------

For a two-tailed test at :math:`\alpha = 0.05`, the critical value from the
standard normal table is:

.. math::
   Z_{\text{critical}} = \pm 1.96

Step 4: Make a Decision
------------------------

The computed :math:`Z = 1.48` is less than the critical value
:math:`Z_{\text{critical}} = 1.96`, meaning we are in the acceptance region.

Since :math:`|Z| < Z_{\text{critical}}`, we fail to reject :math:`H_0`.

Conclusion
----------

There is not enough statistical evidence to conclude that the average customer
arrival rate differs from the claimed 3 customers per minute.

