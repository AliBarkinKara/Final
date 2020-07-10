# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:56:56 2020

@author: Ali Barkın Kara
"""
#Ödev1
#from datetime import datetime, date
#print("tarih  giriniz")
#gun=int(input("tarih  gün degeri: "))
#ay=int(input("tarih  ay degeri: "))
#yıl=int(input("tarih  yıl degeri: "))

#tarih2 = date(day = gun, month = ay, year = yıl)  
#print("1.tarih : ",tarih2)

#Ödev2
#def durum1(x): 

    #fact=1;
  
    #for i in range (1,(3*x)+1): 
  
        #fact = fact * i
  
    #return fact 
  
#def durum2(x): 
  
    #out=0 
  
    #for i in range (1,x+1):
  
        #out = out + (2*i) 

    #return out
#x = int(input("x değerini giriniz ")) 

#if (x>=0 and x<9): 

    #print(durum1(x)) 
  
#elif (x>=9 and x<16): 
  
        #print(durum2(x)) 
#else:
  
    #print("Geçersiz girdi") 
#Ödev3
#import string
#import numpy as np
#import math
#from sympy import Matrix #inverse key


#def letterToNumber(letter):
	#return string.ascii_lowercase.index(letter)

#def numberToLetter(number):
	#return chr(int(number) + 97)


#module = 26 

#raw_message = "alk"
#raw_message = "ali karaba"
#print("raw message: ",raw_message)

#message = []

#key = np.array([
	#[1, 2, -1], 
	#[2, 5, 2], 
	#[-1, -2, 2]
#]) 

#key_rows = key.shape[0]
#key_columns = key.shape[1]

#if key_rows != key_columns:
	#raise Exception('anahtar kare matris olmalıdır')


#for i in range(0, len(raw_message)):
	#current_letter = raw_message[i:i+1].lower()
	#if current_letter != ' ':
		#letter_index = letterToNumber(current_letter)
		#message.append(letter_index)
		


#if len(message) % key_rows != 0:
	#for i in range(0, len(message)):
		#message.append(message[i])
		#if len(message) % key_rows == 0:
			#break


#message = np.array(message)
#message_length = message.shape[0]
#print("message: ",message)


#message.resize(int(message_length/key_rows), key_rows)


#encryption = np.matmul(message, key)
#encryption = np.remainder(encryption, module)
#print("şifreli metin: \n",encryption)




#print("ters anahtarı bulma")
#inverse_key = Matrix(key).inv_mod(module)
#inverse_key = np.array(inverse_key) 
#inverse_key = inverse_key.astype(float)
#print("ters anahtarı bulma: ",inverse_key)


#print("ters anahtarı doğrulama. ")
#check = np.matmul(key, inverse_key)
#check = np.remainder(check, module)
#print("key times inverse key: ",check)
#print("bu matris ",np.allclose(check, np.eye(3)))


#print("şifre çözme:")
#decryption = np.matmul(encryption, inverse_key)
#decryption = np.remainder(decryption, module).flatten()
#print("şifre çözme ",decryption)

#decrypted_message = ""
#for i in range(0, len(decryption)):
	#letter_num = int(decryption[i])
	#letter = numberToLetter(decryption[i])
	#decrypted_message = decrypted_message + letter
	
#print("şifresi çözülmüş mesaj: ",decrypted_message)
#ödev4
#print(1,"ile",51,"arasındaki asal sayılar:")
 
#for sayi in range(1,51 + 1):
   #if sayi > 1:
       #for i in range(2,sayi):
           #if (sayi % i) == 0:
               #break
       #else:
           #print(sayi)








            
