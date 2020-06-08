import java.util.Objects;
/**
 * Purpose:
 * GradeItem will contain information pertaining to a specific assignment.
 * The information includes the assignment type, maximum score, actual grade, date completed,
 * course ID, and assignment ID.
 * 
 * Assumptions: 
 * None.
 *
 * CS2050
 * @author Joshua Hoshiko
 * @version January_24_2019
 */ 
public class GradeItem
{
   private String studentId;        // Student identification number
   private int itemId;              // Item identification number
   private String courseId;         // Course identification number
   private String itemType;         // Grade item type
   private String date;             // Date of completion
   private int maxScore;            // Maximum score possible
   private int actualScore;         // Actual score on assignment
   
   // Array of accepted grade item types
   private final String[] ITEM_TYPE_ARRAY = {"HW", "Quiz", "Class Work", "Test", "Final"}; 
   //-----------------------------------------------------------------------------------------
   /**
    * Default Constructor
    */
   public GradeItem() {
       studentId = "";
       itemId = 0;
       courseId = "";
       itemType = "";
       date = "";
       maxScore = 0;
       actualScore = 0;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * GradeItem constructor accepts seven parameters for the appropriate field information.
    * Parameters are checked for blank information, valid item type, 
    * and valid max/actual score ranges.
    * @param studentId Student identification number string.
    * @param itemId Item identification number integer
    * @param courseId Course identification string
    * @param itemType Grade item type string
    * @param date Date of completion string
    * @param maxScore Maximum score for assignment integer
    * @param actualScore Score achieved by the student integer
    */
   public GradeItem(String studentId, int itemId, String courseId, String itemType, 
   String date, int maxScore, int actualScore) {
       
       // An array containing all strings to check for a blank entry and 
       // boolean flag for whether item type is a valid type
       
       String[] stringArray = {studentId, courseId, itemType, date}; 
       boolean gradeItemPass = false; 
       
       // Loop through string array to check for blank parameters
       
       for (int i = 0; i < stringArray.length; i++) {
           if(stringArray[i].equals("")){
               throw new IllegalArgumentException("Error: GradeItem field cannot be blank.");
           } // End if
       } // End for
       
       // Loop through item type array to check whether given item type is valid
       
       for (int i = 0; i < ITEM_TYPE_ARRAY.length; i++) {
           if(itemType.equals(ITEM_TYPE_ARRAY[i])){
               gradeItemPass = true;
           } // End if
       } // End for
       
       // Check for if item type flag is false. Throws exception if false
       if (!gradeItemPass) {
           throw new IllegalArgumentException("Error: Invalid grade item type");
       } // End if
       
       // Max score must be greater than 0
       
       if (maxScore < 0) {
           throw new IllegalArgumentException("Error: Max score: " 
           + maxScore + " must be greater than 0");
       } // End if
       
       // Actual score must fall between 0 and "max score"
       
       if (actualScore < 0 || actualScore > maxScore) {
           throw new IllegalArgumentException("Error: Actual score: " 
                    + actualScore + " must be greater than 0"
                    + " and less than or equal to max score: " + maxScore);
       } // End if
       
       // Assign data to field accordingly
       
       this.studentId = studentId;
       this.itemId = itemId;
       this.courseId = courseId;
       this.itemType = itemType;
       this.date = date;
       this.maxScore = maxScore;
       this.actualScore = actualScore;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * Returns student ID string
    * @return String studentId - Returns student id string.
    */
   public String getStudentId() {
       return studentId;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * Returns item ID integer
    * @return int itemId - Returns item id integer.
    */
   public int getItemId() {
       return itemId;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * Returns course ID string
    * @return String courseId - Returns course id string.
    */
   public String getCourseId() {
       return courseId;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * Returns Item type string
    * @return String itemType - Returns item type string.
    */
   public String getItemType() {
       return itemType;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * Returns date string
    * @return String date - Returns date of completion string.
    */
   public String getDate() {
       return date;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * Returns max score integer
    * @return int maxScore - Returns maximum score integer.
    */
   public int getMaxScore() {
       return maxScore;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * Returns actual score integer
    * @return int actualScore - Returns actual score integer
    */
   public int getActualScore() {
       return actualScore;
   }
   //-----------------------------------------------------------------------------------------
   public int hashCode() {
        int hash = 3;
        hash += 97 * hash + Objects.hashCode(this.studentId);
        hash += 97 * hash + Objects.hashCode(this.itemId);
        hash += 97 * hash + Objects.hashCode(this.courseId);
        hash += 97 * hash + Objects.hashCode(this.itemType);
        hash += 97 * hash + Objects.hashCode(this.date);
        hash += 97 * hash + Objects.hashCode(this.maxScore);
        hash += 97 * hash + Objects.hashCode(this.actualScore);
        return hash;
    } // End hashCode
   
   /**
    * The equals method compares two GradeItems and compares whether 
    * their attributes are equal.
    * @param other Another GradeItem object to compare attributes to.
    * @return boolean result - Returns true if both objects contain the same attributes
    */
   public boolean equals(Object obj) {
       boolean result = false; // Result as to whether tow students are equal
       
       // Check to see if all fields of this object are the same as the given object
       
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
        GradeItem other = (GradeItem) obj;
        
        if ( Objects.equals(this.studentId, other.studentId) &&
             Objects.equals(this.itemId, other.itemId) &&
             Objects.equals(this.courseId,  other.courseId)  &&
             Objects.equals(this.itemType, other.itemType)  &&
             Objects.equals(this.date, other.date) &&
             Objects.equals(this.maxScore,  other.maxScore)  &&
             Objects.equals(this.actualScore, other.actualScore)){
                isEqual = true;
        }
        return isEqual;
   }
   //-----------------------------------------------------------------------------------------
   /**
    * toString will return a string containing all of the grade item information
    * @return String resultString - Returns string with all GradeItem attributes
    * @override Overrides toString
    */
   public String toString() {
      
       // Create a formatted string with all field information
       
       String resultString = "Student ID: " + studentId + "\n"
                + "Item ID: " + itemId + "\n"
                + "Course ID: " + courseId + "\n"
                + "Item type: " + itemType + "\n"
                + "Date: " + date + "\n"
                + "Max score: " + maxScore + "\n"
                + "Actual Score: " + actualScore;
      return resultString;         
   }
}


