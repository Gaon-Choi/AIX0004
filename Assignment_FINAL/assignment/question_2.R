d_1<-function(S, K, r_f, σ, T) {
	(log(exp(S/K))+(r_f+(1/2)*σ*σ)*T)/(σ*sqrt(T))
	# S: 주식의 가격
	# K: 행사가격
	# r_f: 무위험이자율
	# σ: 주식수익률의 연간 표준편차
	# T: 옵션의 만기
}

d_2<-function(S, K, r_f, σ, T) {
	d_1(S, K, r_f, σ, T) - σ*sqrt(T)
}

N<-function(num) {
	pnorm(num, mean = 0, sd = 1)
}

C<-function(S, K, r_f, σ, T) {
	S * N(d_1(S, K, r_f, σ, T)) - K * exp((-1)*r_f*T)*N(d_2(S, K, r_f, σ, T))
}

C(100, 100, 0.04, 0.1, 0.5)