from time import sleep
name=input("What is your name? ").upper()
print(f"{name},WELCOME TO CCHUB HEALTHCARE CENTRE")
sleep(2)
def diseases():
    print('''
Malaria
Common cold
Cholera
Diarrhea
HIV/AIDS
Yellow fever
Dengue fever
Pneumonia
Polio
Ebola
Meningitis
Tuberculosis
              ''')
diseases()    
sleep(5)
disease=input("What disease would you like to learn about today: ").lower()
def malaria():
    print('''
Malaria is  the greatest threat to Nigerians. Each year, the death rate from malaria is 20% of the total number of people who died due to common diseases.
It is caused by intracellular parasites - plasmodia, the most dangerous of them leads to tropical malaria.
Infection occurs as a result of a mosquito bite. The pathogen is contained in the saliva of the mosquito.
The symptom is usually fever, chills, headache, and weakness. For tropical malaria, a fatal outcome is possible without timely treatment.
To protect yourself from mosquito bites: make sure your windows and doors are fortified with nets, apply repellents and fumigate as often as possible.
You can also take special anti malarial medicines(coartem).Thanks to the efforts made to eradicate this disease,
the rate of new cases of malaria in Nigeria has decreased.
          ''')
def yellow():
    print('''
Yellow fever is caused by the virus of the Flavivirus genus. It is carried by special tropical mosquitoes.
When the mosquito bites a person, the virus penetrates the skin and settles in the lymph nodes.
After 3-6 days, the viruses are released into the blood, and the person falls ill.
He or she will have a fever, headache, and a reddish rash will appear on the body. In half the cases, it is impossible to save the patient.
Getting a vaccination against Yellow fever is necessary. Once this is done, immunity to the disease can last ten years.
          ''')
def dengue():
    print('''
Dengue fever is an acute transmissible viral disease. Its symptoms are fever,severe headaches,pain behind the eyes,severe joint and muscle pain,
fatigue,vomiting and even skin rash which appears two to five days after the onset of fever. In some cases, Dengue fever develops into a hemorrhagic condition.
Although there is still no way to cure Dengue fever and no vaccine against it, it is not life-threatening. A tropical hemorrhagic fever may be fatal.
It is an acute form a Dengue fever, causing severe bleeding and affects children and young people.
          ''')
def pneumonia():
    print('''
In Nigeria, respiratory diseases can come in form of pneumonia, for example, and lower respiratory tract infections.
They rank second on the list of deaths as a result of illness.Pneumonia develops, typically, as a complication from an acute respiratory viral infection.
This disease is detected by X-ray examination.Severe forms of pneumonia can lead to death. It is also especially dangerous for children.
          ''')
def cold():
    print('''
Common cold is a viral infection of your nose and throat(upper respiratory tract).It is usually harmless,although it might not feel that way.
Many types of viruse can cause a common cold. Children younger than 6 are at greatest risk of colds,
but healthy adults can also expect to have two or three colds annually.
Most people recover from a common cold in a week or 10 days. Symptoms might last longer in people who smoke. If symptoms don't improve, see your doctor.
It's symptoms are running nose,sore throat,cough,slight body aches.
          ''')
def cholera():
    print('''
Cholera is an infectious disease that causes severe watery diarrhea,which can lead to dehydration and even death if untreated.
It is caused by taking in contaminated food or water that has a bacterium called Vibrio cholerae.Cholera is common in places with poor sanitation,
crowding,war and farmine.Places like Africa,South Asia and Latin America.
It's symptoms are watery diarrhea,vomiting,rapid heart rate,low blood pressure,dry mouth.Cholera requires immediate treatment because it can cause
death within hours. You can protect yourself and your family by using only water that has been boiled, water that has been chemically disinfected or bottled water.
If watery diarrhea is developed,seek medical attention immediately.
          ''')
def hiv():
    print('''
HIV is a deadly disease that is found in Nigeria. It is the abbreviated form of the human immunodeficiency virus.
The virus causes damages to the immune system. When the virus enters the human body, it leads to AIDS after a while.
The symptoms are sore throat,prolonged fever,night sweats,tiredness,weight loss,mouth ulcers. AIDS is an incurable disease.
To date, only effective supportive therapy has been developed. But it can only prolong a patient’s life.
Therefore, the primary method of combating HIV / AIDS is a prevention of the infection altogether.
It can be prevented by avoiding casual sex and limiting your sex partners,safe blood tranfusion,regular checkups for sexually transmitted diseases(STD's)
          ''')
def diarrhea():
    print('''
Diarrhea is a dangerous and common disease.It is the second leading cause of death among children under the age of five.
It can last several days and can make the body deficient in water and salt which is very necessary for survival.
In the past, the main causes of death associated with diarrhea in most cases were dehydration and fluid loss.
Currently, an increasing proportion of all deaths associated with diarrhea occurs in other causes, such as septic bacterial infection.
The measures to prevent diarrhea include providing safe drinking water, awareness of improved sanitation and washing of hands with soap to help to reduce the risk
of the disease.Diarrhea is treated with oral rehydration salts (ORS) - a mixture of pure water, salt, and sugar.
It is a symptom of infection caused by a wide range of bacteria, viruses, and parasites.
Most of them are spread through contaminated water. Infections take place where there is a shortage of clean water for drinking, cooking, and personal hygiene.
          ''')
