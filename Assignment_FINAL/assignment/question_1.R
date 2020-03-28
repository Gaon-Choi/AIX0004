price=c(0:200)
Y=vector("numeric", 201)
for(i in 1:201) {
Y[i]=max(price[i]-100, 0)
}
plot(price,Y,type='l')


