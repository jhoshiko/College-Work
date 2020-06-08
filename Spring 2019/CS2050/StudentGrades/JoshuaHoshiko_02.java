import java.util.Scanner;   // Import Scanner for reading text file 
import java.io.*;           // Import IO for reading text file
/**
 * Purpose:
 * This program will test the functionality of both the Student annd GradeItem classes
 * 
 * Assumptions:
 * None.
 *
 * CS2050
 * @author Joshua Hoshiko
 * @version February_5_2019
 */
public class JoshuaHoshiko_02
{   
    static Student student1;            // Student for testing constructor and toString
    static Student student2;            // Student for testing input file
    static Student student3;            // Student for testing equality
    static Student student4;            // Student for testing equality
    static GradeItem gradeItem1;        // GradeItem for testing constructor and toString
    static GradeItem gradeItem2;        // GradeItem for testing input file
    static GradeItem gradeItem3;        // GradeItem for testing equality
    static GradeItem gradeItem4;        // GradeItem for testing equality
    static final String INPUT_FILENAME = "Project_02_Input01.txt";
    
    public static void main(String[] args) {
        Scanner reader = null;      // Create scanner for test 2. 
        String[] inputArray1;       // Input array for file IO testing
        
        // Begin test 1(a)
        System.out.println("Test 1(a):");
        
        // Instantiate student1 with appropriate test parameters
        student1 = new Student("Jerry", "Freeman", "1022163", "jfreeman@msudenver.edu");
        
        // Test Student toString functionality
        System.out.println(student1 + "\n");
        
        System.out.println("***********************************************************\n");
        
        // Begin test 1(b)
        System.out.println("Test 1(b): ");
        
        // Instantiate gradeItem1 with appropriate test parameters
        gradeItem1 = new GradeItem("1022163", 4, "Biology", "Quiz", "20190215", 
                20, 16);
        
        // Test GradeItem toString functionality      
        System.out.println(gradeItem1+ "\n");
        System.out.println("***********************************************************\n");
        
        // Begin test 2(a)
        System.out.println("Test 2(a):");
        
        // Attempt to open file
        try {
            reader = new Scanner(new File(INPUT_FILENAME));
        } // End try
        catch(IOException e) {
            System.err.println("Error, unable to read file: " + INPUT_FILENAME);
        } // End catch
        
        // Split first input line from text file into inputArray1
        inputArray1 = reader.nextLine().split(",");
        
        // Test if the first input is "STUDENT" and then processes data if it is
        if (inputArray1[0].equals("STUDENT")) {
                processStudentData(inputArray1);
            } // End if
        else {
                System.out.println("The first element of the inputArray is not 'STUDENT', "
                        + "aborting.");
                System.exit(1);
            } //End Else
        
        // Display processed data in student2 using/testing getters
        System.out.println("First name: " + student2.getFirstName() + "\n"
                        + "Last name: " + student2.getLastName() + "\n"
                        + "ID: " + student2.getId() + "\n"
                        + "Email: " + student2.getEmail() + "\n");
                        
        System.out.println("***********************************************************\n");
        
        // Begin test 2(b)
        System.out.println("Test 2(b):");
        
        // Split second input line from text file to inputArray2
        String[] inputArray2 = reader.nextLine().split("\\,");
        
        // Test if the first input is "GRADE ITEM" and then processes data if it is
        if (inputArray2[0].equals("GRADE ITEM")) {
                processGradeItemData(inputArray2);
            } // End if
        else {
                System.out.println("The first element of the inputArray is not 'STUDENT', "
                        + "aborting.");
                System.exit(1);
            } //End Else
        
        // Display processed data in gradeItem2 using/testing getters
        System.out.println("Student ID: " + gradeItem2.getStudentId() + "\n"
                + "Item ID: " + gradeItem2.getItemId() + "\n"
                + "Course ID: " + gradeItem2.getCourseId() + "\n"
                + "Item type: " + gradeItem2.getItemType() + "\n"
                + "Date: " + gradeItem2.getDate() + "\n"
                + "Max score: " + gradeItem2.getMaxScore() + "\n"
                + "Actual Score: " + gradeItem2.getActualScore() + "\n");
        
        // Close input stream
        reader.close();
        System.out.println("***********************************************************\n");
        
        // Begin test 3(a)
        System.out.println("Test 3(a):");
        
        // Instantiate two identical student objects
        student3 = new Student("Jerry", "Freeman", "1022163", "jfreeman@msudenver.edu");
        student4 = new Student("Jerry", "Freeman", "1022163", "jfreeman@msudenver.edu");
        
        // Display contents of the student objects
        System.out.println("student3: " + student3 + "\n");
        System.out.println("student4: " + student4 + "\n");
        
        // Test student equals method
        System.out.println("Testing equality of student 3 and student 4:\n" 
                + student3.equals(student4) + "\n");
                
        System.out.println("***********************************************************\n");
                
        // Instantiate two different student objects
        student3 = new Student("Jeff", "Man", "3022198", "jman@msudenver.edu");
        student4 = new Student("Jerry", "Freeman", "1022163", "jfreeman@msudenver.edu");
        
        // Display contents of the student objects
        System.out.println("student3: " + student3 + "\n");
        System.out.println("student4: " + student4 + "\n");
        
        // Test student equals method
        System.out.println("Testing equality of student 3 and student 4:\n" 
                + student3.equals(student4) + "\n");
                
        System.out.println("***********************************************************\n");
        
        //Begin test 3(b)
        System.out.println("Test 3b:");
        
        // Instantiate two identical gradeitem objects
        gradeItem3 = new GradeItem("1022163", 4, "Biology", "Quiz", "20180215", 
                20, 16);
        gradeItem4 = new GradeItem("1022163", 4, "Biology", "Quiz", "20180215", 
                20, 16);
        
        // Display contents of the gradeitem objects     
        System.out.println("gradeItem3: " + gradeItem3 + "\n");
        System.out.println("gradeItem4: " + gradeItem4 + "\n");
        
        // Test gradeitem equals method
        System.out.println("Testing equality of grade item 3 and 4:\n" 
                + gradeItem3.equals(gradeItem4) + "\n");
                
        System.out.println("***********************************************************\n");
                
        // Instantiate two different gradeitem objects
        gradeItem3 = new GradeItem("1022163", 4, "Biology", "Quiz", "20180215", 
                20, 16);
        gradeItem4 = new GradeItem("3029765", 2, "Chemistry", "HW", "20180215", 
                20, 16);
        
        // Display contents of the gradeitem objects     
        System.out.println("gradeItem3: " + gradeItem3 + "\n");
        System.out.println("gradeItem4: " + gradeItem4 + "\n");
        
        // Test gradeitem equals method
        System.out.println("Testing equality of grade item 3 and 4:\n" 
                + gradeItem3.equals(gradeItem4) + "\n");
    }
    //----------------------------------------------------------------------------------------
    /**
     * The processStudentData method accepts a string array and attempts to instantiate a
     * student object with the data. The methods checks for the "ADD" keyword and assigns 
     * the rest of the data accordingly. If an invalid parameter is passed, it will catch 
     * the IllegalArgumentEception and display the error message from the student class.
     * @param studentData A String array holding data for a student object that requires processing.
     */
    private static void processStudentData(String[] studentData){
        // Check if key word "ADD" is present
        if (studentData[1].equals("ADD")) {
            
            // Attempt to instantiate student object with data
            try {
                student2 = new Student(studentData[2], studentData[3], studentData[4], 
                    studentData[5]);
            } // End try
            catch(IllegalArgumentException e) {
                System.err.println(e);
            } // End catch
        }
        else {
            System.out.println("Second element of studentData array is not 'ADD', aborting.");
            System.exit(1);
        } // End else
    }
    
    //----------------------------------------------------------------------------------------
    /**
     * The processGradeItemData method accepts a string array and attempts to instantiate a
     * gradeitem object with the data. The methods checks for the "ADD" keyword and assigns 
     * the rest of the data accordingly. If an invalid parameter is passed, it will catch 
     * the IllegalArgumentEception and display the error message from the gradeitem class.
     * @param gradeItemData A String array holding data for a gradeitem object that requires processing.
     */
    private static void processGradeItemData(String[] gradeItemData){
        if (gradeItemData[1].equals("ADD")) {
            
            // Attempt to instantiate gradeitem object with data
            try {
                gradeItem2 = new GradeItem(gradeItemData[2], 
                        Integer.parseInt(gradeItemData[3]), 
                        gradeItemData[4], gradeItemData[5], gradeItemData[6], 
                        Integer.parseInt(gradeItemData[7]), 
                        Integer.parseInt(gradeItemData[8]));
            } // End try
            catch(IllegalArgumentException e) {
                System.err.println(e);
            } // End catch
        }
        else {
            System.out.println("Second element of studentData array is not 'ADD', aborting.");
            System.exit(1);
        } // End else
    }
}
