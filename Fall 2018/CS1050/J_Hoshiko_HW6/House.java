
/**
 * This class will draw a picture of a house, a sun and a person using various shapes.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class House
{
    /**
     * main method will create objects of various shapes, set their color, move
     * them to appropriate position, and make them visible.
     * 
     * @param args command line arguments
     */
    public static void main (String[] args)
    {

        //Task # 1 - Create a Wall
        Square wall = new Square();
        wall.moveHorizontal(-140);
        wall.moveVertical(20);
        wall.changeSize(120);
        wall.makeVisible();

        //Code for task # 2 - Create a window
        Square window = new Square();
        window.moveHorizontal(-120);
        window.moveVertical(20);
        window.changeColor("black");
        window.changeSize(40);
        window.makeVisible();
        //Code for task # 3 - Create a roof
        Triangle roof = new Triangle();
        roof.moveHorizontal(20);
        roof.moveVertical(-60);
        roof.changeSize(60, 180);
        roof.changeColor("blue");
        roof.makeVisible();
        //Code for task # 4 - Create a sun
        Circle sun = new Circle();
        sun.moveHorizontal(100);
        sun.moveVertical(-40);
        sun.changeColor("yellow");
        sun.changeSize(80);
        sun.makeVisible();
        //Code for task # 5 - Create a person
        Person person = new Person();
        person.moveHorizontal(40);
        person.moveVertical(30);
        person.makeVisible();
        //Code for task # 6 - Move the person to left so it
        //is under the window.
        person.slowMoveHorizontal(-110);
        //Code for task # 7 - Move the person to right so it
        //is under the sun.
        person.slowMoveHorizontal(160);
        
    }

}
