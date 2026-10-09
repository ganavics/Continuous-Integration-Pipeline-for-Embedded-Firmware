#include "alarm.h"

int check_alarm(float temperature)
{
    if (temperature >= ALARM_THRESHOLD)
        return 1;

    return 0;
}