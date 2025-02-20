# **Understanding Probability Distributions: Derivations and Interpretations**

Probability distributions describe how random variables behave. In this document, we explore their derivations and real-world interpretations.

---

## **1. Normal Distribution (Gaussian Distribution)**

### **Derivation**
The normal distribution arises from the **Central Limit Theorem (CLT)**, which states that the sum of a large number of independent random variables tends to be normally distributed.

A random variable \( X \) follows a normal distribution if its probability density function (PDF) is:

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

where:
- \( \mu \) is the mean.
- \( \sigma \) is the standard deviation.

### **Physical Interpretation**
- Heights of people, IQ scores, and errors in measurements follow this distribution due to small, independent influences.

---

## **2. Uniform Distribution**

### **Derivation**
For a continuous uniform distribution over \( [a, b] \), the PDF must satisfy:

$$
\int_a^b f(x)dx = 1
$$

Since every value is equally likely, we get:

$$
f(x) = \frac{1}{b-a}, \quad a \leq x \leq b
$$

### **Physical Interpretation**
- Rolling a fair die, random number generation.

---

## **3. Binomial Distribution**

### **Derivation**
The probability of exactly \( k \) successes in \( n \) trials is:

$$
P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}
$$

where:
- \( \binom{n}{k} \) is the binomial coefficient.

### **Physical Interpretation**
- Coin flips, quality control testing.

---

## **4. Poisson Distribution**

### **Derivation**
Derived from the binomial distribution as \( n \to \infty \), \( p \to 0 \) while keeping \( np = \lambda \):

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

### **Physical Interpretation**
- Counting rare events, like earthquakes per year.

---

## **5. Exponential Distribution**

### **Derivation**
Derived from the Poisson process, the time until the next event occurs follows:

$$
f(t) = \lambda e^{-\lambda t}, \quad t \geq 0
$$

### **Physical Interpretation**
- Time until a lightbulb burns out, wait time at a service center.

---

## **6. Student’s t-Distribution**

### **Derivation**
For a normal population with unknown variance, the test statistic:

$$
t = \frac{\bar{X} - \mu}{S / \sqrt{n}}
$$

follows the **t-distribution** with \( n-1 \) degrees of freedom.

### **Physical Interpretation**
- Hypothesis testing for small samples.

---

## **7. Chi-Square Distribution**

### **Derivation**
If \( Z_i \) are independent standard normal variables, then:

$$
X = \sum_{i=1}^{k} Z_i^2
$$

follows a chi-square distribution with \( k \) degrees of freedom.

### **Physical Interpretation**
- Used in categorical data testing.

---

## **8. Gamma Distribution**

### **Derivation**
A generalization of the exponential distribution, where \( k \) Poisson events have occurred by time \( T \):

$$
f(x) = \frac{\lambda^k x^{k-1} e^{-\lambda x}}{\Gamma(k)}
$$

### **Physical Interpretation**
- Modeling the time until multiple failures in a system.

---

## **9. Log-Normal Distribution**

### **Derivation**
A variable \( X \) follows a log-normal distribution if:

$$
Y = \ln(X) \sim N(\mu, \sigma^2)
$$

### **Physical Interpretation**
- Stock prices, income distributions.

---

## **10. Beta Distribution**

### **Derivation**
Used for modeling probabilities:

$$
f(x) = \frac{x^{\alpha - 1} (1 - x)^{\beta - 1}}{B(\alpha, \beta)}
$$

where \( B(\alpha, \beta) \) is the beta function.

### **Physical Interpretation**
- Bayesian statistics, A/B testing.

---

## **Conclusion**
Each probability distribution arises from different principles:
- **Normal:** Central Limit Theorem.
- **Uniform:** Equal likelihood.
- **Binomial:** Independent trials.
- **Poisson & Exponential:** Rare event modeling.
- **Chi-Square & t:** Sample variance.
- **Gamma & Beta:** Generalizations of Poisson and probability modeling.

Understanding these distributions helps in choosing the right model for statistical analysis and real-world problems.

