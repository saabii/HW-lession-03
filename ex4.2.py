invitation = input('Dear ')
l = invitation.split(' ')
male = 'mr'
female = ['mrs', 'miss', 'ms']
if l[0].lower() in female:
    print('Female')
elif l[0].lower() in male:
    print('Male')
else:
    print('Error')
