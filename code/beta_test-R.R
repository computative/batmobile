A = read.table("/home/marius/Dokumenter/fys4150/batmobile/resources/Data_l_0.250000.txt")
data = as.vector(t(A))
N = as.numeric(table(cut(data,breaks=c(seq(0,5,0.1),10000000000000) ) ) )
P = diff(pexp(c(seq(0,5,0.1),10000000000000), 1))
chisq.test(x=N,p=P)$p.value