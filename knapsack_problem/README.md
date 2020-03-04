# Objective

You accidentally glide with your slippers on your flying carpet and fall through quicksand into a magical cavern where there is a fabulous treasure.
Of course, you don't like doing things by hand, so you're going to automate this task.

The treasure is composed of different powdersand whose price is given to you per kilogram as well as the total quantity of each of the powders contained in the cave. The treasure also contains precious stones, each with an indivisible weight and value. You only have with you an old oil lamp (you believed what? it's not magic eh!) and you have to indicate which powders and gems you must selectinorderto maximize the value of the treasure you will bring to the surface (greedy that you are)!

Hint: if you have recognized here the ["Knapsack problem"](https://en.wikipedia.org/wiki/Knapsack_problem), you are on the right track, but the very large number of objects changes will require additional code!

## Data format

__input__

**Row 1** : 3 integers separated by spaces: **N** the number of gemstones, **M** the number of types of powders, **C** number (in gram) of stones or powder that the lamp can hold, each between 1 and 100.

**Rows 2** to **N+1** : 2 integers separated by spaces, respectively the value (in gold coins) and the weight (in grams) of each gemstone, between 1 and 1000 and 1 and **C** respectively.

Rows **N+2** to **N+M+2**: 2 integers separated by spaces, respectively the price by weight (in gold coins per gram) and the amount available (in grams) of each type of powder, between 1 and 100 and 1 and **C** respectively.

__Output__

The maximum value that the lamp can hold in precious stones and powders!

## Example
__input__

2 2 100

600 40

1000 50

20 40

15 80

__output__

1950

In this example the optimal is to take the object of value 1000, then 40 grams of powder whose value is 20 gold coins per gram, then 10 grams of powder whose value is 15 gold coins per gram. It leads to a value of `1000 + 800 + 150 = 1950`
