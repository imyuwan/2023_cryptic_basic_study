import random

permuted_sequence = [i for i in range(64)]

random.shuffle(permuted_sequence)

def IP(pt_64):
    ct_64 = ''
    for i in range(64):
        permutation_index = permuted_sequence[i]
        ct_64 += pt_64[permutation_index]
    return ct_64

def Inverse_IP(ct_64):
    dict_ct = {permuted_sequence[i] : list(ct_64)[i] for i in range(64)}
    pt_64 = ''
    for i in sorted(dict_ct):
        pt_64 += dict_ct.get(i)
    return pt_64

#Excution Example
'''
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?"
ct = IP(text)

print(permuted_sequence) 
print(ct)
print(Inverse_IP(ct))
'''