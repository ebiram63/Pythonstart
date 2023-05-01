"""دو لیست زیر را در نظر بگیرید لیست اول شامل اقلام مورد نیاز برای خرید و لیست دوم شامل مقدار مورد نیاز می باشد"""

"""
list_1=['milk','suger','butter','yogurt','cheese']
list_2 =  [5,2,10,1,3]


res = {}
for key in list_1:
    for value in list_2:
        res[key] = value
        list_2.remove(value)
        break

print(res)
"""
"""=========================================================================="""

"""برنامه ای بنویسید که مقدار ماکزیمم و مینیمم value های دیکشنری را خروجی دهد."""

"""
res = {'milk': 5, 'suger': 2, 'butter': 10, 'yogurt': 1, 'cheese': 3}

max_ = max(res.values())
min_ = min(res.values())

print("max is: ", max_,"\n","min is: " , min_)
"""

"""=========================================================================="""
"""برنامه ای بنویسید که یک جمله گرفته و تعداد تکرار هر کلمه را در یک دیکشنری ذخیره کند"""

"""
sentences = "In the 15th century, the native Safavids re-established a unified Iranian state and national identity, and converted the country to Shia Islam. Under the reign of Nader Shah in the 18th century, Iran presided over the most powerful military in the world, though by the 19th century, a series of conflicts with the Russian Empire led to significant territorial losses. The early 20th century saw the Persian Constitutional Revolution. Efforts to nationalize its fossil fuel supply from Western companies led to an Anglo-American coup in 1953, which resulted in greater autocratic rule under Mohammad Reza Pahlavi and growing Western political influence. He went on to launch a far-reaching series of reforms in 1963. After the Iranian Revolution, the current Islamic Republic was established in 1979 by Ruhollah Khomeini, who became the country's first Supreme Leader. "

res2 = {}
for i in sentences:
    res2[i] = 0
for i in sentences:
    if i in res2:
        res2[i] += 1
print(res2)

"""
"""=========================================================================="""
"""برنامه ای بنویسید که دو دیکشنری مانند زیر گرفته و اینها را در هم ادغام کند و برای کلیدهای یکسان در دیکشنری ها مقادیر آنها جمع کند"""

d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200, 'd':400}


d3 = {}

d3 = d1
#print(d3)
for i in d2.keys():
    if i in d3.keys():
        d3[i] = d1[i] + d2[i]
    else:
        d3[i] = d2[i] 
print(d3)

