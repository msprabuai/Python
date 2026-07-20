class Invoice:
    def calculate(self, price, gst):
        gst_amount = price * gst / 100
        total = price + gst_amount
        print("GST:", gst_amount)
        print("Invoice Amount:", total)

class MultipleFunc:
    def calculate(self, salary):
        bonus = salary * 0.10
        total = salary + bonus
        print("Bonus:", bonus)
        print("Total Salary:", total)

    def deposit(self, balance, amount):
        new_balance = balance + amount
        print("Updated Balance:", new_balance)

class Salary:
    def calculate(self, salary):
        bonus = salary * 0.10
        total = salary + bonus
        print("Bonus:", bonus)
        print("Total Salary:", total)

class SubfieldsInAI:
    def Subfields(self):
        ai_fields=[
            "Machine Learning","Neural Networks","Vision","Robotics",
            "Speech Processing","Natural Language Processing"
        ]
        print("Sub-fields in AI are:")
        for field in ai_fields:
            print(field)

def marriage_eligibility(gender, age):
    if gender=="M":
        print("Eligible for Marriage" if age>=21 else "Not Eligible for Marriage")
    elif gender=="F":
        print("Eligible for Marriage" if age>=18 else "Not Eligible for Marriage")
    else:
        print("Invalid Gender")

def odd_even(number):
    return "Even Number" if number % 2 == 0 else "Odd Number"
