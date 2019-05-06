
rows =0

with open('/Users/mgaikwad/MGwork/VM_Shared/Win10Pro/Work/test2.csv', mode ='r')  as my_new_file:
    for item in my_new_file:
        print(item)
        rows += 1

print(rows)

