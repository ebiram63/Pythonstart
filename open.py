import pandas as pd
  
details = {
     'age' : [20, 21 ,22, 23, 25, 26, 27],
     'bmi' :[25, 30, 32, 33, 34, 35, 40],
     'diabet': [1, 0, 1, 0, 1, 0, 0]
}

df = pd.DataFrame(details)
df.to_csv('csv2.txt')


def func(r):
    return r['age']*r['bmi']*r['diabeles']

df['result'] = df.apply(func, axis=1)
print(df)
#with open('convert.txt', 'w') as convert_file:
 #    convert_file.write(json.dumps(details))


#with open("myfile.txt", 'w') as f: 
#    for key, value in details.items(): 
#        f.write('%s:%s\n' % (key, value))

