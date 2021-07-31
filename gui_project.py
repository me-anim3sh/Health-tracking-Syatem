from tkinter import *
from tkinter import Frame
from tkinter.ttk import Progressbar
from tkinter.font import Font
from time import sleep
from tkinter import ttk

def heart():
    tp = Toplevel(bg="black")
    tp.title("CUSTOM LOADER....")
    tp.attributes("-fullscreen", True)
    # tp.geometry("1920x1080+0+0")
    # loading text
    Label(tp, text="Loading....", font="Bahnschrift 15", bg="black", fg="#FF8D09").place(x=490, y=320)

    # loading block..
    for i in range(16):
        Label(tp, bg="#1F2732", width=2, height=1).place(x=(i + 22) * 22, y=350)
    for i in range(3):
        for j in range(16):
            # make block yellow
            Label(tp, bg="#ffbd09", width=2, height=1).place(x=(j + 22) * 22, y=350)
            sleep(0.06)
            tp.update_idletasks()
            # make block dark
            Label(tp, bg="#1F2732", width=2, height=1).place(x=(j + 22) * 22, y=350)
    else:
        top2 = Toplevel(bg="black")
        # top2.geometry("1900x1080+0+0")
        top2.attributes("-fullscreen", True)
        top2.title("HEART")
        # create main frame
        main_frame = Frame(top2)
        main_frame.pack(fill=BOTH, expand=1)
        # create a canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # add scrollbar
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        # configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        # create another frame inside the canvas
        second_frame = Frame(my_canvas)
        # add the new frame to a window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        label10 = Label(second_frame,
                    text="1.  Don't smoke or use tobacco \n \n One of the best things you can do for your heart is "
                         "to stop smoking or using smokeless tobacco. \n Even if you're not a smoker, "
                         "be sure to avoid secondhand smoke. \n Chemicals in tobacco can damage your heart and "
                         "blood vessels. Cigarette smoke reduces the oxygen in your blood, which increases \n"
                         "your blood pressure and heart rate because your heart has to work harder to supply "
                         "enough oxygen to your body and brain. \n There's good news though. Your risk of heart "
                         "disease starts to drop in as little as a day after quitting. \n After a year without "
                         "cigarettes, your risk of heart disease drops to about half that of a smoker. \n No "
                         "matter how long or how much you smoked, you'll start reaping rewards as soon as you "
                         "quit. \n\n 2. Get moving: Aim for at least 30 to 60 minutes of activity daily. \n\n Regular, "
                         "daily physical activity can lower your risk of heart disease.\n Physical activity "
                         "helps you control your weight and reduce your chances of developing other "
                         "conditions that may put a strain on your heart,\n such as high blood pressure, "
                         "high cholesterol and type 2 diabetes.\n If you haven't been active for a while, "
                         "you may need to slowly work your way up to these goals, but in general, you should "
                         "aim for at least: \n -150 minutes a week of moderate aerobic exercise, "
                         "such as walking at a brisk pace \n -75 minutes a week of vigorous aerobic activity, "
                         "such as running \n -Two or more strength training sessions a week \n Even shorter "
                         "bouts of activity offer heart benefits, so if you can't meet those guidelines, "
                         "don't give up.\n Just five minutes of moving can help, and activities such as "
                         "gardening, housekeeping, taking the stairs and walking the dog all count toward "
                         "your total.\n You don't have to exercise strenuously to achieve benefits, but you can "
                         "see bigger benefits by increasing the intensity, duration and frequency of your "
                         "workouts.\n\n 3. Eat a heart-healthy diet \n\n A healthy diet can help protect your heart, "
                         "improve your blood pressure and cholesterol,\n and reduce your risk of type 2 "
                         "diabetes.\n A heart-healthy eating plan includes: \n -Vegetables and fruits \n -Beans "
                         "or other legumes \n -Lean meats and fish \n -Low-fat or fat-free dairy foods \n "
                         "-Whole grains \n -Healthy fats, such as olive oil \n\n 4. Maintain a healthy weight "
                         "\n\n Being overweight — especially around your middle — increases your risk "
                         "of heart disease. \n Excess weight can lead to conditions that increase your "
                         "chances of developing heart disease \n — including high blood pressure, "
                         "high cholesterol and type 2 diabetes. \n One way to see if your weight is "
                         "healthy is to calculate your body mass index (BMI), \n which uses your height "
                         "and weight to determine whether you have a healthy or unhealthy percentage "
                         "of body fat. \n A BMI of 25 or higher is considered overweight and is "
                         "generally associated with higher cholesterol, \n higher blood pressure, "
                         "and an increased risk of heart disease and stroke. \n Even a small weight "
                         "loss can be beneficial. \n Reducing your weight by just 3% to 5% can help "
                         "decrease certain fats in your blood (triglycerides), \n lower your blood sugar "
                         "(glucose) and reduce your risk of type 2 diabetes. \n Losing even more helps "
                         "lower your blood pressure and blood cholesterol level. \n\n 5. Get good "
                         "quality sleep \n\n A lack of sleep can do more than leave you yawning; it "
                         "can harm your health. \n People who don't get enough sleep have a higher risk "
                         "of obesity, high blood pressure, heart attack, diabetes and depression. \n "
                         "Most adults need at least seven hours of sleep each night. \n Make sleep a "
                         "priority in your life. \n Set a sleep schedule and stick to it by going to bed "
                         "and waking up at the same times each day. \n Keep your bedroom dark and quiet, "
                         "so it's easier to sleep. \n If you feel like you've been getting enough "
                         "sleep but you're still tired throughout the day, \n ask your doctor if you "
                         "need to be evaluated for obstructive sleep apnea, \n a condition that can "
                         "increase your risk of heart disease. \n Signs of obstructive sleep apnea "
                         "include loud snoring, \n stopping breathing for short times during sleep and "
                         "waking up gasping for air. \n Treatments for obstructive sleep apnea may "
                         "include losing weight if you're overweight or using a continuous positive \n "
                         "airway pressure (CPAP) device that keeps your airway open while you sleep. "
                         "\n\n 6. Manage stress \n\n Some people cope with stress in unhealthy ways \n — "
                         "such as overeating, drinking or smoking. \n Finding alternative ways to manage "
                         "stress \n — such as physical activity, relaxation exercises or meditation \n — "
                         "can help improve your health. \n\n 7. Get regular health screenings \n\n "
                         "High blood pressure and high cholesterol can damage your heart and blood "
                         "vessels. \n But without testing for them, you probably won't know whether you "
                         "have these conditions. \n Regular screening can tell you what your numbers are "
                         "and whether you need to take action. \n\n 1) Blood pressure. Regular blood "
                         "pressure screenings usually start in childhood. \n You should have a blood "
                         "pressure test performed at least once every two years to screen for high \n "
                         "blood pressure as a risk factor for heart disease and stroke, \n starting at "
                         "age 18. \n If you're age 40 or older, or you're between the ages of 18 \n and "
                         "39 with a high risk of high blood pressure, \n ask your doctor for a blood "
                         "pressure reading every year. \n Optimal blood pressure is less than 120/80 "
                         "millimeters of mercury (mm Hg). \n\n 2) Cholesterol levels. Adults should "
                         "generally have their cholesterol \n measured at least once every five years "
                         "starting at age 18. \n Earlier testing may be recommended if you have other "
                         "risk factors, \n such as a family history of early-onset heart disease. \n\n "
                         "3) Diabetes screening. Since diabetes is a risk factor for developing heart "
                         "disease,\n you may want to consider being screened for diabetes. \n Talk to your "
                         "doctor about when you should have a fasting blood sugar test or hemoglobin \n"
                         "A1C test to check for diabetes. \n Depending on your risk factors, "
                         "such as being overweight or having a family history of diabetes, \n "
                         "your doctor may recommend early screening for diabetes. \n If your weight is "
                         "normal and you don't have other risk factors for type 2 diabetes, \n "
                         "the American Diabetes Association recommends starting screening at age 45, \n "
                         "and then retesting every three years. \n\n", font="Times 18", bg="black", fg="#FF8D09").pack()
        button7 = Button(top2, text = "BACK", command = second_page, bg = "black", fg = "#FF8D09", font = sec_font, width = 55).pack(fill = X, side  = LEFT)
        button8 = Button(top2, text = "QUIT", command = root.destroy, bg = "black", fg = "#FF8D09", font = sec_font, width = 55).pack(fill = X, side = RIGHT)


