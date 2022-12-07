#!/usr/bin/env python3.7

message = input("message ")
print("First char:", message[0])
print("Last char:", message[-1])
middle_char = int(len(message)/2)
print("Middle char:", message[middle_char])
print("Even index chars:", message[0::2])
print("Odd index chars:", message[1::2])
print("Reverse message:", message[::-1])