class Time:
    def __init__(self,h,m,s):
        self.__hour=h
        self.__minute=m
        self.__second=s
    def __add__(self,other):
        self.__hour+=other.__hour
        self.__minute+=other.__minute
        self.__second+=other.__second
        if (self.__second>=60):
            extra_minute=int(self.__second/60)
            self.__second=self.__second%60
            self.__minute+=extra_minute
        if (self.__minute>=60):
            extra_hour=int(self.__minute/60)
            self.__minute=self.__minute%60
            self.__hour+=extra_hour
        return "Hour(s):"+str(self.__hour)+": Minute(s): "+str(self.__minute)+": second(s): "+str(self.__second)

ob1=Time(5,40,30)
ob2=Time(3,40,15)
print(ob2+ob1)

# Step 1:start
# Step 2: define a class time with a constructor, and function naming time.
# Step 3: use_add_function to overload '+'.
# Step 4:create two objects and call the function Time.
# Step 5: print the corresponding output.
# Step 6:stop.
