# python ProcessSurveillance.py 2 MarvellousLog
# python ProcessSurveillance.py time_interval Folder_Name
#               0                   1             2 
# len(sys.argv) -> 3

import psutil
import sys
import os

def main():
    Border = "_"*50
    print(Border)
    print("----Platform Surveillance System----")
    print(Border)


    # ---h and ---u handling
    if(len(sys.argv) == 2):
          if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
               print("this automation script is use to perform")
               print("1 : it fetch the info of running processes")
               print("2 : it fetch info about the Primary storage as RAM")
               print("3 : it fetch info about the secondary storafe as HDD")
               print("4 : it fetch info about the Microprocessor")
               print("5 : it gets auto scheduled periodically")
               print("6 : it maintains all records into log files")
               print("7 : it sends the log files through mail directory")

          elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
               print("Ise the automatiomn script as : ")
               print(f"pyhton {sys.argv[0]} Time_Interval Folder_Name")
               print("Time in minutes : Time in minutes for periodic execution")
               print("Folder_name : Name of folder for the log creation")


          else: 
               print("Unable to proceed as there is no matching arguments")
               print("please use --h or --u for getting more details")


    # Actual project code
    elif(len(sys.argv) == 3):
         pass

    else:
         print("Invcalid no. of arguments")
         print("Unable to proceed as arguments are not matching")
         print("Please use --h or --u flag for getting more details")

    print(Border)
    print("----Thankyou for Using our Automation System----")
    print(Border)
    

if __name__ == "__main__":
    main()