def polio():
    print('''
Polio, or poliomyelitis, is a crippling and potentially deadly infectious disease. It is caused by the poliovirus.
The virus spreads from person to person and can invade an infected person’s brain and spinal cord, causing paralysis (can’t move parts of the body).
Polio vaccine protects children by preparing their bodies to fight the polio virus.
Almost all children (99 children out of 100) who get all the recommended doses of vaccine will be protected from polio.
The vaccination has worked for the past ten years, and educational work has yielded positive results.
          ''')
def ebola():
    print('''
Ebola also known as ebola hemorrhagic fever is a viral infection. It causes fever, body aches, and diarrhea, and sometimes bleeding inside and outside the body.
As the virus spreads through the body, it damages the immune system and organs. Ultimately, it causes levels of blood-clotting cells to drop.
The symptoms are high fever,headache,joint and muscle aches,sore throat,weakness,stomach pain,lack of appetite.
There is no specific treatment for this disease. However, doctors can help the patient to fight infection with fluid infusions, oxygen masks,
blood transfusions and medications for supporting blood pressure.Regarding Ebola, Nigeria, together with the WHO,
has managed to control and stop the infection from spreading in 2014.
          ''')
def meningitis():
    print('''
Meningitis is a very dangerous disease if not treated in time.3.8% of the total death as a result of various diseases in Nigeria is due to meningitis.
It’s a serious but rare infection that affects the brain cell. It can lead to severe brain damage, and the absence of treatment in 50% of cases result in death.
It is mainly caused by viral and bacterial infection.It's symptoms include headache,fever,stiff neck,sensitivity to light,vomiting,numbness in the face.
The best ways to prevent it is getting adequate amount of rest,not smoking and also avoiding contact with sick people.
          ''')
def tuberculosis():
    print('''
Tuberculosis is a disease caused by bacteria called Mycobacterium tuberculosis.It usually affects the lungs,but sometimes,it affects other organs and systems.
Mycobacterium tuberculosis is transmitted by airborne elements if you are having a conversation or at the proximity of a coughing and sneezing patient.
Most often, after an infection with mycobacterium, the disease occurs in an asymptomatic, latent form (tubinfication).
But approximately one in ten cases of latent infection eventually becomes active.
The classic symptoms of pulmonary tuberculosis are prolonged cough with sputum,sometimes with hemoptysis appearing at later stages,fever,weakness,night sweats,
and significant weight loss.
          ''')

if disease=="malaria":
   malaria()
   sleep(25)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')  
if disease=="common cold":
   cold()
   sleep(20)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''') 
if disease=="cholera":
   cholera()
   sleep(23)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
if disease=="diarrhea":
   diarrhea()
   sleep(28)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
if disease=="hiv/aids":
   hiv()
   sleep(23)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
if disease=="yellow fever":
   yellow()
   sleep(20)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
if disease=="dengue fever":
   dengue()
   sleep(20)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
if disease=="pneumonia":
   pneumonia()
   sleep(18)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
if disease=="polio":
   polio()
   sleep(20)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
if disease=="ebola":
   ebola()
   sleep(20)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
if disease=="meningitis":
   meningitis()
   sleep(20)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
if disease=="tuberculosis":
   tuberculosis()
   sleep(23)
   print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
   

repeat=input("Would you like to learn about any other disease? ").lower()
while repeat=="yes":
      repeat=input("Would you like to learn about any other disease? ").lower()
      if repeat=="yes":
         disease2=input("Which other one will you like to learn? ")
         if disease2=="malaria":
            malaria()
            sleep(25)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')  
         if disease2=="common cold":
            cold()
            sleep(20)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''') 
         if disease2=="cholera":
            cholera()
            sleep(23)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
         if disease2=="diarrhea":
            diarrhea()
            sleep(28)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
         if disease2=="hiv/aids":
            hiv()
            sleep(23)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
         if disease2=="yellow fever":
            yellow()
            sleep(20)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
         if disease2=="dengue fever":
            dengue()
            sleep(20)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
         if disease2=="pneumonia":
            pneumonia()
            sleep(18)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
         if disease2=="polio":
            polio()
            sleep(20)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
         if disease2=="ebola":
            ebola()
            sleep(20)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
         if disease2=="meningitis":
            meningitis()
            sleep(20)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
         if disease2=="tuberculosis":
            tuberculosis()
            sleep(23)
            print('''
Now you know about these common and dangerous diseases. Follow the preventive measures, and vaccinate your children to avoid health issues in Nigeria.
As they say, God helps those who help themselves.''')
      elif repeat!="yes":
           print("Alright,Have a nice and safe day") 
    

   
    
    
    

          
    
