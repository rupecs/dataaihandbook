.. _probability_distributions_guide:

Understanding Probability Distributions: A Comprehensive Guide
==============================================================

Probability distributions describe how random variables behave and play a fundamental role in statistics, probability theory, and real-world data modeling. This document provides a detailed exploration of the most important probability distributions, their derivations, and their physical interpretations. We will also discuss how some distributions extend or generalize from others, creating a rich hierarchy of probability models.

Bernoulli Trials
=================

A Bernoulli trial is a fundamental concept in probability theory that represents a single experiment or event with only two possible outcomes: success (1) or failure (0). The probability of success is denoted by :math:`p`, while the probability of failure is :math:`1 - p`. Bernoulli trials are the building blocks of more complex probability distributions, including the binomial and geometric distributions.

Mathematical Definition
-----------------------

A random variable :math:`X` follows a Bernoulli distribution if it takes the values:

.. math::
   P(X = 1) = p, \quad P(X = 0) = 1 - p

where:

*  :math:`p` is the probability of success (:math:`0 \leq p \leq 1`),
*  :math:`1 - p` is the probability of failure.

The probability mass function (PMF) of a Bernoulli trial is given by:

.. math::
   P(X = x) = p^x (1 - p)^{1 - x}, \quad x \in \{0,1\}

Properties of the Bernoulli Distribution
---------------------------------------

*   **Mean:** :math:`E[X] = p`
*   **Variance:** :math:`\text{Var}(X) = p(1 - p)`
*   **Mode:** :math:`1` if :math:`p > 0.5`, else :math:`0`
*   **Skewness:** :math:`\frac{1 - 2p}{\sqrt{p(1 - p)}}`
*   **Kurtosis:** :math:`\frac{6p^2 - 6p + 1}{p(1 - p)}`

Relation to Other Distributions
-------------------------------

*   **Binomial Distribution:** The sum of :math:`n` independent Bernoulli trials forms a binomial distribution.
*   **Geometric Distribution:** The number of Bernoulli trials needed to get the first success follows a geometric distribution.
*   **Poisson Approximation:** For small :math:`p` and large :math:`n`, the sum of Bernoulli trials approximates a Poisson distribution.

Worked Example
--------------

**Problem:** Suppose a fair coin (:math:`p = 0.5`) is flipped once. What is the probability of getting heads?

**Solution:**

Here, :math:`X` follows a Bernoulli distribution with :math:`p = 0.5`. The probability of getting heads (success) is:

.. math::
   P(X = 1) = 0.5

Similarly, the probability of getting tails (failure) is:

.. math::
   P(X = 0) = 1 - 0.5 = 0.5

Thus, for a fair coin, the probability of getting heads or tails in a single Bernoulli trial is **50%**.

Applications of Bernoulli Trials
--------------------------------

*   **Quality Control:** Testing whether a product meets a certain standard.
*   **Medical Trials:** Determining whether a treatment is successful or not.
*   **Finance:** Modeling binary outcomes in risk assessments.
*   **Computer Science:** Randomized algorithms in decision-making processes.

This example illustrates the simplicity and utility of Bernoulli trials in modeling single-step experiments with binary outcomes.


Binomial Distribution
======================

The Binomial distribution extends the concept of Bernoulli trials to multiple independent repetitions of the same experiment. While a Bernoulli trial models a single success or failure event, a Binomial distribution models the total number of successes in :math:`n` independent Bernoulli trials, each with the same probability of success :math:`p`. This distribution is one of the most fundamental discrete probability distributions and is widely used in statistical modeling.

Mathematical Definition
-----------------------

A random variable :math:`X` follows a Binomial distribution if it represents the number of successes in :math:`n` independent Bernoulli trials, where the probability of success in each trial is :math:`p`. The probability mass function (PMF) of a Binomially distributed random variable :math:`X \sim \text{Bin}(n, p)` is given by:

.. math::
   P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \quad k = 0,1,2,\dots,n

where:

*   :math:`n` is the number of independent trials,
*   :math:`p` is the probability of success in each trial,
*   :math:`k` is the number of successes (:math:`0 \leq k \leq n`),
*   :math:`\binom{n}{k} = \frac{n!}{k!(n-k)!}` is the binomial coefficient, representing the number of ways to choose :math:`k` successes out of :math:`n` trials.

Properties of the Binomial Distribution
---------------------------------------

