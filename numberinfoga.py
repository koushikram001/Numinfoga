import sys
import signal
import phonenumbers
import colorama
from colorama import Fore
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

print('''
	 _                 _______  ______   _______  _______ _________ ________ ________ _______  _______ 
( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )\__   __/( (    /|(  ____ \(  ___  )(  ____ \(  ___  )
|  \  ( || )   ( || () () || (   ) )| (    \/| (    )|   ) (   |  \  ( || (    \/| (   ) || (    \/| (   ) |
|   \ | || |   | || || || || (__/ / | (__    | (____)|   | |   |   \ | || (__    | |   | || |      | (___) |
| (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)   | |   | (\ \) ||  __)   | |   | || | ____ |  ___  |
| | \   || |   | || |   | || (  \ \ | (      | (\ (      | |   | | \   || (      | |   | || | \_  )| (   ) |
| )  \  || (___) || )   ( || )___) )| (____/\| ) \ \_____) (___| )  \  || )      | (___) || (___) || )   ( |
|/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/\_______/|/    )_)|/       (_______)(_______)|/     \|
                                                                                                            \n ''')
print("\n\n Coded By koushikram001\n\n")
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
prRed("PRINT THE PHONENUMBER ALONG WITH THE COUNTRYCODE OTHERWISE IT WILL SHOW ERROR !!!")
def sigint_handler(signal, frame):
    print ('BYEBYE')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)
x = input(Fore.GREEN + "Enter the PhoneNumber for Gathering INFO'S: ")
phonenumber = phonenumbers.parse(x)
Country = (geocoder.description_for_number(phonenumber,"en"))
Carrier = (carrier.name_for_number(phonenumber,"en"))
Timezone = (timezone.time_zones_for_number(phonenumber))
valid = phonenumbers.is_valid_number(phonenumber)
possible = phonenumbers.is_possible_number(phonenumber) 

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
prGreen(x)
prYellow(Country)
prYellow(Carrier)
prYellow(Timezone)
prYellow(valid)
prYellow(possible)
