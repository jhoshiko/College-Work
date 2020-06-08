import java.util.Scanner;
/**
 * This program lets users input the amount of cookies they want to eat. 
 * The program will then report the amount of calories the user ate.
 *
 * @author Joshua Hoshiko
 * @version 09202018
 */
public class Cookies
{
  public static void main(String[] args){
  Scanner kb = new Scanner(System.in);
  double cookies = 0;
  double calories = 0;
 
  System.out.println("A bag of cookies holds 40 cookies and 10 servings.\nA serving equals 300 calories.\n"
  + "How many cookies do you want to eat?");
  cookies = kb.nextDouble();
  calories = Calories(Servings(cookies));
  System.out.printf("The number of calories you have eaten is:  %.2f", calories);
  
  
  }
  
  /**
   * The Servings method accepts a number of cookies eaten and then calculates the amount of 
   * serving for that amount of cookies.
   */
  public static double Servings(double cookiesEaten){
      double servingsEaten;
      final double SERVING = 4;
      
      servingsEaten = cookiesEaten/SERVING;
      return servingsEaten;
  }
  /**
   *The Calories method accepts a number of servings of cookies and then calculates the amount
   *of calories consumed.
   */
  public static double Calories(double numberServings){
      double eatenCalories = 0;
      final double CAL_SERVING = 300;
      
      eatenCalories = numberServings*CAL_SERVING;
      return eatenCalories;
  }
}
