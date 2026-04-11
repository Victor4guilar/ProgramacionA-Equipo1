// programa de suma 
// autor:Equipo 1 SD
// version: 1.0.1
// Descripción: Es una claculadora la cual solo realiza la operación de una suma ya establecida
// actualizacion : se arreglo el problema de una resta a una suma

#include<stdio.h>

int main(){
	//se cambia int por float para que tambien acapare las decimales 
    float suma;
    float N1, N2;
    
    N1 = 10;
    N2 = 3;
    
    suma = N1 + N2;
    // es %.2f para mostrar decimales 
    printf("La suma es: %.2f", suma);
}