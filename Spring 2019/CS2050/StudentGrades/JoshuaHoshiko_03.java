import java.util.Scanner;   // Import Scanner for reading text file 
import java.io.*;           // Import IO for reading text file
import java.util.Objects;   // Import for Object arrays
/**
 * This class is designed to test the List class and to process data about students and 
 * their grade items. This class reads form an input file and then generates an output file 
 * with a data report
 *
 * @author Joshua Hoshiko
 * @version 20190304
 */
public class JoshuaHoshiko_03
{
    static List<Student> studentList;       // List for storing students
    static List<GradeItem> gradeItemList;   // List for storing Grade Items
    static Student student;                 // Student object for data transfer
    static GradeItem gradeItem;             // Grade Item object for data transfer
    static Scanner reader = null;           // Reader for input file reading
    static PrintWriter output = null;       // PrintWriter for writing to output file
    static final String INPUT_FILE = "Project_03_Input01.txt";      // Input file name
    static final String OUTPUT_FILE = "Project_03_Output01.txt";    // Output file name
    
    /**
     * Main Method for initializing lists and facilitating data processing.
     */
    public static void main(String[] args) {
    studentList = new List<Student>();      // Make a list of type Student
    gradeItemList = new List<GradeItem>();  // make a list of typoe Grade Item
    processInput();                         // Begin data processing phase
    generateReport();                       // Begin report generation
    reader.close();                         // Close input stream
    output.close();                         // Close output stream
    }
//============================================================================================    
    /**
     * Process input opens the necessary files, reads a data file and calls 
     * the appropriate data processing methods for students and for grade items.
     */
    public static void processInput() {
        // Attempt to open input file
        String[] inputArray;
        try {
            reader = new Scanner(new File(INPUT_FILE));
        } // End try
        catch(IOException e) {
            System.err.println("Error, unable to read file: " + INPUT_FILE);
            System.exit(1);
        } // End catch
        //Attempt to open output file
        try {
            output = new PrintWriter(new File(OUTPUT_FILE));
        } // End try
        catch(IOException e) {
            System.err.println("Error, unable to read file: " + OUTPUT_FILE);
            System.exit(1);
        } // End catch
        
        // Read throught the input file and call the Appropriate methods
        while(reader.hasNextLine()){
            inputArray = reader.nextLine().split(",");
            
            // Test if the first input is "STUDENT" and then processes data if it is
            if (inputArray[0].equals("STUDENT")) {
                processStudentData(inputArray);
            } // End if
            // test if the first input is "GRADE ITEM" and then process data if it is
            else if (inputArray[0].equals("GRADE ITEM")) {
                processGradeItemData(inputArray);
            } // End if
            // Display an error message if the first input is not a keyword
            else {
                System.err.println("The first element: " + inputArray[0] 
                        + " from inputArray is not\n" 
                        + "'STUDENT' or 'GRADE ITEM', "
                        + "aborting.");
                System.exit(1);
            } //End Else
        }
    }
//============================================================================================
    /**
     * Process student data handles all student data and can add 
     * or remove from the student list.
     */    
    public static void processStudentData(String[] info) {
        boolean validStudent = true; // Boolean value for tracking whether student is valid
        
        // Check if key word "ADD" is present
        if (info[1].equals("ADD")) {
            
            // Attempt to instantiate student object with data
            try {
                student = new Student(info[2], info[3], info[4], 
                    info[5]);
            } // End try
            catch(IllegalArgumentException e) {
                System.err.println(e);
                validStudent = false;
            } // End catch
            // Check to see if student is a duplicate
            if(studentList.contains(student) && validStudent) {
                System.err.println("Student: " + student.getFirstName() 
                        + " " + student.getLastName() 
                        + " is already on the list, aborting.");
                validStudent = false;
            } // End if
            
            //Attempt to add the student if it is a valid student
            if(validStudent) {
                if(studentList.add(student)) {
                    System.out.println("Added Student: " + student.getFirstName() 
                           + " " + student.getLastName() 
                           + " to the list");
                } // End if
                else {
                    System.err.println("Error adding Student: " + student.getFirstName() 
                            + " " + student.getLastName() 
                            + " to the list");
                } // End else
            } // End if
        } // End if
        // Check if key word "DEL" is present
        else if (info[1].equals("DEL")) {
            
            // Attempt to instantiate student object with data
            try {
                student = new Student(info[2], info[3], info[4], 
                    info[5]);
            } // End try
            catch(IllegalArgumentException e) {
                System.err.println(e);
                validStudent = false;
            } // End catch
            
            //Attempt to remove student from the list if it is a valid student
            if(validStudent){
                if(studentList.remove(student)){
                    System.out.println("Removed Student: " 
                            + student.getFirstName() 
                            + " " + student.getLastName() 
                            + " from the list");
                        } // End if
                else{
                    System.err.println("Error, unable to remove student: " 
                            + student.getFirstName() 
                            + " " + student.getLastName());
                }  //End else
            } // End if
        } // End else if
        // If no keyword is read, return an error message
        else {
            System.err.println("Second element of student info array is not 'ADD' "
                    + "or 'DEL', aborting.");
        } // End else
    }
//============================================================================================
    /**
     * Proces grade item data handles all grade item data and can add or remove from the
     * grade item list.
     */    
    public static void processGradeItemData(String[] info) {
        boolean validGradeItem = true;  // Boolean value for tracking whether GradeItem 
                                        // is valid 
        // Check if key word "ADD" is present
        if (info[1].equals("ADD")) {
            
            // Attempt to instantiate gradeitem object with data
            try {
                gradeItem = new GradeItem(info[2], 
                        Integer.parseInt(info[3]), 
                        info[4], info[5], info[6], 
                        Integer.parseInt(info[7]), 
                        Integer.parseInt(info[8]));
            } // End try
            catch(IllegalArgumentException e) {
                System.err.println(e);
                validGradeItem = false;
            } // End catch
            // Check to see if grade item is a duplicate
            if(gradeItemList.contains(gradeItem) && validGradeItem) {
                System.err.println("Grade Item: " + gradeItem.getItemId() 
                        + " for " + gradeItem.getStudentId() 
                        + " is already on the list, aborting.");
                validGradeItem = false;
            } // End if
            // If the item is valid, add it to the list
            if(validGradeItem) {
                if(gradeItemList.add(gradeItem)){
                    System.out.println("Added Grade Item: " + gradeItem.getItemId() 
                            + " for " + gradeItem.getStudentId() 
                            + " to the list");
                } // End if
                else{
                    System.err.println("Error adding Grade Item: " + gradeItem.getItemId() 
                            + " for " + gradeItem.getStudentId() 
                            + " to the list");
                }
            } // End if
        } // End if
        // Check if key word "DEL" is present 
        else if (info[1].equals("DEL")) {
            
            // Attempt to instantiate gradeitem object with data
            try {
                gradeItem = new GradeItem(info[2], 
                        Integer.parseInt(info[3]), 
                        info[4], info[5], info[6], 
                        Integer.parseInt(info[7]), 
                        Integer.parseInt(info[8]));
            } // End try
            catch(IllegalArgumentException e) {
                System.err.println(e);
                validGradeItem = false;
            } // End catch
            
            //Attempt to remove student from the list if it is a valid grade item
            if(validGradeItem){
                if(gradeItemList.remove(gradeItem)){
                    System.out.println("Removed Grade Item: " + gradeItem.getItemId() 
                                + " for " + gradeItem.getStudentId() 
                                + " from the list");
                 } // End if
                 else{
                     System.err.println("Error removing Grade Item: " + gradeItem.getItemId() 
                                + " for " + gradeItem.getStudentId() 
                                + " from the list");
                }  //End else
            }
        } // End if
        // If no keyword is read, return an error message
        else {
            System.err.println("Second element of student info array is not 'ADD' "
                    + "or 'DEL', aborting.");
        } // End else
    }
//============================================================================================    
    /**
     * Generate report takes all the relevant data in the lists, sorts them, and then formats
     * a report to be written to an output file.
     */
    public static void generateReport() {
        
        Object[] students = studentList.toArray();  // Convert list to an array
        Object[] grades = gradeItemList.toArray();  // Convert list to an array
        Student s1;                                 // Student for holding data from array
        GradeItem g1;                               // Grade item for holding data from array
        int totalGradeItems;    // Holds total quantity of gradeitems for a student
        int totalMaxScore;      // Holds total points for a student's grade
        int totalActualScore;   // Holds total achieved points by the student
        double percentage;      // Holds the percentage the student has in the class
        // For all students, search for their grade items and format their report
        for(int i = 0; i < students.length; i++) {
            totalGradeItems = 0;
            totalMaxScore = 0;
            totalActualScore = 0;
            s1 = (Student) students[i];
            output.println(s1.toString());
            output.println("    Grade-Items:");
            // Search grade items for matching student IDs 
            // and add them to their respective student
            for(int j = 0; j < grades.length; j++){
                g1 = (GradeItem) grades[j];
                if(s1.getId().equals(g1.getStudentId())) {
                    output.println("    " + g1.getItemId() + "  " + g1.getCourseId()
                            + "  " + g1.getItemType() + "  " + g1.getDate()
                            + "  " + g1.getMaxScore() + "  " + g1.getActualScore());
                    totalGradeItems++;
                    totalMaxScore += g1.getMaxScore();
                    totalActualScore += g1.getActualScore();
                } // End if
            } // End for
            // Format and add their point totals and percentage in the class
            percentage = (totalActualScore / ((double)totalMaxScore)) * 100;
            output.println("=====================================================");
            output.println("    Total:              Max: " + totalMaxScore + "  Actual: "
                    + totalActualScore + "  Percentage: " + percentage + "%\n\n");
            
        } // End for
    } // End generateReport
}
