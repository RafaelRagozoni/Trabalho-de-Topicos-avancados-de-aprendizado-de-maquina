c = 's'
x = [1,2,3,4,5]
y = [3,4,2,4,5]
i = 5

xmedia =0
ymedia=0
j=0
for j in range(i):
    xmedia+=int(x[j])
    ymedia+=int(y[j])
xmedia=xmedia/i
ymedia=ymedia/i

sCima = 0
sBaixo = 0

for j in range(i):
    sCima += (float(x[j])-xmedia)*(float(y[j])-ymedia)
    sBaixo += (float(x[j])-xmedia)*(float(x[j])-xmedia)

m = sCima/sBaixo
print(m)

c = ymedia - xmedia*m
print(c)

print('y = '+str(m)+'*x + '+str(c))

ypR = 0
yR = 0

for j in range(i):
    ypR += ((x[j]*m+c)-ymedia)*((x[j]*m +c)-ymedia)
    yR += (y[j] - ymedia)*(y[j] - ymedia)

r = ypR/yR
print(r)