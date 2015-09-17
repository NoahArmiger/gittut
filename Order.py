# File:        lab2.py
# Written by:  Noah Armiger
# Date:        9/12/2015
# Lab Section: 10
# UMBC email:  ano3@umbc.edu
# Description: This is a program made for lab 2 and demonstrates order of operations 

def main():
	#/usr/bin/scl enable python33 bash 
	print("Noah Armiger")
	print("This program was made to increase understanding of order of operations in python")
	print("press Enter to end")
	
	
	#Question 1 
	#Expected answer 24
	num1 = (7 + 1) * 3
	print("Question 1  evaluates to:",num1)
	#Actual output 24
	#Explanation: Parentheses 7 + 1 = 8 then multiplication 8 * 3 = (24)
	
	#Question 2 
	#Expected answer 2f
	num2 = (12 % 5)
	print("Question 2  evaluates to:",num2)
	#Actual output = 2
	#Explanation 12/5 = 2 r2 so 12 % 5 = the remainder of 2 
	
	#Question 3 
	#Expected answer 21
	num3 = (21 % 49)
	print("Question 3  evaluates to:",num3)
	#Actual answer 21
	#Explanation since 49 does not go into 21 as it is larger then all of 21 is the remainder 
	
	#Question 4
	#Expected answer 2
	num4 = (5 - 3) + (10 -5) * (8 % 2)
	print("Question 4  evaluates to:",num4)
	#Actual answer 2
	#Explanation parentheses 8 % 2 = 0 by order of operations (10- 5) * 0 = 0 
	#            parentheses (5 -3) = 2 and 2- 0 = 2
	
	#Question 5 
	#Expected answer 34
	num5 = 6.5 + 5 / 2 * (4 + 7)
	print("Question 5  evaluates to:",num5)
	# Actual answer 34
	#Explanation  first because of parentheses (4 + 7 ) = 11 then since 5 /2 is the first on the left out of all the division and multiplication it is 
	#             enacted first so 5/2 = 2.5 so the next multiplication/division is 2.5 * 11 or 27.5
	#             and at the end 6.5 is added makeing the total 34
	
	#Question 6 
	#Expected answer 5
	num6 = 9 / 3 + 18 - 4 * 4 
	print("Question 6  evaluates to:",num6)
	#Actual answer 5.0
	#Explination 9 / 3 = 3 amd 4 * 4 = 16 these are exicuted first as they are higher priority and 
	#            are seperated by lower priority operations so 3 + 18 = 21, 21 - 16 = (5)
	
	#Question 7 
	#Expected answer 22
	num7 = 8 % 3 + 5 * 4	
	print("Question 7  evaluates to:",num7)
	#Actual answer 22
	#Explination Both mod and multiplication are higher priority then addition so they are done 
	#            Seprate first and then added together 
	
	#Question 8
	#Expected answer aprox 79.9 
	num8 =  81.3 / 2.1 + ((51.5 % 65.2) * 2 / 2.5)
	print("Question 8  evaluates to:",num8)
	#Actual answer 79.91428
	#explintaion parentheses (51.5 % 65.2 ) returns 51.5 as 65.2 is a larger number then in the second 
	#            layer of parentheses this is multiplied by 2 51.5 * 2 = 103 and then divided by 2.5 
	#            103 / 2.5 = 41.2 this is then added to 81.3/2.1 so 38.714exc + 41.2 = 79.91428exc 
	
	#Question 9 
	#Given equation 100 - 8 * 8 + 1 /  0.5
	#Solved equation 100 - ((8 * 8)+1)/.5
	#target -30
	num9 = 100 - ((8 * 8)+1)/.5
	print("Question 9  evaluates to:",num9,"and should be -30")
	
	#Question 10
	#Given equation 84 / 10 + 11 - 4 * 4
	#Solved equaton (84 / (10 + 11) -4)* 4
	#Target 0 
	num10 = (84 / (10 + 11) -4)* 4
	print("Question 10 evaluates to:",num10,"and should be 0" )
	
	cont = input("press enter to continue: ")
	
	
	
main ()


