A = read.table("/home/marius/Dokumenter/fys4150/batmobile/resources/data_194.txt")
data = as.vector(t(A))
data = data[1000*(1:5000)]
N = as.numeric(table(cut(data,breaks=c(seq(0,5,1),10000000000000) ) ) )
P = diff(pexp(c(seq(0,5,1),10000000000000), mean(data)))
chisq.test(x=N,p=P)
