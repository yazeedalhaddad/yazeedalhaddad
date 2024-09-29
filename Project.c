/*
char name[] = "Yazeed_ALHADDAD";
int id = 1221902;
int lec_sec=2;
char lab_sec[]="3L";
*/

#include <stdio.h>
#define MAXSIZE 100
void displayMainMenu(void);
void addBook(int [], double [], int*);
void removeBook(int [], double [], int*);
void searchForBook(int [], double[], int);
void printBooks (int [], double[], int );
void uploadDataFile(void);
void updateDataFile(void);
int main() {
  printf("Welcome to My BookStore Mangement System\n\n");
  printf("Uploading data file...\n");
  printf("Data File uploaded\n\n");
  int bins[MAXSIZE];
  double prices[MAXSIZE];
  int size=0;
  int opr;
  while (1) {
    displayMainMenu();
    opr=0;
    scanf("%d",&opr);
    switch (opr) {
      case 1:addBook(bins,prices,&size);
            break;
      case 2:removeBook(bins,prices,&size);
            break;
      case 3:searchForBook(bins,prices,size);
          break;
      case 4: printBooks(bins,prices,size);
          break;
      case 5:uploadDataFile();
            updateDataFile();
            break;
      default: printf("No such operation! Please try again\n");
    }
    if (opr==5) break;
}
printf("\nThank you for using My BookStore Management System.GoodBye.");
return 0;
}
void displayMainMenu(){
  printf("Please Select an Operation (1-5):\n1- Add a Book:\n2- Remove a Book:\n3- Search for a Book:\n4-Print Book List\n5- Exit System:\n");
}
void addBook(int bins[], double prices[], int *size){
  int bin
  double price;
  printf("Enter bin number for book\n");
  scanf("%d",&bin);
  printf("Enter the Price of the book\n");
  scanf("%lf",&price);
  // check if the list is full and check if bin is already there then adding it
  if ((*size)<MAXSIZE){
  int postion=0;
    while (postion<=(*size) && bins[postion]>bin){
      postion++;}
      if(bins[postion]==bin){
      printf("The bin of the book is already added\n");
      return;
  }
    for (int i=postion;i<(*size);i++){
      bins[i+1]=bins[i];
      prices[i+1]=prices[i];
    }
    bins[postion]=bin;
    prices[postion]=price;
    (*size)++;
    printf("Book info has been added%d\n\n",(*size));
  }
  else printf("You reached the maximum size of books\n");
}
void removeBook(int bins[], double prices[], int *size){
  if ((*size)>0){
    int bin;
    scanf("Enter the bin of the book you want to remove",&bin );
    int postion=0;
    while (postion<=(*size) && bins[postion]!=bin) {
      postion++;}
    if (postion == (*size)) {
      printf("the bin cannot be found\n");
      return;
    }
    else{
      for (int i=(*size);i>=postion;i--){
      bins[i]=bins[i-1];
      prices[i]=prices[i-1];
    }
    printf("Book info has been removed\n\n");
    (*size)--;
  }}
  else printf("there is no books added\n");


}
void searchForBook(int bins[], double prices[], int  size) {
  if (size>0){
    int bin,postion=0;
    printf("Enter the bin of the book you are looking for:\n");
    scanf("%d\n",&bin);
    while (postion<=size && bins[postion]!=bin) {
      postion++;}
    if (postion==size) {
      printf("the book couldn't be found\n");
      return;
    }
    else {printf("BIN# : %d\n Price: %lf",bins[postion],prices[postion]);
  printf("Book has been searched for\n\n");
}}}
void printBooks (int bins[], double prices[], int size) {
  for (int i=0;i<=size;i++){
    printf("bin#:%d price: %lf ",bins[i],prices[i]);
  }
}
void uploadDataFile(){
  printf("\nUpdating data file...\n");
}
void updateDataFile(){
  printf("Data File updated\n");
}
