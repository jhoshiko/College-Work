import java.util.Scanner;
/**
 * Thermostat is designed to test the Hvac and its various methods
 *
 * @author Joshua Hoshiko
 * @version October 29, 2018
 */
public class Thermostat
{
    public static void main(String[] args){
        Hvac test = new Hvac(50, 5);
        Scanner kB = new Scanner(System.in);
        String choice = new String();
        boolean quit = false;
        
        System.out.println("The current temperature is: " + test.getTemperature());
        while(!quit){
            System.out.println("A. Display current temperature.\nB. Increase the temperature.\n"
                           +"C. Decrease the temperature.\nQ. Quit"
                           +"\nPlease make a selection: \n");
            choice = kB.nextLine();
            switch(choice){
                case "A":
                case "a":
                System.out.println("The current temperature is: " + test.getTemperature() 
                                    +"\n");
                break;
                case "B":
                case "b":
                System.out.println("Increasing temperature...\n");
                test.warmer();
                break;
                case "C":
                case "c":
                System.out.println("Decreasing temperature...\n");
                test.cooler();
                break;
                case "Q":
                case "q":
                System.out.println("Program is exiting...");
                quit = true;
                break;
                default:
                System.out.println("Please enter a valid input!\n");
            }
        }
    }
}

