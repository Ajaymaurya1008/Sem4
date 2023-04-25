import matplotlib.pyplot as plt
x = ['C++','Java','Php','Go','Python','C#']
y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
"""x_pos = [i for i, _ in enumerate(x)]"""
plt.title("Popularity of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.bar(x,y,color = 'blue')
plt.xticks(x,y)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',color='red',linewidth='0.5')
plt.grid(which='minor',linestyle=':',color='black',linewidth='0.5')
plt.show()
