
/**
 * Hvac class simulate a HVAC system. It has four fields: temperature, min,
 * max, and delta. Temperature of the heater goes up and down by delta. It
 * can never go below min and above max
 *
 * @author Salim Lakhani
 * @version 20171008
 */
public class Hvac
{
    private int temperature;
    private int min;
    private int max;
    private int delta;
    
    /**
     * Initializes a newly created Heater object using the arguments value for
     * temperature and delta. min is set to the default value of 0 and max is set
     * to default value of 100.
     * @param inTemperatur Initial value for temperature
     * @param delta Initial value for delta
     */
    public Hvac (int inTemperature, int inDelta)
    {
        min = 0;
        max = 100;
        temperature = inTemperature;
        delta = inDelta;
        
    }
    
    /**
     * Return current value of temperature
     * @return current value of temperature
     */
    public int getTemperature ()
    {
        return temperature;
    }
    
    /**
     * Set the new value for delta. If the new value is negative or 0
     * then delta will be set to default value of 5
     * @param newDelta new value for delta
     */
    public void setDelta (int newDelta)
    {
        delta = newDelta;
        
        if (delta <= 0)
        {
            delta = 5;
        }
            
    }
    
    /**
     * Mutator method that will cool down the heater by reducing the temperatur
     * by delta. If temperature falls below min then it will set it to min.
     */
    public void cooler ()
    {
        temperature = temperature - delta;
        
        if (temperature < min)
        {
            temperature = min;
        }
    }
    
    
    /**
     * Mutator method that will warm up the heater by increasing the temperatur
     * by delta. If temperature falls above max then it will set it to max.
     */
    public void warmer ()
    {
        temperature = temperature + delta;
        
        if (temperature > max)
        {
            temperature = max;
        }
    }
    
}
