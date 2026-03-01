name = input("Enter Student name: \n")
scored = input("Enter the score \n")
print("-" * 30)
if not scored or not name:
    print("No Input Entered! ")
else:
    student_names = [x.strip() for x in name.split(",")]
    scores = [int(y.strip()) for y in scored.split(",")]
    if len(student_names) != len(scores):
         print("Number of names and scores must match!")
         exit()
    else:
        pass_count = 0
        fail_count = 0
        student_data = {student_name:score for student_name,score in zip(student_names,scores)}
        for student, score in student_data.items():
            if score >= 90:
                grade, result, status = "A+", "Excellent performance", "Pass"
            elif score >= 80:
                grade, result, status = "A", "Excellent performance", "Pass"
            elif score >= 70:
                grade, result, status = "B", "Very Good Performance", "Pass"
            elif score >= 60:
                grade, result, status = "C", "Good performance", "Pass"
            elif score >= 50:
                grade, result, status = "D", "Satisfactory", "Pass"
            else:
                grade, result, status = "F", "Poor Performance", "Failed"
            print(f"Student: {student}")
            print(f"Score:   {score}")
            print(f"Grade:   {grade}")
            print(f"Result:  {result}")

            if status == "Pass":
                pass_count += 1
                print(f"Passing Student: {student} Score: {score}")
            else:
                fail_count += 1
                print(f"Failed Student: {student} Score: {score}")
        highest_student = max(student_data, key=student_data.get)
        lowest_student = min(student_data, key=student_data.get)

        print("-" * 30)
        print(f"✅ Highest scoring student: {highest_student} ({student_data[highest_student]})")
        print(f"✅ Lowest scoring student:  {lowest_student} ({student_data[lowest_student]})")
        print(f"✅ Count of passing students: {pass_count}")
        print(f"✅ Count of failing students: {fail_count}")
        print("-" * 30)
