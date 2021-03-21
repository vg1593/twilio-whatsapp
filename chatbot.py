Flow = {
    "start":{
        "text":"Please Select a language(يرجى تحديد لغة):\n[1] Enter 1 for English\n[2] أدخل 2 للغة العربية",
        "branches":{
            "1":"en",
            "2":"ar"
        },
        "value":"conversation started/ language changed"
    },
    "en":{
        "text":"I can help with the followings:\n[1] Enter 1 for Submitting a new application (A Housekeeper - Private Driver)\n[2] Enter 2 To inquire about an existing request\n[3] Enter 3 For general inquiries\n[4] Enter 4 to Submit a new application for the corporate sector\n[5] Etner 5 to Change the language\n[q] Enter q to end chat",
        "branches":{
            "1":"new",
            "2":"existing",
            "3":"general",
            "4":"new corporate",
            "5":"start",
            "q":"quit"
        },
        "value":"selected english as language",
        "language":True
    },
    "ar":{
        "text":"يمكنني المساعدة فيما يلي:\n[1] أدخل 1  تقديم طلب جديد ( عاملة منزلية – سائق خاص )\n[2] أدخل 2  للاستفسار عن طلب قائم\n[3] أدخل 3  للاستفسارات العامة\n[4] أدخل 4 تقديم طلب جديد لقطاع الشركات \n[5] أدخل 5  لتغير اللغة المختارة\n[q] أدخل q لإنهاء الدردشة",
        "branches":{
            "1":"new",
            "2":"existing",
            "3":"general",
            "4":"new corporate",
            "5":"start",
            "q":"quit"
        },
        "value":"selected arabic as language",
        "language":True
    },
    "new":{
        "text":{
            "en":"To submit your application, Please select your option\n[1] Enter 1  for A Housekeeper\n[2] Enter 2 for Private driver\n[3] Enter 3 For others",
            "ar":"لتقديم طلب جديد، الرجاء الاختيار من القائمة التالية:\n[1] أدخل 1  عاملة منزلية\n[2] أدخل 2  سائق خاص\n[3] أدخل 3  أخرى"
        },
        "branches":{
            "1":"housekeeper",
            "2":"driver",
            "3":"others",
            "q":"quit"
        },
        "value":"Submitting a new application (A Housekeeper - Private Driver)"
    },
    "existing":{
        "text":{
            "en":"To inquire about an existing request, please provide us with the ID number or the contract number",
            "ar":"للاستعلام عن طلب قائم ، الرجاء تزويدنا برقم الهوية أو رقم العقد"
        },
        "branches":{
            
        },
        "value":"To inquire about an existing request",
        "expect_input":True
    },
    "general":{
        "text":{
            "en":"We hope that you will write your inquiry and it will be transferred to one of the specialists in the office, currently the specialist is serving other clients. You will be contacted soon. Thank you for waiting",
            "ar":"نأمل منكم كتابة استفساركم وسيتم تحويله إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ,, شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"For general inquiries",
    },
    "new corporate":{
        "text":{
            "en":"Welcome to the corporate sector. To submit a new application, please choose from the following list\n[1] Enter 1 for Contracting sector\n[2] Enter 2 for Restaurants and cafes sector\n[3] Enter 3 for Hotel & tourism sector\n[4] Enter 4 for Other",
            "ar":"مرحبا بك في قطاع الشركات لتقديم طلب جديد، الرجاء الاختيار من القائمة التالية:\n[1] أدخل 1 قطاع المقاولات\n[2] أدخل 2 قطاع المطاعم والكافيهات\n[3] أدخل 3 قطاع الفنادق والسياحة\n[4] أدخل 4 آحرون"
        },
        "branches":{
            "1":"contracting",
            "2":"restaurants",
            "3":"hotel",
            "4":"others_corp"
        },
        "value":"Submit a new application for the corporate sector"
    },
    "quit":{
        "text":{
            "en":"Thank you for contacting us, have a great day!",
            "ar":"شكرًا على تواصلك معنا ، أتمنى لك يومًا سعيدًا!"
        },
        "branches":{
            
        },
        "value":"exited the application"
    },
    "housekeeper":{
        "text":{
            "en":"Please choose the required country\n[1] Enter 1 for Uganda is Muslim 11730 riyals (Salary: 900 riyals) (Duration: 90 days)\n[2] Enter 2 for Non-Muslim Uganda 11,155 riyals (Salary: 900 riyals) (Duration: 90 days)\n[3] Enter 3 for Kenya, a Muslim 13,455 riyals (Salary: 900 riyals) (Duration: 90 days)\n[4] Enter 4 for Non-Muslim Kenya 12305 Riyals (Salary: 900 Riyals) (Duration: 90 days)\n[5] Enter 5 for The Philippines is Muslim 23,000 riyals (Salary: 1,500 riyals) (Duration: 90 days)\n[6] Enter 6 for A non-Muslim Philippines 21850 riyals (Salary: 1500 riyals) (Duration: 90 days)\n[7] Enter 7 for Burundian Muslim 13455 riyals (Salary: 900 riyals) (Duration: 90 days)\n[8] ENter 8 for Burundian non-Muslim 12880 riyals (Salary: 900 riyals) (Duration: 90 days)\n[9] Enter 9 for Bangladesh 16,330 riyals (Salary: 1,000 riyals) (Duration: 90 days)",
            "ar":"الرجاء اختيار الدولة المطلوبة\n[1] أدخل 1 أوغندا مسلمة 11730 ريال ( الراتب : 900 ريال ) ( المدة : 90 يوم )\n[2] أدخل 2 أوغندا غير مسلمة 11155 ريال ( الراتب : 900 ريال ) ( المدة : 90 يوم )\n[3] أدخل 3 كينيا  مسلمة 13455 ريال ( الراتب : 900 ريال ) ( المدة : 90 يوم )\n[4] أدخل 4 كينيا غير مسلمة 12305 ريال ( الراتب : 900 ريال ) ( المدة : 90 يوم )\n[5] أدخل 5 الفلبين  مسلمة 23000 ريال ( الراتب : 1500 ريال ) ( المدة : 90 يوم )\n[6] أدخل 6 الفلبين غير مسلمة 21850 ريال ( الراتب : 1500 ريال ) ( المدة : 90 يوم )\n[7] أدخل 7 بوروندي مسلمة 13455 ريال ( الراتب : 900 ريال ) ( المدة : 90 يوم )\n[8] أدخل 8 بوروندي غير مسلمة 12880 ريال ( الراتب : 900 ريال) ( المدة : 90 يوم )\n[9] أدخل 9 بنجلاديش 16330 ريال ( الراتب : 1000 ريال ) ( المدة : 90 يوم )"
        },
        "branches":{
            "1":"ugandam",
            "2":"ugandanm",
            "3":"kenyam",
            "4":"kenyanm",
            "5":"philippinesm",
            "6":"philippinesnm",
            "7":"burundianm",
            "8":"burundiannm",
            "9":"bangladesh",
            "q":"quit"
        },
        "value":"A Housekeeper"
    },
    "driver":{
        "text":{
            "en":"Please choose the required country\n[1] Enter 1 for India (New) 3450 Riyals (Salary: 1400 Riyals) (Duration: 90 days)\n[2] Enter 2 for India (previously worked) 4600 riyals (Salary: 1700 riyals) (Duration: 90 days)",
            "ar":"الرجاء اختيار الدولة المطلوبة:\n[1] أدخل 1 الهند ( جديد ) 3450 ريال ( الراتب : 1400 ريال ) ( المدة : 90 يوم )\n[2] أدخل 2 الهند ( سبق له العمل ) 4600 ريال ( الراتب : 1700 ريال ) ( المدة : 90 يوم )"
        },
        "branches":{
            "1":"indian",
            "2":"indiapw"
        },
        "value":"Private driver"
    },
    "others":{
        "text":{
            "en":"We hope that you will write the required profession and your request will be transferred to one of the specialists in the office, currently the specialist is serving other clients. You will be contacted soon. Thank you for waiting.",
            "ar":"نأمل منكم كتابة المهنة المطلوبة وسيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Others"
    },
    "ugandam":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Uganda is Muslim 11730 riyals (Salary: 900 riyals) (Duration: 90 days)"
    },
    "ugandanm":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Non-Muslim Uganda 11,155 riyals (Salary: 900 riyals) (Duration: 90 days)"
    },
    "kenyam":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Kenya, a Muslim 13,455 riyals (Salary: 900 riyals) (Duration: 90 days)"
    },
    "kenyanm":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Non-Muslim Kenya 12305 Riyals (Salary: 900 Riyals) (Duration: 90 days)"
    },
    "philippinesm":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"The Philippines is Muslim 23,000 riyals (Salary: 1,500 riyals) (Duration: 90 days)"
    },
    "philippinesnm":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"A non-Muslim Philippines 21850 riyals (Salary: 1500 riyals) (Duration: 90 days)"
    },
    "burundianm":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Burundian Muslim 13455 riyals (Salary: 900 riyals) (Duration: 90 days)"
    },
    "burundiannm":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Burundian non-Muslim 12880 riyals (Salary: 900 riyals) (Duration: 90 days)"
    },
    "bangladesh":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Bangladesh 16,330 riyals (Salary: 1,000 riyals) (Duration: 90 days)"
    },
    "indian":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"India (New) 3450 Riyals (Salary: 1400 Riyals) (Duration: 90 days)"
    },
    "indiapw":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"India (previously worked) 4600 riyals (Salary: 1700 riyals) (Duration: 90 days)"
    },
    "contracting":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Contracting sector"
    },
    "restaurants":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Restaurants and cafes sector"
    },
    "hotel":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Hotel & tourism sector"
    },
    "others_corp":{
        "text":{
            "en":"Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting.",
            "ar":"سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        },
        "branches":{
            
        },
        "value":"Others"
    },
}



