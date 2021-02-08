pizzaria = [{'sabor':'calabresa', 'tamanho':'brotinho', 'massa': 'fina', 'preço': 5}]
def cadastrar_Produto():
    sabor = input('Digite o sabor da pizza: ')
    tamanho = input('Digite o tamanho da pizza: ')
    massa = input('Digite o tipo de massa da pizza: ')
    preço = float(input('Digite o preço da pizza: '))
    pizza = {'sabor':sabor, 'tamanho':tamanho, 'massa': massa, 'preço': preço}
    pizzaria.append (pizza)

def exibir_pizzaria():
    for pizza in pizzaria:
        print('Sabor:', pizza['sabor'])
        print('Tamanho:', pizza['tamanho'])
        print('Massa:', pizza['massa'])          
        print('Preço:', pizza['preço'])
        print()
        

def pesquisar_tamanho():
    tamanho = input('Digite o tamanho a ser pesquisado')
    for pizza in pizzaria:
        if tamanho == pizza['tamanho']:
            print('Sabor', pizza['sabor'])
            print('Tamanho', pizza['tamanho'])
            print('Massa', pizza['massa'])          
            print('Preço', pizza['preço'])
        
def pesquisar_massa():
    massa = input('Digite o tipo de massa ser pesquisada')
    for pizza in pizzaria:
        if massa == pizza['massa']:
            print('Sabor', pizza['sabor'])
            print('Tamanho', pizza['tamanho'])
            print('Massa', pizza['massa'])          
            print('Preço', pizza['preço'])
        
op = 1
while op!= 0:
    print("""
        0 - Sair
        1 - Cadastrar
        2 - Exibir
        3 - Pesquisar tamanho
        4 - Pesquisar por massa
        """)
    op=int(input(':>'))
    if op == 0:
        print ('Tchau')
    elif op == 1:
        cadastrar_Produto()
    elif op == 2:
        exibir_pizzaria()
    elif op == 3:
        pesquisar_tamanho()
    elif op == 4:
        pesquisar_massa()
        

        
        
    
    
    
    
        