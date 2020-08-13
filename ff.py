# st='aaabba'

# start=0
# end=len(st)-1
# cur_pos=start

# new_a=[]

# while start<=end:
#     if start==end:
#         new_a.append(st[start])
#         break
#     if st[cur_pos]!=st[cur_pos+1]:
#         new_a.append(st[cur_pos])
#         cur_pos+=1
#         start=cur_pos
#         continue
#     else:
#         count=0
#         while st[cur_pos]==st[cur_pos+1]:
#             count+=1
#             cur_pos+=1
#         if count>1:
#             cur_pos+=1
#             start=cur_pos
#         else:
#             new_a.append(st[cur_pos-1])
#             new_a.append(st[cur_pos])
#             cur_pos+=1
#             start=cur_pos
#             continue
# re=''
# for e in new_a:
#     re=re+e
# print(re)



N=input()
str_0='1011111'
str_1='0000011'
str_2='1110110'
str_3='1110011'
str_4='0101011'
str_5='1110101'
str_6='1111101'
str_7='1100011'
str_8='1111111'
str_9='1111011'

dic_r={'0':str_0,'1':str_1,'2':str_2,'3':str_3,'4':str_4,'5':str_5,'6':str_6,'7':str_7,'8':str_8,'9':str_9}

set_r={'',}
for key,value in dic_r.items():
    set_r.add(value)


str_n=str(N)
list_n=[]
for s in str_n:
    if str(s) in dic_r.keys():
        str_s=dic_r[str(s)]
        list_n.append(str_s)
for str_num in list_n:
    for i in range(7):
        if str_num[i]=='0':
            str_num[i]='1'
            break
    if str_num in set_r and str_num:



#print(list_n)