alphabet = "abcdefghijklmnopqrstuvwxyz"
code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddg" \
       "agclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
code = 'www.pythonchallenge.com/pc/def/map'

code = list(code)

for pos, element in enumerate(code):
    if element is 'y':
        code[pos] = 'a'
        continue
    if element is 'z':
        code[pos] = 'b'
        continue
    if element in alphabet:
        code[pos] = chr(ord(element) + 2)

print(''.join(code))

'''
"Proposed solution:"
import string

code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddg" \
       "agclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "


intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
table= str.maketrans(intab,outtab)
print (code.translate(table))
'''
