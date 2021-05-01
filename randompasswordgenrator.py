
####################################################################################################################################################################
# Author: Prajwal Prakash
# Date: 20/11/2020
# Goal: Random Password genrator according to the user requirements.
###################################################################################################################################################################
import math
import random

while True:
    print("""what type of password do you want ? 
1.4 Digit numeric password.
2. Your choice of numbered digit numeric password.
3. Your choice of numbered alphanumeric password""")
    choice = input()


    def OTPgenerator():
        digits_in_otp = "0123456789"
        OTP = ""

        for i in range(4):
            OTP += digits_in_otp[math.floor(random.random() * 10)]

        return OTP


    if choice == '1':
        print(f"4 digit random numeric code: {OTPgenerator()}")
    elif choice == '2':
        print("How many digits ? ")
        number = input()


        def OTPxgenerator():
            digits_in_otp = "0123456789"
            OTP = ""

            for i in range(int(number)):
                OTP += digits_in_otp[math.floor(random.random() * 10)]

            return OTP


        print(f"{number} digit random numeric code: {OTPxgenerator()}")
    elif choice == '3':
        print("How many digits ? ")
        num = input()


        def stringgenerator():
            digits_in_otp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            otp = ""
            length = len(digits_in_otp)
            for i in range(int(num)):
                otp += digits_in_otp[math.floor(random.random() * length)]

            return otp


        print(f"{num} digit alphanumeric code:{stringgenerator()}")
    else:
        print("Enter only given choices (1/2/3)")
