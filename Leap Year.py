def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    x = 1
    return x
    # print("Given Year is a leap Year");  
  # Else it is not a leap year  
  else:  
    x = 0
    return x

def DeretLeap(y1,y2):  
    for x in range(y1, y2):
        if CheckLeap(x)==1:
            print(x)
            
y1, y2 = [int(x) for x in input("Masukkan range tahun (Contoh: 2010 2020) = ").split()]
DeretLeap(y1,y2)