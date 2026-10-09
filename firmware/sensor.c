#include "sensor.h"

#include <stdlib.h>

float read_temperature(void)
{
    float temperature;

    temperature = 20 + (rand() % 16);

    return temperature;
}

float validate_temperature(float temperature)
{
    if (temperature < SENSOR_MIN_TEMP)
        return -1;

    if (temperature > SENSOR_MAX_TEMP)
        return -1;

    return temperature;
}