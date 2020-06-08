public class AddTwo
{
	public static void main(String[] args) throws java.io.IOException
	{
		java.util.Scanner reader = new java.util.Scanner(System.in);
		System.out.print("Insert A: ");
		int a = reader.nextInt();
		System.out.print("Insert B: ");
		int b = reader.nextInt();
		System.out.print("A + B = ");
		System.out.println(a+b);
	}
}
