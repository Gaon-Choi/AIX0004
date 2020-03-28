library("ggplot2")

S0 <- 100	# 처음 주식의 가격
r_f <- 0.04	# 무위험이자율
T <- 0.5		# 옵션의 만기
dt <- 0.001	# 아주 작은 시간(미분개념)
N <- 10000	# 시뮬레이션 횟수
sigma <- 0.1	# 주식수익률의 연간 표준편차
K <- 100		# 행사 가격

S <- matrix(0L, nrow = N, ncol = (T/dt) + 1)
S[, 1] <- matrix(S0, nrow = N, ncol = 1)
for (x in 1:N) {
for (y in 1:(T/dt)) {
S[x, y+1] <- S[x, y] * exp((r_f - 0.5 * sigma*sigma) * dt + sigma * sqrt(dt) * rnorm(1, 0, 1))
}
}

X <- matrix(0L, nrow = 1, ncol = (T/dt) + 1)
for (x in 1:(T/dt)) {
X[1, x + 1] <- X[1, x] + dt
}

# 만기 시점의 옵션의 가치
V <- matrix(0L, nrow = 1, ncol = N)
for (x in 1:N){
V[1, x] <- max(S[x, (T/dt) + 1] - K, 0)
}

# 최종 옵션의 가치
C <- exp(-r_f * T) * sum(V) / N
print("옵션의 가치: ")
C

# 그래프 그리기
ggplot()+
geom_line(aes(x=X[1, ], y=S[1, ], color="red"))+
geom_line(aes(x=X[1,], y=S[2, ], color="purple"))+
geom_line(aes(x=X[1,], y=S[3, ], color="blue"))+
geom_line(aes(x=X[1,], y=S[4, ], color="yellow"))+
geom_line(aes(x=X[1,], y=S[5, ], color="green"))+
xlab("Time")+
ylab("Stock Price")+
ggtitle("Changes of Stock Price Over Time")
