
#encoding:utf-8
import math
from itertools import groupby

def item_vector(packet): #試題對錯矩陣，對為1，錯為0
	
	item_type=[]
	correct_ans=[]
	stu_ans=[]
	item_vector=[]

	for value in packet['type']:
		item_type.append(value)
	
	for value in packet['correct_ans']:
		correct_ans.append(value)

	for value in packet['stu_ans']: 
		stu_ans.append(value)

	item_number=len(correct_ans)
	stu_number=len(stu_ans)

	for i in range(stu_number):
		item_vector.append([]) #new layer
		for j in range(item_number):
			if(item_type[j]=="selection"):#selection one
				if(stu_ans[i][j]==correct_ans[j]):
					item_vector[i].append(1) #correct one
				else:
					item_vector[i].append(0) #error one
			else:
				item_vector[i].append(1)#non-selection one
	
	return (item_vector,stu_number,item_number)
	

def correct_rate(item_vector,stu_number,item_number):		
	correct_rate=[]

	for i in range(item_number):
		correct_rate.append(0)


	for i in range(item_number):
		for j in range(stu_number):
			if(item_vector[j][i]==1):
				correct_rate[i]=correct_rate[i]+1

	for i in range(item_number):
		  correct_rate[i]=round(correct_rate[i]/float(stu_number),2)

	return correct_rate

def felt_difficulty(packet):
	felt_difficulty_temp=[]
	felt_difficulty=[0,0,0]
	for value in packet['felt_difficulty']:
		felt_difficulty_temp.append(value)

	for i in range(len(felt_difficulty_temp)):
		if(felt_difficulty_temp[i]=="1"):
			felt_difficulty[0]=felt_difficulty[0]+1
		elif(felt_difficulty_temp[i]=="2"):
			felt_difficulty[1]=felt_difficulty[1]+1
		elif(felt_difficulty_temp[i]=="3"):
			felt_difficulty[2]=felt_difficulty[2]+1

	return felt_difficulty

def memory_type_quantity(packet):
	memory_type_temp=[]
	memory_type=[0,0,0,0,0,0]
	for value in packet['level']:
		memory_type_temp.append(value)

	for i in range(len(memory_type_temp)):
		if(memory_type_temp[i]=="1"):
			memory_type[0]=memory_type[0]+1
		elif(memory_type_temp[i]=="2"):
			memory_type[1]=memory_type[1]+1
		elif(memory_type_temp[i]=="3"):
			memory_type[2]=memory_type[2]+1
		elif(memory_type_temp[i]=="4"):
			memory_type[3]=memory_type[3]+1
		elif(memory_type_temp[i]=="5"):
			memory_type[4]=memory_type[4]+1
		elif(memory_type_temp[i]=="6"):
			memory_type[5]=memory_type[5]+1

	return memory_type

def memory_correct_quantity(packet,correct_rate,memory_type):
	memory_type_temp=[]
	memory_correct_quantity=[0,0,0,0,0,0]
	for value in packet['level']:
		memory_type_temp.append(value)

	for i in range(len(memory_type_temp)):
		if(memory_type_temp[i]=="1"):
			memory_correct_quantity[0]=memory_correct_quantity[0]+correct_rate[i]
		elif(memory_type_temp[i]=="2"):
			memory_correct_quantity[1]=memory_correct_quantity[1]+correct_rate[i]
		elif(memory_type_temp[i]=="3"):
			memory_correct_quantity[2]=memory_correct_quantity[2]+correct_rate[i]
		elif(memory_type_temp[i]=="4"):
			memory_correct_quantity[3]=memory_correct_quantity[3]+correct_rate[i]
		elif(memory_type_temp[i]=="5"):
			memory_correct_quantity[4]=memory_correct_quantity[4]+correct_rate[i]
		elif(memory_type_temp[i]=="6"):
			memory_correct_quantity[5]=memory_correct_quantity[5]+correct_rate[i]

	for i in range(len(memory_correct_quantity)):
		if(memory_correct_quantity[i]!= 0):
			memory_correct_quantity[i]=round(memory_correct_quantity[i]/memory_type[i],2)		
		else:
			memory_correct_quantity[i]=memory_correct_quantity[i]

	return memory_correct_quantity

