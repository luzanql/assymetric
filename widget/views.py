from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from base64 import b64encode, b64decode, binascii
from Crypto.Util.Padding import pad, unpad
import json



def index(request):
    return render(request, 'widget/index.html')

def nonce(request):
    # Shared Key between servers!
    #key = b'A3ildelkRxNqzmjzA3ildelkRxNqzmjz'
    #nonce = "sVxaXVDNXmT2eSgVY6BPgs1cYNuDZeU+1DWt6u/q3JWQkMYayBDYMM+WbUu0vtT68KEBi/PBvVQIo8WoaYSkwXmyM0yCOgHQNWjvmszyNe0Bjq/AA1aPqVXGwEPmgmWHXD357tHlX8bCunGOx+LBS5M4ulaE/oJveWaEehq3U5/d5aIlH5h4k+7CcL88o0/Zm2kFg2gVLuP7SgS8ck7N7YZJUmRXhyF/RAjH3JlwfKKGAGSpOKTgVy5Es++N7rYNUDRmak4U7YFPrtreKilad3DIAA5I78spGfE7P1T+V6kWLkQk3//oz1FIIT27/HcCFWB/aKXPZLJvzao2aYKsYxvIC3ovKDrjsobKd9KuxClYZyT5t3xlimg80xLGvF+79d7Dmeepesw8rDo4D9kklNBnunk8lP1Dw4NWg/cN/NCuhDrrBurOIr3cD00DpS7fCs2qgQpglkjDDZrVqKjBywJO2lCucIq7PE/GRzEfi9qaLJ//IUjgVpFffH6tbdgA7d8q5mUnhfCDSkBu/1TfrzPhry8Uo/bWeC2zKPbzXT35giARa7Kx2npD4/v+x4fYEX/cSENR7MAwuRhsiMi2Yy/64A0hd1NS5yidjvnrPCWO30+Myb0xF5dLfzzFFDgZPCa47YHCZ8jhlRGZ03ldyuE8rjC+lM5TmnEFBsFchxo="
    #nonce = "F7ZDid2IEsJYK+LTVFmfJqtPajHItR/CpOthxhZFRac5VEHd+XOxE+GyCWdIfYHWVTXOk+wt1uYAVuAAL2fIJghEANQLYkbAX71x0QEb2Qr6Txy0ZyM2gkHA6adahl5+jkwTa+5EPgFNB4bIfiEKUvd8nLCK5De+J8N3T31Tu1g4K9uAU2ozrDQinMXw/VQyP6vjQMKi+uMBhJH2Bds+51z4Lk5f2OcAUe8JWM0lYDTIRO+uY3DAWoRUnN0X+tgx72wnbqwdxNmtVJ8BCsIE9bG1ibg1M5sM9MS0U1f6BRT5xgMH8SLgCaIKZ8rI6J40p7Lk/svG5UfWyo0/2T+0hbqiYS8qa5dHdChSMGt6k+dFRwVE46rXkIgkw0vrej9Eh4oXpPR/23adQ9WYz1jFn0E7x827gsk2ghuU3gbDCMXDSb6W/iweK+2lD9Mdq2UDXpw0f1ChARPLHwiRiUes3j8y+MAQb+OAExHZVyeyPDqdWA0IHXMc28fCTxC1bh4/ScPK8LK880uzdN8nume/lcW0t11oMNxinpKqwrhrUffVqjvCcH0jzwnHRanDlIuK16dN33DL0b6/ddQcUm4qoeSGB/DsVuu+1//a6DpxUPqlEjQCeh9mzj+TLVlnnQ3mWAsd8bnq84NcUKNwBJyaMe28waDEWmU8LMyuDW/TKew="
    nonce = b64decode(request.POST.get('n'))
    raw_cipher_data = b64decode(nonce)
    pkey = RSA.importKey(open('private.pem').read())
    # Important to use pkcs1_oap cypher. Data was encrypted using this padding.
    # RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(pkey)
    message = cipher.decrypt(raw_cipher_data)
    decoded_json = json.loads(b64decode(message).decode())
    print(decoded_json)
    return JsonResponse(decoded_json)


def generateKeys(request):
    ##Important to encrypt the key with this lenght
    key = RSA.generate(4096)
    private, public = key, key.publickey()
    f = open('private.pem','wb')
    f.write(private.export_key('PEM'))
    f = open('public.pem','wb')
    f.write(public.export_key('PEM'))
    f.close()
    return render(request, 'widget/index.html')

    