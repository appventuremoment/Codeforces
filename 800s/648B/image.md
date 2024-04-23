# It was in Russian

Vasya bought a table with n legs. Each leg consists of two parts that connect to each other. Each part can be of arbitrary positive length, but it is guaranteed that from all 2n parts it is possible to create n legs of the same length. When composing a leg, any two parts can be connected to each other. Initially, all the table legs are disassembled, and you are given the lengths of 2n parts in random order.

Help Vasya assemble all the table legs so that they are all the same length, dividing the given 2n parts into pairs in the correct way. Each leg must be made up of exactly two parts; it is not allowed to use only one part as a leg.

Input data
The first line contains the number n (1 ≤ n ≤ 1000) — the number of legs of the table that Vasya bought.

The second line contains a sequence of 2n positive integers a1, a2, ..., a2n (1 ≤ ai ≤ 100 000) — the lengths of the table legs in random order.

Output
Print n lines of two integers each — the lengths of the parts of the legs that need to be connected to each other. It is guaranteed that it is always possible to assemble n legs of the same length. If there are several answers, you are allowed to display any of them