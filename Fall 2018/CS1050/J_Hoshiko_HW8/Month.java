
/**
 * Creates a Month object which contains a month number.
 *
 * @author Joshua Hoshiko
 * @version November, 13, 2018
 */
public class Month
{
   int monthNumber;
   
   public Month(){
   monthNumber = 1;
   }
   public Month(int newMonth){
   if(newMonth > 12 || newMonth < 1)
       monthNumber = 1;
   else
       monthNumber = newMonth;
   }
   public Month(String monthName){
       switch(monthName){
       case "January":
       case "january":
            monthNumber = 1;
            break;
       case "February":
       case "february":
            monthNumber = 2;
            break;
       case "March":
       case "march":
            monthNumber = 3;
            break;
       case "April":
       case "april":
            monthNumber = 4;
            break;
       case "May":
       case "may":
            monthNumber = 5;
            break;  
       case "June":
       case "june":
            monthNumber = 6;
            break;
       case "July":
       case "july":
            monthNumber = 7;
            break;
       case "August":
       case "august":
            monthNumber = 8;
            break;
       case "September":
       case "september":
            monthNumber = 9;
            break;
       case "October":
       case "october":
            monthNumber = 10;
            break;
       case "November":
       case "november":
            monthNumber = 11;
            break;
       case "December":
       case "december":
            monthNumber = 12;
            break;
       default:
            monthNumber = 1;
       }
   }
   public Month(Month other){
   this.monthNumber = other.monthNumber;
   }
   public void setMonthNumber(int newMonth){
       if(newMonth > 12 || newMonth < 1)
            monthNumber = 1;
       else
            monthNumber = newMonth;
   }
   public int getMonthNumber(){
       return monthNumber;
   }
   public String getMonthName(){
       String name;
       switch(monthNumber){
       case 1:
            name = "January";
            break;
       case 2:
            name = "February";
            break;
       case 3:
            name = "March";
            break;
       case 4:
            name = "April";
            break;
       case 5:
            name = "May";
            break;  
       case 6:
            name = "June";
            break;
       case 7:
            name = "July";
            break;
       case 8:
            name = "August";
            break;
       case 9:
            name = "September";
            break;
       case 10:
            name = "October";
            break;
       case 11:
            name = "November";
            break;
       case 12:
            name = "December";
            break;
       default:
            name = "January";
       }
       return name;
   }
   public boolean equals(Month other){
   boolean equal = false;
   if(this.monthNumber == other.monthNumber)
        equal = true;
   return equal;
   }
   public boolean greaterThan(Month other){
   boolean greater = false;
   if(this.monthNumber > other.monthNumber)
        greater = true;
   return greater;
   }
   public boolean lessThan(Month other){
   boolean less = false;
   if(this.monthNumber < other.monthNumber)
        less = true;
   return less;
   }
}
