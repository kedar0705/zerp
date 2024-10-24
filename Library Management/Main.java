import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println("Library Management System\n" + 
                        "1. Add a Book\n" + //
                        "2. Remove a Book\n" + //
                        "3. Search for a Book\n" + //
                        "4. Borrow a Book\n" + //
                        "5. Return a Book\n" + //
                        "6. Display All Books\n" + //
                        "7. Exit\n" + //
                        "Choose an option (1-7):");

        Scanner option = new Scanner(System.in);
        int opt = option.nextInt();
            
        switch (opt) {
            case 1:
                AddBook.addBooks();
                break;

            case 2:
                RemoveBook.removeBook();
                break;

            case 3:
                SearchBook.searchBooks();
                break;

            case 4:
                BorrowBook.borrowBook();
                break;

            case 5:
                ReturnBook.returnBook();
                break;

            case 6:
                DisplayBooks.readBooks();
                break;
                
            case 7:
                System.out.println("Thank you.");
                break;

            default:
                System.out.println("Enter a valid option.");
                break;
        }

        option.close();
        
    }
}