import javax.swing.JOptionPane;
/**
 * This program accepts a meals subtotal and calculates tip and sales tax. 
 * The program then calculates a final cost.
 *
 * @author Joshua Hoshiko
 * @version 09202018
 */
public class TaxAndTip
{
    public static void main(String[] args){
     double subTotal;
     double total; 
     String subTotalString;
     
     subTotalString = JOptionPane.showInputDialog("Input Meal Sub-Total: ");
     subTotal = Double.parseDouble(subTotalString);
     total = subTotal + Tax(subTotal) + Tip(subTotal);
     JOptionPane.showMessageDialog(null, "Meal Charge: " + subTotal + "\n Sales Tax: " 
     + Tax(subTotal) + "\nTip: " + Tip(subTotal) + "\nTotal Bill: " + total);
     
    }
    /**
     * The Tax method accepts a sub-total and calculates the tax total for the meal.
     */
    public static double Tax(double subTotal){
    final double TAX_PERCENT = 0.075;
    double taxTotal = subTotal * TAX_PERCENT;
    return taxTotal;
    }
    /**
     * The Tip method accepts a sub-total and calculates the tip total for the meal.
     */
    public static double Tip(double subTotal){
    final double TIP_PERCENT = 0.18;
    double tipTotal = subTotal * TIP_PERCENT;
    return tipTotal;
    }
}
