import random
import pandas as pd
from time import sleep

def validPhoneNumber(df,index):
    print("번호를 서식대로 입력하지 않은 사람들을 제거합니다.")
    dic = df[df.keys()[index]]
    droplist = []
    for i in range(len(dic)-1):
        if(len(str(dic[i]))==13 and str(dic[i]).count('-')==2):
            pass
        else:
            droplist.append(i)
    df = df.drop(droplist,axis=0).reset_index(drop=True)
    return df

def findPhoneIndex(df):
    for i in range(0,len(df.keys())):
        if(df.keys()[i].find('연락처')>-1):
            index = i
        if(df.keys()[i].find('번호')>-1):
            index = i
    return index

def makeAnnonyCode(code):
    return code[:5] + "*****"

def makeAnnonyPhone(phone):
    return phone[:4] + "****" + phone[8:13]

def makeAnnonyName(name):
    if(len(name)==2):
        return "*"+name[1]
    elif(len(name)==3):
        return name[0]+ "*" +name[2]
    elif(len(name)==4):
        return name[:2] + "*" + name[3]    

def printInfo(df,random_list):
    for i in range(len(random_list)):
        sleep(0.5)
        if(i>=10): 
            grade = "예비 " + str(i-9) + "번"
        else:
            grade = str(i + 1)+"번"

        index = random_list[i]
        name = makeAnnonyName(str(df[df.keys()[1]][index]))
        major = str(df[df.keys()[2]][index])
        code = makeAnnonyCode(str(df[df.keys()[3]][index]))
        phoneNumber = makeAnnonyPhone(str(df[df.keys()[4]][index]))
        
        print(grade + " / " + name + " / " + major + " / " + code + " / " + phoneNumber)

def Lots(number):
    random_list = []
    rand_num = random.randint(0,count-1)
    for i in range(number):
        while rand_num in random_list:
            rand_num = random.randint(0,count-1)
        random_list.append(rand_num)
    random_list.sort()
    return random_list

if __name__ == "__main__":
    print("*****************************************************")
    name = input("Excel Name : ")
    df = pd.read_excel(name + '.xlsx', encoding='utf-8')
    print("*****************************************************")
    count = len(df.values)
    print("총 응답 개수 : " + str(count)+"개")

    phoneIndex = findPhoneIndex(df)
    df = validPhoneNumber(df,phoneIndex)
    
    count = len(df.values)
    print("정상 응답 개수 : " + str(count)+"개")
    print("*****************************************************")
    number = int(input("Lots Number : "))
    print(str(number)+"개를 추첨합니다")
    print("*****************************************************")
    random_list = Lots(number)
    printInfo(df,random_list)
    print("*****************************************************")
