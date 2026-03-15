/* c_no_opt.c
   Versión: 1.2.0
   Autor: Jonathaan
   Fecha: 14/03/2026
   Descripción: Mejora del algoritmo de verificación de números primos.
                Se reduce el número de divisiones comprobando solo hasta
                la raíz cuadrada del número y evitando evaluar números pares.
   Entrada esperada: Un número entero N que define el rango de búsqueda.
   Salida esperada: Cantidad de números primos encontrados, suma de primos,
                    número de primos pares e impares.
*/

#include <stdio.h>
#include <math.h>

int main() {

    // BLOQUE 1: Inicialización de variables
    int N = 1000;
    int count_primos = 0;
    long long suma_primos = 0;
    int primos_pares = 0;
    int primos_impares = 0;

    // BLOQUE 2: Caso especial del número 2 (único primo par)
    if (N >= 2) {
        count_primos++;
        suma_primos += 2;
        primos_pares++;
    }

    // BLOQUE 3: Evaluación de números impares
    // MOD v1.2.0 — Se incrementa de 2 en 2 para evitar pares
    for (int m = 3; m <= N; m += 2) {

        int es_primo = 1;
        int limite = sqrt(m);  // solo se prueban divisores hasta raiz de m

        // BLOQUE 4: Verificación de divisores
        // MOD v1.2.0 — límite optimizado hasta raíz cuadrada
        for (int d = 3; d <= limite; d += 2) {

            if (m % d == 0) {
                es_primo = 0;
                break;
            }
        }

        // BLOQUE 5: Actualización de estadísticas
        if (es_primo) {
            count_primos++;
            suma_primos += m;
            primos_impares++;
        }
    }

    // BLOQUE 6: Mostrar resultados
    printf("Primos encontrados: %d\n", count_primos);
    printf("Suma de primos: %lld\n", suma_primos);
    printf("Primos pares: %d\n", primos_pares);
    printf("Primos impares: %d\n", primos_impares);

    return 0;
}