*   **Mean:** :math:`E[X] = np`
*   **Variance:** :math:`\text{Var}(X) = np(1 - p)`
*   **Mode:** :math:`\lfloor (n+1)p \rfloor`
*   **Skewness:** :math:`\frac{1 - 2p}{\sqrt{np(1 - p)}}`
*   **Kurtosis:** :math:`\frac{1 - 6p(1 - p)}{np(1 - p)}`

Relation to the Bernoulli Distribution
-------------------------------------

The Binomial distribution is a natural extension of the Bernoulli distribution:

*   A single Bernoulli trial is equivalent to a Binomial distribution with :math:`n = 1`.
*   The sum of :math:`n` independent Bernoulli trials, each with probability :math:`p`, follows a Binomial distribution with parameters :math:`n` and :math:`p`.
*   As :math:`n` increases, the Binomial distribution approximates a Normal distribution when :math:`np` and :math:`n(1-p)` are sufficiently large (Central Limit Theorem).

Worked Example
--------------

**Problem:** Suppose a fair coin (:math:`p = 0.5`) is flipped 10 times. What is the probability of getting exactly 6 heads?

**Solution:**

Here, :math:`X \sim \text{Bin}(10, 0.5)`. Using the Binomial PMF:

.. math::
    P(X = 6) = \binom{10}{6} (0.5)^6 (0.5)^4 = \frac{10!}{6!4!} (0.5)^{10}

.. math::
   = \frac{210}{1024} \approx 0.205

Thus, the probability of getting exactly 6 heads in 10 flips of a fair coin is approximately 20.5%.

Applications of the Binomial Distribution
----------------------------------------

*   **Quality Control:** Counting defective products in a batch of manufactured items.
*   **Medical Studies:** Modeling the number of patients who respond positively to a treatment.
*   **Marketing Research:** Estimating the number of customers who purchase a product after an advertisement.
*   **Genetics:** Predicting the probability of inheriting specific traits.

This example illustrates the versatility of the Binomial distribution in modeling repeated binary events across various fields.

Poisson Distribution
====================

The Poisson distribution is a fundamental discrete probability distribution that models the occurrence of rare events over a fixed interval of time or space. Unlike the Binomial distribution, which counts the number of successes in a fixed number of trials, the Poisson distribution is used when the number of trials is very large, but the probability of success in each trial is very small. This distribution is widely used in fields such as telecommunications, physics, biology, and insurance risk analysis.

Mathematical Definition
-----------------------

A random variable :math:`X` follows a Poisson distribution if it represents the number of occurrences of an event in a fixed interval, given that the events occur independently and at a constant average rate. The probability mass function (PMF) of a Poisson-distributed random variable :math:`X \sim \text{Poisson}(\lambda)` is given by:

.. math::
   P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0,1,2,\dots

where:

*   :math:`\lambda` is the average number of occurrences in the given interval (also known as the rate parameter),
*   :math:`k` is the number of occurrences (:math:`k \geq 0`),
*   :math:`e` is the base of the natural logarithm.

Properties of the Poisson Distribution
--------------------------------------

*   **Mean:** :math:`E[X] = \lambda`
*   **Variance:** :math:`\text{Var}(X) = \lambda`
*   **Mode:** :math:`\lfloor \lambda \rfloor` or :math:`\lfloor \lambda \rfloor - 1` (if :math:`\lambda` is an integer)
*   **Skewness:** :math:`\frac{1}{\sqrt{\lambda}}`
*   **Kurtosis:** :math:`\frac{1}{\lambda}`

Limiting Case: Binomial to Poisson Distribution
----------------------------------------------

The Poisson distribution can be derived as a limiting case of the Binomial distribution.  If a Binomial random variable :math:`X \sim \text{Bin}(n, p)` has a very large number of trials (:math:`n \to \infty`) while keeping the expected number of successes :math:`np = \lambda` constant, then the Binomial distribution converges to a Poisson distribution with rate parameter :math:`\lambda`:

.. math::
   \lim_{n \to \infty} P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}.

This approximation is useful when dealing with rare events, where the probability of success in each trial is very small (:math:`p \to 0`) and the number of trials is large (:math:`n \to \infty`).

Worked Example
--------------

**Problem:** Suppose a website receives an average of 3 error reports per hour. What is the probability of receiving exactly 5 error reports in an hour?

**Solution:**

