import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class SearchBook {
    public static void searchBooks() throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("lib_data.txt"));
        System.out.println("Enter Book ID:");
        Scanner inpObj = new Scanner(System.in);
        String bookID = inpObj.next();
        inpObj.close();
        String line;
            while ((line = reader.readLine()) != null) {
                String[] bookDetails = line.split(", ");
                if (bookDetails[0].equals(bookID)) {
                    System.out.println("Book ID: " + bookDetails[0]);
                    System.out.println("Title: " + bookDetails[1]);
                    System.out.println("Author: " + bookDetails[2]);
                    System.out.println("Genre: " + bookDetails[3]);
                    System.out.println("Availability: " + bookDetails[4]);
                    break;
                }
            }
            reader.close();

    }
}
