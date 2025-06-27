import pandas as pd
data={"rollno":[1,2,3,4,5,6,7,8,9,10],
    "name":["vamshi","ravi","jana","srinu","abhi","teja","ajith","raja","snehith","adhi"],
    "section":["apollo","crypto","apollo","crypto","apollo","crypto","apollo","crypto","apollo","crypto"],
    "PYTHON":[98,99,96,95,97,92,93,94,90,98],
    "C++":[95,98,96,97,94,92,88,86,85,87],
    "JAVA":[88,95,97,96,93,92,94,97,89,78],
    "AIML":[99,98,95,96,93,97,94,91,90,99],
    "MATHS":[89,87,85,86,87,84,82,81,83,80]}
df=pd.DataFrame(data)
print(df)
print("MEAN of given subjects:\nPYTHON:",df["PYTHON"].mean(),"\nC++:",df["C++"].mean(),"\nJAVA:",df["JAVA"].mean(),"\nAIML:",df["AIML"].mean(),"\nMATHS:",df["MATHS"].mean())
print("subject average:\nPYTHON:",(df["PYTHON"].sum()/1000)*100,"\nC++:",(df["C++"].sum()/1000)*100,"\nJAVA:",(df["JAVA"].sum()/1000)*100,"\nAIML:",(df["AIML"].sum()/1000)*100,"\nMATHS:",(df["MATHS"].sum()/1000)*100)
print("first 5 rows are:")
print(df.head())
print("last 5 rows are:")
print(df.tail())
