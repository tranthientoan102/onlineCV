<head>
    <style>
        html body h1,h2,html body h3{
            color: #368BC1;
            font-family: Typori;
            /* background-color:Tomato; */
        }
        html body h5 ,html body h6 {
            color: #56A5EC;
            font-weight: normal;
        }
        /* p{
            font-family: Typori;
        } */
    </style>
</head>
<h1 style="text-align: center">
    Probability and Statistics 2021 <br>
    Assignment 5<br>

</h1>
<h3 style="text-align: center">
    Student name: Thien Toan Tran <br>
    Student ID: A1808080<br>
</h3>

### Exercise 1

Lightening strikes occur as a Poisson process with rate $\lambda$ per hour.
Let $X$, $Y$ and $Z$ be the number of strikes between the time 9-11, 11-3, 3-7pm respectively.

##### Join pmf of $X$,$Y$,$Z$
$$\begin{align*}
   X &\sim exp(2\lambda) \Rightarrow P[X=x] = \frac{(2\lambda)^x}{x!}e^{-2\lambda}\\
   Y &\sim exp(4\lambda) \Rightarrow P[Y=y] = \frac{(4\lambda)^y}{y!}e^{-4\lambda}\\
   Z &\sim exp(4\lambda) \Rightarrow P[Z=z] = \frac{(4\lambda)^z}{z!}e^{-4\lambda}
\end{align*}
$$
Since X,Y,Z are independent
$$\begin{align*}
P[X=x,Y=y,Z=z] &= P[X=x]*P[Y=y]*P[Z=z]\\
&= \frac{(2\lambda)^x}{x!}e^{-2\lambda}\frac{(4\lambda)^y}{y!}e^{-4\lambda}\frac{(4\lambda)^z}{z!}e^{-4\lambda}\\
&= e^{-10\lambda}\frac{(2\lambda)^x (4\lambda)^y (4\lambda)^z}{x!y!z!}
\end{align*}
$$



##### Conditional joint pmf of $X$,$Y$,$Z$ given that $X+Y+Z=20$
Previously we have prove that if $X \sim exp(2\lambda)$ and $Y \sim exp(4\lambda)$ and $Z \sim exp(4\lambda)$, than $X+Y+Z \sim exp(10\lambda)$
$$\begin{align*}
P[X=x|X+Y+Z=20] &= \frac{P[X=x,X+Y+Z=20]}{P[X+Y+Z=20]}\\
&= \frac{P[X=x]*P[Y+Z=20-x]}{P[X+Y+Z=20]}\\
&= \frac{\frac{(2\lambda)^x}{x!}e^{-2\lambda}
            * \frac{(8\lambda)^{20-x}}{(20-x)!}e^{-8\lambda}}
        { \frac{(10\lambda)^{20}}{20!}e^{-10\lambda}}\\
&= \frac{20!}{(10\lambda)^{20}} \frac{2^x\lambda^x8^{20-x}\lambda^{20-x}}{x!(20-x)!}\\
&= \frac{20!\lambda^{20}}{(10\lambda)^{20}} \frac{2^x 8^{20-x}}{x!(20-x)!}\\
&=\frac{20!}{x!(20-x)!}\left({\frac{2}{10}}\right)^x\left({\frac{8}{10}}\right)^{20-x}\\
&=C^{20}_x\left({\frac{2}{10}}\right)^x\left({\frac{8}{10}}\right)^{20-x}
\end{align*}
$$
Based on its conditional joint pmf, $X=x|X+Y+Z=20$ follows binominal distribution with $n=20$, $p=0.2$
Similarly, we have following results:
      - $Y=y|X+Y+Z=20$ follows binominal distribution with $n=20$, $p=0.4$
      - $Z=z|X+Y+Z=20$ follows binominal distribution with $n=20$, $p=0.4$

### Exercise 2

An eight-sided die is rolled $n$ times. Let $X_1$ be the number of 1s that are observed, $X_4$ be the number of 4s.
We also have $X_i \rightarrow$ numbers of $i$, where $1\leq i \leq 8$

###### Find $cov(X_1,X_4)$

$X$ has following properties:
      - $n$ identical trials
      - there're 8 outcomes for each trials
      - probability for each outcome is the same $p_i =\frac{1}{8} $
      - trials are independent  
$\Rightarrow X$ follows multinomial distribution with $p =\frac{1}{8} $
$$cov(X_1,X_4) = -np_1p_4 = \frac{-n}{64}$$

###### Find $corr(X_1,X_4)$
$$\begin{align*}
var(X_1)=var(X_4) &= np(1-p) = \frac{7n}{64} \\
corr(X_1,X_4)& = \frac{cov(X_1,X_4)}{sd(X_1)sd(X_4)}\\
&= \frac{\frac{-n}{64}}{\sqrt{var(X_1)var(X_4)}}\\
&= \frac{-n}{64\frac{7n}{64}} \\
&= -\frac{1}{7}
\end{align*}
$$

### Exercise 3

Bookshelf have $N$ books, including:
      - 1 book with red cover and has selecting probability of $p$
      - $N-1$ books with plain covers and has selecting probability of $\frac{1-p}{N-1}$
