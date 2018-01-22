# This script is intended to reduce the time required in account creation for
# new employees by automating most of the creation and requiring the neccessary 
# inputs only once
# 
# Written for Python 2.7 and depends on the following:
#
# Use at your own risk, no liability assumed. Released under the MIT license.
# for more info see https://github.com/rmduddy/staffaccounts
import datetime

primaryemaildomain = "@primary.com"
secondaryemaildomain = "@secondary.com"

class Employee:
	
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		self.site = ""
		self.distributionlists = []
		self.schoologyrole = ""
	
	def primaryemail(self):
		primaryemail = "%s%s%s" % (
			self.firstname[:1], self.lastname, primaryemaildomain
			)
		return primaryemail.lower()
		
	def secondaryemail(self):
		secondaryemail = "%s%s%s" % (
			self.firstname, self.lastname, secondaryemaildomain
			)
		return secondaryemail.lower()
		
	def schoologyaccount(self):
		schoologyaccount = self.primaryemail()
		return schoologyaccount
		
	def password(self):
		date = datetime.datetime.now()
		date = date.strftime("%m%d%y")
		#Obiously this is not my password structure, be sure to create a good
		#standard or generate randomly
		password = "%s!%s!%s!" % (self.firstname[:1], self.lastname[:1], date)
		return password.lower()

def get_employee_info():
	firstname = raw_input("First name of new employee:")
	lastname = raw_input("Last name of new employee:")
	
	employee = Employee(firstname, lastname)
	
	print ("First name: %s" % employee.firstname)
	print ("Last name:  %s" % employee.lastname)
	print ("Primary:    %s" % employee.primaryemail())
	print ("Secondary:  %s" % employee.secondaryemail())
	print ("Schoology:  %s" % employee.schoologyaccount())
	print ("Password:   %s" % employee.password())
	return employee;
	
def main():
	get_employee_info()
	return;

main()
