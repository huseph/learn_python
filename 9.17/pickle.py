import pickle


f = open(r'C:\Users\huseph\Desktop\python\tmp\pickle.pkl', 'wb')
my_list = ['hello', 'world']

pickle.dump(my_list, f)

f.close()

fi = open(r'C:\Users\huseph\Desktop\python\tmp\pickle.pkl', 'rb')

my_list2 = pickle.load(fi)

print(my_list2)