When selected, a book and its neighbour to the left swap position. If the leftmost is selected, it is returned there
$X_n$ denotes the position of the red books after $n$ unit of time.
###### Show that ${X_n}$ is a Markov chain with non-zero transition probabilites
$X$ process can be presented as a finite Markov chain with finite state space $S=\{1,2,3,...,N\}$:
![](32.png)
At every moment of n, 1 of following case will happen:

1. $X_n$ = $i$, $X_{n+1}$ = $i-1$, where $2 < i < N$
This case happen only when:
    - red book is not the leftmost
    - a red book is seletected
$$p_{i,i-1} = p$$
1. $X_n$ = $i$, $X_{n+1}$ = $i$, where $2 < i < N-1$
    This case happen when:
    - red book is not the leftmost
    - neither a red book nor its right neighbor is selected
      - probability of selecting a red book nor its right neighbor is $p + \frac{1-p}{N-1}$
    $$p_{i,i} = 1- p - \frac{1-p}{N-1}
    $$
2. $X_n$ = 1, $X_{n+1}$ = 1
This case happen when:
    - red book is the leftmost
    - selected book is any but the red book's right neighbor
      - probability of selecting a red book nor its right neighbor is $ \frac{1-p}{N-1}$
    $$p_{1,1} = 1-  \frac{1-p}{N-1}
    $$
1. $X_n$ = $i$, $X_{n+1}$ = $i+1$, where $1 < i < N-1$
    This case happen when neither a red book's right neighbor is selected
    $$p_{i,i+1} = \frac{1-p}{N-1}
    $$
2. $X_n$ = $N$, $X_{n+1}$ = $N$
This case happen when:
    - red book is the rightmost
    - selected book is any but the red book
    $$p_{N,N} = 1- p
    $$
###### Let ${\pi_i}$ is limiting probability of the system being in start $i$
![](32.png)

$$\begin{align*}
\pi_{i} &= \sum P_{ij}\pi_j \\ 
\pi_{1} &= P_{2,1}\pi_2 + P_{1,1}\pi_{1} \\
&= p\pi_2  +  \left(1-  \frac{1-p}{N-1}\right)\pi_1                \\
\pi_{2} &= P_{1,2}\pi_1 + P_{2,2}\pi_{2} + P_{3,2}\pi_{3} \\
&= \frac{1-p}{N-1}\pi_1  +  \left(1- p - \frac{1-p}{N-1}\right)\pi_2 + p\pi_3                \\
...
\end{align*}
$$
**Caclulate $\pi_2$ based on $\pi_1$**
$$\begin{align*}
\pi_{1} &= p\pi_2  +  \left(1-  \frac{1-p}{N-1}\right)\pi_1                \\
\Leftrightarrow  p\pi_2 &= \pi_1 - \left(1-  \frac{1-p}{N-1}\right)\pi_1 \\
\Leftrightarrow  p\pi_2 &= \frac{1-p}{N-1}\pi_1 \\
\Leftrightarrow  \pi_2 &= \frac{1-p}{p(N-1)}\pi_1
\end{align*}
$$
We also have $$\pi_1 = \frac{p(N-1)}{1-p}\pi_2$$
**Caclulate $\pi_3$ based on $\pi_2$**

$$\begin{align*}
\pi_{2} &= \frac{1-p}{N-1}\pi_1  +  \left(1- p - \frac{1-p}{N-1}\right)\pi_2 + p\pi_3\\
&=\frac{1-p}{N-1}\frac{p(N-1)}{1-p}\pi_2+  \left(1- p - \frac{1-p}{N-1}\right)\pi_2 + p\pi_3\\
&=p\pi_2+  \left(1- p - \frac{1-p}{N-1}\right)\pi_2 + p\pi_3\\
&=\left(1- \frac{1-p}{N-1}\right)\pi_2 + p\pi_3\\
\Rightarrow p\pi_3 &=\frac{1-p}{N-1}\pi_2 \\
\Leftrightarrow \pi_3 &=\frac{1-p}{p(N-1)}\pi_2 \\
\end{align*}
$$
By extending $\pi_2$, we also have $$\pi_3 =\left(\frac{1-p}{p(N-1)}\right)^2\pi_1$$
###### Find general solution for $\pi_i$ for $1 \leq i \leq N$
Based on previous findings, we have:
$$\begin{align*}
\pi_i &=\left(\frac{1-p}{p(N-1)}\right)^{i-1}\pi_1, 2 \leq i \leq N
\end{align*}
$$
As a finite Markov chain,
$$\begin{align*}
&\sum_{i=1}^{N}\pi_i = 1\\
\Leftrightarrow &\pi_1\sum_{i=1}^N\left(\frac{1-p}{p(N-1)}\right)^{i-1}= 1\\
\Leftrightarrow &\pi_1\frac{1-\left(\frac{1-p}{p(N-1)}\right)^N}{1-\left(\frac{1-p}{p(N-1)}\right) } = 1 \\
\Leftrightarrow &\pi_1 = \frac{1-\frac{1-p}{p(N-1)}}{1-\left(\frac{1-p}{p(N-1)}\right)^N}\\
\Rightarrow &\pi_i =\left(\frac{1-p}{p(N-1)}\right)^{i-1}\frac{1-\frac{1-p}{p(N-1)}}{1-\left(\frac{1-p}{p(N-1)}\right)^N}
\end{align*}
$$


