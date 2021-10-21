str= input("enter a string ")     
def main(str):
            str= input("enter a string ")
            a=str[-1::-1]
            if str==a:
                print("yes it is a palidrome")
            else:
                print("enter string is not a palidrome")
            
def length(str):
            n=input("enter a caracter whose len you want to check :")
            count=0
            for i in str:
                if i==n:
                    count+=1
            print(f"number of {n} repeated in the string is {count} ")
           
def check_substring(str,sub):
    
            if (str.count(sub)>0):
                print("yes substring exist in the string")
            else:
                print("no the substring you enter does not exist in the strng")

def lenght_word(str):
    longest=str.split(" ")
    l=0
    for long in longest:
        if len(long)>l:
            l=len(long)
    print(" longest word in the string is :",long)
main(str)
length(str)
sub=input("enter the substring :")
check_substring(str,sub)
lenght_word(str)

