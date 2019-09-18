#include <stdio.h>
 
int main() {
 double num;
   int nota, moeda; 
    int n100,n50,n20,n10,n5,n2;
    int m100,m50,m25,m10,m5,m1;
    scanf("%lf",&num);
    
    nota = num;
    moeda = num*100;
    moeda = moeda % 100;
      
    
    n100= nota / 100; nota = nota % 100;
    n50= nota / 50; nota = nota % 50;
    n20= nota / 20; nota = nota % 20;
    n10= nota / 10; nota = nota % 10;
    n5= nota / 5; nota = nota % 5;
    n2= nota / 2; nota = nota % 2;
    
    if (nota ==1) {
        moeda+= 100;
    }
    m100 = moeda / 100; moeda = moeda % 100;
    m50 = moeda / 50; moeda = moeda % 50;
    m25 = moeda / 25; moeda = moeda % 25;
    m10 = moeda / 10; moeda = moeda % 10;
    m5 = moeda / 5; moeda = moeda % 5;
    m1 = moeda / 1; moeda = moeda % 1;
    
    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n",n100);
    printf("%d nota(s) de R$ 50.00\n",n50);
    printf("%d nota(s) de R$ 20.00\n",n20);
    printf("%d nota(s) de R$ 10.00\n",n10);
    printf("%d nota(s) de R$ 5.00\n",n5);
    printf("%d nota(s) de R$ 2.00\n",n2);
    printf("MOEDAS:\n");
    printf("%d moeda(s) de R$ 1.00\n",m100);
    printf("%d moeda(s) de R$ 0.50\n",m50);
    printf("%d moeda(s) de R$ 0.25\n",m25);
    printf("%d moeda(s) de R$ 0.10\n",m10);
    printf("%d moeda(s) de R$ 0.05\n",m5);
    printf("%d moeda(s) de R$ 0.01\n",m1);
    return 0;
}
