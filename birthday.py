from datetime import datetime

def birthday():
    person_bd = input("Data de nascimento?")
    databd = datetime.strptime(person_bd, '%d/%m/%Y').date()
    dnow = datetime.date(datetime.now())
    data_in_days = (dnow - databd).days
    data_in_months = data_in_days / 30
    data_in_weeks = data_in_days / 7
    data_in_years = data_in_days / 365

    print(f'Anos desde o nascimento:    {int(data_in_years)}')
    print(f'Meses desde o nascimento:   {int(data_in_months)}')
    print(f'dias desde o nascimento:    {int(data_in_days)}')
    print(f'Semanas desde o nascimento: {int(data_in_weeks)}')


if __name__ == '__main__':
    birthday()



###########################
# Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: 
# a) a idade dessa pessoa em anos; 
# b) a idade dessa pessoa em meses; 
# c) a idade dessa pessoa em dias;
# d) a idade dessa pessoa em semanas
############################





