/* c_no_opt.c
   Versión: 2.0.0
   Autor: Victor
   Fecha: 14/03/2026
   Descripción: Generación de reporte estadístico optimizado.
   MOD: v2.0.0 - Rediseño del programa para generar un reporte estadístico y soportar múltiples modas
*/

#include <stdio.h>

int main() {

    int datos[] = {3, -1, 0, 5, -7, 0, 2, 3, 3, -1, 5, 5, 5};
    int n = sizeof(datos)/sizeof(datos[0]);

    int valores[13];
    int frecuencias[13];

    int cantidad = 0;

    for (int i = 0; i < n; i++) {               //Bucle para hacer el cálculo de las frecuencias

        int pos = -1;

        for (int j = 0; j < cantidad; j++) {
            if (datos[i] == valores[j]) {
                pos = j;
                break;
            }
        }

        if (pos >= 0)
            frecuencias[pos]++;
        else {
            valores[cantidad] = datos[i];
            frecuencias[cantidad] = 1;
            cantidad++;
        }
    }

    for (int i = 0; i < cantidad - 1; i++) {       //En este bucle se ordenan los valores
        for (int j = i + 1; j < cantidad; j++) {

            if (valores[i] > valores[j]) {

                int t = valores[i];
                valores[i] = valores[j];
                valores[j] = t;

                t = frecuencias[i];
                frecuencias[i] = frecuencias[j];
                frecuencias[j] = t;
            }
        }
    }

    int max_f = frecuencias[0];

    for (int i = 1; i < cantidad; i++)            //En este bucle se encuentra la frecuencia máxima
        if (frecuencias[i] > max_f)
            max_f = frecuencias[i];

    printf("========================================\n"); //Se imprime la tabla para los reultados
    printf("       REPORTE ESTADISTICO V2.0.0       \n");
    printf("========================================\n");
    printf("VALOR           | FRECUENCIA\n");
    printf("-----------------------------------\n");

    int primera_moda = 0;
    int bandera = 1;

    for (int i = 0; i < cantidad; i++) {

        if (frecuencias[i] == max_f) {

            printf("%-15d | %-15d (MODA)\n", valores[i], frecuencias[i]);

            if (bandera) {
                primera_moda = valores[i];
                bandera = 0;
            }

        } else
            printf("%-15d | %-15d\n", valores[i], frecuencias[i]);
    }

    printf("-----------------------------------\n");

    printf("Modas detectadas: ["); //Se imprimen las modas

    int first = 1;

    for (int i = 0; i < cantidad; i++) {

        if (frecuencias[i] == max_f) {

            if (!first) printf(", ");

            printf("%d", valores[i]);

            first = 0;
        }
    }

    printf("]\n");

    int num = primera_moda;        //Se hace la suma de dígitos
    if (num < 0) num = -num;

    int suma = 0;

    while (num > 0) {
        suma += num % 10;
        num /= 10;
    }

    printf("Frecuencia maxima: %d\n", max_f);
    printf("Suma digitos (Moda 1): %d\n", suma);
    printf("========================================\n");

    return 0;
}
