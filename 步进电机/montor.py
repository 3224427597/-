import time#引用时间
import RPi.GPIO as GPIO#引用树莓派引脚
IN1=17
IN2=22
IN3=23
IN4=24

GPIO.setmode(GPIO.BCM)#设置GPIO引脚的模式
GPIO.setwarnings(False)#移除警告

pins=(17,22,23,24)
GPIO.setup(pins,GPIO.OUT)

#GPIO.setup(IN1,GPIO.OUT)#设置17引脚为输出引脚
#GPIO.setup(IN2,GPIO.OUT)
#GPIO.setup(IN3,GPIO.OUT)
#GPIO.setup(IN4,GPIO.OUT)

def setStep(h1,h2,h3,h4):#定义函数setStep
    GPIO.output(IN1,h1)
    GPIO.output(IN2,h2)
    GPIO.output(IN3,h3)
    GPIO.output(IN4,h4)
    
delay=0.003
steps=510

for i in range(0,steps):
    setStep(1,0,0,0)
    time.sleep(delay)
    setStep(0,1,0,0)
    time.sleep(delay)
    setStep(0,0,1,0)
    time.sleep(delay)
    setStep(0,0,0,1)
    time.sleep(delay)
    
setStep(0,0,0,0)
time.sleep(3)
GPIO.cleanup()#清理释放