import random

pass_len = int(input("Enter the length of the password : "))
gen_pass = ""
chr_list_s = [chr(i) for i in range(97,123)]
chr_list_c = [chr(i) for i in range(65,81)]
chr_list_d = [str(i) for i in range(0,10)]
chr_list_spl = ["!","@","#","$","%","^","&","-","_","~"]
if pass_len>=4:
    gen_pass  = (random.choice(chr_list_s)+random.choice(chr_list_c)+random.choice(chr_list_d)+random.choice(chr_list_spl))
    final_list = chr_list_c+chr_list_d+chr_list_s+chr_list_spl
    for i in range(pass_len-4):
        gen_pass+=random.choice(final_list)
    temp_l = [i for i in gen_pass]
    random.shuffle(temp_l)
    gen_pass = "".join(temp_l)
    print("THE GENERATED PASSWORD IS : ",gen_pass)
else:
    print("PLEASE ENTER ATLEAST 4 CHARACTERS")