def covid():
    tp = Toplevel(bg="black")
    tp.title("CUSTOM LOADER....")
    tp.attributes("-fullscreen", True)
    # tp.geometry("1920x1080+0+0")
    # loading text
    Label(tp, text="Loading....", font="Bahnschrift 15", bg="black", fg="#FF8D09").place(x=490, y=320)

    # loading block..
    for i in range(16):
        Label(tp, bg="#1F2732", width=2, height=1).place(x=(i + 22) * 22, y=350)

    for i in range(3):
        for j in range(16):
            # make block yellow
            Label(tp, bg="#ffbd09", width=2, height=1).place(x=(j + 22) * 22, y=350)
            sleep(0.06)
            tp.update_idletasks()
            # make block dark
            Label(tp, bg="#1F2732", width=2, height=1).place(x=(j + 22) * 22, y=350)
    else:
        top3 = Toplevel(bg="black")
        top3.attributes("-fullscreen", True)
        # top3.geometry("1920x1080+0+0")
        top3.title("COVID-19")
        main_frame1 = Frame(top3)
        main_frame1.pack(fill=BOTH, expand=1)
        # create a canvas
        my_canvas1 = Canvas(main_frame1)
        my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)
        # add scrollbar
        my_scroll = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
        my_scroll.pack(side=RIGHT, fill=Y)
        # configure the canvas
        my_canvas1.configure(yscrollcommand=my_scroll.set)
        my_canvas1.bind('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))
        # create another frame inside the canvas
        second_frame1 = Frame(my_canvas1)
        # add the new frame to a window in the canvas
        my_canvas1.create_window((0, 0), window=second_frame1, anchor="center")
        label11 = Label(second_frame1, text="1) Wash your hands often \n\n Wash your hand often with soap and water for at "
                                        "least 20 seconds especially after you have been in a public place,  "
                                        "or after blowing your nose, coughing, or \n sneezing. It’s especially important "
                                        "to wash: \n -Before eating or preparing food \n -Before touching your face \n "
                                        "-After using the restroom \n -After blowing your nose, coughing, or sneezing \n "
                                        "-After handling your mask \n -After changing a diaper \n -After caring for someone "
                                        "sick \n -After touching animals or pets \n If soap and water are not readily "
                                        "available, use a hand sanitizer that contains at least 60% alcohol. \n Cover all "
                                        "surfaces of your hands and rub them together until they feel dry. \n Avoid "
                                        "touching your eyes, \n nose, and mouth with unwashed hands. \n\n 2) Avoid close "
                                        "contact \n\n Inside your home: Avoid close contact with people who are "
                                        "sick. \n -If possible, maintain 6 feet between the person who is sick and "
                                        "other household members. \n Outside your home: Put 6 feet of distance "
                                        "between yourself and people who don’t live in your household. \n -Remember "
                                        "that some people without symptoms may be able to spread virus. \n -Stay "
                                        "atleast 6 feet from other people \n -Keeping distance from others is "
                                        "especially important for people who are at high risk of getting very sick "
                                        "\n\n 3) Cover your mouth and nose with a mask when around others \n\n You "
                                        "could spread COVID-19 to others even if you do not feel sick. \n The mask "
                                        "is meant to protect other people in case you are infected. \n Everyone "
                                        "should wear a mask in public settings and when \n around people who don’t "
                                        "live in your household, \n especially when other social distancing measures "
                                        "are difficult to maintain. \n Masks should not be placed on young children "
                                        "under age 2, \n  anyone who has trouble breathing, or is unconscious, \n  "
                                        "incapacitated or otherwise unable to remove the mask without assistance. "
                                        "\n Do NOT use a mask meant for a healthcare worker. \n Currently, "
                                        "surgical masks and N95 respirators are critical supplies that should be \n "
                                        "reserved for healthcare workers and other first responders. \n Continue to "
                                        "keep about 6 feet between yourself and others. \n The mask is not a "
                                        "substitute for social distancing. \n\n  4)Cover coughs and sneezes \n\n "
                                        "Always cover your mouth and nose with a tissue when you cough or sneeze or \n "
                                        "use the inside of your elbow and do not spit. \n Throw used tissues in the "
                                        "trash. \n Immediately wash your hands with soap and water for at least 20 "
                                        "seconds. \n If soap and water are not readily available, \n clean your hands "
                                        "with a hand sanitizer that contains at least 60% alcohol. \n\n 5) Clean "
                                        "and disinfect \n\n Clean AND disinfect frequently touched surfaces daily.\n "
                                        "This includes tables, doorknobs, light switches, countertops, handles,\n "
                                        "desks, phones, keyboards, toilets, faucets, and sinks. \n If surfaces are "
                                        "dirty, clean them.\n Use detergent or soap and water prior to disinfection. "
                                        "\n If surfaces are dirty, clean them.\n Use detergent or soap and water "
                                        "prior to disinfection. \n\n 6) Monitor Your Health Daily \n\n Be alert for "
                                        "symptoms.\n Watch for fever, cough, shortness of breath, or other symptoms "
                                        "of COVID-19. \n Especially important if you are running essential errands,\n "
                                        "going into the office or workplace, and in settings where it may be \n "
                                        "difficult to keep a physical distance of 6 feet. \n Take your temperature "
                                        "if symptoms develop \n Don’t take your temperature within 30 minutes of "
                                        "exercising or after taking medications that \n could lower your temperature, "
                                        "like acetaminophen. \n\n 7) Protect Your Health This Flu Season \n\n It’s "
                                        "likely that flu viruses and the virus that causes \n COVID-19 will both "
                                        "spread this fall and winter. \n Healthcare systems could be overwhelmed "
                                        "treating both patients with flu and patients with COVID-19. \n This means "
                                        "getting a flu vaccine during 2020-2021 is more important than ever. \n "
                                        "It’s likely that flu viruses and the virus that causes COVID-19 will both "
                                        "spread this fall and winter. \n Healthcare systems could be overwhelmed "
                                        "treating both patients with flu and patients with COVID-19. \n This means "
                                        "getting a flu vaccine during 2020-2021 is more important than ever.\n 1) "
                                        "Flu vaccines have been shown to \n reduce the risk of flu illness, "
                                        "hospitalization, and death. \n 2) Getting a flu vaccine can also save "
                                        "healthcare resources for the care of patients with COVID-19. \n\n ",
                                        font="Times 18", bg="black", fg="#FF8D09").pack()
        button9 = Button(top3, text = "BACK", bg = "black", fg = "#FF8D09", command = second_page, font = sec_font, width = 55).pack(fill = X, side = LEFT)
        button10 = Button(top3, text = "QUIT", bg = "black", fg = "#FF8D09", command = root.destroy, font = sec_font, width = 55).pack(fill = X, side = RIGHT)


def lungs():
    tp = Toplevel(bg="black")
    tp.title("CUSTOM LOADER....")
    tp.attributes("-fullscreen", True)
    # tp.geometry("1920x1080+0+0")
    # loading text
    Label(tp, text="Loading....", font="Bahnschrift 15", bg="black", fg="#FF8D09").place(x=490, y=320)

    # loading block..
    for i in range(16):
        Label(tp, bg="#1F2732", width=2, height=1).place(x=(i + 22) * 22, y=350)

    for i in range(3):
        for j in range(16):
            # make block yellow
            Label(tp, bg="#ffbd09", width=2, height=1).place(x=(j + 22) * 22, y=350)
            sleep(0.06)
            tp.update_idletasks()
            # make block dark
            Label(tp, bg="#1F2732", width=2, height=1).place(x=(j + 22) * 22, y=350)
    else:
        top4 = Toplevel(bg="black")
        top4.title("LUNGS")
        top4.attributes("-fullscreen", True)
        main_frame2 = Frame(top4)
        main_frame2.pack(fill=BOTH, expand=1)
        # create a canvas
        my_canvas2 = Canvas(main_frame2)
        my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)
        # add scrollbar
        my_scroll1 = ttk.Scrollbar(main_frame2, orient=VERTICAL, command=my_canvas2.yview)
        my_scroll1.pack(side=RIGHT, fill=Y)
        # configure the canvas
        my_canvas2.configure(yscrollcommand=my_scroll1.set)
        my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion=my_canvas2.bbox("all")))
        # create another frame inside the canvas
        second_frame2 = Frame(my_canvas2)
        # add the new frame to a window in the canvas
        my_canvas2.create_window((0, 0), window=second_frame2, anchor="center")
        label13 = Label(second_frame2,
                    text="1) Don't Smoke \n\n Cigarette smoking is the major cause of lung cancer and chronic "
                         "obstructive pulmonary disease (COPD), which includes chronic bronchitis and "
                         "emphysema. \n Cigarette smoke can narrow the air passages and make breathing more "
                         "difficult. It causes chronic inflammation, or swelling in the lung, \n which can lead "
                         "to chronic bronchitis. Over time cigarette smoke destroys lung tissue and may \n "
                         "trigger changes that grow into cancer. \n If you smoke, it's never too late to benefit "
                         "from quitting. \n The American Lung Association can help whenever you are ready. "
                         "\n\n 2) Avoid Exposure to Indoor Pollutants That Can Damage Your Lungs \n\n "
                         "Secondhand smoke, chemicals in the home and workplace, and radon all can cause or "
                         "worsen lung disease. Make your home and car smokefree. \n Test your home for radon. "
                         "Avoid exercising outdoors on bad air days. \n And talk to your healthcare provider if "
                         "you are worried that something in your home, \n school or work may be making you sick. "
                         "\n\n 3) Minimize Exposure to Outdoor Air Pollution \n\n The air quality outside can "
                         "vary from day to day and sometimes is unhealthy to breathe. \n Knowing how outdoor air "
                         "pollution affects your health and useful strategies to minimize \n prolonged exposure "
                         "can help keep you and your family well. \n Climate change and natural disasters can "
                         "also directly impact lung health. \n\n A cold or other respiratory infection can "
                         "sometimes become very serious. There are several things you can do to protect "
                         "yourself: \n -Wash your hands often with soap and water. Alcohol-based cleaners are "
                         "a good substitute if you cannot wash. \n -Avoids crowds during the cold and flu "
                         "season. \n -Good oral hygiene can protect you from the germs in your mouth leading "
                         "to infections. \n Brush your teeth at least twice daily and see your dentist at least "
                         "every six months. \n -Get vaccinated every year against influenza. Talk to your "
                         "healthcare provider to find out if the pneumonia vaccine is right for you. \n If "
                         "you get sick, keep it to yourself! Protect the people around you, \n including your "
                         "loved ones, by keeping your distance. Stay home from work or school until you're "
                         "feeling better. \n\n", font="Times 18", bg="black", fg="#FF8D09").pack()
        button11 = Button(top4, text = "BACK", bg = "black", fg = "#FF8D09", command = second_page, font = sec_font, width = 55).pack(fill = X, side = LEFT)
        button12 = Button(top4, text = "QUIT", bg = "black", fg = "#FF8D09", command = root.destroy, font = sec_font, width = 55).pack(fill = X, side = RIGHT)


