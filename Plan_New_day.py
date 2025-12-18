import json





class New_Day :


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
        
        except FileExistsError :
            print("Databace not found ❌")
            return False
        

        else :
            return databace
        




    # Check day date
    def check_date(self, databace) :
        '''این تابع بررسی می کند که تاریخ 
        از قبل داخل دیتابیس وجود نداشته باشد'''

        if self.__date not in databace :
            return True
        
        else :
            return False
        


    


    # Save plan in databace
    def save_plan(self, databace) :
        '''این تابع ابتدا ورودی های شیء را
        ساختاردهی کرده و سپس
        آن را در دیتابیس برنامه ریزی روزانه 
        ذخیره می کند'''

        databace[self.__date] = {}

        databace[self.__date][self.__row] = {
            "Activity" : self.__activity,
            "Start Time" : self.__start_time,
            "End Time" : self.__end_time,
            "Description" : self.__description
            }
        

        

        try :
            with open("Daily_Plan_Databace.json", "w", encoding="utf-8") as file :
                json.dump(databace, file, ensure_ascii=False, indent=4)

        except FileNotFoundError :
            print("Databace not found ❌")

        else :
            print("Plan Saved ✅")






# Create Object
plan = New_Day("1404/09/27", 1, "Python", "11:30", "14:00", "Study lesson one of season 3 - OOP")


databace = plan.load_databace()

if plan.check_date(databace) :
    plan.save_plan(databace)


else :
    print("Date arlead excastid ❌")