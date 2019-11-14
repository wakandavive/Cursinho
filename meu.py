def valida_cpf (cpf):

    cpf = cpf.replace('.','')
    cpf = cpf.replace('-','')

    if not cpf.isnumeric():
        return 'não contem numero'
    if len(cpf) != 11:
        return 'nao tem 11 digitos'
    else:
        return 'valido'
  



# testes

print(valida_cpf('123.456.789-00')) # true
print(valida_cpf('1')) #none
print(valida_cpf('rrrrrrrrr')) # none
print(valida_cpf('12345678900')) #none
print(valida_cpf('234543234567')) #true