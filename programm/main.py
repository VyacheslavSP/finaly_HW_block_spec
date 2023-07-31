from Cat import Cat
from Dog import Dog
from Humster import Humster
from  Donkey import Donkey
from Camel import Camel
from Horse import Horse
from Counter import Counter
import re 
Select_Type=' Выберите  класс животного: 1-кот,2-собака,3-хомяк,4-лошадь,5-верблюд,6-осел '+'\n'
Main_Menu_str='Выберите вариант работы 1-показать всех,2-Завести новое животное, 3-Определить животное в новый класс, 4- Увидеть список команд, которое выполняет животное, 5- Обучить новой команде, q-Выход'+'\n'
Main_Menu_str_start='Список животных пуст. нажмите 1 для создания нового животного или q для выхода'+'\n'
def Show_all(List_obj):
    for i in List_obj:
        print(str(List_obj.index(i))+"   "+i.Name + "    " + i.__class__.__name__)
    answer=input ("Выберите животное для дальнейшей работы или нажите любую букву"+'\n')
    try:
        index_search=int(answer)
        return index_search
    except ValueError:
        index_search=0
        return index_search
def Build_animal(List_obj):
    while True:
        Name=input(" Введите кличку животного"+'\n')
        if Name != None:
            break
        else:
            print(" кличка не может быть пустой. поторите ввод")
    while True:
        Date_birth=input(" Введите дату рождения в формате гггг-мм-дд"+'\n')
        if (re.search(r'\d{4}-\d\d\-\d\d',Date_birth))!= None:
            if int(Date_birth.split('-')[1])<=12 and int(Date_birth.split('-')[2])<=31: # минимальная проверка на корректость даты
                break
        else:
            print(" неккоректный ввод данных")
    while True:
        answer=input(Select_Type)
        match answer.split():
            case ["1"]:  
                Object=Cat(Name,Date_birth)
                break
            case ["2"]:  
                Object=Dog(Name,Date_birth)
                break
            case ["3"]:  
                Object=Humster(Name,Date_birth)
                break
            case ["4"]:  
                Object=Horse(Name,Date_birth)
                break
            case ["5"]:  
                Object=Camel(Name,Date_birth)
                break
            case ["6"]: 
                Object=Donkey(Name,Date_birth)
                break
            case _:  
                print("неверная команда, введите еще раз")
    check_count_input=False
    if Object.getName != None:
        if Object.getDate_birth != None:
            if Object.__class__.__bases__ != None:
                check_count_input=True
    List_obj.append(Object)
    try:
        counter.Acsess(check_count_input)
        counter.add()
    except ValueError:
        print ("нет доступа к счетчику")
    print("счетчик равен    "+str(counter.printCount()))
    return len(List_obj)-1
    
def change_class(Object): ### видимо это необходимо для создания отряда ездовых хомяков. в противном случае не представляю как объект кот должен становиться объектом лошадь и как все это безобразие храниить
    while True:
        answer=input(Select_Type)
        flag=False
        match answer.split():
            case ["1"]:  
                tmp_id=Object.getID()   # Python, конечно, позволяет и налету делать такое. но для наглядности оставил так,принцип- собери все во временные удали объект а потом создай новый
                tmp_name=Object.getName()
                tmp_Date=Object.getDate_birth()
                if(Object.__class__.__bases__==Cat.__bases__):
                    tmp_commands=Object.getCommands()
                    flag= not flag
                del Object
                Object=Cat(tmp_name,tmp_Date)
                Object.ID=tmp_id
                Object.List_Commands_Pets=tmp_commands if flag else []
                return Object
            case ["2"]:  
                tmp_id=Object.getID()
                tmp_name=Object.getName()
                tmp_Date=Object.getDate_birth()
                if(Object.__class__.__bases__==Cat.__bases__):
                    tmp_commands=Object.getCommands()
                    flag= not flag
                del Object
                Object=Dog(tmp_name,tmp_Date)
                Object.ID=tmp_id
                Object.List_Commands_Pets=tmp_commands if flag else []
                return Object
            case ["3"]:  
                tmp_id=Object.getID()
                tmp_name=Object.getName()
                tmp_Date=Object.getDate_birth()
                if(Object.__class__.__bases__==Cat.__bases__):
                    tmp_commands=Object.getCommands()
                    flag= not flag
                del Object
                Object=Humster(tmp_name,tmp_Date)
                Object.ID=tmp_id
                Object.List_Commands_Pets=tmp_commands if flag else []
                return Object
            case ["4"]:  
                tmp_id=Object.getID()
                tmp_name=Object.getName()
                tmp_Date=Object.getDate_birth()
                if(Object.__class__.__bases__==Horse.__bases__):
                    tmp_commands=Object.getCommands()
                    flag= not flag
                del Object
                Object=Horse(tmp_name,tmp_Date)
                Object.ID=tmp_id
                Object.List_Commands_Pack_Animal=tmp_commands if flag else []
                return Object
            case ["5"]:  
                tmp_id=Object.getID()
                tmp_name=Object.getName()
                tmp_Date=Object.getDate_birth()
                if(Object.__class__.__bases__==Horse.__bases__):
                    tmp_commands=Object.getCommands()
                    flag= not flag
                del Object
                Object=Camel(tmp_name,tmp_Date)
                Object.ID=tmp_id
                Object.List_Commands_Pack_Animal=tmp_commands if flag else []
                return Object
            case ["6"]: 
                tmp_id=Object.getID()
                tmp_name=Object.getName()
                tmp_Date=Object.getDate_birth()
                if(Object.__class__.__bases__==Horse.__bases__):
                    tmp_commands=Object.getCommands()
                    flag= not flag
                del Object
                Object=Donkey(tmp_name,tmp_Date)
                Object.ID=tmp_id
                Object.List_Commands_Pack_Animal=tmp_commands if flag else []
                return Object
            case _:  
                print("неверная команда, введите еще раз")
def Main_menu(List_obj,index_search):
    while True:
        if len(List_obj)>0:
            Object=List_obj[index_search]
            print("Вы сейчас работаете с объектом "+ Object.Name + " класса " + Object.__class__.__name__)
            answer=input(Main_Menu_str)
            match answer.split():
                case ["1"]:  
                    index_search=Show_all(List_obj)
                case['2']:
                    index_search=Build_animal(List_obj)
                case ['3']:  
                    Object=List_obj[index_search]
                    Object=change_class(Object)
                    List_obj[index_search]=Object
                case ['4']:  
                    Object=List_obj[index_search]
                    list=Object.getCommands()
                    for i in list:
                        print(i)
                case ['5']:  
                    Object=List_obj[index_search]
                    answer=input(' Введите новую команду для обучения: '+ '\n')
                    Object.setCommands(answer)
                case ['q']:  
                    break
                case _:  
                    print("неверная команда, введите еще раз")
        else:
             answer=input(Main_Menu_str_start)
             match answer.split():
                case ["1"]:  
                    Build_animal(List_obj)
                case ['q']:  
                    break
                case _:  
                    print("неверная команда, введите еще раз")

c = Cat("Cat","2023-10-11")
d=Donkey("Donkey",'1990-15-05')
counter=Counter()
c.setCommands("test_cat")
d.setCommands("test_Domkey")
index_search=0
List_obj=[c,d]
for i in range(len(List_obj)):
    try:
        counter.Acsess(True)
        counter.add()
    except ValueError:
        print ("нет доступа к счетчику")

Main_menu(List_obj,index_search)
# Animal moves
# Cat moves