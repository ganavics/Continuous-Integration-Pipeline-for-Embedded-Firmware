CC = gcc

CFLAGS = -Wall

TARGET = firmware

SRC = main.c sensor.c alarm.c

all:
	$(CC) $(CFLAGS) $(SRC) -o $(TARGET)

clean:
	del /Q firmware.exe 2>nul || exit 0