import java.util.Objects;
/**
 * Purpose:
 * The Student class contains student information such as ID, name, and student email
 * 
 * Assumptions: 
 * None
 * 
 * CS2050
 * @author Joshua Hoshiko
 * @version January_24_2019
 */
public class Student
{
    // Declare Fields
    private String id;          // Student identification number
    private String firstName;   // Student first name
    private String lastName;    // Student last name
    private String email;       // Student email
    //----------------------------------------------------------------------------------------
    /**
     * Default constructor
     */
    public Student() {
        id = "";
        firstName = "";
        lastName = "";
        email = "";
    }
   //----------------------------------------------------------------------------------------
    /**
     * Student Constructor which accepts strings for a first and last name, id, and email.
     * The parameters are also checked for blank information and the email string is checked
     * for an "@" symbol.
     * @param firstName First name string of the student
     * @param lastName Last name string of the student
     * @param id Student's identification number string
     * @param email Student's email address string
     */
    public Student(String firstName, String lastName, String id, String email) {
        String[] stringArray = {firstName, lastName, id, email}; // String array to check data 
        
        // Loop through string array to check for blank parameters
        
        for (int i = 0; i < stringArray.length; i ++) {
            if (stringArray[i].equals("")) {
               throw new IllegalArgumentException("Error: Atleast one student field is blank.");
           } // End if
        }
        
        // Check for "@" symbol in email
        
        if (!(email.contains("@"))) {
            throw new IllegalArgumentException ("Error: Student email: "
                    + email + " must have an '@'");
        } // End if
        
        // Assign data to fields accordingly
        
        this.firstName = firstName;     // Set firstName to the given parameter
        this.lastName = lastName;       // Set lastName to the given parameter
        this.id = id;                   // Set id to the given parameter
        this.email = email;             // Set email to the given parameter
    }
    //----------------------------------------------------------------------------------------
    /**
     * @return String id - Returns student's identification number string.
     */
    public String getId() {
        return id; 
    }
   //-----------------------------------------------------------------------------------------
    /**
     * @return String firstName - Returns first name string.
     */
   public String getFirstName() {
       return firstName;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * @return String lastName - Returns last name string.
    */
   public String getLastName() {
       return lastName;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * @return String email - Returns email string.
    */
   public String getEmail() {
       return email;
   }
   //-----------------------------------------------------------------------------------------
   public int hashCode() {
        int hash = 3;
        hash += 97 * hash + Objects.hashCode(this.id);
        hash += 97 * hash + Objects.hashCode(this.firstName);
        hash += 97 * hash + Objects.hashCode(this.lastName);
        hash += 97 * hash + Objects.hashCode(this.email);
        return hash;
   } // End hashCode
   //-----------------------------------------------------------------------------------------
   /**
    * The equals method compares two students and compares whether all of their
    * attributes are equal.
    * @param other Student object to compare attributes to.
    * @return boolean result - True if the two students have the same attributes
    */
   public boolean equals(Object obj) {
       boolean isEqual = false;
        if (this == obj) {
            return true;
        }
        // Make sure the object is not null
        if (obj == null) {
            return false;
        }
        // Makes sure class types are equivalent
        if (getClass() != obj.getClass()) {
            return false;
        }

        // Cast the object to that of the same type as this object
        // Student would cast as Student, and GradeItem as GradeItem
        Student other = (Student) obj;
        if ( Objects.equals(this.id, other.id) &&
             Objects.equals(this.firstName, other.firstName) &&
             Objects.equals(this.lastName,  other.lastName)  &&
             Objects.equals(this.email, other.email)) {
                isEqual = true;
        }
        return isEqual;
   } // End equals
   //-----------------------------------------------------------------------------------------
   /**
    * toString will return a string containing all of the student's information
    * @return String resultString - String containing all student information
    * @override Overrides toString
    */
   public String toString() {
       
       // Create a formatted string with all field information
       
       // String resultString = "First name: " + firstName + "\n"
                // + "Last name: " + lastName + "\n"
                // + "ID: " + id + "\n"
                // + "Email: " + email;
       String resultString = id + " " + firstName + " " + lastName + " " + email;
       return resultString;     
   }
    
}
