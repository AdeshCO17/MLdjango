from django.shortcuts import render
from joblib import load
import speech_recognition as sr
model =load('./savedModels/classifier.joblib')
print("printing.................")


#submit code by putting values.
def PredictModel(request):

    print("printing.................")
    if request.method =='POST':
        x1=request.POST['Pregnancies']
        x2=request.POST['Glucose']
        x3=request.POST['BloodPressure']
        x4=request.POST['SkinThickness']
        x5=request.POST['Insulin']
        x6=request.POST['BMI']
        x7=request.POST['DiabetesPedigreeFunction']
        x8=request.POST['Age']
        y_pred=model.predict([[x1,x2,x3,x4,x5,x6,x7,x8]])
        print("hello")
        if y_pred[0]==0:
            y_pred='Person not in diabetes'
        elif y_pred[0]==1:
            y_pred='Person is in diabetes'    
        return render(request,'Home.html',{'result1' : y_pred})
    return render(request,'Home.html')


#runable code
def take_voice_input():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 4000  # Adjust this value based on your microphone sensitivity
    recognizer.pause_threshold = 0.8  # Adjust this value to control the pause duration required to stop listening
    inputs = []

    for i in range(8):
        with sr.Microphone() as source:
            print(f"Speak input {i+1}:")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)

        try:
            text = recognizer.recognize_google(audio)
            inputs.append(text)
            print(f"You said: {text}")

            if text.lower() == "stop":
                print("Terminating input capture.")
                break
        except sr.UnknownValueError:
            print("Sorry, I could not understand your speech.")
     
        except sr.RequestError as e:
            print(f"Error: {str(e)}")
      

    return inputs

def invoke_function(request):


    if request.method == 'POST':
        try:
            inputs = take_voice_input()
            if len(inputs) >= 8:
                result0 = inputs[0]
                result1 = inputs[1]
                result2 = inputs[2]
                result3 = inputs[3]
                result4 = inputs[4]
                result5 = inputs[5]
                result6 = inputs[6]
                result7 = inputs[7]

                y_pred = model.predict([[result0, result1, result2, result3, result4, result5, result6, result7]])
                print("diabetes", y_pred)

                if y_pred[0] == 0:
                    y_pred = 'Person not in diabetes'
                elif y_pred[0] == 1:
                    y_pred = 'Person is in diabetes'

                return render(request, 'Home.html', {'result1': y_pred, 'value1': result0, 'value2': result1,
                                                     'value3': result2, 'value4': result3, 'value5': result4,
                                                     'value6': result5, 'value7': result6, 'value8': result7})
            else:
                error_message = f"Expected 8 inputs, but only received {len(inputs)}."
                return render(request, 'Home.html', {'error_message': error_message})
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'Home.html', {'error_message': error_message})

    return render(request, 'Home.html')
