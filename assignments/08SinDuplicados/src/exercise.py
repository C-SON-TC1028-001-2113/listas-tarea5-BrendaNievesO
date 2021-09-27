def main():
    #escribe tu código abajo de esta línea
    a=int(input(''))
    lista=[]
    lista2=[]
    i=0
    if a>=1:
        while i<a and a>=1:
            i=i+1
            b=(input(''))
            lista.append(b)
            if (b in lista2)==False:
                lista2.append(b)
        print(lista)
        print(lista2)
    else:
        print("Error")
    
if __name__=='__main__':
    main()