Here, :math:`X \sim \text{Poisson}(3)`. Using the Poisson PMF:

.. math::
   P(X = 5) = \frac{3^5 e^{-3}}{5!} = \frac{243 e^{-3}}{120}.

Using :math:`e^{-3} \approx 0.0498`:

.. math::
   P(X = 5) \approx \frac{243 \times 0.0498}{120} \approx 0.1008.

Thus, the probability of receiving exactly 5 error reports in an hour is approximately 10.08%.

Applications of the Poisson Distribution
----------------------------------------

*   **Telecommunications:** Modeling the number of incoming calls to a call center.
*   **Physics:** Predicting the number of radioactive decays in a given time interval.
*   **Biology:** Estimating the number of mutations in a DNA sequence over a fixed region.
*   **Insurance and Risk Analysis:** Assessing the number of claims received by an insurance company per day.
*   **Traffic Flow:** Modeling the number of cars passing through a toll booth in an hour.

This example demonstrates how the Poisson distribution effectively models random occurrences in time or space when the events are rare and independent.

Normal Distribution
===================

The Normal distribution, also known as the Gaussian distribution, is one of the most fundamental and widely used probability distributions in statistics and probability theory. It is a continuous probability distribution that describes a symmetric, bell-shaped curve, often used to model natural phenomena such as heights, test scores, and measurement errors. The importance of the Normal distribution arises from the Central Limit Theorem (CLT), which states that the sum of a large number of independent and identically distributed (i.i.d.) random variables, regardless of their original distribution, will tend to follow a Normal distribution.

Mathematical Definition
-----------------------

A random variable :math:`X` follows a Normal distribution if it has the probability density function (PDF):

.. math::
    f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \quad x \in \mathbb{R},

where:

*   :math:`\mu` is the mean (expected value) of the distribution,
*   :math:`\sigma^2` is the variance,
*   :math:`\sigma` is the standard deviation,
*   :math:`e` is the base of the natural logarithm.

A special case of the Normal distribution is the Standard Normal distribution, which has a mean of 0 and a standard deviation of 1:

.. math::
    Z \sim \mathcal{N}(0,1) \Rightarrow f(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}.

Properties of the Normal Distribution
--------------------------------------

*   **Mean:** :math:`E[X] = \mu`
*   **Variance:** :math:`\text{Var}(X) = \sigma^2`
*   **Mode:** :math:`\mu` (the peak of the distribution)
*   **Skewness:** 0 (perfect symmetry)
*   **Kurtosis:** 3 (mesokurtic)


Limiting Cases: Convergence to the Normal Distribution
------------------------------------------------------

Several important distributions converge to the Normal distribution under appropriate limiting conditions:

*   **Central Limit Theorem (CLT):** If :math:`X_1, X_2, ..., X_n` are i.i.d. random variables with finite mean :math:`\mu` and variance :math:`\sigma^2`, then the sum (or average) of these variables follows an approximate Normal distribution as :math:`n \to \infty`:

    .. math::
        \frac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}} \approx \mathcal{N}(0,1).

    This result is fundamental in probability and justifies the Normal approximation in many practical scenarios.

*   **Binomial to Normal Approximation:** The Binomial distribution :math:`X \sim \text{Bin}(n, p)` approximates a Normal distribution as :math:`n` increases, provided :math:`np` and :math:`n(1-p)` are sufficiently large:

    .. math::
        X \approx \mathcal{N}(np, np(1-p)).

    This is useful in statistical applications, particularly when computing probabilities for large sample sizes.

*   **Poisson to Normal Approximation:** A Poisson-distributed variable :math:`X \sim \text{Poisson}(\lambda)` approaches a Normal distribution when :math:`\lambda` is large:

    .. math::
        X \approx \mathcal{N}(\lambda, \lambda).

    This is particularly beneficial in modeling rare events over large sample spaces.

*   **Gamma to Normal Approximation:** A Gamma-distributed variable :math:`X \sim \text{Gamma}(k, \theta)` with a large shape parameter :math:`k` behaves approximately like a Normal distribution:

    .. math::
        X \approx \mathcal{N}(k\theta, k\theta^2).

    The Gamma distribution is often used in Bayesian statistics and reliability analysis.

*  **Chi-Square to Normal Approximation:** If  :math:`X \sim  \chi^2(k)` with large degrees of freedom k, then:

    .. math::

        X \approx \mathcal{N}(k,2k)

        The Chi-Square distributions appears frequently in hypothesis testing



