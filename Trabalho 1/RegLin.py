
c = 's'
x = [0]*10
y = [0]*10
i = 0
while (c == 's') or (i>=10):
    x[i] = input('\nEntre com x: ')
    y[i] = input('\nEntre com y: ')
    i=i+1
    c = input('\nContinuar? s/n \n')

xmedia =0
ymedia=0
for j in range(i):
    xmedia+=int(x[j])
    ymedia+=int(y[j])
xmedia=xmedia/i
ymedia=ymedia/i

sCima = 0
sBaixo = 0

for j in range(i+1):
    sCima += (float(x[j])-xmedia)*(float(y[j])-ymedia)
    sBaixo += (float(x[j])-xmedia)*(float(x[j])-xmedia)

m = sCima/sBaixo
print(m)

c = ymedia - xmedia*m
print(c)

print('y = '+str(m)+'*x + '+str(c))