def diabetes():
    tp = Toplevel(bg="black")
    tp.title("CUSTOM LOADER....")
    tp.attributes("-fullscreen", True)
    # tp.geometry("1920x1080+0+0")
    # loading text
    Label(tp, text="Loading....", font="Bahnschrift 15", bg="black", fg="#FF8D09").place(x=490, y=320)

    # loading block..
    for i in range(16):
        Label(tp, bg="#1F2732", width=2, height=1).place(x=(i + 22) * 22, y=350)

    for i in range(3):
        for j in range(16):
            # make block yellow
            Label(tp, bg="#ffbd09", width=2, height=1).place(x=(j + 22) * 22, y=350)
            sleep(0.06)
            tp.update_idletasks()
            # make block dark
            Label(tp, bg="#1F2732", width=2, height=1).place(x=(j + 22) * 22, y=350)
    else:
        top5 = Toplevel(bg="black")
        top5.title("DIABETES")
        top5.attributes("-fullscreen", True)
        main_frame3 = Frame(top5)
        main_frame3.pack(fill=BOTH, expand=1)
        # create a canvas
        my_canvas3 = Canvas(main_frame3)
        my_canvas3.pack(side=LEFT, fill=BOTH, expand=1)
        # add scrollbar
        my_scroll2 = ttk.Scrollbar(main_frame3, orient=VERTICAL, command=my_canvas3.yview)
        my_scroll2.pack(side=RIGHT, fill=Y)
        # configure the canvas
        my_canvas3.configure(yscrollcommand=my_scroll2.set)
        my_canvas3.bind('<Configure>', lambda e: my_canvas3.configure(scrollregion=my_canvas3.bbox("all")))
        # create another frame inside the canvas
        second_frame3 = Frame(my_canvas3)
        # add the new frame to a window in the canvas
        my_canvas3.create_window((0, 0), window=second_frame3, anchor="center")
        label15 = Label(second_frame3, font="Times 18", bg="black", fg="#FF8D09",
                    text="Diabetes mellitus, commonly known as diabetes, is a metabolic disease that causes high "
                         "blood sugar.The hormone insulin moves sugar from the blood into ur's \n cells to be stored or "
                         "used for energy. With diabetes,your body either doesn't make enough insulin or can't "
                         "effectively use the insulin it does make. \n\n If type 2 diabetes were an infectious "
                         "disease, passed from one person to another, public health officials would say we’re in the "
                         "midst of an epidemic. \n This difficult disease is striking an ever-growing number of adults, "
                         "and with the rising rates of childhood obesity,it has become more common in youth, \n "
                         "especially among certain ethnic groups (learn more about diabetes, including the other "
                         "types and risk factors).\n The good news is that prediabetes and type 2 diabetes are "
                         "largely preventable. \n About 9 in 10 cases in the U.S. can be avoided by making lifestyle "
                         "changes.\n These same changes can also lower the chances of developing heart disease and some "
                         "cancers.\n The key to prevention can be boiled down to five words: Stay lean and stay active. "
                         "\n\n What if I already have diabetes? \n\n Guidelines for preventing or lowering your risk "
                         "of developing type 2 diabetes are also appropriate if you currently have a diabetes "
                         "diagnosis. \n Achieving a healthy weight,eating a balanced carbohydrate-controlled diet,"
                         "and getting regular exercise all help to improve blood glucose control. \n If you are taking "
                         "insulin medication, you may need more or less carbohydrate at a meal or snack to ensure a "
                         "healthy blood glucose range.\n There may also be special dietary needs for exercise,"
                         "such as bringing a snack so that your blood glucose does not drop too low.\n For specific "
                         "guidance on scenarios such as these, refer to your diabetes care team who are the best "
                         "resources for managing your type of diabetes. \n\n 1) Control your weight- \n\n Excess "
                         "weight is the single most important cause of type 2 diabetes.\n Being overweight increases "
                         "the chances of developing type 2 diabetes seven-fold.\n Being obese makes you 20 to 40 times "
                         "more likely to develop diabetes than someone with a healthy weight. \n Losing weight can "
                         "help if your weight is above the healthy-weight range.\n Losing 7-10% of your current weight "
                         "can cut your chances of developing type 2 diabetes in half.\n\n 2)Get moving—and turn off "
                         "the television- \n\n Inactivity promotes type 2 diabetes.Working your muscles more "
                         "often and making them work harder \n improves their ability to use insulin and absorb glucose. \n "
                         "This puts less stress on your insulin-making cells. So trade some of your sit-time for "
                         "fit-time. \n Long bouts of hot, sweaty exercise aren’t necessary to reap this benefit. \n "
                         "Findings from the Nurses’ Health Study and Health Professionals Follow-up Study suggest\n "
                         "that walking briskly for a half hour every day reduces the \n risk of developing type 2 "
                         "diabetes by 30%.\n [3,4] More recently, The Black Women’s Health Study reported similar "
                         "diabetes-prevention \n benefits for brisk walking of more than 5 hours per week.\n This "
                         "amount of exercise has a variety of other benefits as well. \n And even greater cardiovascular "
                         "and other advantages can be attained by more,\n and more intense, exercise. \n "
                         "Television-watching appears to be an especially-detrimental form of inactivity: \n Every two "
                         "hours you spend watching TV instead of pursuing something more active increases the chances \n "
                         "of developing diabetes by 20%; \n it also increases the risk of heart disease (15%) and early "
                         "death (13%).\nThe more television people watch, the more likely they are to be "
                         "overweight or obese, \n and this seems to explain part of the TV viewing-diabetes link. \n The "
                         "unhealthy diet patterns associated with TV watching may also explain some of this \n "
                         "relationship. \n\n 3)Don’t smoke - \n\n Add type 2 diabetes to the long list of health "
                         "problems linked with smoking. \n Smokers are roughly 50% more likely to develop diabetes than "
                         "nonsmokers, \n and heavy smokers have an even higher risk. \n\n 4)Light to moderate alcohol "
                         "consumption - \n\n Evidence has consistently linked moderate alcohol consumption with "
                         "reduced risk of heart disease. \n The same may be true for type 2 diabetes. Moderate amounts "
                         "of alcohol—up to a drink a day for women, \n up to two drinks a day for men—increases the \n "
                         "efficiency of insulin at getting glucose inside cells. \n And some studies indicate that "
                         "moderate alcohol \n consumption decreases the risk of type 2 diabetes. [1, 34-39],\n  but excess "
                         "alcohol intake actually increases the risk. \n If you already drink alcohol, the key is to "
                         "keep your consumption in the moderate range, \n as higher amounts of alcohol could increase "
                         "diabetes risk. [40] If you don’t drink alcohol, \n there’s no need to start—you can get the "
                         "same benefits by losing weight, exercising more, \n and changing your eating patterns. \n\n "
                         "5) Beyond individual behavior - \n\n Type 2 diabetes is largely preventable by taking "
                         "several simple steps: keeping weight under control, \n exercising more, eating a healthy diet, "
                         "and not smoking.\n Yet it is clear that the burden of behavior change cannot fall entirely on "
                         "individuals. \n Families, schools, worksites, healthcare providers, communities, media, "
                         "the food industry,\n and government must work together to make healthy choices easy choices. \n "
                         "For links to evidence-based guidelines, \n research reports, and other resources for action, "
                         "visit our diabetes prevention toolkit. \n\n").pack()
        button13 = Button(top5, text="BACK", bg="black", fg="#FF8D09", command=second_page, font=sec_font, width=55).pack(fill=X, side=LEFT)
        button14 = Button(top5, text="QUIT", bg="black", fg="#FF8D09", command=root.destroy, font=sec_font, width=55).pack(fill=X, side=RIGHT)


