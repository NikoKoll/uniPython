
def no_frag(meso_megethos, arithmos_komvon, bit_rateR):

    print((arithmos_komvon+1)*(meso_megethos/bit_rateR))

def frag(meso_megethos, arithmos_komvon, bit_rateR, megethosF, h):

    g = meso_megethos/megethosF 
    delay_info_leaves_source = (g*(megethosF+h)/bit_rateR)
    delay_last_fragment_reaches_dest = arithmos_komvon*((megethosF+h)/bit_rateR)
    print(delay_info_leaves_source+delay_last_fragment_reaches_dest)

def main():

    while (True):
        try:
            meso_megethos = float(input('Bale to meso megethos tou paketou L bits:\n'))
            if(meso_megethos >0):
                break
        except ValueError:
            print ("Not a float")
    
    while (True):
        try:
            arithmos_komvon = float(input('Bale ton arithmo ton komvon metaxi ton T1 kai T2:\n'))
            if(arithmos_komvon >0):
                break
        except ValueError:
            print ("Not a float")
    
    while (True):
        try:
            bit_rateR = float(input('Bale to bit rate R:\n'))
            if(bit_rateR >0):
                break
        except ValueError:
            print ("Not a float")
    
    while (True):
        try:
            megethosF = float(input('Bale to megethos F:\n'))
            if(megethosF >0):
                break
        except ValueError:
            print ("Not a float")

    while (True):
        try:
            h = float(input('Bale thn epikefalida h:\n'))
            if(h >=0):
                break
        except ValueError:
            print ("Not a float")
    
    print('Kathisterisi xwirs fragmentation')
    no_frag(meso_megethos, arithmos_komvon, bit_rateR)
 
    print('Kathisterisi me fragmentation')
    frag(meso_megethos, arithmos_komvon, bit_rateR, megethosF, h)

main()