Applications of the Normal Distribution
---------------------------------------

*   **Natural Phenomena:** Modeling heights, IQ scores, and measurement errors.
*   **Finance:** Stock market returns and risk analysis.
*   **Engineering:** Signal processing and quality control.
*   **Medical Studies:** Biological measurements such as blood pressure and cholesterol levels.
*   **Social Sciences:** Standardized test scores and psychological research.

The Normal distribution is a cornerstone of statistical theory and is essential in hypothesis testing, regression analysis, and many other scientific applications.

Student's t-Distribution
=========================

The Student's t-distribution is a continuous probability distribution that arises in situations where the sample size is small, and the population standard deviation is unknown. It is widely used in hypothesis testing, particularly in the context of estimating the mean of a normally distributed population when the sample size is limited. The distribution was first introduced by William Sealy Gosset under the pseudonym "Student" and is commonly used in t-tests for statistical inference.

Mathematical Definition
-----------------------

A random variable :math:`T` follows a Student's t-distribution with :math:`\nu` degrees of freedom if its probability density function (PDF) is given by:

.. math::
    f(t) = \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi} \Gamma\left(\frac{\nu}{2}\right)} \left(1 + \frac{t^2}{\nu}\right)^{-\frac{\nu+1}{2}}, \quad t \in \mathbb{R},

where:

*   :math:`\nu` is the degrees of freedom,
*   :math:`\Gamma(\cdot)` is the Gamma function,
*   The distribution is symmetric about zero, similar to the Normal distribution but with heavier tails.

As the degrees of freedom increase (:math:`\nu \to \infty`), the Student's t-distribution approaches the standard Normal distribution.

Properties of the Student's t-Distribution
------------------------------------------

*   **Mean:** :math:`E[T] = 0` for :math:`\nu > 1`
*   **Variance:** :math:`\text{Var}(T) = \frac{\nu}{\nu - 2}` for :math:`\nu > 2`
*   **Skewness:** 0 (symmetric distribution)
*   **Kurtosis:** Higher than 3 (leptokurtic), meaning it has heavier tails than the Normal distribution

Comparison with the Normal Distribution
---------------------------------------

The Student's t-distribution resembles the Normal distribution but with heavier tails. This means that it assigns a higher probability to extreme values, making it more robust for small sample sizes. The heavier tails account for the additional uncertainty in estimating the population standard deviation from a small sample.

Applications of the Student's t-Distribution
--------------------------------------------

*   **Hypothesis Testing:** Used in t-tests for comparing sample means.
*   **Confidence Intervals:** Helps construct confidence intervals for the mean when the standard deviation is unknown.
*   **Regression Analysis:** Used in linear regression to determine the significance of coefficients when sample sizes are small.
*   **Small Sample Inference:** Particularly useful in experiments or studies with limited data.

The Student's t-distribution is essential in inferential statistics, providing a reliable method for making statistical conclusions when data availability is constrained.

Chi-Square Distribution
=======================

The chi-square (:math:`\chi^2`) distribution is a continuous probability distribution that arises in statistical inference, particularly in hypothesis testing and variance estimation. It is widely used in tests of independence, goodness-of-fit tests, and confidence interval estimation for variance.  The chi-square distribution is derived from the sum of the squares of independent standard normal random variables and plays a crucial role in frequentist statistical analysis.

Mathematical Definition
-----------------------

A random variable :math:`X` follows a chi-square distribution with :math:`k` degrees of freedom if its probability density function (PDF) is given by:

.. math::
   f(x) = \frac{x^{(k/2)-1} e^{-x/2}}{2^{k/2} \Gamma(k/2)}, \quad x > 0,

where:

*   :math:`k` is the degrees of freedom,
*   :math:`\Gamma(\cdot)` is the Gamma function,
*   The distribution is defined only for non-negative values (:math:`x > 0`).

The chi-square distribution is positively skewed, especially for small degrees of freedom, and becomes more symmetric as :math:`k` increases.

Properties of the Chi-Square Distribution
-----------------------------------------

*   **Mean:** :math:`E[X] = k`
*   **Variance:** :math:`\text{Var}(X) = 2k`
*   **Skewness:** :math:`\frac{\sqrt{8}}{\sqrt{k}}` (decreases as :math:`k` increases)
*   **Kurtosis:** :math:`3 + \frac{12}{k}` (approaches 3 as :math:`k` increases)

