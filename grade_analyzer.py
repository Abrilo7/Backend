students= []
def get_grade_data(score):
    if score >= 90: grade, perf = "A+", "Excellent!"
    elif score >= 80: grade, perf = "A", "Excellent!"
    elif score >= 70: grade, perf = "B", "Very Good!"
    elif score >= 60: grade, perf = "C", "Good!"
    elif score >= 50: grade, perf = "D", "Satisfactory"
    else: grade, perf = "F", "Poor"
    status = "Pass" if score >= 50 else "Failed"
    return grade, perf, status


def register_student():
    name = input("Enter The Name: ").upper().strip()
    if any(s["name"] == name for s in students):
        print(f"{name} is already registered.")
        return
    try:
        score_input = input("Enter The Score: ")
        score = float(score_input)
        if not 0 <= score <= 100:
            print("❌ Invalid Score! Must be between 0 and 100.")
            return


        grade, perf, status = get_grade_data(score)
        students.append({
            "name": name, "score": score, 
            "perf": perf, "grade": grade, "status": status
        })
        print(f"{name} added successfully! ")
    except ValueError:
        print("❌ Error: Score must be a number.")

def view_students():
    if not students:
        print("No students registered. ")
        return
    print("\n--- Registered Students ---")
    for s in students:
        print(f"Name: {s['name']} | Score: {s['score']}")


def show_statistics():
    if not students:
        print(" No data available.")
        return
    

    total_score = sum(s["score"] for s in students)
    avg = total_score / len(students)
    pass_count = sum(1 for s in students if s['score'] >= 50)
    highest = max(students, key=lambda x: x['score'])
    lowest = min(students, key=lambda x: x['score'])
    print(f"Average Score:   {avg:.2f}")
    print(f"Highest Scorer:  {highest['name']} ({highest['score']})")
    print(f"Lowest Scorer:   {lowest['name']} ({lowest['score']})")
    print(f"✅ Pass/Fail:    {pass_count} Pass | {len(students)-pass_count} Fail")
    print("="*35)


def search_student():
    query = input("Enter name to search: ").upper().strip()
    found = [s for s in students if s['name'] == query]
    
    if found:
        s = found[0]
        print(f"""
🔍 Match Found:
----------------------
Name:    {s['name']}
Score:   {s['score']}
Grade:   {s['grade']}
Status:  {s['status']}
Comment: {s['perf']}
----------------------""")
    else:
        print("❌ Student not found.")

def main_menu():
    while True:
        print("""
--- MAIN MENU ---
1. Register Student
2. View Students
3. View Statistics
4. Search Student
5. Exit
""")
        choice = input(">> ")
        if choice == '1': register_student()
        elif choice == '2': view_students()
        elif choice == '3': show_statistics()
        elif choice == '4': search_student()
        elif choice == '5': 
            print("Goodbye!")
            break
        else:
            print("Invalid input.")
if __name__ == "__main__":
    main_menu()