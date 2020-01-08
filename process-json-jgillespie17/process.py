import json

def main():
    with open('grades.json') as f:
        grades = json.load(f)
    print("Exam result for Class 28")
    print("========================")
    filtered_dict = dict(filter(lambda 'class_id':value, 'class_id' == 28, grades.items()))
    print(filtered_dict)

if __name__ == "__main__":
        main()
