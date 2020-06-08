

import static org.junit.Assert.*;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

/**
 * This is MonthTester which can be used to test your Month class. Please do not
 * make any changes to this class.
 *
 * @author  Dr. Salim Lakhani
 * @version 20181104
 */
public class MonthTester
{
    /**
     * Default constructor for test class MonthTester
     */
    public MonthTester()
    {
    }

    /**
     * Sets up the test fixture.
     *
     * Called before every test case method.
     */
    @Before
    public void setUp()
    {
    }

    /**
     * Tears down the test fixture.
     *
     * Called after every test case method.
     */
    @After
    public void tearDown()
    {
    }

    /**
     * Test no-arg constructor
     *
     */
    @Test
    public void testCase1()
    {
        Month month = new Month();
        assertEquals(1, month.getMonthNumber());
        assertEquals("January", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with invalid input.
     *
     */
    @Test
    public void testCase2()
    {
        Month month = new Month(0);
        assertEquals(1, month.getMonthNumber());
        assertEquals("January", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 1.
     *
     */
    @Test
    public void testCase3()
    {
        Month month = new Month(1);
        assertEquals(1, month.getMonthNumber());
        assertEquals("January", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 2.
     *
     */
    @Test
    public void testCase4()
    {
        Month month = new Month(2);
        assertEquals(2, month.getMonthNumber());
        assertEquals("February", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 3.
     *
     */
    @Test
    public void testCase5()
    {
        Month month = new Month(3);
        assertEquals(3, month.getMonthNumber());
        assertEquals("March", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 4.
     *
     */
    @Test
    public void testCase6()
    {
        Month month = new Month(4);
        assertEquals(4, month.getMonthNumber());
        assertEquals("April", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 5.
     *
     */
    @Test
    public void testCase7()
    {
        Month month = new Month(5);
        assertEquals(5, month.getMonthNumber());
        assertEquals("May", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 6.
     *
     */
    @Test
    public void testCase8()
    {
        Month month = new Month(6);
        assertEquals(6, month.getMonthNumber());
        assertEquals("June", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 7.
     *
     */
    @Test
    public void testCase9()
    {
        Month month = new Month(7);
        assertEquals(7, month.getMonthNumber());
        assertEquals("July", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 8.
     *
     */
    @Test
    public void testCase10()
    {
        Month month = new Month(8);
        assertEquals(8, month.getMonthNumber());
        assertEquals("August", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 9.
     *
     */
    @Test
    public void testCase11()
    {
        Month month = new Month(9);
        assertEquals(9, month.getMonthNumber());
        assertEquals("September", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 10.
     *
     */
    @Test
    public void testCase12()
    {
        Month month = new Month(10);
        assertEquals(10, month.getMonthNumber());
        assertEquals("October", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with input = 11.
     *
     */
    @Test
    public void testCase13()
    {
        Month month = new Month(11);
        assertEquals(11, month.getMonthNumber());
        assertEquals("November", month.getMonthName());
    }

    /**
     * Test monthNumber constructor with input = 12.
     *
     */
    @Test
    public void testCase14()
    {
        Month month = new Month(12);
        assertEquals(12, month.getMonthNumber());
        assertEquals("December", month.getMonthName());
    }
    
    /**
     * Test monthNumber constructor with invalid input.
     *
     */
    @Test
    public void testCase15()
    {
        Month month = new Month(13);
        assertEquals(1, month.getMonthNumber());
        assertEquals("January", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = January.
     *
     */
    @Test
    public void testCase16()
    {
        Month month = new Month("January");
        assertEquals(1, month.getMonthNumber());
        assertEquals("January", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = February.
     *
     */
    @Test
    public void testCase17()
    {
        Month month = new Month("February");
        assertEquals(2, month.getMonthNumber());
        assertEquals("February", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = March.
     *
     */
    @Test
    public void testCase18()
    {
        Month month = new Month("March");
        assertEquals(3, month.getMonthNumber());
        assertEquals("March", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = April.
     *
     */
    @Test
    public void testCase19()
    {
        Month month = new Month("April");
        assertEquals(4, month.getMonthNumber());
        assertEquals("April", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = May.
     *
     */
    @Test
    public void testCase20()
    {
        Month month = new Month("May");
        assertEquals(5, month.getMonthNumber());
        assertEquals("May", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = June.
     *
     */
    @Test
    public void testCase21()
    {
        Month month = new Month("June");
        assertEquals(6, month.getMonthNumber());
        assertEquals("June", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = July.
     *
     */
    @Test
    public void testCase22()
    {
        Month month = new Month("July");
        assertEquals(7, month.getMonthNumber());
        assertEquals("July", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = August.
     *
     */
    @Test
    public void testCase23()
    {
        Month month = new Month("August");
        assertEquals(8, month.getMonthNumber());
        assertEquals("August", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = Sepetmber.
     *
     */
    @Test
    public void testCase24()
    {
        Month month = new Month("September");
        assertEquals(9, month.getMonthNumber());
        assertEquals("September", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = October.
     *
     */
    @Test
    public void testCase25()
    {
        Month month = new Month("October");
        assertEquals(10, month.getMonthNumber());
        assertEquals("October", month.getMonthName());
    }
    
    /**
     * Test month name constructor with input = November.
     *
     */
    @Test
    public void testCase26()
    {
        Month month = new Month("November");
        assertEquals(11, month.getMonthNumber());
        assertEquals("November", month.getMonthName());
    }

    /**
     * Test month name constructor with input = December.
     *
     */
    @Test
    public void testCase27()
    {
        Month month = new Month("December");
        assertEquals(12, month.getMonthNumber());
        assertEquals("December", month.getMonthName());
    }
    
    /**
     * Tset copy constructor.
     *
     */
    @Test
    public void testCase28()
    {
        Month month = new Month("December");
        Month month2 = new Month (month);
        assertEquals(12, month2.getMonthNumber());
        assertEquals("December", month2.getMonthName());
    }
    
    /**
     * Test setMonthNumber method with invalid value.
     *
     */
    @Test
    public void testCase29()
    {
        Month month = new Month("December");
        month.setMonthNumber (0);
        assertEquals(1, month.getMonthNumber());
        assertEquals("January", month.getMonthName());
    }
    
    /**
     * Test setMonthNumber method with input = 1.
     *
     */
    @Test
    public void testCase30()
    {
        Month month = new Month("December");
        month.setMonthNumber (1);
        assertEquals(1, month.getMonthNumber());
        assertEquals("January", month.getMonthName());
    }
    
    /**
     * Test setMonthNumber method with input = 6.
     *
     */
    @Test
    public void testCase31()
    {
        Month month = new Month("December");
        month.setMonthNumber (6);
        assertEquals(6, month.getMonthNumber());
        assertEquals("June", month.getMonthName());
    }
    
    /**
     * Test setMonthNumber method with input = 12.
     *
     */
    @Test
    public void testCase32()
    {
        Month month = new Month(6);
        month.setMonthNumber (12);
        assertEquals(12, month.getMonthNumber());
        assertEquals("December", month.getMonthName());
    }
    
    /**
     * Test setMonthNumber method with invalid input.
     *
     */
    @Test
    public void testCase33()
    {
        Month month = new Month(6);
        month.setMonthNumber (13);
        assertEquals(1, month.getMonthNumber());
        assertEquals("January", month.getMonthName());
    }
    
    /**
     * Test equals method with two month objects having same value for monthNumber.
     *
     */
    @Test
    public void testCase34()
    {
        Month month1 = new Month(1);
        Month month2 = new Month(1);
        assertEquals(true, month1.equals(month2));
    }
    
    /**
     * Test equals method with two month objects having different value for monthNumber.
     *
     */
    @Test
    public void testCase35()
    {
        Month month1 = new Month(1);
        Month month2 = new Month(2);
        assertEquals(false, month1.equals(month2));
    }
    
    /**
     * Test lessThan method with two month objects haveing same value monthNumber.
     *
     */
    @Test
    public void testCase36()
    {
        Month month1 = new Month(1);
        Month month2 = new Month(1);
        assertEquals(false, month1.lessThan(month2));
    }
    
    /**
     * Test lessThan method.
     *
     */
    @Test
    public void testCase37()
    {
        Month month1 = new Month(1);
        Month month2 = new Month(2);
        assertEquals(true, month1.lessThan(month2));
    }
    
    /**
     * Test lessThan method.
     *
     */
    @Test
    public void testCase38()
    {
        Month month1 = new Month(2);
        Month month2 = new Month(1);
        assertEquals(false, month1.lessThan(month2));
    }
    
    /**
     * Test greaterThan method.
     *
     */
    @Test
    public void testCase39()
    {
        Month month1 = new Month(1);
        Month month2 = new Month(1);
        assertEquals(false, month1.greaterThan(month2));
    }
    
    /**
     * Test greaterThan method.
     *
     */
    @Test
    public void testCase40()
    {
        Month month1 = new Month(1);
        Month month2 = new Month(2);
        assertEquals(false, month1.greaterThan(month2));
    }
    
    /**
     * Test greaterThan method.
     *
     */
    @Test
    public void testCase41()
    {
        Month month1 = new Month(2);
        Month month2 = new Month(1);
        assertEquals(true, month1.greaterThan(month2));
    }
}

