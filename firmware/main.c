#include <stdio.h>

#include "sensor.h"
#include "alarm.h"

int main(void)
{
    float temperature;

    temperature = read_temperature();

    temperature = validate_temperature(temperature);

    if (temperature == -1)
    {
        printf("Invalid Sensor Reading\n");
        return 1;
    }

    printf("Temperature : %.2f C\n", temperature);

    if (check_alarm(temperature))
        printf("ALARM : HIGH TEMPERATURE\n");
    else
        printf("Temperature Normal\n");

    return 0;
}