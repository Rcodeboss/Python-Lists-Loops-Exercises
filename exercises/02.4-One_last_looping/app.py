my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
my_sample_list[1] = 'Steven'
my_sample_list[10] = 'Pepe'
my_sample_list[0] = my_sample_list[2] + my_sample_list[4]

for x in range(len(my_sample_list) -1,-1,-1):
    print(my_sample_list[x])