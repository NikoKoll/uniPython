
import os

os.system('clear')

#vriskei to r to opoio einai to apoetoymeno bit rate toy syndesmoy
def delay_k1_k2(l, d_max, prop):

	return (l*8000000)/(d_max*1000000) - (prop/1000)

#vriskei ton arithmo ton bits gia to xroniko diastima metaxi [t1,t2]
def tb_t1_t2(l, r, prop, t1, t2):

	tb1 = (r/1000000)+(prop/1000)

	return (t2-tb1)/(r/1000000) - (t1-tb1)/(r/1000000) 

def main():

	tmp = False
	while (tmp == False):
		#isagogi metavliotn kai elegxos an vriskontai mesa sto pedio orismou
		l = int(input('Bale to meso megethos packetou(Mbytes):\n'))
		d_max = float(input('Bale tin megisti apodekti kathisterisi(sec):\n'))
		prop = int(input('Bale tin mkathisterisi diadosis(msec):\n'))
		t1 = float(input('arxikos xronos diastimatos [t1,t2]:\n'))
		t2 = float(input('telikos xronos diastimatos [t1,t2]:\n'))
		if (d_max > (prop/1000) and d_max>0 and prop>0 and l>0 and t2<=d_max and t1>=0 and t1<=t2):
			tmp = True
		else:
			print('Lathos Eisagogi\t')

	r = delay_k1_k2(l, d_max, prop)

	tb = tb_t1_t2(l, r, prop, t1, t2)

	os.system('clear')

	print ('To apetoumeno bit rate meatxi K1 kai K2 einai: {}\n'.format(r))
	print ('O arithmos ton bits metaxi t1 kai t2 einai: {}\n'.format(tb))

main()
