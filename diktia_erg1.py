import numpy as np
import os

os.system('clear')

#Metatropi thesi stathmis se binary
def closest_value(input_list, input_value):
 
  arr = np.asarray(input_list)
 
  i = (np.abs(arr - input_value)).argmin()
 
  return "{0:b}".format(int(i))

#Omiomorfi katanomi tou pediou orismou
def kataniomi(stathmes, poso_diaxorismou, kato_pedio_orismou):

    diaxorismos = 0.0
    diaxorismos_lst = list()

    for i in range(stathmes):
        if(i==0):
            diaxorismos= kato_pedio_orismou
        else:
            diaxorismos = diaxorismos + poso_diaxorismou
        diaxorismos_lst.insert(i, diaxorismos)

    return diaxorismos_lst

#Entopismos prisiesteris stathmis
def entopismos(num_list, diaxorismos_lst):
    
    val_list = list()

    for i in range(len(num_list)):
        val=closest_value(diaxorismos_lst,num_list[i])
        val_list.insert(i, val)

    return val_list

def main():
    #isagogi pedio orismou analogikou simatos
    atmp = False
    while (atmp == False):
        #Elegxos an to pano akro einai megalitero apo to kato akro 
        kato_pedio_orismou = float(input('Bale to kato pedio orismou:\n'))
        pano_pedio_orismou = float(input('Bale to pano pedio orismou:\n'))
        if (pano_pedio_orismou > kato_pedio_orismou ):
            atmp = True
        else:
            print('Lathos Eisagogi (kato pedio orismou < pano pedio orismou)\t')

    #isagogi Stathmon
    stathmes = int(input('Bale to Stathmes kvatnisis :\n'))

    num_list = list()

    num = int(input('Bale ton arithmo ton metriseon:\n'))

    for i in range(num) :
        btmp = False
        while (btmp == False):
            #isagogi metrseon kai elegxos an vriskontai mesa sto pedio orismou
            n = float(input('Bale tis metrisis (<= Tou ano akrou Orismou):\n'))
            if (n <=pano_pedio_orismou and n >= kato_pedio_orismou ):
                btmp = True
            else:
                print('Lathos Eisagogi\t')

        num_list.append(n)
     
    poso_diaxorismou = (pano_pedio_orismou - kato_pedio_orismou) /(stathmes-1)

    diaxorismos_lst=kataniomi(stathmes, poso_diaxorismou, kato_pedio_orismou)
     
    val_list = entopismos(num_list, diaxorismos_lst)

    os.system('clear')
    print('Stathmi Kvant. \tMetrisi \tPlisiesteri Stathmi \tKodikos(Binary)')

    for i in range(len(val_list)):
        print ("{}  \t\t{} \t\t{} \t\t\t{}".format(i, num_list[i], int(val_list[i], 2), val_list[i]))


main()

