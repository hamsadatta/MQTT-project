def c_broker():
		import os
		import time
		os.system('sudo /etc/init.d/mosquitto start')
		
		
def main1():
	 import paho.mqtt.client as mqtt
	 import paho.mqtt.subscribe as subscribe
	 import os
	 import time	
	 msg = subscribe.simple("test1", hostname="192.168.0.50")
	 tem=str(msg.payload)
	 return tem	
			
	   
		
def main2():
		  import paho.mqtt.client as mqtt
		  import paho.mqtt.subscribe as subscribe
		  import os
		  import time	
		  msg = subscribe.simple("test2",msg_count=1,hostname="192.168.0.50")
		  tem=str(msg.payload)
		  return tem
 		
			
		
		
		
		
def main3():
		import paho.mqtt.client as mqtt
		import paho.mqtt.subscribe as subscribe
		import os
		import time	
		msg = subscribe.simple("test3", hostname="192.168.0.50")
		tem=str(msg.payload)
		return tem


		
def main4():
			import paho.mqtt.client as mqtt
			import paho.mqtt.subscribe as subscribe
			import os
			import time	
			msg = subscribe.simple("test4", hostname="192.168.0.50")
			tem=str(msg.payload)
			return tem
		
def main5():
			import paho.mqtt.client as mqtt
			import paho.mqtt.subscribe as subscribe
			import os
			import time	
			msg = subscribe.simple("test5", hostname="192.168.0.50")
			tem=str(msg.payload)
			return tem		

def main6():
			import paho.mqtt.client as mqtt
			import paho.mqtt.publish as publish
			import os
			import time
			
			publish.single("test6", "1", hostname="192.168.0.50")	



def main7():
			import paho.mqtt.client as mqtt
			import paho.mqtt.subscribe as subscribe
			import os
			import time	
			msg = subscribe.simple("test7", hostname="192.168.0.50")
			tem=str(msg.payload)
			return tem

def main8():
			import paho.mqtt.client as mqtt
			import paho.mqtt.subscribe as subscribe
			import os
			import time	
			msg = subscribe.simple("test8", hostname="192.168.0.50")
			tem=str(msg.payload)
			return tem

def main9():
			import paho.mqtt.client as mqtt
			import paho.mqtt.subscribe as subscribe
			import os
			import time	
			msg = subscribe.simple("test9", hostname="192.168.0.50")
			tem=str(msg.payload)
			return tem

def main10():
			import paho.mqtt.client as mqtt
			import paho.mqtt.publish as publish
			import os
			import time
			
			publish.single("test6", "f", hostname="192.168.0.50")	


   
def finalop():
	while(1):
		tem=main1()
		return tem
