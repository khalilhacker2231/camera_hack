#!\user\bin\env\python3
#-*- coding: utf-8 -*-
#https://githup.com/khalilhacker2231
import requests,re,os
import time
import sys


print("""
\033[1;31m\033[1;37m\

===============================================

  Author        :Khalilurahamn Hussaini
  Githup        :https://Githup.com/Khalilhacker2231
 YouTube       :AFGHAN tECH                         
 fACEBOOKE     :AFGHAN tECH                         
 Telegram    : https://t.me/khalil2231              
--------------------------------------------------  

\033[1;31m1)\033[1;37mUnited stat
\033[1;31m2)\033[1;37mJapan
\033[1;31m3)\033[1;37mItaly
\033[1;31m4)\033[1;37mKorea
\033[1;31m5)\033[1;37mFrance
\033[1;31m6)\033[1;37mGermany
\033[1;31m7)\033[1;37mTaiwan
\033[1;31m8)\033[1;37mRussian Federation
\033[1;31m9)\033[1;37mUnited Kindom
\033[1;31m10)\033[1;37mNeter lands
\033[1;31m11)\033[1;37mCzech Republic 
\033[1;31m12)\033[1;37mTurkey
\033[1;31m13)\033[1;37mAstrulia
\033[1;31m14)\033[1;37mSwitzerland
                                                        \033[1;31m91)\033[1;37mExtra
                                               """)


try:
    num = int(input("OPTIONS : "))
  
         


    if num == 1:
        print("\n")
        try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
              for page  in range (0,720):
               url = ("https://www.insecam.org/en/bycountry/US/?page="+str(page))

               res=requests.get(url,headers=headers)
               findip = re.findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
               count = 0

               for _ in findip:
                   hasil = findip[count]

                   print ("\033[1;31m",hasil)
                   count += 1

        except:
            print(" ")
    elif num == 2:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (x11;linux i686; rv:68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,232):
               url = ("https://www.insecam.org/en/bycountry/Jp/?[page="+str(page))

               res=requests.get(url,headers=headers)
               findip = re.findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
               count = 0

               for _ in findip:
                   hasil = findip[count]

                   print ("\033[1;31m",hasil)
                   count += 1
        except:
            print(" ")
    elif num == 3:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;rv:68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,159):
                url = ("https://www.insecam.org/en/bycountry/IT/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:               
                    hasil = findip[count]
                    print ("\033[1;31m",hasil)
                    count += 1
        except:
            print(" ")
    elif num == 4:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;rv:68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,141):
                url = ("https://www.insecam.org/en/bycountry/KR/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:
                    hasil = findip[count]
                    print ("\033[1;31m",hasil)
                    count +=1
        except:
            print(" ")
    elif num == 5:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;rv:68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,120):
                url = ("https://www.insecam.org/en/bycountry/FR/?[page="+str(page))

                res=requests.get(url,headers=headers)
                fingip = re,fingall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:
                    hasil = findip[count]
                    print ("\033[1;31m",hasil)
                    count +=1
        except:
            print(" ")
    elif num == 6:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;rv:68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,107):
                url = ("https://www.insecam.org/en/bycountry/GE/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:
                    hasil = findip[count]
                    print ("\033[1;31m",hasil)
                    count +=1
        except:
            print(" ")
    elif num == 7:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;rv:68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,92):
                url = ("https://www.insecam.org/en/bycountry/TW/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:
                    hasil = find[count]
                    print ("\033[1;31m",hasil)
                    count +=1
        except:
            print(" ")
    elif num == 8:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;rv:68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,82):
                url = ("https://www.insecam.org/en/bycountry/RU/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:
                    hasil = findip[count]
                    print ("\033[1;31m",hasil)
                    count +=1
        except:
            print(" ")
    elif  num == 9:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;rv68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,81):
                url = ("https://www.insecam.org/en/bycountry/UK/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:
                    hasil = findip[count]
                    prin ("\033[1;31m",hasil)
                    count +=1
        except:
            print(" ")
    elif num == 10:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,66):
                url = ("https://www.insecdam.org/en/bycountry/NL/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)    
                count = 0

                for _ in findip:
                    hasil = findip[count]
                    print ("\033[1;31m",hasil)
                    count +=1
        except:
            print(" ")
    elif num == 11:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,58):
                url = ("https://www.insecam.org/en/bycountry/CZ/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:
                    hasil = find[count]
                    print ("\033[1;31m",hasil)
                    count +=1
        except:
            print(" ")
    elif num == 12:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,54):
                url = ("https://www.insecam.org/en/bycountry/TR/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:
                    hasil = find[count]
                    print ("\033[1;31m",hasil)
                    count +=1
        except:
            print(" ")
    elif num == 13:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozolla\5.0 (x11;linux i686;68.0) Gecko/20100101 firefox/68.0'}
            for page in  rang (0,48):
                url = ("https://wwww.insecam.org/en/bycountry/AS/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:
                    hasil = find[count]
                    print ("\033[1;31m",hasil)
                    count +=1
        except:
            print(" ")
     elif num == 14:
        print("\n")
        try:
            headers = {'User-Agent': 'Mozilla\5.0 (x11;linux i686;68.0) Gecko/20100101 firefox/68.0'}
            for page in range (0,44):
                url = ("https://www.insecam.org/en/bycountry/SL/?[page="+str(page))

                res=requests.get(url,headers=headers)
                findip = re,findall('http://\d+.\d+.\d+.\d+.\d+', res.text)
                count = 0

                for _ in findip:
                    hasil = find[count]
                    print ("\033[1;31m",hasil)
                    count +=1                                                                                                                                                            

           except:
               print(" ")
       
     else:
         print(" ")
    
except keybourdInterrupt:
        print(" ")