def memory_difficulty_combine(packet):
	memory_difficulty_combine=[]
	felt_difficulty=[]
	level=[]

	for i in range(18):
		memory_difficulty_combine.append(0)


	for value in packet['felt_difficulty']:
		felt_difficulty.append(value)

	for value in packet['level']:
		level.append(value)

	for i in range(len(felt_difficulty)):
		if(felt_difficulty[i]=="1")and(level[i]=="1"):
			memory_difficulty_combine[0]=memory_difficulty_combine[0]+1
		elif(felt_difficulty[i]=="1")and(level[i]=="2"):
			memory_difficulty_combine[1]=memory_difficulty_combine[1]+1
		elif(felt_difficulty[i]=="1")and(level[i]=="3"):
			memory_difficulty_combine[2]=memory_difficulty_combine[2]+1
		elif(felt_difficulty[i]=="1")and(level[i]=="4"):
			memory_difficulty_combine[3]=memory_difficulty_combine[3]+1
		elif(felt_difficulty[i]=="1")and(level[i]=="5"):
			memory_difficulty_combine[4]=memory_difficulty_combine[4]+1
		elif(felt_difficulty[i]=="1")and(level[i]=="6"):
			memory_difficulty_combine[5]=memory_difficulty_combine[5]+1
		elif(felt_difficulty[i]=="2")and(level[i]=="1"):
			memory_difficulty_combine[6]=memory_difficulty_combine[6]+1
		elif(felt_difficulty[i]=="2")and(level[i]=="2"):
			memory_difficulty_combine[7]=memory_difficulty_combine[7]+1
		elif(felt_difficulty[i]=="2")and(level[i]=="3"):
			memory_difficulty_combine[8]=memory_difficulty_combine[8]+1
		elif(felt_difficulty[i]=="2")and(level[i]=="4"):
			memory_difficulty_combine[9]=memory_difficulty_combine[9]+1
		elif(felt_difficulty[i]=="2")and(level[i]=="5"):
			memory_difficulty_combine[10]=memory_difficulty_combine[10]+1
		elif(felt_difficulty[i]=="2")and(level[i]=="6"):
			memory_difficulty_combine[11]=memory_difficulty_combine[11]+1
		elif(felt_difficulty[i]=="3")and(level[i]=="1"):
			memory_difficulty_combine[12]=memory_difficulty_combine[12]+1
		elif(felt_difficulty[i]=="3")and(level[i]=="2"):
			memory_difficulty_combine[13]=memory_difficulty_combine[13]+1
		elif(felt_difficulty[i]=="3")and(level[i]=="3"):
			memory_difficulty_combine[14]=memory_difficulty_combine[14]+1
		elif(felt_difficulty[i]=="3")and(level[i]=="4"):
			memory_difficulty_combine[15]=memory_difficulty_combine[15]+1
		elif(felt_difficulty[i]=="3")and(level[i]=="5"):
			memory_difficulty_combine[16]=memory_difficulty_combine[16]+1
		elif(felt_difficulty[i]=="3")and(level[i]=="6"):
			memory_difficulty_combine[17]=memory_difficulty_combine[17]+1
	
	return memory_difficulty_combine





def item_type(packet):
	item_type_temp=[]
	for value in packet['scope']:
		item_type_temp.append(value)

	item_type=sorted(dict.fromkeys(item_type_temp).keys())

	return item_type

def item_type_quantity(packet):
	item_type_quantity=[]
	item_type_temp=[]
	for value in packet['scope']:
		item_type_temp.append(value)

	item_type_quantity=[len(list(group)) for key, group in groupby(sorted(item_type_temp))]
	
	return item_type_quantity

