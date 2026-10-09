#ifndef SENSOR_H
#define SENSOR_H

#define SENSOR_MIN_TEMP   (-40.0f)
#define SENSOR_MAX_TEMP   (125.0f)

float read_temperature(void);
float validate_temperature(float temperature);

#endif