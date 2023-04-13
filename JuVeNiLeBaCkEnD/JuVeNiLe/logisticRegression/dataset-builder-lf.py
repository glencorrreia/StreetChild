import pandas as pd ;
import random



col_names = ["criminal-record","lost-found","Hinduism","Islam","Christianity","Sikhism","Buddhism","Jainism" ,"Other religions","age"
		,"male","female","transgender","orphan","parents-earning","has-siblings","goes-to-school","child-labour","safe-area" ,"INC","BJP","CPI","NCP","BSP","AITC","output"]

my_df  = pd.DataFrame(columns = col_names)




def getRandomNumberInRange(min,max):
	return random.randint(min,max)



for i in range(0,1000):
	religion =  getRandomNumberInRange(0,7)
	age =  getRandomNumberInRange(0,2)
	gender = getRandomNumberInRange(0,3)
	party = getRandomNumberInRange(0,6)
	my_df.loc[i] = [0,1, 1 if religion == 0 else 0 
	,1 if religion == 1 else 0 
	,1 if religion == 2 else 0 
	,1 if religion == 3 else 0 
	,1 if religion == 4 else 0 
	,1 if religion == 5 else 0 
	,1 if religion == 6 else 0
  	,age
	,1 if gender == 8 else 0
	,1 if gender == 9 else 0
	,1 if gender == 10 else 0
	,0
	,getRandomNumberInRange(0,2)
	,getRandomNumberInRange(0,2)
	,getRandomNumberInRange(0,2)
	,getRandomNumberInRange(0,2)
	,getRandomNumberInRange(0,2)
	,1 if gender == 17 else 0
	,1 if gender == 18 else 0
	,1 if gender == 19 else 0
	,1 if gender == 20 else 0
	,1 if gender == 21 else 0
	,1 if gender == 22 else 0
	,0
	]
	



print(my_df)