def common_cold():
    tp = Toplevel(bg="black")
    tp.title("CUSTOM LOADER....")
    tp.attributes("-fullscreen", True)
    # tp.geometry("1920x1080+0+0")
    # loading text
    Label(tp, text="Loading....", font="Bahnschrift 15", bg="black", fg="#FF8D09").place(x=490, y=320)

    # loading block..
    for i in range(16):
        Label(tp, bg="#1F2732", width=2, height=1).place(x=(i + 22) * 22, y=350)

    for i in range(3):
        for j in range(16):
            # make block yellow
            Label(tp, bg="#ffbd09", width=2, height=1).place(x=(j + 22) * 22, y=350)
            sleep(0.06)
            tp.update_idletasks()
            # make block dark
            Label(tp, bg="#1F2732", width=2, height=1).place(x=(j + 22) * 22, y=350)
    else:
        top6 = Toplevel(bg="black")
        top6.title("COMMON COLD")
        top6.attributes("-fullscreen", True)
        main_frame4 = Frame(top6)
        main_frame4.pack(fill=BOTH, expand=1)
        # create a canvas
        my_canvas4 = Canvas(main_frame4)
        my_canvas4.pack(side=LEFT, fill=BOTH, expand=1)
        # add scrollbar
        my_scroll3 = ttk.Scrollbar(main_frame4, orient=VERTICAL, command=my_canvas4.yview)
        my_scroll3.pack(side=RIGHT, fill=Y)
        # configure the canvas
        my_canvas4.configure(yscrollcommand=my_scroll3.set)
        my_canvas4.bind('<Configure>', lambda e: my_canvas4.configure(scrollregion=my_canvas4.bbox("all")))
        # create another frame inside the canvas
        second_frame4 = Frame(my_canvas4)
        # add the new frame to a window in the canvas
        my_canvas4.create_window((0, 0), window=second_frame4, anchor="center")
        label16 = Label(second_frame4, font = "Times 18", bg = "black", fg = "#ff8d09",
                        text = "\n The common cold usually involves symptoms including runny nose, cough, sore throat, "
                               "and sneezing.Each year, the common cold affects millions of America\nns causing them "
                               "to miss school and work. The Centers for Disease Control (CDC) estimates \n adults have "
                               "about 2-3 colds per year, and children experience 8-12 colds annually. \n\n 1) Wash "
                               "your hands often. \n\n Washing your hands for at least 20 seconds can help protect "
                               "you from getting sick. Washing your hands frequently \n helps prevent the spread of "
                               "infection. Use plain soap and water, making sure to pay attention to spaces between \n "
                               "fingers, and under the fingernails. Rinse and dry with a clean towel. Teach your "
                               "children to wash their hands properly. \n If soap and water is unavailable, "
                               "alcohol-based hand sanitizers are an alternative. \n Make sure to wash hands after "
                               "sneezing or coughing, and before handling food. \n\n 2)Avoid touching your face. \n\n"
                               "Viruses can enter your body through the areas around your nose, mouth, and eyes. \n It "
                               "is important to avoid touching your face if you are exposed to a person with a cold, "
                               "especially \n if you have not washed your hands. \n\n 3) Don't smoke \n\n Smoking "
                               "tobacco products irritates and damages the throat and lungs, and can worsen cold "
                               " \n symptoms – which already include a sore throat and cough. Even secondhand smoke can "
                               "cause irritation. A recent study also found the anti-viral \n response in smokers may "
                               "become suppressed, making them less able to fight off infection. \n\n 4) Use disposable items if a family member is infected. \n\n"
                               "Use your own disposable plates, cups, and utensils and discard them after use if you "
                               "have a cold. This is especially helpful if there are \n children in the household, "
                               "who may attempt to take food off others' plates, or drink from others' cups. \n\n 5) "
                               "Keep household surfaces clean. \n\n Clean all household surfaces frequently to keep "
                               "them germ-free. Viruses can live on surfaces for several hours \n after being touched by "
                               "an infected person. Pay attention to the areas you touch most often and use soap and "
                               "water, bleach, \n or disinfectant cleaners to wipe off doorknobs, keyboards, phones, "
                               "remote controls, desks, toys, countertops, faucet handles, and drawer pulls. \n\n 6) "
                               "Use paper towels \n\n Cloth towels can harbor viruses for hours after being touched, "
                               "just as many surfaces do. To avoid contamination, \n use paper towels to clean up in the "
                               "kitchen and to dry your hands after washing. \n\n 7) Maintain a healthy lifestyle "
                               "\n\n It's important to be healthy at all times, so that if you do get a cold your "
                               "body's immune system is strong and can fight the infection. \n Eat a balanced diet with "
                               "plenty of fruits and vegetables, exercise regularly, and get enough sleep. \n\n 8) "
                               "Control stress \n\n When we experience stress we release a hormone called cortisol, "
                               "which has anti-inflammatory properties. \n Chronic stress causes an over-production of "
                               "this hormone, which in turn causes the immune system to become resistant to it. \n "
                               "Studies have shown that when a chronically stressed person is exposed to the common "
                               "cold virus, which causes inflammation, \n their bodies are less able to fight it because "
                               "their natural anti-inflammatory response does not work as well as it should. \n\n").pack()
        button18 = Button(top6, text="BACK", bg="black", fg="#FF8D09", command=second_page, font=sec_font,
                          width=55).pack(fill=X, side=LEFT)
        button19 = Button(top6, text="QUIT", bg="black", fg="#FF8D09", command=root.destroy, font=sec_font,
                          width=55).pack(fill=X, side=RIGHT)