def item_correct_quantity(packet,item_number,item_type,item_type_quantity,correct_rate):
	item_type_temp=[]
	item_correct_quantity=[]
	

	for i in range(len(item_type)):
		item_correct_quantity.append(0)

		
	for value in packet['scope']:
		item_type_temp.append(value)

		

	for i in range(len(item_type)):
		for j in range(item_number):
			if(item_type_temp[j]==item_type[i]):
				item_correct_quantity[i]=item_correct_quantity[i]+correct_rate[j]

	for i in range(len(item_type)):
		item_correct_quantity[i]=round(item_correct_quantity[i]/item_type_quantity[i],2)			
		
	return item_correct_quantity


def item_difficulty_combine(packet,item_type):
	item_difficulty_combine=[]
	item_type_temp=[]
	felt_difficulty=[]

	for i in range(len(item_type)*3):
		item_difficulty_combine.append(0)

	for value in packet['felt_difficulty']:
		felt_difficulty.append(value)

	for value in packet['scope']:
		item_type_temp.append(value)	

	for i in range(len(item_type)):
		for j in range(len(item_type_temp)):
			if(item_type_temp[j]==item_type[i]):
				if(felt_difficulty[j]=="1"):
					item_difficulty_combine[(i*3+0)]=item_difficulty_combine[(i*3+0)]+1
				elif(felt_difficulty[j]=="2"):
					item_difficulty_combine[(i*3+1)]=item_difficulty_combine[(i*3+1)]+1
				elif(felt_difficulty[j]=="3"):
					item_difficulty_combine[(i*3+2)]=item_difficulty_combine[(i*3+2)]+1			

	return item_difficulty_combine



def grade_find(packet,item_vector,item_number,stu_number):
	grade=[]
	stu_grade=[]

	for value in packet['grade']:
		grade.append(int(value))

	for i in range(stu_number):
		stu_grade.append(0)

	for i in range(stu_number):
		for j in range(item_number):
			stu_grade[i]=stu_grade[i]+item_vector[i][j]*grade[j]

	for i in range(stu_number):
		stu_grade[i]=stu_grade[i]*1000+i

	return sorted(stu_grade)

def PL_PH(stu_grade,stu_number,item_number,item_vector):
	P_number = int(math.floor(stu_number*0.27))
	pl_who=[]
	ph_who=[]

	pl=[]
	ph=[]

	for i in range(P_number):
		pl_who.append(stu_grade[i]%1000)
		ph_who.append(stu_grade[stu_number-1-i]%1000)

	for i in range(item_number):
		pl.append(0)
		ph.append(0)

	for i in range(item_number):
		for j in range(P_number):
			if(item_vector[pl_who[j]][i]==1):
				pl[i]=pl[i]+1

	for i in range(item_number):
		for j in range(P_number):
			if(item_vector[ph_who[j]][i]==1):
				ph[i]=ph[i]+1

	
	for i in range(item_number):
		pl[i]=round(pl[i]/float(P_number),2)
		ph[i]=round(ph[i]/float(P_number),2)		

	return (pl,ph)

def real_difficulty(pl,ph,item_number):
	real_difficulty_temp=[]
	real_difficulty=[]
	real_difficulty_quantity=[0,0,0]

	for i in range(item_number):
		real_difficulty_temp.append(round(float((pl[i]+ph[i])/2),2))

	for i in range(item_number):
		if(real_difficulty_temp[i]<0.3):
			real_difficulty.append(1)
		elif(real_difficulty_temp[i]>0.7):		
			real_difficulty.append(3)
		else:
			real_difficulty.append(2)

	for i in range(item_number):
		if(real_difficulty[i]==1):
			real_difficulty_quantity[0]=real_difficulty_quantity[0]+1
		elif(real_difficulty[i]==2):
			real_difficulty_quantity[1]=real_difficulty_quantity[1]+1
		elif(real_difficulty[i]==3):
			real_difficulty_quantity[2]=real_difficulty_quantity[2]+1

	return (real_difficulty_quantity,real_difficulty)

