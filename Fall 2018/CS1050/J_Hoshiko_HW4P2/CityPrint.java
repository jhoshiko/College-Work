import java.util.Scanner;
/**
 * This Program will accept a city name and then print variations of the city name
 *
 * @author Joshua Hoshiko
 * @version 09202018
 */
public class CityPrint
{
    public static void main(String[] args){
    String cityName;
    Scanner kb = new Scanner(System.in);
    
    System.out.println("Please input your favorite city name:");
    cityName = kb.nextLine();
    System.out.println("Number of characters: " + cityName.length());
    System.out.println("Name in uppercase: " + cityName.toUpperCase());
    System.out.println("Name in lowercase: " + cityName.toLowerCase());
    char first = cityName.charAt(0);
    System.out.println("The first character is: " + first);
    }
}
