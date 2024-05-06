import argparse
import csv
import re
import colorama
import openpyxl
import pandas as pd


def GetStudents(file):
    with open(file,"r",encoding="UTF-8") as f:
        html=f.read()

    wb=openpyxl.Workbook()
    sheet=wb.active

    regex=r"<span style.*title=\"姓名 \">(.{1,3})<\/span>\n +<span style=\"color: \#afafaf;\" title=\"帳號 \">([0-9Cc]{9})</span>"
    studentsAmount=0
    sheet.append(["id","name"])
    for name,id in re.findall(regex,html):
        print(studentsAmount+1,name,id)
        sheet.append([id,name])
        studentsAmount+=1

    wb.save('students.xlsx')
    print()
    print(colorama.Fore.CYAN+"-"*40)
    print("Generated students.xlsx")
    print("The amount of students is",studentsAmount)
    print(colorama.Style.RESET_ALL)

def GenerateAccounts(studentsData,id):
    startID=id
    with open('accounts.tsv','w',encoding="UTF-8") as f:
        tsv_w=csv.writer(f,delimiter='\t',lineterminator="\n")
        tsv_w.writerow(['accounts', '1'])
        # ['team', 'name', 'account', 'password']
        for i in studentsData.values:
            password=i[0]
            name=i[1]
            tsv_w.writerow(['team', name, f"team{id}", password])
            id+=1
    endID=id-1
    print()
    print(colorama.Fore.CYAN+"-"*40)
    print("Generated accounts.tsv")
    print(f"The ID from {startID} to {endID}"+colorama.Style.RESET_ALL)


def GenerateTeams(studentsData,id):
    startID=id
    with open('teams.tsv','w',encoding="UTF-8") as f:
        tsv_w=csv.writer(f,delimiter='\t',lineterminator="\n")
        tsv_w.writerow(['teams', '1'])
        # ['id', 'exid', '3', 'name', 'University', 'NTUT', 'TWN', 'ntut']
        for i in studentsData.values:
            ICPC_ID=i[0]
            name=i[1]
            tsv_w.writerow([id, ICPC_ID, '3', f"{name}-{id}", 'University', 'NTUT', 'TWN', 'ntut'])
            id+=1
    endID=id-1
    print()
    print(colorama.Fore.CYAN+"-"*40)
    print("Generated teams.tsv")
    print(f"The ID from {startID} to {endID}"+colorama.Style.RESET_ALL)

if "__main__"==__name__:
    parser=argparse.ArgumentParser()
    parser.add_argument("file")
    args=parser.parse_args()

    if args.file[-4:]!='html':
        print("input html file")
        print(parser.print_help())
        exit()

    GetStudents(args.file)

    id=int(input("ID start from? (number)\n"))
    studentsData=pd.read_excel('students.xlsx')
    GenerateAccounts(studentsData,id)
    GenerateTeams(studentsData,id)