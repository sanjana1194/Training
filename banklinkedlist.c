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
struct node* SearchAccount(char *id, char *operation);
void DeleteNode(struct node *nodetobedeleted);

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


struct node* SearchAccount(char *idnumber, char *operation)
{
	if (head == NULL)
	{
		printf("No record found. File is empty.\n");
		pause();
		return NULL;
	}

	struct node *temp = head;
	while (temp != NULL)
	{
		if (strcmp(temp->account.accountno, idnumber) == 0)
		{
			return temp;
		}
		temp = temp->next;
	}
	printf("Record with Account number %s not found to %s.\n", idnumber, operation);
	pause();
	return NULL;
}

void UpdateAccount()
{
	char idnumber[30];
	char operation[] = "update";
	ReadID(idnumber, sizeof(idnumber), operation);
	struct node *target = SearchAccount(idnumber, operation);
	if (target == NULL)
	{
		return;
	}
	int choice;
	clear();
	printf("\nCurrent Details:\n");
	printf("___________________________________________\n");
	printf("Account Number: %s\n", target->account.accountno);
	printf("Account Holder Name: %s\n", target->account.name);
	printf("Balance: %.2f\n", target->account.balance);
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
			ReadText(target->account.name, sizeof(target->account.name));
			printf("Name updated successfully.\n");
			break;

		case 2:
			printf("Enter the new balance: ");
			ReadFloat(&target->account.balance);
			printf("Balance updated successfully.\n");
			break;

		default:
			printf("Invalid choice.\n");
			return;
	}

	SavetoFile();

	clear();
	printf("\nUpdated Details:\n");
	printf("___________________________________________\n");
	printf("Account Number: %s\n", target->account.accountno);
	printf("Account Holder Name: %s\n", target->account.name);
	printf("Balance: %.2f\n", target->account.balance);
	printf("___________________________________________\n");
	pause();
}

void DeleteNode(struct node *nodetobedeleted)
{
	struct node **indirect = &head;

	while (*indirect != NULL)
	{
		if (*indirect == nodetobedeleted)
		{
			struct node *temp = *indirect;
			*indirect = (*indirect)->next;  
			free(temp);
			SavetoFile();
			printf("Record deleted successfully.\n");
			pause();
			return;
		}
		indirect = &(*indirect)->next;
	}

}


void DeleteAccount()
{
	char idnumber[30];
	char operation[] = "delete";
	ReadID(idnumber, sizeof(idnumber), operation);

	struct node *target = SearchAccount(idnumber, operation);
	if (target == NULL)
	{
		return;
	}
	DeleteNode(target); 
}

