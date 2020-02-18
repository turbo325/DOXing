
# -----------------DOXing.py------------------------------------
# this is a doxing file ment to hold info on a person or compaey
# 2-17-20

# basic info
print ("Basic Info")

print ("NA If It Doesn't Apply")
	
FirstName = input ("\nWhat is there firstname?\n")
MiddleName = input ("\nWhat is there middle name?\n")	
Name = input ("\nWhat is the targets last name?\n")
Phone = input ("\nWhat is the targets Phone number?\n")
SSN = input ("\nwhat is there ssn?\n")
Race = input ("\nWhat is there race?\n")
Age = input ("\nwhat is there age?\n")
Dob = input ("\nWhat is there date of birth?\n")

# Locations

print ("\nLocation")

Country = input ("\nwhat country do they live?\n")
CurrenState = input ("\nWhat State do they live?\n")
City = input ("\nWhat City do they live?\n")
Zip = input ("\nWhat is there Zip-code?\n")
Street = input ("\nWhat is there street address?\n") 



# this writes to text file

doxprofile = input("\nGive the Dox File a Name, \nPreferably with Target's First and Last Name-Dox-Profile.txt\n\n>")
doxfile = open(doxprofile, 'w')

doxfile.write("\n---------------------------------->Basic Info<---------------------------------")
doxfile.write("\n")
doxfile.write("\t -> Firstname:" + FirstName)
doxfile.write("\n")
doxfile.write("\t -> MiddleName:"+ MiddleName)
doxfile.write("\n")
doxfile.write("\t-> Name:" + Name)
doxfile.write("\n")
doxfile.write("\t-> Phone:" + Phone)
doxfile.write("\n")
doxfile.write("\t -> SSN:" + SSN)
doxfile.write("\n")
doxfile.write("\t -> Race:"+ Race)
doxfile.write("\n")
doxfile.write("\t -> age:"+ Age)
doxfile.write("\n")
doxfile.write("\t -> Date of birth:" + Dob)

doxfile.write("\n------------------------------>Location<---------------------------------------\n")
doxfile.write("\t -> Country:" + Country)
doxfile.write("\n")
doxfile.write ("\t -> State:" + CurrenState)
doxfile.write("\n")
doxfile.write("\t -> City:" + City)
doxfile.write("\n")
doxfile.write("\t -> Zip:"+ Zip)
doxfile.write("\n")
doxfile.write






