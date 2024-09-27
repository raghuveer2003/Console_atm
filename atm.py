def withdraw(i):
    print("enter your amount:")
    amount=int(input())
    print("enter your pin:")
    pin_code=int(input())
    if(pin_code!=pin[i]):
        print("invalid pin")
        print("end")
    else:
        if(amount>bal[i]):
            print("insufficient balance:")
            print("end")
        else:
            bal[i]-=amount
            print("collect your amount:")
            print("do you want to display balance?(y/n)")
            a=input()
            if(a=='y'):
                print("your avaiable balanace is:",bal[i])
                print("Thank You for banking with us")
            else:
                print("Thank you for banking with us")
def deposit(i):
    print("enter pincode:")
    pincode=int(input())
    if(pincode!=pin[i]):
        print("invalid pin")
        print("end")
    else:
        print("enter the amount to be deposited:")
        money=int(input())
        bal[i]+=money
        print("The cash is deposited:",bal[i])
def account(i):
    print("enter the pinnumber:")
    pinnumber=int(input())
    if(pinnumber!=pin[i]):
        print("Invalid pin")
        print("end")
    else:
        print("The available balance is:",bal[i])
def password(i):
    print("Enter the current password")
    paswword=input()
    if(paswword!=passcode[i]):
        print("Invalid passcode")
    else:
        print("Enter the new password:")
        newpassword=input()
        print("Confirm password:")
        cpassword=input()
        if(newpassword==cpassword):
            print("Password updated successfully")
        else:
            print("Try again")

def atm():
    print("enter your passcode:")
    pass_code=input()
    flag=0
    if(pass_code!=passcode[i]):
        print("wrong password,More 2 attempts")
        pass_code=input()
        if(pass_code!=passcode[i]):
            print("wrong password,More 1 attempts")
            pass_code=input()
            if(pass_code!=passcode[i]):
                print("wrong password,Account blocked")
            else:
                flag=1
        else:
            flag=1
    else:
        flag=1
    if(flag==0):
        print("end")
    else:
        print("1.Withdrawal")
        print("2.deposit")
        print("3.account balance")
        print("4.change password")
        print("enter your choice:")
        while(1):
            choice=int(input())
            if(choice in [1,2,3,4]):
                break
            else:
                print("wrong choice")
        if(choice==1):
            withdraw(i)
        elif(choice==2):
            deposit(i)
            pass
        elif(choice==3):
            account(i)
            pass
        elif(choice==4):
            password(i)
            pass


user=['sriya','dev','harsha','vidya']
passcode=['sriya12','dev345','harsha1204','vidya120']
pin=[1808,5803,1204,1220]
bal=[25000,35000,30000,80000]
print("Enter username:")
user_name=input()
if(user_name in user):
    i=user.index(user_name)
atm()