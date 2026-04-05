# get total bill
# get % tip 
# get amount of that tip = bill_amt / tip *100
# get total amount to be paid = total_bill + tip_amt
# get no_to_split
# split amt = total_paid / no_of_split
#5% of 120 ==> 5/100  of 120 ==> 0.05*120==> 6

print ("Welcome to the tip calculator!")
bill_amt= int (input("What was the total Bill ? Rs"))
tip_percent=int (input("How much tip percentage would you like to give ? :"))
tip_amt = tip_percent/100 * bill_amt
total_bill = bill_amt + tip_amt
no_of_splits = int (input ("How many people to split the bill ? :"))
split_amt = total_bill/no_of_splits
print (f"Each person to pay : Rs {round(split_amt)}")
