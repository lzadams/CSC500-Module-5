#Part 1
#Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
#The program should first ask for the number of years.
number_of_years = int(input('Enter the number of years:'))
total_inches_of_rainfall = 0
number_of_months = 0
# The outer loop will iterate once for each year.
for i in range(number_of_years):
    print(f'Year {i+1}:')
    for i in range(12): #The inner loop will iterate twelve times,once for each month
        inches_of_rainfall_for_the_month = int(input(f'Enter the inches of rainfall for the month {i+1}:')) #Each iteration of the inner loop will ask the user for the inches of
        # rainfall for that month
        total_inches_of_rainfall += inches_of_rainfall_for_the_month
number_of_months += number_of_years * 12
average_rainfall_per_month = total_inches_of_rainfall / number_of_months
print('The number of months are:', number_of_months) # display the number of months
print('The total inches of rainfall for the entire period:', total_inches_of_rainfall) # display the total inches of rainfall
print('The average rainfall per month for the entire period is:', average_rainfall_per_month) # display the average rainfall per month for the entire period.

#Part 2
#The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:
#If a customer purchases 0 books, they earn 0 points.
#If a customer purchases 2 books, they earn 5 points.
#If a customer purchases 4 books, they earn 15 points.
#If a customer purchases 6 books, they earn 30 points.
#If a customer purchases 8 or more books, they earn 60 points.
#Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
number_of_books = int(input('Enter the number of books you have purchased this month:'))
number_of_points = 0
if number_of_books == 0:
    number_of_points += 0
elif number_of_books == 2:
    number_of_points += 5
elif number_of_books == 4:
    number_of_points += 15
elif number_of_books == 6:
    number_of_points += 30
elif number_of_books >= 8:
    number_of_points += 60
else:
    print('You have entered an invalid number')
print('The number of points awarded:',number_of_points)