from pyknow import *

class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Provide Details about your vehicle")
		yield Fact(action="vehicle")


	@Rule(Fact(action='vehicle'), NOT(Fact(sensor1=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(sensor1=input("Does the vehicle lose power? : ")))

	@Rule(Fact(action='vehicle'), NOT(Fact(sensor2=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(sensor2=input("Does the vehicle burst when accelerating? : ")))

	@Rule(Fact(action='vehicle'), NOT(Fact(sensor3=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(sensor3=input("Does it have a spark or short circuit making noise on spark plugs?: ")))

	@Rule(Fact(action='vehicle'), NOT(Fact(esensor1=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(esensor1=input("Does the motor have no power or the sound of the motor is irregular? : ")))

	@Rule(Fact(action='vehicle'), NOT(Fact(esensor2=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(esensor2=input("Does the infotainment system not work properly or shows irregular data? : ")))

	@Rule(Fact(action='vehicle'), NOT(Fact(throttle1=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(throttle1=input("Does the vehicle not move even after pusing the throttle hard ?: ")))
	 
	@Rule(Fact(action='vehicle'), NOT(Fact(throttle2=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(throttle2=input("Does the accelerator feel unusually heavy? : ")))
	
	@Rule(Fact(action='vehicle'), NOT(Fact(battery1=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(battery1=input("Does the battery drain faster than usual ?: ")))
	
	@Rule(Fact(action='vehicle'), NOT(Fact(battery2=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(battery2=input("Does it take longer to charge than usual? : ")))
	
	@Rule(Fact(action='vehicle'), NOT(Fact(battery3=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(battery3=input("Is the battery range less than usual? : ")))
	
	@Rule(Fact(action='vehicle'), NOT(Fact(battery4=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(battery4=input("Does the battery heat up quickly and shows indicator on dashboard? : ")))

	@Rule(Fact(action='vehicle'),Fact(sensor1="yes"),Fact(sensor2="yes"),Fact(sensor3="yes"),Fact(esensor1="no"),Fact(esensor2="no"),Fact(throttle1="no"),Fact(throttle2="no"),Fact(battery1="no"),Fact(battery2="no"),Fact(battery3="no"),Fact(battery4="no"))
	def disease_0(self):
		self.declare(Fact(vehicleType="Distribution Sensor Problem"))
  

	@Rule(Fact(action='vehicle'),Fact(sensor1="no"),Fact(sensor2="no"),Fact(sensor3="no"),Fact(esensor1="yes"),Fact(esensor2="yes"),Fact(throttle1="no"),Fact(throttle2="no"),Fact(battery1="no"),Fact(battery2="no"),Fact(battery3="no"),Fact(battery4="no"))
	def disease_1(self):
		self.declare(Fact(vehicleType="Electrical Sensor Problem"))

	@Rule(Fact(action='vehicle'),Fact(sensor1="no"),Fact(sensor2="no"),Fact(sensor3="no"),Fact(esensor1="no"),Fact(esensor2="no"),Fact(throttle1="yes"),Fact(throttle2="yes"),Fact(battery1="no"),Fact(battery2="no"),Fact(battery3="no"),Fact(battery4="no"))
	def disease_2(self):
		self.declare(Fact(vehicleType="Throttle Position Sensor Problem"))

	@Rule(Fact(action='vehicle'),Fact(sensor1="no"),Fact(sensor2="no"),Fact(sensor3="no"),Fact(esensor1="no"),Fact(esensor2="no"),Fact(throttle1="no"),Fact(throttle2="no"),Fact(battery1="yes"),Fact(battery2="yes"),Fact(battery3="yes"),Fact(battery4="yes"))
	def disease_3(self):
		self.declare(Fact(vehicleType="Battery Issue"))

	@Rule(Fact(action='vehicle'),Fact(vehicleType=MATCH.vehicleType),salience = -998)
	def vehicleTypefun(self, vehicleType):
		print("The Issue is with the  " + vehicleType)
		

	@Rule(Fact(action='vehicle'),
		  Fact(sensor1=MATCH.sensor1),
		  Fact(sensor2=MATCH.sensor2),
		  Fact(sensor3=MATCH.sensor3),
      Fact(esensor1=MATCH.esensor1),
      Fact(esensor2=MATCH.esensor2),
      Fact(throttle1=MATCH.throttle1),
      Fact(throttle2=MATCH.throttle2),
      Fact(battery1=MATCH.battery1),
      Fact(battery2=MATCH.battery2),
      Fact(battery3=MATCH.battery3),
      Fact(battery4=MATCH.battery4),NOT(Fact(vehicleType=MATCH.vehicleType)),salience = -999)

	def not_matched(self,sensor1,sensor2,sensor3,esensor1,esensor2,throttle1,throttle2,battery1,battery2,battery3,battery4):
		print("The error is unknown. Please recheck the inputs entered")



if __name__ == "__main__":
	engine = Greetings()
	while(1):
		engine.reset()  
		engine.run()  
		print("Try Again?")
		if input() == "no":
			exit()