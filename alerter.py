#beginning of code from Freenove tutorial
import RPi.GPIO as GPIO 
import time 
import math 
 
buzzerPin= 17
buttonPin = 18
 
def setup(): 
 global p  
 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(buzzerPin, GPIO.OUT)
 GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
mode, and pull up to HIGH level, 3.3V 
 p = GPIO.PWM(buzzerPin, 1)  
 p.start(0); 
  
def loop(): 
 while True: 
  if GPIO.input(buttonPin)==GPIO.LOW: 
   alertor() 
   print ('alertor turned on >>> ') 
  else : 
   stopAlertor() 
   print ('alertor turned off <<<') 
def alertor(): 
 p.start(50) 
 for x in range(0,361):
  sinVal = math.sin(x * (math.pi / 180.0))
  toneVal = 2000 + sinVal * 500
  p.ChangeFrequency(toneVal)
  time.sleep(0.001) 
   
def stopAlertor(): 
  p.stop() 
    
def destroy(): 
 GPIO.output(buzzerPin, GPIO.LOW)
 GPIO.cleanup()
 
if __name__ == '__main__':
 print ('Program is starting...') 
 setup() 
 try: 
  loop() 
 except KeyboardInterrupt:
  destroy() 
  #end of code from Freenove tutorial
