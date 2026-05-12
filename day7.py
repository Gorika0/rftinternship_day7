import pandas as pd
data={
    "Name":["Amit" ,"Riya","John"],
    "Math":[80,90,60],
    "Science":[70,88,65],
    "English":[85,92,70]
}
df=pd.DataFrame(data)
df["AVERAGE"]=(df["Math"]+df["Science"]+df["English"])/3
print(df)
#topper
topper=df.loc[df["AVERAGE"].idxmax()]
print("topper is:",topper["Name"])
#count students above avg
overall_avg=df["AVERAGE"].mean()
count=df[df["AVERAGE"]>overall_avg].shape[0]
print("students above avg:",count)
#add grade column
grades=[]
for avg in df["AVERAGE"]:
    if avg>=90:
        grades.append("A")
    elif avg>=75:
        grades.append("B")
    elif avg>=60:
        grades.append("C")
    else:
        grades.append("D")
df["grade"]=grades
print(df)
#subject wise mean
print(df[["Math","Science","English"]].mean())
