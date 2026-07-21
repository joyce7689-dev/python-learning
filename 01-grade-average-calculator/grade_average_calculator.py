def enter_grades():
    """
    Allows the user to enter subjects and their grades.

    Returns:
        subjects (list): List of subject names.
        grades (list): List of grades.
    """

    subjects = []
    grades = []

    while True:
        subject = input("Enter the subject name: ").strip()

        while subject == "":
            print("The subject name cannot be empty.")
            subject = input("Enter the subject name: ").strip()

        while True:
            try:
                grade = float(input(f"Enter the grade for {subject} (0-10): "))

                if 0 <= grade <= 10:
                    break
                else:
                    print("The grade must be between 0 and 10.")

            except ValueError:
                print("Please enter a valid number.")

        subjects.append(subject)
        grades.append(grade)

        continue_input = input("Do you want to add another subject? (y/n): ").lower()

        while continue_input not in ("y", "n"):
            continue_input = input("Invalid answer. Please enter 'y' or 'n': ").lower()

        if continue_input == "n":
            break

    return subjects, grades


def calculate_average(grades):
    """
    Calculates the average grade.
    """

    if len(grades) == 0:
        return 0

    return sum(grades) / len(grades)


def get_subject_status(grades, passing_grade=5.0):
    """
    Returns the indexes of passed and failed subjects.
    """

    passed = []
    failed = []

    for i in range(len(grades)):
        if grades[i] >= passing_grade:
            passed.append(i)
        else:
            failed.append(i)

    return passed, failed


def find_highest_and_lowest(grades):
    """
    Returns the indexes of the highest and lowest grades.
    """

    highest = 0
    lowest = 0

    for i in range(1, len(grades)):
        if grades[i] > grades[highest]:
            highest = i

        if grades[i] < grades[lowest]:
            lowest = i

    return highest, lowest


def main():

    print("=" * 45)
    print(" GRADE AVERAGE CALCULATOR ")
    print("=" * 45)

    subjects, grades = enter_grades()

    if len(subjects) == 0:
        print("\nNo subjects were entered.")
        print("Thank you for using the program.")
        return

    average = calculate_average(grades)

    passed, failed = get_subject_status(grades)

    highest, lowest = find_highest_and_lowest(grades)

    print("\n" + "=" * 45)
    print("FINAL SUMMARY")
    print("=" * 45)

    print("\nRegistered Subjects:")

    for i in range(len(subjects)):
        print(f"- {subjects[i]}: {grades[i]}")

    print(f"\nAverage Grade: {average:.2f}")

    print("\nPassed Subjects:")
    if passed:
        for i in passed:
            print(f"- {subjects[i]} ({grades[i]})")
    else:
        print("None.")

    print("\nFailed Subjects:")
    if failed:
        for i in failed:
            print(f"- {subjects[i]} ({grades[i]})")
    else:
        print("None.")

    print("\nHighest Grade:")
    print(f"{subjects[highest]} -> {grades[highest]}")

    print("\nLowest Grade:")
    print(f"{subjects[lowest]} -> {grades[lowest]}")

    print("\nThank you for using the Grade Average Calculator.")


if __name__ == "__main__":
    main()