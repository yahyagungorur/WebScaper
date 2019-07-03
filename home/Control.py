def Control(text,search_term):
    if(text.isspace()==True):#hepsi boşluktan oluşuyorsa...
        return " "
    elif(text[0]==" "):
        return text.strip()#eğer başında ve sonunda çok boşluk varsa..
    elif(text[len(text)-1]==" "):
        return text.strip()
    elif(len(text)<=len(search_term)+3):#eğer sadece aranan kelime kadarsa
        return " "                       #gerek yok yazdırmasına sanki
