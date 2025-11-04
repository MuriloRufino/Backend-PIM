def cadastro(credencial, senha):
    with open('data.txt', 'a') as f:
        f.write(credencial + '\n' + senha + '\n')
        

def login(credencial, senha):
    with open('data.txt', 'r') as f:
        ctemp = f.readline().strip()
        while ctemp != "":
            stemp = f.readline().strip()
            if ctemp == credencial and stemp == senha:
                return True
            ctemp = f.readline().strip()
        return False






    

    
