#Given a string, extract the email address from string typed in
#by a user. If there is no email address, print an appropriate
#error message. Other specifications:

#email = 'hello a@b this@example.where this@.is.fun'

def is_valid(email):
    for i in range(0, len(email)):
        if email[i] == '@' or email[i] == '.':
            pass
        elif not ord('a') <= ord(email[i]) <= ord('z'):
            return False
    at = email.find('@')
    dot = email.find('.')
    if email.count('.') > 1 or email.count('@') > 1:
        return False
    if at > dot:
        return False
    if at == -1 or dot == -1:
        return False
    if at == 0 or dot == 0:
        return False
    if at == len(email)-1 or dot == len(email)-1:
        return False
    return True

email = raw_input('Enter e-mail: ').strip()
temp = ''
for c in email:
    if c == ' ':
        if is_valid(temp):
            break
        else:
            temp = ''
    else:
        temp += c
if is_valid(temp):
    print 'Valid e-mail is: ' + temp
else:
    print 'No valid e-mail found'
