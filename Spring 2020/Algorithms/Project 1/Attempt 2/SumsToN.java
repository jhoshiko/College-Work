import java.io.*;
import java.util.*;

// Joshua Hoshiko
// Version 2

public class SumsToN {

   public static void main(String[] args) throws IOException {
	   
      // Initialize buffered reader for user input
      BufferedReader sysIn = new BufferedReader(new InputStreamReader(System.in));
      String fromUser;
      int N;
      
      // Get valid input for N
      while (true) {
         System.out.print("Please enter a value for N: ");
         fromUser = sysIn.readLine();
         if (validateDigits(fromUser)) {
            break;
         }
         System.out.println("Input must be a number!");
      }
      N = Integer.parseInt(fromUser);
      
      findSums(N,N,new ArrayList<Integer>());
   }
   
   // Method to find all the sum subsets to N
   public static void findSums(int N, int curr, ArrayList<Integer> list) {
      int sum = 0;
    
      // First check, if all the values add to equal the target
      for (int number: list) {
         sum += number;
      }
      
      // if the list is larger than 1 and equal to the target, print and return 
      if(curr == 0 && sum == N && list.size() > 1) {
         System.out.println(formatSum(list)+" = "+ N);
         return;
      }
      
      // Else, we loop and create subset lists for each value in the original list
      // Cycling the last value of the list for all combinations (Also making sure we add a value
      // as large as the previous to avoid duplicates)
      // Then, we recall the method with these new lists
      for(int i = 1; i <=N ; i++) {
         if(i<=curr) {
            ArrayList<Integer> newList = new ArrayList<Integer>(list);
            if(newList.size() > 0 && i < newList.get(newList.size() - 1)) {
                newList.add(newList.get(newList.size() - 1));
            }
            else {
               newList.add(i);
            }
            findSums(N, curr-i, newList);
         }
      }
   }
   // Helper Methods
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
    private static String formatSum(ArrayList<Integer> list) {
      String result = Integer.toString(list.get(0));
      for(int i = 1; i < list.size(); i++) {
         result = result + " + " + Integer.toString(list.get(i));
      }
      return result;
    }

}