As the degrees of freedom increase (:math:`k \to \infty`), the chi-square distribution approaches a normal distribution with mean :math:`k` and variance :math:`2k`, according to the central limit theorem.

Comparison with the Normal Distribution
---------------------------------------

Unlike the normal distribution, which is symmetric about its mean, the chi-square distribution is asymmetric and skewed to the right. The skewness decreases as the degrees of freedom increase, making the distribution more normal-like for large :math:`k`. Additionally, while the normal distribution is defined over the entire real line, the chi-square distribution is only defined for non-negative values.

Applications of the Chi-Square Distribution
-------------------------------------------

*   **Goodness-of-Fit Tests:** Used to determine how well an observed distribution fits an expected distribution.
*   **Tests of Independence:** Commonly used in contingency table analysis (e.g., chi-square test for independence in categorical data).
*   **Confidence Intervals for Variance:** Helps construct confidence intervals for the variance of a normal population.
*   **Analysis of Variance (ANOVA):** Plays a role in deriving distributions of test statistics in ANOVA.

The chi-square distribution is a fundamental tool in statistical inference, particularly for analyzing categorical data and variance-related hypothesis testing.


F Distribution
==============

The F distribution, also known as Fisher's F distribution, arises frequently in the context of statistical hypothesis testing, particularly in the analysis of variance (ANOVA), regression analysis, and comparing variances of two populations. It is a continuous probability distribution that represents the ratio of two independent chi-square distributed random variables, each divided by their respective degrees of freedom. The F distribution is commonly used in assessing whether two population variances are equal and in determining the significance of regression models.

Mathematical Definition
-----------------------

A random variable :math:`F` follows an F distribution with degrees of freedom :math:`d_1` and :math:`d_2`, denoted as :math:`F \sim F(d_1, d_2)`, if it is given by:

.. math::
   F = \frac{(X_1 / d_1)}{(X_2 / d_2)}

where:

*  :math:`X_1 \sim \chi^2(d_1)` is a chi-square distributed random variable with :math:`d_1` degrees of freedom,
*  :math:`X_2 \sim \chi^2(d_2)` is a chi-square distributed random variable with :math:`d_2` degrees of freedom,
*  :math:`d_1` and :math:`d_2` are the degrees of freedom associated with :math:`X_1` and :math:`X_2`, respectively.

The probability density function (PDF) of the F distribution is given by:

..  math::

    f(F) = \frac{\Gamma(\frac{d_1 + d_2}{2})}{\Gamma(\frac{d_1}{2}) \Gamma(\frac{d_2}{2})} (\frac{d_1}{d_2})^{\frac{d_1}{2}}  \frac{F^{\frac{d_1}{2}-1}}{(1+ \frac{d_1}{d_2}F)^{\frac{d_1+ d_2}{2}}}, \quad F>0.


Properties of the F Distribution
---------------------------------

*   **Mean:** :math:`E[F] = \frac{d_2}{d_2 - 2}` for :math:`d_2 > 2`.
*   **Variance:** :math:`\text{Var}(F) = \frac{2 d_2^2 (d_1 + d_2 - 2)}{d_1 (d_2 - 2)^2 (d_2 - 4)}` for :math:`d_2 > 4`.
*   **Mode:** :math:`\frac{(d_1 - 2) d_2}{d_1 (d_2 + 2)}` for :math:`d_1 > 2`.
*   **Shape:** The distribution is right-skewed and depends on the degrees of freedom. As :math:`d_1` and :math:`d_2` increase, the distribution approaches a normal shape.
*   **Relation to Other Distributions:** If :math:`X \sim F(d_1, d_2)`, then :math:`1/X \sim F(d_2, d_1)`.

Relation to the Chi-Square Distribution
----------------------------------------

The F distribution is fundamentally derived from the chi-square distribution:

*   If :math:`X_1 \sim \chi^2(d_1)` and :math:`X_2 \sim \chi^2(d_2)`, then :math:`F = \frac{(X_1 / d_1)}{(X_2 / d_2)}` follows an F distribution.
*   The F distribution is used to test hypotheses regarding the equality of variances between two populations.

Worked Example
--------------

**Problem:** Suppose we have two independent samples with variances :math:`s_1^2 = 25` and :math:`s_2^2 = 16` from populations with sample sizes :math:`n_1 = 10` and :math:`n_2 = 15`. We want to test whether the variances of the two populations are equal at a 5% significance level.

