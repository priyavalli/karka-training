#file=open("/home/valli/karka/karka.txt","r")
#print(file)
#data=file.read()
#print(data)

#for line in file:
    #print(line)

file=open("/home/valli/karka/karka.txt","w")
file.write("iam priya\n iam a softaware developer\n my age is 21")
file.write("iam a software dveloper")
file.write("my age is 21")
file.close()
#file=open("/home/valli/karka/karka.txt","r")
#data=file.read()
#print(data)
file=open("/home/valli/karka/karka.txt","a")
#file=open("/home/valli/karka/karka.txt","w")
file.write("iam vajeeha\n iam mr.bananas wife")
file.close()
file=open("/home/valli/karka/karka.txt","r")
data=file.read()
print(data)


#for line in file:
    #print(line.split())
