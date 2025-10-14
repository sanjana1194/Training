#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void RemoveNewLine(char *text);
void clear();
void pause();
void ReadText(char *text, int length);
void ReadFloat(float *number);

void RemoveNewLine(char *text)
{
	text[strcspn(text, "\n")] = '\0';
}

void clear()
{
	system("cls");
}

void pause()
{
	system("pause");
}

void ReadText(char *text, int length)
{
	fgets(text, length, stdin);
	RemoveNewLine(text);
}

void ReadFloat(float *number)
{
	scanf("%f", number);
	getchar();
}
