import json





class Plan :


    def __init__(self, date, row, activity, start_time, end_time, description):
        self.__date = date
        self.__row = row
        self.__activity = activity
        self.__start_time = start_time
        self.__end_time = end_time
        self.__description = description




    # load Datebace
    def load_databace(self) :
        '''این تابع دیتابیس برنامه روزانه 
        را باز می کند'''

        try :
            with open("Daily_Plan_Databace.json", "r", encoding="utf-8") as file :
                databace = json.load(file)
        
        except FileNotFoundError :
            print("Databace not found ❌")
            return False
        

        else :
            return databace
        




    # Check day date
    def check_date(self, databace, set_date : bool) :
        '''این تابع از ورودی می گیرد که
        آیا تاریخ در دیتابیس ورودی 
        باشد یا خیر
        در نتیجه براساس ورودی, نتیجه را بر می گرداند'''

        # بررسی نبودن تاریخ
        if not set_date :
            return self.__date not in databace 

        
        # بررسی بودن تاریخ
        elif set_date :

            return self.__date in databace 

        



    
    # Check date row
    def check_date_row(self, databace, date, row) :
        '''این تابع بررسی می کند 
        که ردیف ورودی در تاریخ ورودی در دیتابیس ورودی
        نباشد'''
        
        if row in databace[date] :
            return False

        else :
            return True
        

        

            


    # Save plan in databace
    def save_plan(self, databace, create_date : bool) :
        ''' این تابع ابتدا اینکه تاریخ ساخته شود و یا خیر
        را از ورودی می گیرد
        سپس ورودی های شیء را
        ساختاردهی کرده و سپس
        آن را در دیتابیس برنامه ریزی روزانه 
        ذخیره می کند'''
        

        # ساخت تاریخ
        if create_date :
            databace[self.__date] = {}


        
        # ساختاردهی
        databace[self.__date][self.__row] = {
            "Activity" : self.__activity,
            "Start Time" : self.__start_time,
            "End Time" : self.__end_time,
            "Description" : self.__description
            }
        

        
        # بازکردن و ذخیره در دیتابیس
        try :
            with open("Daily_Plan_Databace.json", "w", encoding="utf-8") as file :
                json.dump(databace, file, ensure_ascii=False, indent=4)

        except FileNotFoundError :
            print("Databace not found ❌")

        else :
            print("Plan Saved ✅")

















# Start new day
def new_day(Object, databace, date) :

    # Check Date not in Databace
    if Object.check_date(databace, False) :

        # Save Plan
        Object.save_plan(databace, True)


    else :
        print("Date arleady excastid ❌")





# Add New plan on date
def add_new_plan(Object, databace, date, row) :

    # Check Date in Databace
    if Object.check_date(databace, True) :
        
        # Check Row not in date
        if Object.check_date_row(databace, date, row) :

            # Save Plan
            Object.save_plan(databace, False)


        else :
            print("This row used early in this date ❌")

    else :
        print("Date not found !")








def mine_meno() :

    # Get inputs
    date = input("Date :  ")
    row = input("Row :  ")
    activity = input("Activity :  ")
    start_time = input("Start Time :  ")
    end_time = input("End time :  ")
    description = input("Description :  ")


    # Create Object
    plan = Plan(date, row, activity, start_time, end_time, description)
    
    # Load Daily_Plan databace
    databace = plan.load_databace()



    # Start new day or add new plan to the date
    print("1. New Day")
    print("2. Add New Plan ")

    meno = input(" >>>  ")


    # Start new day
    if meno == "1" :
        new_day(plan, databace, date)

    # Add new plan to the date
    elif meno == "2" :
        add_new_plan(plan, databace, date, row)








mine_meno()