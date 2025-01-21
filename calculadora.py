nome = input('Digite seu nome: ');
peso = float(input('Digite seu Peso: '));
altura = float(input('Digite sua altura: ')); 

altpeso = peso / (altura ** 2);
altpesofor = round(altpeso, 1);

if altpesofor <= 18.5:
    print('Opa ' + nome + ' seu IMC é '+ str(altpesofor) + ', você está abaixo do peso ideal');
    
elif altpesofor <= 24.9:
    print('Opa ' + nome + ' seu IMC é '+ str(altpesofor) + ', você está no peso ideal');
    
elif altpesofor <= 29.9:
    print('Opa ' + nome + ' seu IMC é '+ str(altpesofor) + ', você está acima do peso');

elif altpesofor <= 39.9:
    print('Opa ' + nome + ' seu IMC é '+ str(altpesofor) + ', você está com Obesidade Nível 1');

elif altpesofor >= 40:
    print('Opa ' + nome + ' seu IMC é '+ str(altpesofor) + ', você está com Obesidade Nível 2');
    
else:
    print('Possivelmente os valores estão incorretos.');