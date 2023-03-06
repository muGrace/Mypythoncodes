
import time;
ticks=time.time()
print(" Number of ticks since 12:00am,January 1,1970:",ticks)
localtime=time.localtime(time.time())
print("local current time:",localtime)
import calendar
cal=calendar.month(2023,2)
print( "Here is the calendar.")
print(cal)
def happyBirthday(person):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday to you, dear " + person +".")
    print("Happy birthday to you!")
def main():
    Name=input("Enter the name of Person with birthday:")
    happyBirthday(Name)
main()  
          


