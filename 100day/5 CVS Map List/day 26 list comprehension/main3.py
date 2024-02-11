students_dict = {
    "student": ["Angela", "Bella", "Cathy", "David", "Eva", "Frank", "Gina", "Helen", "Ivy", "Jack", "Kathy", "Linda", "Mike", "Nancy", "Oscar", "Peter", "Queen", "Rose", "Steve", "Tom"],
    "score": [90, 85, 88, 79, 92, 95, 87, 83, 78, 80, 89, 91, 94, 82, 76, 85, 88, 90, 93, 77]
}

# for (k,v) in students_dict.items():
#     print(v)
    
import pandas

students_df = pandas.DataFrame(students_dict)

print(students_df)

for (i, row) in students_df.iterrows():
    print(f'{row.student} \t #{i:03} has a score of {row.score}.')