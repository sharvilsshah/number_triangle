def digit_count(digit):
    digit=str(digit)
    count=0
    for i in digit:
        count+=1
    return int(count)

    
    
def digit_diff(digit,digit_2):
    diff=digit_count(digit_2)-digit_count(digit)
    return diff
def row_converter(row):
	last=0
	for i in row:
		last+=1
	n=int(last/3)
	
	count=digit_count(last)
	space=count
	total=space*n
	difference=digit_diff(1,3*n)
	sec_space=1*space
	magic_row=[i for i in range(n)]
	magic_row.append('')
	last_row=''   
	magic_row[0]=' '*total+' '*difference+'1'
	total-=1
	
	for i in range(1,n):
		espace=0
		if digit_count(row[i])>1:
			espace=count-digit_count(row[i])-1
		magic_row[i]=' '*(total+espace)+str(row[i])+' '*(sec_space+count-digit_count(row[3*n-i]))+str(row[3*n-i])

		sec_space=sec_space+2*space
		total=total-1*count

	for i in range(n,2*n+1):
		last_row=last_row+' '*abs(count-digit_count(row[i]))+str(row[i])+' '*space
	magic_row[n]=last_row  
	return magic_row


def display(row):
    for i in row:
        print(i)

#main function    
n=int(input("Enter a no: "))
total=3*n
row=[i+1 for i in range(total)]
new_row=row_converter(row)
display(new_row)