def second_page():
    top1 = Toplevel(bg="black")
    top1.attributes("-fullscreen", True)
    top1.title("ENTRY")
    label7 = Label(top1, text="PLEASE SELECT THE PROBLEM", font=my_font, fg="red", bg="black").pack()
    button3 = Button(top1, width = 200, command = heart, bg = "black", font = sec_font, fg = "#FF8D09", text = "HEART")
    button3.pack(fill=BOTH, pady=60)
    button4 = Button(top1, width=200, command=covid, bg = "black", fg = "#FF8D09", font = sec_font, text = "COVID-19")
    button4.pack(fill=BOTH, pady=60)
    button5 = Button(top1, width=200, command=lungs, bg = "black", fg = "#FF8D09", font = sec_font, text = "LUNGS")
    button5.pack(fill=BOTH, pady=60)
    button6 = Button(top1, width=200, command=diabetes, bg = "black", fg = "#FF8D09", font = sec_font, text = "DIABETES")
    button6.pack(fill=BOTH, pady=60)
    button17 = Button(top1, width = 200, command = common_cold, bg = "black", fg = "#ff8d09", font = sec_font, text = "COMMON COLD").pack(fill = BOTH, pady = 30)
    button15 = Button(top1, text="BACK", bg="black", fg="#FF8D09", command=page_first, font=sec_font, width=55).pack(fill="x", side=LEFT)
    button16 = Button(top1, text="QUIT", bg="black", fg="#FF8D09", command=root.destroy, font=sec_font, width=55).pack(fill="x", side=RIGHT)


