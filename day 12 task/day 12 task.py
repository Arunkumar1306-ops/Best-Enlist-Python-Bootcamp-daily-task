file=open(r"30days_30hours_fileoperation.txt","w+") 
file.write("I've completed 10 days successfully")
file.close()
file2=open(r"30days_30hours_fileoperation.txt","a+")
file2.writelines(" Best enlist")
print(file2.read())
file2.close()