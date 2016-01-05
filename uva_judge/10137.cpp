#include <stdio.h>
#include <math.h>

int main() {
    int students_number;

    scanf("%d\n", &students_number);

    float expenses[students_number];
    float sum = 0;
    float avg = 0;
    float money_to_change = 0;

    for(int i = 0; i < students_number; i++) {
        scanf("%f\n", &expenses[i]);
        sum += expenses[i];
    }

    avg = roundf((sum / students_number) * 100) / 100;

    for(int i = 0; i < students_number; i++) {
        if(expenses[i] > avg) {
            money_to_change += (expenses[i] - avg);
            printf("\n");
        }
    }

    printf("money_to_change: %.2f\n", money_to_change);
    printf("sum: %f\n", sum);
    printf("avg: %f\n", avg);

    return 0;
}