def discrimination(pl,ph,item_number):
	discrimination_temp=[]
	discrimination=[]

	for i in range(10):
		discrimination.append(0)

	for i in range(item_number):
		discrimination_temp.append(round(ph[i]-pl[i],2))

	for i in range(item_number):
		if(discrimination_temp[i]>= -1) and (discrimination_temp[i] < -0.8):
			discrimination[0]=discrimination[0]+1
		elif(discrimination_temp[i]>= -0.8) and (discrimination_temp[i] < -0.6):
			discrimination[1]=discrimination[1]+1
		elif(discrimination_temp[i]>= -0.6) and (discrimination_temp[i] < -0.4):
			discrimination[2]=discrimination[2]+1
		elif(discrimination_temp[i]>= -0.4) and (discrimination_temp[i] < -0.2):
			discrimination[3]=discrimination[3]+1
		elif(discrimination_temp[i]>= -0.2) and (discrimination_temp[i] < 0):
			discrimination[4]=discrimination[4]+1
		elif(discrimination_temp[i]>= 0) and (discrimination_temp[i] < 0.2):
			discrimination[5]=discrimination[5]+1
		elif(discrimination_temp[i]>= 0.2) and (discrimination_temp[i] < 0.4):
			discrimination[6]=discrimination[6]+1
		elif(discrimination_temp[i]>= 0.4) and (discrimination_temp[i] < 0.6):
			discrimination[7]=discrimination[7]+1
		elif(discrimination_temp[i]>= 0.6) and (discrimination_temp[i] < 0.8):
			discrimination[8]=discrimination[8]+1
		elif(discrimination_temp[i]>= 0.8) and (discrimination_temp[i] < 1):
			discrimination[9]=discrimination[9]+1
		

	return (discrimination,discrimination_temp)

def output(memory_type,felt_difficulty,memory_difficulty_combine,discrimination,discrimination_temp,real_difficulty_quantity,real_difficulty,memory_correct_quantity,item_correct_quantity,item_type,item_type_quantity,item_difficulty_combine,correct_rate):
	data={}
	data["memory_type_quantity"] = memory_type #每種記憶層次的數量，六大層次的個別數量，總共六個數值
	data["felt_difficult_type_quantity"]= felt_difficulty #自定義難度的數量，三個難度的數量，總共三個數值
	data["memory_difficulty_combiine"]= memory_difficulty_combine #每種記憶層次個別三種難度的數量，共18個數值
	data["discrimination"]= discrimination_temp #各題的鑑別度
	data["discrimination_quantity"]= discrimination #統計的鑑別度分佈，-1~1,0.2為間隔，共10個數據
	data["real_difficulty"]=real_difficulty #每題的實際難易度
	data["real_difficulty_quantity"]= real_difficulty_quantity #實際難易度的數量，分為難中易，共三個
	data["memory_correct_quantity"]=memory_type #各種記憶層次的答對率
	data["item_correct_quantity"]=item_correct_quantity #各種分年細目的答對率
	data["item_type"]= item_type #總共的分年細目種類
	data["item_type_quantity"]= item_type_quantity #各種分年細目的數量
	data["item_difficulty_combine"]=item_difficulty_combine #各種分年細目難易度的數量，總數=分年細目＊3
	data["correct_rate"]= correct_rate #每題的答對率

	return data

def output_before(memory_type,felt_difficulty,memory_difficulty_combine,item_difficulty_combine):
	data={}
	data["memory_type_quantity"]=memory_type
	data["felt_difficult_type_quantity"]=felt_difficulty
	data["memory_difficulty_combine"]=memory_difficulty_combine
	data["item_difficulty_combine"]=item_difficulty_combine

	return data

