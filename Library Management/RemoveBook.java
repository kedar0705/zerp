import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;

public class RemoveBook {
    public static void removeBook() throws IOException {
        Scanner inpObj = new Scanner(System.in);
        System.out.println("Enter Book ID to remove: ");
        String bookID = inpObj.next();
        inpObj.close();
        
        File inputFile = new File("lib_data.txt");
        File tempFile = new File("books_temp.txt");

        BufferedReader reader = new BufferedReader(new FileReader(inputFile));
        FileWriter writer = new FileWriter(tempFile);
        
        String line;
        while ((line = reader.readLine()) != null) {
            String[] bookDetails = line.split(", ");
            if (!bookDetails[0].equals(bookID)) {
                writer.write(line + "\n");
            }
        }
        reader.close();
        writer.close();

        inputFile.delete();
        tempFile.renameTo(inputFile);
        
        System.out.println("Book with ID " + bookID + " removed.");
    }

}
