import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

LED = 7
Trig = 36 
Echo = 38 

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(Trig,GPIO.OUT) 
GPIO.setup(Echo,GPIO.IN) 
GPIO.output(Trig, False) 

val = GPIO.PWM(LED, 100) 
val.start(0); 

try:
    while True:
        GPIO.output(Trig, True)
        time.sleep(0.0001)
        GPIO.output(Trig, False)
        
        
        while GPIO.input(Echo)==0: 
            start_pulse = time.time()
         
        while GPIO.input(Echo)==1:
            stop_pulse = time.time()

        total_time = stop_pulse - start_pulse
        
        dist = round(((total_time * 34000) / 2 ), 2)

        print ("Distance:",dist,"cm")

        if dist<=50: 
            for i in range(50,101,10): 
                val.ChangeDutyCycle(x) 
                time.sleep(0.1)
                
        elif dist>50:
            for i in range(50,-1,-10):  
                val.ChangeDutyCycle(x)
                time.sleep(0.1)

except KeyboardInterrupt:
    val.stop()
    GPIO.cleanup()