def output_after(memory_correct_quantity,felt_difficulty,real_difficulty,discrimination,item_type_quantity,item_correct_quantity):
	data={}
	data["memory_correct_quantity"]=memory_correct_quantity
	data["felt_difficult_quantity"]=felt_difficulty
	data["real_difficulty_quantity"]=real_difficulty
	data["discrimination"]=discrimination
	data["item_type_quantity"]=item_type_quantity
	data["item_correct_quantity"]=item_correct_quantity

	return data


def all(packet):
	(item_vector_t,stu_number,item_number)=item_vector(packet)
	correct_rate_t=correct_rate(item_vector_t,stu_number,item_number)
	felt_difficulty_t=felt_difficulty(packet)
	memory_type=memory_type_quantity(packet)
	memory_correct_quantity_t=memory_correct_quantity(packet,correct_rate_t,memory_type)
	memory_difficulty_combine_t=memory_difficulty_combine(packet)
	item_type_t=item_type(packet)
	item_type_quantity_t=item_type_quantity(packet)
	item_difficulty_combine_t=item_difficulty_combine(packet,item_type_t)
	item_correct_quantity_t=item_correct_quantity(packet,item_number,item_type_t,item_type_quantity_t,correct_rate_t)
	stu_grade=grade_find(packet,item_vector_t,item_number,stu_number)
	(pl,ph)=PL_PH(stu_grade,stu_number,item_number,item_vector_t)
	(real_difficulty_quantity,real_difficulty_t)=real_difficulty(pl,ph,item_number)
	(discrimination_t,discrimination_temp_t)=discrimination(pl,ph,item_number)
	packet_return=output(memory_type,felt_difficulty_t,memory_difficulty_combine_t,discrimination_t,discrimination_temp_t,real_difficulty_quantity,real_difficulty_t,memory_correct_quantity_t,item_correct_quantity_t,item_type_t,item_type_quantity_t,item_difficulty_combine_t,correct_rate_t)

	return packet_return

def before(packet):
	memory_type=memory_type_quantity(packet)
	felt_difficulty_t=felt_difficulty(packet)
	memory_difficulty_combine_t=memory_difficulty_combine(packet)
	item_type_t=item_type(packet)
	item_difficulty_combine_t=item_difficulty_combine(packet,item_type_t)
	packet_return=output_before(memory_type,felt_difficulty_t,memory_difficulty_combine_t,item_difficulty_combine_t)

	return packet_return

def after(packet):
	(item_vector_t,stu_number,item_number)=item_vector(packet)
	correct_rate_t=correct_rate(item_vector_t,stu_number,item_number)
	felt_difficulty_t=felt_difficulty(packet)
	memory_type=memory_type_quantity(packet)
	memory_correct_quantity_t=memory_correct_quantity(packet,correct_rate_t,memory_type)
	memory_difficulty_combine_t=memory_difficulty_combine(packet)
	item_type_t=item_type(packet)
	item_type_quantity_t=item_type_quantity(packet)
	item_difficulty_combine_t=item_difficulty_combine(packet,item_type_t)
	item_correct_quantity_t=item_correct_quantity(packet,item_number,item_type_t,item_type_quantity_t,correct_rate_t)
	stu_grade=grade_find(packet,item_vector_t,item_number,stu_number)
	(pl,ph)=PL_PH(stu_grade,stu_number,item_number,item_vector_t)
	(real_difficulty_quantity,real_difficulty_t)=real_difficulty(pl,ph,item_number)
	(discrimination_t,discrimination_temp_t)=discrimination(pl,ph,item_number)
	packet_return=output(memory_type,felt_difficulty_t,memory_difficulty_combine_t,discrimination_t,discrimination_temp_t,real_difficulty_quantity,real_difficulty_t,memory_correct_quantity_t,item_correct_quantity_t,item_type_t,item_type_quantity_t,item_difficulty_combine_t,correct_rate_t)

	return packet_return

if __name__ == '__main__':	
	packet_return=after(packet)
	print packet_return
