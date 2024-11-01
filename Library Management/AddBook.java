import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class AddBook {
    public static void createFile() throws IOException {
        File lib = new File("lib_data.txt");
        if (lib.createNewFile()) {
            System.out.println("File created: " + lib.getName());
          } else {
            System.out.println("File already exists.");
          }
    }

    public static void addBooks() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter Book ID: ");
        String bookID = scanner.nextLine();
        System.out.println("Enter Title: ");
        String title = scanner.nextLine();
        System.out.println("Enter Author: ");
        String author = scanner.nextLine();
        System.out.println("Enter Genre: ");
        String genre = scanner.nextLine();
        
        String availability = "Available";
        String status = "Checked in";

        String book = bookID + ", " + title + ", " + author + ", " + genre + ", " + availability + ", " + status;

        try {
            FileWriter writer = new FileWriter("lib_data.txt", true); // 'true' to append data
            writer.write(book + "\n");
            writer.close();
            System.out.println("Book details added to text file.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }

    public static void main(String[] args) throws IOException {
        // createFile();
    }
}