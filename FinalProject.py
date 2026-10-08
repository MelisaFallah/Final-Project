

import random

def game():

    print ("  🎲بازی جفت تاس  ")

    Player_name = input("Enter ur name: ")

    score = 0
    roll_count = 0
    double_count = 0

    print (" welcome dear ", Player_name )
    print (" lets see how lucky you are today🫩 ")

    while True:

        input(" برای انداختن تاس Enter بزن ")

        t1 = random.randint(1,6)
        t2 = random.randint(1,6)

        roll_count += 1

        print("تاس اول", t1 )
        print("تاس دوم", t2 )

        match (t1 , t2):

            case (1,1):
                print("جفت یککک1️⃣")
                score += 10
                double_count += 1

            case (2,2):
                print("جفت دووو2️⃣")
                score += 20
                double_count += 1

            case (3,3):
                print("جفت سههه3️⃣")
                score += 30
                double_count += 1
            case (4,4):
                print("جفت چهاررر4️⃣")
                score += 40
                double_count += 1

            case (5,5):
                print("جفت پنججج5️⃣")
                score += 50
                double_count += 1

            case (6,6):
                print("جفت شیشششششش6️⃣","امتیاز ویژه گرفتیی🙂‍↔️") 
                score += 100
                double_count += 1

            case _:
                print("اینبار جفت نشد🫩")

        print("امتیاز فعلی:",score)

        choice = input("بازم بازی میکنی? (y/n)")
        if choice == "n":
         break

    print ("پایان بازی")

    print("بازیکن:",Player_name)
    print("تعداد پرتاب ها:",roll_count)
    print("تعداد جفت ها:",double_count)
    print("امتیاز نهایی:",score)

    if score >= 100:
        print("Wizard🤯🎰")
    elif score >= 50:
        print("good job🫢")
    else:
        print("try next time💤")

game()