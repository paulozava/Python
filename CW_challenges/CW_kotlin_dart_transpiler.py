# https://www.codewars.com/kata/597ccf7613d879c4cb00000f/train/python

def transpile (expression):
    return ""

# If you successfully parsed the input, return Right output, otherwise give me Left "Hugh?".

# names,
#       like abc, ABC, run, a1,
#       beginning with _/letters and followed by _/letters/numbers
# numbers,
#       like 123, 2333, 66666
# lambda expressions,
#       like { a -> a }, { a, b -> a b }(source), (a){a;}, (a,b){a;b;}(target)
        # Lambda expressions consist of two parts:
        #
        # parameters, they're just names/numbers
        # statements, a list of names/numbers, seperated by:
#                whitespaces in source language
#                ; in target language.
        # Invoking a function is to pass some arguments to something
#         callable(names and lambdas), like plus(1, 2), or repeat(10, { xxx }).
# We have empty characters blank space and \n.

# There's a syntax sugar in Kotlin: if the last argument is a lambda, it can be out of the brackets. Like, repeat(10, { xxx }) can be written in repeat(10) { xxx }. And if that lambda is the only argument, you can even ignore the brackets. Like: run({ xxx }) is equaled to run { xxx }.

# fun() => fun()
# fun(a) => fun(a)
# fun(a, b) => fun(a,b)
# {}() => (){}()
# fun {} => fun((){})
# fun(a, {}) => fun(a,(){})
# fun(a) {} => fun(a,(){})
# fun {a -> a} => fun((a){a;})
# {a -> a}(1) => (a){a;}(1)
# fun { a, b -> a b } => fun((a,b){a;b;})
# {a, b -> a b} (1, 2) => (a,b){a;b;}(1,2)
# f { a } => f((){a;})
# f { a -> } => f((a){})