

from matplotlib import pyplot as plt
from ast import literal_eval
import re
fv_hash = {}
with open('field_value.txt') as all:
    for l in all:
        l = re.sub('\n','',l)
        a_split = l.split('=')
        val_conv = literal_eval(a_split[1])
        fv_hash[a_split[0]] = val_conv

#print("Age\tprincipal\ts_gain\t       c_gain\t self_curr_SSI\t   spouse_curr_SSI\t withdraw")
self_prev_SSI = 0
spouse_prev_SSI = 0
spouse_curr_SSI = 0
age_arr = []
principal_arr = []
withdraw_arr = []
stock_gain_arr = []
withdraw = fv_hash['withdraw']
 
for age in range(62,91):
    age_arr.append(age)
    if self_prev_SSI == 0:
        self_curr_SSI = fv_hash['initial_SSI']
    else:
        self_curr_SSI = self_prev_SSI + (self_prev_SSI * fv_hash['COLA'])
    if fv_hash['spouse_work_history'] == "y" and spouse_prev_SSI == 0:
        spouse_curr_SSI = fv_hash['initial_SSI']
    elif fv_hash['spouse_work_history'] == "y" and spouse_prev_SSI:
        spouse_curr_SSI = spouse_prev_SSI + (spouse_prev_SSI * fv_hash['COLA'])
    elif fv_hash['spouse_work_history'] == "n" and age < 65:
        spouse_curr_SSI = 0
    elif fv_hash['spouse_work_history'] == "n" and age >= 65:
        spouse_curr_SSI = self_curr_SSI / 2
    if age == 62:
        principal = (fv_hash['principal'] + self_curr_SSI + spouse_curr_SSI) - fv_hash['withdraw']
        s_gain = 00000
        c_gain = 00000
        principal_arr.append(principal)
        withdraw_arr.append(100000)
        stock_gain_arr.append(0)
        #cd_gain_arr.append(0)
    elif age > 62:
        withdraw = withdraw + (withdraw * 0.03)
        withdraw_arr.append(withdraw)
        s_wo_gain = prev_principal * fv_hash['stock_distribution']
        s_gain = s_wo_gain * fv_hash['stock_gain_rate']
        stock_gain_arr.append(s_gain)
        c_wo_gain = prev_principal * fv_hash['CD_distribution']
        c_gain = c_wo_gain * fv_hash['cd_gain_rate']
        principal = (s_wo_gain + c_wo_gain + s_gain + c_gain + self_curr_SSI + spouse_curr_SSI) - withdraw
        principal_arr.append(principal)
    self_prev_SSI = self_curr_SSI
    spouse_prev_SSI = spouse_curr_SSI
    prev_principal = principal
    prev_withdraw = withdraw
    
    #print("%d\t%7.2f\t%6.2f\t%8.2f\t%6.2f\t%6.2f\t%6.2f" % (age,principal,s_gain,c_gain,self_curr_SSI,spouse_curr_SSI,withdraw))
#plt.plot(age_arr,principal_arr,'b')
plt.title("Retirement Financial Estimation")
plt.xlabel('Age')
plt.ylabel('Stock gain $')
plt.plot(age_arr,withdraw_arr,'b',label='Yearly Withdraw')
plt.plot(age_arr,stock_gain_arr,'r',label='Stock gain')
plt.legend()
plt.grid('both')
plt.show()
