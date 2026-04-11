//Programa: Calculadora de suma
//Autor: Equipo 1 SD
//Version: 1.2.0
//Descripcion: Se agrega validación de datos con manejo de errores.

#include<stdio.h>

int main(){
    float N1, N2;

    try {
    	printf("Ingresa el dato 1: ");
    	if (scanf("%f", &N1) != 1){
    		throw 1;
		}
		printf("Ingresa el dato 2: ");
		if (scanf("%f", &N2) != 1){
			throw 1;
		}
		printf("La suma es: %.2f\n", N1 + N2);
	}
	catch (int e){
		printf("Error: Debes ingresar solo numeros\n");
	}

    return 0;
}
