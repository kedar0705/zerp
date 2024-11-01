import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedReader;

public class DisplayBooks {
    public static void displayAllBooks() throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("lib_data.txt"));
        String line;
            while ((line = reader.readLine()) != null) {
                String[] bookDetails = line.split(", ");
                System.out.println("\n------------------------------\n");
                System.out.println("Book ID: " + bookDetails[0]);
                System.out.println("Title: " + bookDetails[1]);
                System.out.println("Author: " + bookDetails[2]);
                System.out.println("Genre: " + bookDetails[3]);
                System.out.println("Availability: " + bookDetails[4]);
                System.out.println("Status: " + bookDetails[5]);
            }
            reader.close();

    }
}
