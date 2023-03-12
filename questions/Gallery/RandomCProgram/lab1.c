#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
  double t;
  printf("t= ");
  scanf("%lf", &t);
  printf("\nx=%.3lf\n",
	 1*sqrt(t)*pow(sin(2*t),3)/1 +
	 3*pow(cos(t), 3)/5
	 +pow(2.0/9,t));
  return 0;
}
