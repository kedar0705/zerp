import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SearchBook {
    public static void searchBooks() throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("lib_data.txt"));
        System.out.println("Search for book (ID/Title/Author/Genre): ");
        Scanner inpObj = new Scanner(System.in);
        String searchTerm = inpObj.next();
        Pattern pattern = Pattern.compile(searchTerm, Pattern.CASE_INSENSITIVE);
        String line;

        while ((line = reader.readLine()) != null) {
            Matcher matcher = pattern.matcher(line);
            if (matcher.find()) {
                String[] bookDetails = line.split(", ");
                System.out.println("\n------------------------------\n");
                System.out.println("Book ID: " + bookDetails[0]);
                System.out.println("Title: " + bookDetails[1]);
                System.out.println("Author: " + bookDetails[2]);
                System.out.println("Genre: " + bookDetails[3]);
                System.out.println("Availability: " + bookDetails[4]);
            }
        }
    reader.close();

    }
}
