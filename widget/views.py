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
    #nonce = "F7ZDid2IEsJYK+LTVFmfJqtPajHItR/CpOthxhZFRac5VEHd+XOxE+GyCWdIfYHWVTXOk+wt1uYAVuAAL2fIJghEANQLYkbAX71x0QEb2Qr6Txy0ZyM2gkHA6adahl5+jkwTa+5EPgFNB4bIfiEKUvd8nLCK5De+J8N3T31Tu1g4K9uAU2ozrDQinMXw/VQyP6vjQMKi+uMBhJH2Bds+51z4Lk5f2OcAUe8JWM0lYDTIRO+uY3DAWoRUnN0X+tgx72wnbqwdxNmtVJ8BCsIE9bG1ibg1M5sM9MS0U1f6BRT5xgMH8SLgCaIKZ8rI6J40p7Lk/svG5UfWyo0/2T+0hbqiYS8qa5dHdChSMGt6k+dFRwVE46rXkIgkw0vrej9Eh4oXpPR/23adQ9WYz1jFn0E7x827gsk2ghuU3gbDCMXDSb6W/iweK+2lD9Mdq2UDXpw0f1ChARPLHwiRiUes3j8y+MAQb+OAExHZVyeyPDqdWA0IHXMc28fCTxC1bh4/ScPK8LK880uzdN8nume/lcW0t11oMNxinpKqwrhrUffVqjvCcH0jzwnHRanDlIuK16dN33DL0b6/ddQcUm4qoeSGB/DsVuu+1//a6DpxUPqlEjQCeh9mzj+TLVlnnQ3mWAsd8bnq84NcUKNwBJyaMe28waDEWmU8LMyuDW/TKew="
    # nonce = request.POST.get('n')
    # print(request.POST)
    # parsed = urllib.parse.unquote(url)
    # print(parsed)
    id = request.POST.get('n')
    encrypted = json.loads(b64decode(id).decode())
    print("encrypted")
    print(encrypted)
    print("encrypted data")
    print(encrypted['data'])
    raw_cipher_data = b64decode(encrypted['data'])
    print("raw")
    print(raw_cipher_data)

    #nonce = 'KrStvkIIbdTZ3c0TdhWJ5GCnqr /wUt5s64dEPKY4jh1lgFV8 QNxhVZ0mqNUdVITBMqb3gWLdlTBP 9AAoxU4tCVPlr/SSmvuMCCa51mM6J34KDk1JoU0pAOTwit360SRYsBc5eSZgWhHI8uYTwR1ILbK7CQd2bWs9xWGhITc9UmB/yaPEIRKC94x5DgCyLSgwN 4dYI41o/BcD8tR6JeSFfEacT8VmstnDPpOXctrbA0CDmNhIoVfnTgFW5pTA00/WMjOv/7GCMSihy7wmDpkNbVSveqtu4yy kBZl8u6aRDIbjviFZEEiA1nn7eqpHEZwH6X2UfpuvzKh1DDQmvwltxvBiQsKsSGcW pCUE qPQKu2TMf2tJtBaK6oLhI5YHhR9BAWuZ70S3k5jlzng1ePASpdlPFiiutb3CWi7V5FkILn2fnYjmEx0sLqZjpRLs1EqOi58uQebvoaYbYF1Eojt0rxUMRQBVuymkqUbzLHgGtcI59C/TCd6hJEz3MSmH/fsV9L7wmh7f6HukcWSgJsypwDKOPO66nHTAmdHuzDUIOqQeLHuWbwyLOrXgsFSVKYOuQ/X306bUP 8Mb7nHnY1idmqHPeNLWipFSxzgA2wragUZ2y7NP4rbHjKyD bFOb2kHE/6DMhw9YL1aUf3g/nSEkgZ yIhP4nNUm34='
    # print(encrypted)
    # raw_cipher_data = b64decode(parsed)
    # print("nonnnnceeee")
    # print(nonce)
    #raw_cipher_data = b64decode(nonce)
    pkey = RSA.importKey(open('private.pem').read())
    # Important to use pkcs1_oap cypher. Data was encrypted using this padding.
    # RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(pkey)
    message = cipher.decrypt(raw_cipher_data)
    decoded_json = json.loads(b64decode(message).decode())
    print(decoded_json)
    return JsonResponse(decoded_json)
    # print("nonce")
    # print(nonce)
    # return (request)


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

    