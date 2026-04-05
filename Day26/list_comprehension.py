# #list comprehension
# new_list = [item*2 for item in range(1,5)]
# print(new_list)


# #Conditional list comprehension
# # new_list = [new_item for item in list if test ] 

# names = ['preksha','Pragya','Ishan','Sapna','Pankaj']
# short_names = [ name for name in names if len(name)<=5]
# print(short_names)
# large_names = [name.upper() for name in names if len(name)>5]
# print(large_names)
# large_name = [name.capitalize() for name in names if len(name)>5]
# print(large_name)


# numbers_square = [number**2  for number in range(1,5)]
# print(numbers_square)

# numbers_onlyeven = [number for number in range(1,10) if number%2 ==0]
# print(numbers_onlyeven)


# #Dict Comprehension
# #new_dict = {new_key: new_value for item in list }
# #new_dict = {new_key: new_value for (key,value) in dict.items()}
# #new_dict = {new_key: new_value for (key,value) in dict.items() if test }
# import random
# names = ['Preksha','Pragya','Ishan','Sapna','Pankaj']
# students_score = {student:random.randint(80,100) for student in names }
# print(students_score)

# hindi_students = {key:value for (key,value) in students_score.items() if value>=90}
# print(hindi_students)
# # iteration over pandas data frame 
# student_scores = {"Student": ["Mukul","Adarsh"],"Scores" : [55,66]}
# import pandas 
# student_data_frame = pandas.DataFrame(student_scores)
# print(student_data_frame)

# for (index , row) in student_data_frame.iterrows():
#     print(index)
#     print(row)
#     print(row.Student)
#     print(row.Scores)
import pandas as pd

# # NATO phonetic alphabet data
# nato_data = {
#     "Letter": list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#     "Code": [
#         "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel",
#         "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa",
#         "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey",
#         "X-ray", "Yankee", "Zulu"
#     ]
# }

# df = pd.DataFrame(nato_data)

# # Save as CSV
# file_path = "C:\\Users\\Preksha Asati\\PY\\Day26\\NATO_Phonetic_Alphabet.csv"
# df.to_csv(file_path, index=False)

#file_path
import pandas as pd
new_df = pd.read_csv("C:\\Users\\Preksha Asati\\PY\\Day26\\NATO_Phonetic_Alphabet.csv")
#print(new_df)
#{new_key : new_value for (index,row) in df.iterrows()}
nato_dict = {row.Letter : row.Code for (index,row) in new_df.iterrows()}
print(nato_dict)


word = input("Enter a Word : ").upper()
nato_list = [nato_dict[letter] for letter in word]
print(nato_list)



