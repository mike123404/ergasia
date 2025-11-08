#συναρτηση που μετραει τις λεξεις και τις αποθηκευει στο λεξικο words
def words_count(text):
    for word in text:
        if word not in words:
            words.update({word:1})
            #αν δεν βρεθει η λεξη την προσθετει στο λεξικο με τιμη 1( αφου ειναι πρωτη φορα που την βρισκει)
        else:
            words[word]+=1
            #αλλιως προσθετει 1 στον μετρητη της λεξης
#συναρτηση που μετραει τους χαρακτηρες και τους αποθηκευει στο λεξικο chars            
def chars_count(text):
    for word in text:
        for char in word:
            if char not in chars:                
                chars.update({char:1})
                #αν δεν βρεθει ο χαρακτηρας τον προσθετει στο λεξικο με τιμη 1( αφου ειναι πρωτη φορα που τον βρισκει)
            else:
                chars[char]+=1
                #αλλιως προσθετει 1 στον μετρητη της λεξης
#συναρτηση που αφαιρει ολους τους ειδικους χαρακτηρες απο το text
def rm_special_chars(f):
    cleantext=''
    for char in f:
        if char.isalpha() or char.isspace():
            cleantext+=char
    return cleantext
words={}#{λεξη : φορες που αναφερεται στο text} πχ {apple:3}
chars={}#{γραμμα : φορες που αναφερεται στο text} πχ {a:7}    
filename=input('give me filename')#αποθηκευει το ονομα του φακελου στη μεταβλητη filename
with open(filename,'r',encoding='utf-8') as f:#ανοιγουμε τον φακελο για διαβασμα με κωδικοποιηση utf-8
    text=f.read()#η μεταβλητη text εχει τα στοιχεια ολοκληρου του φακελου
    text=rm_special_chars(text)#εχουμε βγαλει τους ειδικους χαρακτηρες απο το text 
    text=text.lower().split()#κανουμε τα κεφαλαια γραμματα μικρα και διαχωριζουμε το text σε λεξεις
    words_count(text)#υπολογιζει ποσες φορες αναφερεται η καθε λεξη
    chars_count(text)#υπολογιζει ποσες φορες αναφερεται ο καθε χαρακτηρας
    
    '''
    #αποτελεσματα
    print("Words:", words)
    print("Chars:", chars)
    '''