def generate_response(msg,last,selection,language):
    if last and Flow[last]["branches"].keys():
        if msg in Flow[last]["branches"].keys():
            current = Flow[last]["branches"][msg]
            branch = Flow[current]
            if isinstance(branch["text"],str):
                reply = branch["text"]
            else:
                reply = branch["text"][language]
            selection.append(branch["value"])
            if "language" in branch.keys():
                language = current
        else:
            current = last
            reply = "Wrong input, please select a valid input."
            selection.append(msg)
            if language == "ar":
                reply = "إدخال خاطئ ، الرجاء تحديد إدخال صالح."
    else:
        reply = None
        if last:
            if "expect_input" in Flow[last]:
                current = None
                selection.append(msg)
                if language == "en":
                    reply = "Your order will be transferred to one of our specialists in the office, the specialist is currently serving another costumer, we will contact you as soon as possible, thank you for waiting"
                elif language == "ar":
                    reply = "سيتم تحويل طلبك إلى احد المختصين بالمكتب، حاليا المختص يخدم عملاء آخرين سوف يتم التواصل معك قريبا ،، شكرا لانتظارك"
        if not reply:
            reply = Flow["start"]["text"]
            current = "start"
            if msg:
                selection.append(msg)
            language = None
            selection.append(Flow["start"]["value"])
    return reply, current, selection, language

if __name__ == "__main__":
    response,last,selection,language = generate_response(None,None,[],None)
    print(response)
    while True:
        msg = input()
        response,last,selection,language = generate_response(msg,last,selection,language)
        print(response)