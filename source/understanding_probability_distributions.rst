Understanding Probability Distributions
=======================================

Introduction
------------

Probability distributions describe how random variables behave and play a fundamental role in statistics, probability theory, and real-world data modeling. This document provides a detailed exploration of the most important probability distributions, their derivations, and their physical interpretations. We will also discuss how some distributions extend or generalize from others, creating a rich hierarchy of probability models.

Bernoulli Trials
----------------

Introduction
^^^^^^^^^^^^

A Bernoulli trial is a fundamental concept in probability theory that represents a single experiment or event with only two possible outcomes: success (1) or failure (0). The probability of success is denoted by :math:`p`, while the probability of failure is :math:`1 - p`. Bernoulli trials are the building blocks of more complex probability distributions, including the binomial and geometric distributions.

Mathematical Definition
^^^^^^^^^^^^^^^^^^^^^^^

A random variable :math:`X` follows a Bernoulli distribution if it takes the values:

.. math::

   P(X = 1) = p, \quad P(X = 0) = 1 - p

where:

- :math:`p` is the probability of success (:math:`0 \leq p \leq 1`),
- :math:`1 - p` is the probability of failure.

The probability mass function (PMF) of a Bernoulli trial is given by:

.. math::

   P(X = x) = p^x (1 - p)^{1 - x}, \quad x \in \{0,1\}

Properties of the Bernoulli Distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Mean:** :math:`E[X] = p`
- **Variance:** :math:`\text{Var}(X) = p(1 - p)`
- **Mode:** ``1`` if :math:`p > 0.5`, else ``0``
- **Skewness:** :math:`\frac{1 - 2p}{\sqrt{p(1 - p)}}`
- **Kurtosis:** :math:`\frac{6p^2 - 6p + 1}{p(1 - p)}`

Relation to Other Distributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Binomial Distribution:** The sum of :math:`n` independent Bernoulli trials forms a binomial distribution.
- **Geometric Distribution:** The number of Bernoulli trials needed to get the first success follows a geometric distribution.
- **Poisson Approximation:** For small :math:`p` and large :math:`n`, the sum of Bernoulli trials approximates a Poisson distribution.

Worked Example
^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Quality Control:** Testing whether a product meets a certain standard.
- **Medical Trials:** Determining whether a treatment is successful or not.
- **Finance:** Modeling binary outcomes in risk assessments.
- **Computer Science:** Randomized algorithms in decision-making processes.

This example illustrates the simplicity and utility of Bernoulli trials in modeling single-step experiments with binary outcomes.