**Solution:**

The test statistic for comparing two variances is:

.. math::
   F = \frac{s_1^2}{s_2^2} = \frac{25}{16} = 1.5625.

The degrees of freedom are :math:`d_1 = n_1 - 1 = 9` and :math:`d_2 = n_2 - 1 = 14`. From the F-table, we compare :math:`F = 1.5625` with the critical value :math:`F_{0.05,9,14}`. If :math:`F` exceeds the critical value, we reject the null hypothesis that the variances are equal.

Applications of the F Distribution
----------------------------------

*   **Analysis of Variance (ANOVA):** Used to determine whether there are significant differences between group means.
*   **Regression Analysis:** Testing the overall significance of a regression model.
*   **Comparing Variances:** Used in statistical tests like Levene's test and Bartlett's test.
*   **Experimental Design:** Evaluating the significance of factors in designed experiments.

This example highlights the practical importance of the F distribution in hypothesis testing and statistical modeling.

Exponential Distribution
========================

The Exponential distribution is a fundamental continuous probability distribution commonly used to model the time until an event occurs. It is widely applied in survival analysis, reliability engineering, and queuing theory. The Exponential distribution is often used to represent the waiting time between events in a Poisson process, where events occur independently at a constant average rate.

Mathematical Definition
-----------------------

A random variable :math:`X` follows an Exponential distribution if it models the time until the first occurrence of an event in a Poisson process with rate :math:`\lambda`. The probability density function (PDF) of an Exponentially distributed random variable :math:`X \sim \text{Exp}(\lambda)` is given by:

.. math::
    f(x) = \lambda e^{-\lambda x}, \quad x \geq 0

where:

*  :math:`\lambda > 0` is the rate parameter, representing the average number of events per unit time,
*  :math:`x \geq 0` is the time until the event occurs.

The cumulative distribution function (CDF) is given by:

.. math::
    F(x) = P(X \leq x) = 1 - e^{-\lambda x}, \quad x \geq 0

Properties of the Exponential Distribution
------------------------------------------

*   **Mean:** :math:`E[X] = \frac{1}{\lambda}`
*   **Variance:** :math:`\text{Var}(X) = \frac{1}{\lambda^2}`
*   **Memoryless Property:** :math:`P(X > s + t \mid X > s) = P(X > t)` for all :math:`s, t \geq 0`
*   **Mode:** :math:`0`
*   **Skewness:** :math:`2`
*   **Kurtosis:** :math:`6`

Relation to the Poisson Distribution
-----------------------------------

The Exponential distribution is closely related to the Poisson distribution:

*   The time between successive events in a Poisson process follows an Exponential distribution.
*   If events occur at a rate of  :math:`\lambda` per unit time, then the number of events occurring within time :math:`t` follows a Poisson distribution with mean :math:`\lambda t`.
*   The sum of :math:`n` independent Exponential(:math:`\lambda`) random variables follows a Gamma distribution with shape parameter :math:`n` and scale parameter :math:`1/\lambda`.

Worked Example
--------------

**Problem:** Suppose a system component fails according to an Exponential distribution with a failure rate of :math:`\lambda = 0.2` failures per hour. What is the probability that the component lasts at least 5 hours before failing?

**Solution:**

We are given that :math:`X \sim \text{Exp}(0.2)`. The probability that the component lasts at least 5 hours before failing is:

.. math::
    P(X \geq 5) = 1 - P(X \leq 5) = 1 - F(5)

Using the CDF:

.. math::
   P(X \geq 5) = e^{-0.2 \times 5} = e^{-1} \approx 0.3679

Thus, the probability that the component lasts at least 5 hours before failing is approximately 36.79%.

Applications of the Exponential Distribution
-------------------------------------------

*   **Reliability Engineering:** Modeling the lifespan of electronic components and mechanical systems.
*   **Survival Analysis:** Estimating time until failure or death in biological and medical studies.
*   **Queuing Theory:** Analyzing the time between arrivals in a queuing system.
*   **Network Traffic Modeling:** Measuring the time between data packet arrivals in network communications.
*   **Radioactive Decay:** Modeling the time between decay events of radioactive atoms.

This example illustrates the significance of the Exponential distribution in modeling continuous random events and its widespread applications in various fields.
