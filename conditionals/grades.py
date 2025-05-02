"""
Escribe un programa que, dado un número entre 0 y 100, imprima la letra correspondiente a su calificación:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: menos de 60
"""

grade = int(input("Enter a grade between 0 and 100: "))

if grade >= 90 or grade <= 100:
    print("Amazing! You got an A!")
elif grade >= 80 and grade <= 89:
    print("Nice! You got a B!")
elif grade >= 70 and grade <= 79:
    print("Well... You got a C!")
elif grade >= 60 and grade <= 69:
    print("Mmm... Better luck next time! You got a D!")
else:
    print("Too bad! You got an F!")
