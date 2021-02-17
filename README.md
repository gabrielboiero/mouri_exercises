# 1. Palindrome

Problem:

> Write a simple function (less than 160 characters) that returns a Boolean indicating whether or not a string is a palindrome.

Solution in file `01_palindrome.py`

Example to use:

```
palindrome("abcdedcba") # return True

palindrome("abcabc") # return False

palindrome("12321") # return True

palindrome("") # return True -> An empty string is also a palindrome, since it "reads" the same forward and backward.
```

----
# 2. DOM Visiting algorithm

Problem:

> Create a function that, given a DOM Element on the page, will visit the element itself and all of its descendants (not just its immediate children). For each element visited, the function should pass
> that element to a provided callback function.
> The arguments to the function should be:
> • a DOM element
> • a callback function (that takes a DOM element as its argument)

Solution in file `02_dom_visiting.py`

Examples to use

```
dom = Dom(4, [])
dom_visiting(dom)
```

```
dom = Dom(4, [Dom(3,[]), Dom(5,[]), Dom(8, [Dom(1,[]), Dom(2,[])])])
dom_visiting(dom)
```

```
dom = Dom(3, [Dom(2, []), Dom(1,[])])
dom_visiting(dom)
```

----

# 3. FizzBuzz

Problem:

> Create a for loop that iterates up to 100 while outputting "fizz" at multiples of 3, "buzz" at multiples of 5 and "fizzbuzz" at multiples of 3 and 5.

Solution in file `03_fizz_buzz.py`

Invoke using `fizz_buzz()`

----

# 4. Move zeros to the end

Problem:

> Given an array of numbers, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements

Solution in file `04_zeros_at_end.py`

Example of use:

```
zeros_at_end([42, 5, 23, 0, 234, 11, 0, 0, 77, 56, 90, 0, 2, 1, 4])
# Output is: [42, 5, 23, 234, 11, 77, 56, 90, 2, 1, 4, 0, 0, 0, 0]
```

----

# 5. Sentences

Problem:

> Given two sentences, return an array that has the words that appear in one sentence and not the other and an array with the words in common.

Solution in file `05_sentences.py`

Example of use:

```
common("this one example sentence", "this is another")
# Output: ['this']
```

```
not_repeated("this one example sentence", "this is another")
# Output: ['is', 'one', 'another', 'example', 'sentence']
```

