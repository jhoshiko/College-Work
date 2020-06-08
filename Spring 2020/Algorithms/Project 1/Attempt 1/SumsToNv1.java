
import java.io.*;
import java.util.*;

// Joshua Hoshiko

public class SumsToNv1 {
   public static void main (String[] args) throws IOException {
      
      // Initialize buffered reader for user input
      BufferedReader sysIn = new BufferedReader(new InputStreamReader(System.in));
      String fromUser;
      
      // Get valid input for n
      while (true) {
         System.out.print("Please enter a value for N: ");
         fromUser = sysIn.readLine();
         if (validateDigits(fromUser)) {
            break;
         }
         System.out.println("Input must be a number!");
      }
      
      // Create an ArrayList with range of 1 -> n
      ArrayList<Integer> range = getRange(Integer.parseInt(fromUser));

      findSums(range);
   }
   
   // Recursive methods for finding solutions
   // First method to call
   private static void findSums(ArrayList<Integer> valueList) {
      findSumsRecursive(valueList, valueList.size(), new ArrayList<Integer>());
   
   }
   // Second method for recursive calls
   private static void findSumsRecursive(ArrayList<Integer> valueList, int target, ArrayList<Integer> partialList) {
      int sum = 0;
      
      // Troubleshooting print. Confirms all subset lists are being created
      System.out.println(Arrays.toString(partialList.toArray()));
      
      // First check, if all the values add to equal the target
      for (int number: partialList) {
         sum += number;
      }
      
      // If the sum is the target and is not a single value, print the resulting sum
      if (sum == target && partialList.size() > 1) {
         System.out.println(formatSum(partialList)+" = "+ target);
      }
      
      // If we hit/exceeded the sum, return
      if (sum >= target) {
         return;
      }
      
      // Else, we loop and create subset lists for each value in the original list
      // Cycling the last value of the list for all combinations
      // Then, we recall the method with these subset lists
      for(int i = 0; i < valueList.size(); i++) {
         ArrayList<Integer> remainingList = new ArrayList<Integer>();
         int n = valueList.get(i);
         
         for (int j = i+1; j < valueList.size(); j++) {
            remainingList.add(valueList.get(j));
         }
         ArrayList<Integer> partialRec = new ArrayList<Integer>(partialList);
         partialRec.add(n);
         findSumsRecursive(remainingList, target, partialRec);
       } 
   }
   
   
   // Helper methods
   // Creates an array list of 1 -> a number n input
   private static ArrayList<Integer> getRange(int end) {
      ArrayList<Integer> result = new ArrayList<>();
      for (int i = 1; i <= end; i++) {
         result.add(i);
      }
      return result;
   }
   
   // Validates that the input n is valid
   private static boolean validateDigits(String input) {
      if (input.equals("")) {
         return false;
      }
      
      char[] characters = input.toCharArray();
      boolean validInput = true;
      
      for (char c : characters) {
         if (!Character.isDigit(c)) {
            validInput = false;
            break;
         }
      }
      return validInput;
    }
    
    // Formats the sum print out for convenience
    private static String formatSum (ArrayList<Integer> valueList) {
      String result = Integer.toString(valueList.get(0));
      for (int i = 1; i < valueList.size(); i++) {
         result = result + " + " + Integer.toString(valueList.get(i));
      }
      return result;
    }
}