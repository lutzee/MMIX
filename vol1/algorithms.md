#Algorithms
###Section 1.1

###Elucids Algorithm
This is just a sample algorithm, for me to make sure I understand how the algorithms are laid out in the book. For consistency I will also format answers in the same format.
Reading this, im not imeediately familliar with the name, Elucid, but I do have a vague understanding of the algorithm.
As stated, Elucids algorithm is as forth: "Given two positive integers _m_ and _n_, find their _greatest common divisor_, that is. the largest possitive integer that evenly divides both _m_ and _n_.

E1: First, it is useful to know wheather or not dividing _m_ by _n_ produces any remainder. This will give a value ![equation](http://latex.codecogs.com/gif.latex?0%20%5Cleq%20r%3C%20n)

E2: So, what if _r_=_0_? Well, thats simple, _n_ is the answer, because you can't go and divide _n_ by a number bigger than itself.

E3: Finally, if _r_ != _0_ what do we do to find the answer? The answer is a reduce function, ![equation2](http://latex.codecogs.com/gif.latex?m%5Cleftarrow%26%20n%2C%26%20n%26%20%5Cleftarrow%26%20r), and go back to step E1.

This is where I get a little lost thinking about it, so I'm going to apply some real numbers too it. 
Thankyou random number generator, I have the numbers _m_= 416 and _n_=196.

E1: _416/196_=2 _remainder_:24

E2: Is the remainder _0_? No, go to step E3

E3: Reduce: _m_=196,_n_=24

E1: _196/24_= 8 _remainder_=4

E2: Is the remainder _0_? No, go to step E3

E3: Reduce: _m_=24,_n_=4

E1: _24/4_=6 _remainder_=0

E2: Is the remainder _0_? **Huzzar! the remainder is 0, the highest common divisor is 4! You just need to remember the answer is the value of the previous remainder, not the final quotient**

###Algorithm Excercises
Note: I will always include the difficulty rating of the excercise questions but not the questions themselves.I'm not willing to type those out, they can get rather long. If you don't know the rating system, you can find it online (google, my friend).

1. [_10_] ![equation3](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20t%5Cleftarrow%20a%20%2C%20a%5Cleftarrow%20b%20%2C%20b%5Cleftarrow%20c%20%2C%20c%5Cleftarrow%20d%20%2C%20d%5Cleftarrow%20t)

2. [_15_] Taking two random positive numbers for _m_ and _n_, probability dictates half of all random numbers selected, _m_ will be greater than _n_(assuming we ignore any cases where both numbers are the same, as the result will equal both values of _m_ and _n_ in these cases.). Likewise, half of the random numbers selected _n_ will be greater than _m_.  We now have half all possibilities obeying the rule set out. 

    Looking at the other half of all possibilities, running these through step E1 would result in a quotient of 0, and remainder of _m_. But not all is lost, moving on to step E2, taking the value of _n_ (the larger number) and moving it to _m_, _m_ becomes a large number, and then moving the remainder _r_ to _n_, where _r_ is the original value of _m_ (the smaller number), we now have _m > n_ which now agrees with the original statement. This only took one extra loop of the algorithm over the cases where _m > n_ originally.

3. [_20_] This took more thinking than I would like, and a lot of writing, but the solution came to me finally.
    I initially started looking at if from a what could actually replace ![equation4](http://latex.codecogs.com/gif.latex?m%5Cleftarrow%26%20n). I got a bit lost in just trial running through every small step of the algorithm. I decided that I probably didn't understand fully what it meant by efficiency. I read up on using the assignment operator in more efficient manors, which lead to identifying variables that are no longer being used, and repurposing them to store a different value, rather than moving the data to be in the right place for the next step. 

    For example: _m_ does not get used again after E1. We also have a new value to store, the remainder. If we use _m_ to store the remainder, we save time on an extra assignment operation (F1). Moving onto E2, we see that value _r_ does not exist, as it is now stored in _m_. So E2 is changed to check if _m_ is 0, and if so _n_ is the answer, for step F2.

    E3 is now going to cause a problem, the remainder is stored in _m_, with the larger value stored in _n_. Swapping the values here would just readd the extra assignment that we are trying to avoid. Instead we can reverse the division from E1 for F3 and divide _n_ by _m_, and assign the remainder into _n_, which is no longer needed.

    This is where we introduce a 4th step, F4, we need to test the remainder again to check if it is 0. The remainder is currently stored in _n_, so we check for _n=0_. If _n!=0_ we then return to F1.

    F1: [Find remainder] Divide _m_ by _n_ and let _m_ take the value of the remainder.
    
    F2: [Is it zero?] Check if _m=0_, if _m=0_ then _n_ is the answer and the algorithm terminates.
    
    F3: [Find the remainder again] Divide _n_ by _m_, and let _n_ take the value of the remainder.
    
    F4: [Is it zero?] Check if _n=0_, if _n=0_ then _m_ is the answer, if not return to step F1.

4. [_16_] Just a basic calculation using the algorithm. Wrote a basic python script to calculate it, includes both algorithms.
    1. 6099%2166=1767
    2. 2166%1767=399
    3. 1767%399=171
    4. 399%171=57
    5. 171%57=0
    6. HCD=57

