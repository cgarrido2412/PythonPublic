import re
voice_mail = 'Hey this is store 1080 please give us a call back at 425-123-1234 today or 425-321-4321 tomorrow!'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(voice_mail))
