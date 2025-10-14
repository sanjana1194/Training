#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "misc.c"

#define DATA_FILE "Bank_Account_Details.dat"

typedef struct {
	char accountno[30];
	char name[30];
	float balance;
} Bank;

struct node {
	Bank account;
	struct node *next;
};

struct node *head = NULL;

void CreateAccount();
void UpdateAccount();
void ReadAccount();
void DeleteAccount();
void ShowMenu();
void ReadData(Bank *account);
void AppendtoList(Bank);
void SavetoFile();
void Load();

int main()
{
	clear();
	Load();
	ShowMenu();
	return 0;
}

void Load()
{
	FILE *fp = fopen(DATA_FILE, "rb");
	if (!fp)
	{
		printf("No existing data file found. Starting fresh.\n");
		return;
	}
	Bank accountdata;
	while (fread(&accountdata, sizeof(Bank), 1, fp) == 1)
	{
		AppendtoList(accountdata);
	}
	fclose(fp);
}

void ShowMenu()
{
	int choice;
	while (1)
	{
		clear();
		printf("\n--- Bank Management System ---\n");
		printf("1. Create Account\n");
		printf("2. Show All Details\n");
		printf("3. Update Details\n");
		printf("4. Delete Details\n");
		printf("5. Exit\n");
		printf("------------------------------\n");
		printf("Enter your choice: ");
		scanf("%d", &choice);
		getchar();

		switch (choice)
		{
			case 1:
				CreateAccount();
				break;
			case 2:
				ReadAccount();
				break;
			case 3:
				UpdateAccount();
				break;
			case 4:
				DeleteAccount();
				break;
			case 5:
				printf("Exiting...\n");
				exit(0);
			default:
				printf("Invalid choice. Please try again.\n");
		}
	}
}

void ReadData(Bank *account)
{
	printf("Enter Account Number: ");
	ReadText(account->accountno, sizeof(account->accountno));

	printf("Enter Account Holder Name: ");
	ReadText(account->name, sizeof(account->name));

	printf("Enter Balance: ");
	ReadFloat(&account->balance);
}

void AppendtoList(Bank p_account)
{
	struct node *newNode = malloc(sizeof(struct node));
	newNode->account = p_account;
	newNode->next = NULL;

	if (head == NULL)
	{
		head = newNode;
	}
	else
	{
		struct node *current = head;
		while (current->next != NULL)
		{
			current = current->next;
		}
		current->next = newNode;
	}
}

void SavetoFile()
{
	FILE *fp = fopen(DATA_FILE, "wb");
	if (!fp)
	{
		printf("Error opening file to save data.\n");
		return;
	}
	struct node *current = head;
	while (current != NULL)
	{
		fwrite(&current->account, sizeof(Bank), 1, fp);
		current = current->next;
	}
	fclose(fp);
}

void CreateAccount()
{
	Bank account;
	ReadData(&account);
	AppendtoList(account);
	SavetoFile();
	printf("Account created successfully.\n\n");
	pause();
}

void ReadAccount()
{
	clear();
	struct node *current = head;
	int counter = 1;
	if (current == NULL)
	{
		printf("No data found.\n");
		return;
	}
	else
	{
		while (current != NULL)
		{
			printf("\nRecord %d\n", counter++);
			printf("___________________________________________\n");
			printf("Account Number: %s\n", current->account.accountno);
			printf("Account Holder Name: %s\n", current->account.name);
			printf("Balance: %.2f\n", current->account.balance);
			current = current->next;
		}
	}
	printf("\n\n");
	pause();
}

void UpdateAccount()
{
	int choice, found = 0;
	struct node *temp = head;
	char idnumber[30];

	printf("Enter Account Number to be Updated: ");
	ReadText(idnumber, sizeof(idnumber));

	if (temp == NULL)
	{
		printf("No record found. File is empty.\n");
		return;
	}

	while (temp != NULL)
	{
		if (strcmp(temp->account.accountno, idnumber) == 0)
		{
			found = 1;
			clear();
			printf("\nCurrent Details:\n");
			printf("___________________________________________\n");
			printf("Account Number: %s\n", temp->account.accountno);
			printf("Account Holder Name: %s\n", temp->account.name);
			printf("Balance: %.2f\n", temp->account.balance);
			printf("___________________________________________\n");

			printf("Which detail do you want to update?\n");
			printf("1. Account Holder Name\n");
			printf("2. Balance\n");
			printf("Enter your choice: ");
			scanf("%d", &choice);
			getchar();

			switch (choice)
			{
				case 1:
					printf("Enter the new name: ");
					ReadText(temp->account.name, sizeof(temp->account.name));
					printf("Name updated successfully.\n");
					break;

				case 2:
					printf("Enter the new balance: ");
					ReadFloat(&temp->account.balance);
					printf("Balance updated successfully.\n");
					break;

				default:
					printf("Invalid choice.\n");
					exit(0);
			}

			SavetoFile();

			clear();
			printf("\nUpdated Details:\n");
			printf("___________________________________________\n");
			printf("Account Number: %s\n", temp->account.accountno);
			printf("Account Holder Name: %s\n", temp->account.name);
			printf("Balance: %.2f\n", temp->account.balance);
			printf("___________________________________________\n");
			pause();
			break;
		}
		temp = temp->next;
	}

	if (!found)
	{
		printf("Record with Account number %s not found.\n", idnumber);
		pause();
	}
}

void DeleteAccount()
{
	char idnumber[30];
	int found = 0;
	printf("Enter Account Number to be Deleted: ");
	ReadText(idnumber, sizeof(idnumber));

	struct node *current = head;
	struct node *prev = NULL;

	if (current == NULL)
	{
		printf("No record found. File is empty.\n");
		return;
	}

	while (current != NULL)
	{
		if (strcmp(current->account.accountno, idnumber) == 0)
		{
			found = 1;
			if (prev == NULL)
			{
				head = current->next;
			}
			else
			{
				prev->next = current->next;
			}
			free(current);
			SavetoFile();
			printf("Data Deleted Successfully.\n");
			pause();
			return;
		}
		prev = current;
		current = current->next;
	}

	if (!found)
	{
		printf("Record with Account number %s not found.\n", idnumber);
		pause();
	}
}
