import speech_recognition as sr
import pyttsx3
import math

print("Say ADD to perform addition")
print("Say SUBTRACT to perform subtraction")
print("Say MULTIPLY to perform multiplication")
print("Say DIVIDE to perform division")
print("Say POWER to perform a number raised to another number function")
print("Say SQUARE to perform number raised to power 2")
print("Say SIN THETA to perform sin of an angle")
print("Say COS THETA to perform cos of an angle")
print("Say TAN THETA to perform tan of an angle")
print("Say LOG to perform log of a number(base e)")
print("Say LOG BASE 10 to perform log of a number(base 10)")
print("Say LOG BASE NUMBER to perform log of a number(base any desired number)")
print("Say SQUARE ROOT to perform square root of a given number")
print("Say SIN INVERSE THETA to perform sin^-1 of an angle")
print("Say COS INVERSE THETA to perform cos^-1 of an angle")
print("Say TAN INVERSE THETA to perform tan^-1 of an angle")
print("Say E RAISED TO POWER to perform e raised to power any number function")
print("Say FACTORIAL to perform factorial of a number")


r = sr.Recognizer()
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            MyText = r.recognize_google(audio,language="en-in")
            MyText=MyText.lower()
            print(MyText)
            

if(MyText=='ad'):
    print("Enter first number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
    print("Enter second number:")
    with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            num2 = int(r.recognize_google(audio2))
            print(num2)
            result=num1+num2
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='subtract'):
    print("Enter first number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
    print("Enter second number:")
    with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            num2 = int(r.recognize_google(audio2))
            print(num2)
            result=num1-num2
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='multiply'):
    print("Enter first number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
    print("Enter second number:")
    with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            num2 = int(r.recognize_google(audio2))
            print(num2)
            result=num1*num2
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='divide'):
    print("Enter first number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
    print("Enter second number:")
    with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            num2 = int(r.recognize_google(audio2))
            print(num2)
            result=num1/num2
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='power'):
    print("Enter first number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
    print("Enter second number:")
    with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            num2 = int(r.recognize_google(audio2))
            print(num2)
            result=pow(num1,num2)
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='square'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            result=pow(num1,2)
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='sin theta'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            result=math.sin(math.radians(num1))
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='cos theta'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            result=math.cos(math.radians(num1))
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='tan theta'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            result=math.tan(math.radians(num1))
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='log'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            result=math.log(num1)
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='log base 10'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            result=math.log(num1,10)
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='log base number'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
    print("Enter the base:")
    with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            num2 = int(r.recognize_google(audio2))
            print(num2)
            result=math.log(num1,num2)
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='square root'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = float(r.recognize_google(audio1))
            print(num1)
            result=math.sqrt(num1)
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='sin inverse theta'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            result=math.asin(math.radians(num1))
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='cos inverse theta'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            result=math.acos(math.radians(num1))
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='tan inverse theta'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            result=math.atan(math.radians(num1))
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='e raised to power'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            e = 2.718281828459045
            result=math.pow(e,num1)
            SpeakText("Result is")
            SpeakText(result)
            print(result)
elif(MyText=='factorial'):
    print("Enter the number:")
    with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.2)
            audio1 = r.listen(source1)
            num1 = int(r.recognize_google(audio1))
            print(num1)
            result=math.factorial(num1)
            SpeakText("Result is")
            SpeakText(result)
            print(result)
else:
    SpeakText("I am Sorry I did not understand it. Can you please repeat it?")





