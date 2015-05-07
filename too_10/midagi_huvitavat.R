#butterfly curve
t = seq(-1000,1000,0.01)
x = sin(t)*(exp(1)**cos(t)-2*cos(4*t)-sin(t/12)*sin(t/12)*sin(t/12)*sin(t/12)*sin(t/12))
y = cos(t)*(exp(1)**cos(t)-2*cos(4*t)-sin(t/12)*sin(t/12)*sin(t/12)*sin(t/12)*sin(t/12))
plot(x,y, cex = 0.1)
