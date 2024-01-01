#NO DECIMALS, ONLY WHOLE NUMBERS

formative_average = int(input('Enter the Amount of Your Formatives: '))
amount_of_formatives = int(input('Enter the Number of Formative Grades: '))
summative_average = int(input('Enter the Amount of Your Summatives: '))
amount_of_summatives = int(input('Enter the Number of Summative Grades: '))

print(formative_average / amount_of_formatives * 0.3 + summative_average / amount_of_summatives * 0.7)