def page_first():
    top = Toplevel(bg="black")
    top.title("PATIENT'S DETAIL")
    top.attributes("-fullscreen", True)
    varb = StringVar()
    label1 = Label(top, text="ENTER THE PATIENT'S DETAIL", font=my_font, fg="red", bg="black").pack(side=TOP, fill=BOTH)
    label2 = Label(top, text="FIRST NAME", bg="black", font = sec_font, fg = "#FF8D09").pack(pady=25)
    entry1 = Entry(top, width=20, cursor="dot", justify=CENTER).pack(pady = 25)
    label3 = Label(top, text="LAST NAME", bg="black", font = sec_font, fg = "#FF8D09").pack(pady=25)
    entry2 = Entry(top, width=20, cursor="dot", justify=CENTER).pack(pady = 25)
    label4 = Label(top, text="AGE", bg="black", font = sec_font, fg = "#FF8D09").pack(pady=25)
    entry3 = Entry(top, width=20, cursor="dot", justify=CENTER).pack(pady = 25)
    label5 = Label(top, text="PHONE NUMBER", bg="black", fg = "#FF8D09", font = sec_font).pack(pady=25)
    entry4 = Entry(top, width=20, cursor="dot", justify=CENTER).pack(pady = 25)
    label6 = Label(top, text="SEX", bg="black", fg = "#FF8D09", font = sec_font).pack(pady=25)
    radio = Radiobutton(top, value="MALE", text="MALE", variable=varb)
    radio1 = Radiobutton(top, value="FEMALE", text="FEMALE", variable=varb)
    radio.pack(pady = 10)
    radio1.pack(pady = 10)
    button2 = Button(top, text="SUBMIT", font=sec_font, bg="black", fg="#FF8D09", command=second_page, width = 55).pack(side=LEFT,
                                                                                                         fill=X)
    button5 = Button(top, text="QUIT", font=sec_font, bg="black", fg="#FF8D09", command = root.destroy, width = 55).pack(side = RIGHT, fill = X)




root = Tk()
root.title("WELCOME :)")
my_font = Font(family="Times New Roman", size="20", weight="bold", slant="italic", underline=1, )
sec_font = Font(family="Times New Roman", size="18", weight="bold", slant="italic")
label = Label(root, text="WELCOME TO HEALTH TRACKER AND RECOMMENDATION SYSTEM", bg="black", fg="#ffbd09", font=my_font)
button = Button(root, text=">>PROCEED TO NEXT PAGE", font=sec_font, bg="black", fg="#ffbd09", command=page_first).pack(
    side=BOTTOM, fill=X)
label.pack(side=LEFT, expand=YES, fill=BOTH)
root.attributes("-fullscreen", True)
root.mainloop()
