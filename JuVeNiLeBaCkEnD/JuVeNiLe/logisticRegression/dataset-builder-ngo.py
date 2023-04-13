import pandas as pd ;
import random
from sklearn.utils import shuffle



col_names = ["criminal-record","lost-found","Hinduism","Islam","Christianity","Sikhism","Buddhism","Jainism" ,"Other religions","age"
		,"male","female","transgender","orphan","parents-earning","has-siblings","goes-to-school","child-labour","safe-area" ,"INC","BJP","CPI","NCP","BSP","AITC","output"]

my_df  = pd.DataFrame(columns = col_names)




def getRandomNumberInRange(min,max):
	return random.randint(min,max)



for i in range(0,1000):
	religion =  getRandomNumberInRange(0,6)
	age =  getRandomNumberInRange(0,1)
	criminal =  getRandomNumberInRange(0,1)
	gender = getRandomNumberInRange(0,2)
	party = getRandomNumberInRange(17,22)
	my_df.loc[i] = [
	criminal
	,0
	,1 if religion == 0 else 0 
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
	,criminal
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,1 if party == 17 else 0
	,1 if party == 18 else 0
	,1 if party == 19 else 0
	,1 if party == 20 else 0
	,1 if party == 21 else 0
	,1 if party == 22 else 0
	,1
	]
	
for i in range(999,2000):
	religion =  getRandomNumberInRange(0,6)
	age =  getRandomNumberInRange(0,1)
	gender = getRandomNumberInRange(0,2)
	party = getRandomNumberInRange(17,22)
	my_df.loc[i] = [0,0, 1 if religion == 0 else 0 
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
	,1
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,1 if party  == 17 else 0
	,1 if party  == 18 else 0
	,1 if party  == 19 else 0
	,1 if party  == 20 else 0
	,1 if party  == 21 else 0
	,1 if party  == 22 else 0
	,-1
	]


for i in range(1999,3000):
	religion =  getRandomNumberInRange(0,6)
	age =  getRandomNumberInRange(0,1)
	gender = getRandomNumberInRange(0,2)
	party = getRandomNumberInRange(17,22)
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
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,1 if party == 17 else 0
	,1 if party == 18 else 0
	,1 if party == 19 else 0
	,1 if party == 20 else 0
	,1 if party == 21 else 0
	,1 if party == 22 else 0
	,0
	]


for i in range(2999,3500):
	religion =  getRandomNumberInRange(0,6)
	age =  getRandomNumberInRange(0,1)
	gender = getRandomNumberInRange(0,2)
	party = getRandomNumberInRange(17,22)
	my_df.loc[i] = [getRandomNumberInRange(0,1),getRandomNumberInRange(0,1), 1 if religion == 0 else 0 
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
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,getRandomNumberInRange(0,1)
	,1 if party == 17 else 0
	,1 if party == 18 else 0
	,1 if party == 19 else 0
	,1 if party == 20 else 0
	,1 if party == 21 else 0
	,1 if party == 22 else 0
	,getRandomNumberInRange(0,1)
	]
my_df = shuffle(my_df)


print(my_df)

my_df.to_csv("normalized-data.csv", sep='\t')







