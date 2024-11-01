import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;

public class BorrowBook {
    public static void borrowBook() throws IOException {
        Scanner inpObj = new Scanner(System.in);
        System.out.println("Enter Book ID to borrow: ");
        String bookID = inpObj.next();
        
        File inputFile = new File("lib_data.txt");
        File tempFile = new File("books_temp.txt");

        BufferedReader reader = new BufferedReader(new FileReader(inputFile));
        FileWriter writer = new FileWriter(tempFile);
        
        String line;
        while ((line = reader.readLine()) != null) {
            String[] bookDetails = line.split(", ");
            if (bookDetails[0].equals(bookID)) {
                if (bookDetails[4].equals("Available")) {
                    bookDetails[4] = "Unavailable";
                    bookDetails[5] = "Checked out";
                    String newLine = String.join(", ", bookDetails);
                    writer.write(newLine + "\n");
                    System.out.println("Book: " + bookID + " checked out.");
                } else {
                    System.out.println("Book is not available for borrowing.");
                    writer.write(line + "\n");
                }
            } else {
                writer.write(line + "\n");
            }
        }
        reader.close();
        writer.close();

        inputFile.delete();
        tempFile.renameTo(inputFile);
        
    }
}
