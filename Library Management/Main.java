import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        boolean exit = false;
        Scanner option = new Scanner(System.in);

        while (!exit) {
            System.out.println("Library Management System\n" + 
                            "1. Add a Book\n" + 
                            "2. Remove a Book\n" + 
                            "3. Search for a Book\n" + 
                            "4. Borrow a Book\n" + 
                            "5. Return a Book\n" + 
                            "6. Display All Books\n" + 
                            "7. Exit\n" + 
                            "Choose an option (1-7):");

            int opt = option.nextInt();
                
            switch (opt) {
                case 1:
                    AddBook.addBooks();
                    System.out.println("\n");
                    break;

                case 2:
                    RemoveBook.removeBook();
                    System.out.println("\n");
                    break;

                case 3:
                    SearchBook.searchBooks();
                    System.out.println("\n");
                    break;

                case 4:
                    BorrowBook.borrowBook();
                    System.out.println("\n");
                    break;

                case 5:
                    ReturnBook.returnBook();
                    System.out.println("\n");
                    break;

                case 6:
                    DisplayBooks.displayAllBooks();
                    System.out.println("\n");
                    break;

                case 7:
                    exit = true;
                    break;

                default:
                    System.out.println("Invalid option. Please choose a number between 1 and 7.");
                    break;
            }
        }
    }
}