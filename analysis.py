# ==============================
# Student Data Analysis Project
# ==============================

# Function to read data from file
def load_data(filename):

    students = []
    filename = "student.txt"

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            student = {
                "id": int(parts[0]),
                "name": parts[1],
                "subject": parts[2],
                "marks": int(parts[3])
            }

            students.append(student)

    return students


# Function to calculate average marks per subject
def average_marks(data):

    subject_total = {}
    subject_count = {}

    for record in data:

        subject = record["subject"]
        marks = record["marks"]

        subject_total[subject] = subject_total.get(subject, 0) + marks
        subject_count[subject] = subject_count.get(subject, 0) + 1

    averages = {}

    for subject in subject_total:
        averages[subject] = subject_total[subject] / subject_count[subject]

    return averages


# Function to find top student per subject
def top_students(data):

    top = {}

    for record in data:

        subject = record["subject"]

        if subject not in top or record["marks"] > top[subject]["marks"]:
            top[subject] = record

    return top


# Function to find failed students
def failed_students(data, pass_mark=60):

    failed = []

    for record in data:
        if record["marks"] < pass_mark:
            failed.append(record)

    return failed


# Function to find highest marks per subject
def highest_per_subject(data):

    highest = {}

    for record in data:

        subject = record["subject"]

        if subject not in highest or record["marks"] > highest[subject]["marks"]:
            highest[subject] = record

    return highest


# Function to generate report
def generate_report(data, filename="report.txt"):

    avg = average_marks(data)
    top = top_students(data)
    failed = failed_students(data)
    highest = highest_per_subject(data)

    with open(filename, "w") as file:

        file.write("STUDENT ANALYSIS REPORT\n\n")

        # Average Marks
        file.write("Average Marks per Subject:\n")
        for subject, value in avg.items():
            file.write(f"{subject} : {value:.2f}\n")

        file.write("\nTop Student per Subject:\n")
        for subject, student in top.items():
            file.write(f"{subject} : {student['name']} ({student['marks']})\n")

        file.write("\nFailed Students:\n")
        for student in failed:
            file.write(f"{student['name']} - {student['subject']} ({student['marks']})\n")

        file.write("\nHighest Marks per Subject:\n")
        for subject, student in highest.items():
            file.write(f"{subject} : {student['name']} ({student['marks']})\n")


# Main program
def main():

    filename = "students.txt"

    data = load_data(filename)

    generate_report(data)

    print("Report generated successfully!")
    print("Check report.txt file.")


# Run program
if __name__ == "__main__":
    main()