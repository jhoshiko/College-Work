import java.util.Objects;
/**
 * The list class is an abstract datatype list based on an array. It has many functions to
 * manage the list. It is important to note that list ignores the element 0.
 *
 * @author Joshua Hoshiko
 * @version 20190304
 */
public class List<T> implements MyCollectionInterface<T>
{
    private T[] list;                  // Abstract list array
    private int numberOfEntries;       // Total number of entries in the list
    private int frequency;             // Frequency variable to cound number similar items
    private int len;                   // Length variable, holds value for max size of list
    private static final int DEFAULT_CAPACITY = 50;     // Default size of list is 50
//============================================================================================    
    /**
     * Default constructor for a list. Sets size to DEFAULT_CAPACITY
     */
    public List() {
        len = DEFAULT_CAPACITY;                 // Set length variable to default size
        T[] tempList = (T[])new Object[len+1];  // Caste a temp list full of null objects
        list = tempList;                        // Set list to this null object list
        numberOfEntries = 0;                    // Starting number of entries is 0
    }
//============================================================================================    
    /**
     * Constructor that sets the size to a desired value
     * 
     * @param len The desired max size of the list
     */
    public List(int len) {
        // Check if given length is greater than 0
        if(len <= 0) {
            throw new IllegalArgumentException("List size must be greater than 0");
        } // End if
        this.len = len;                         // Set lnegth variable to given length                     
        T[] tempList = (T[])new Object[len+1];  // Caste a temp list full of null objects
        list = tempList;                        // Set list to this null object list
        numberOfEntries = 0;                    // Starting number of entries is 0
    }
//============================================================================================    
    /**
    * Adds a new entry to this collection
    * 
    * @param newItem The object to be added to the collection
    * @return True if the addition is successful, or false if not.
    */
    public boolean add (T newItem) {
        // Check to see if list is full and if not, adds a new item to the list
        if(numberOfEntries != len) {
            list[numberOfEntries+1] = newItem;
            numberOfEntries++;
            return true;
        } // End if
        return false;
    }
//============================================================================================    
    /**
    * Removes one unspecified entry from the collection, if possible.
    *
    * @return Either the removed entry, if the removal was successful, or null.
    */
    public T remove () {
        //Check if list is empty
        if(numberOfEntries == 0) {
                return null;
        }
        // Remove the last item in the list and return that item
        T item = list[numberOfEntries];
        list[numberOfEntries] = null;
        numberOfEntries--;
        return item;
    }
//============================================================================================   
    /**
    * Removes one occurrence of a given entry from this collection.
    *
    * @param anEntry The entry to be removed.
    * @return true if the removal was successful, false if not.
    */
    public boolean remove (T anEntry) {
        // Check if list is empty
        if(numberOfEntries == 0) {
                return false;
        } // End if
        // Scan list for the value
        for(int i = 1; i <= numberOfEntries; i++) {
            // If the value is found, remove it and adjust the other items 
            // in the list if necessary
            if(anEntry.equals(list[i])) {
                if(i < numberOfEntries){
                    for(int j = i; j < numberOfEntries; j++){
                        list[j] = list[j + 1];
                    } // End for
                    list[numberOfEntries] = null;
                    numberOfEntries--;
                    return true;
                } // End if
                else {
                    list[i] = null;
                    numberOfEntries--;
                    return true;
                } // End else
            } // End if
        } // End for
        return false;
    }
//============================================================================================    
    /**
    * Removes all entries from this collection.
    */
    public void clear() {
        // If the  list isn't empty, remove all items
        if (numberOfEntries != 0) {
            for(int i = 1; i <= numberOfEntries; i++) {
                list[i] = null;
            } // End for
            numberOfEntries = 0;
        } // End if
    }
//============================================================================================    
    /**
    * Gets the current number of entries in this collection.
    *
    * @return The integer number of entries currently in the collection.
    */
    public int getCurrentSize() {
        return numberOfEntries;
    }
//============================================================================================    
    /**
    * Check to see if the collection is empty.
    *
    * @return True if the collection is empty, or false if not.
    */
    public boolean isEmpty() {
        // Return ttrue if the list is empty
        if(numberOfEntries == 0) {
            return true;
        }
        return false;
    }
//============================================================================================    
    /**
    * Counts the number of times a given entry appears in this collection.
    *
    * @param anEntry The entry to be counted.
    * @return The number of times anEntry appears in the collection.
    */
    public int getFrequencyOf(T anEntry) {
        // Set frequency counter to 0 for new count
        frequency = 0;
        // If the list is empty, don't bother searching
        if(numberOfEntries == 0) {
            return 0;
        } // End if
        
        // Search items and increment frequency counter for each match
        for(int i = 1; i <= numberOfEntries; i++) {
            if(anEntry.equals(list[i])) {
                frequency++;
            } // End if
        } // End for
        return frequency;
    }
//============================================================================================    
    /**
    * Tests whether this collection contains a given entry.
    *
    * @param anEntry The entry to locate.
    * @return True if the collection contains anEntry, or false if not.
    */
    public boolean contains(T anEntry) {
        // If the list is empty, don't bother searching
        if(numberOfEntries == 0) {
            return false;
        } // End if
        // Search for atleast one match
        for(int i = 1; i <= numberOfEntries; i++) {
            if(anEntry.equals(list[i])) {
                return true;
            } // End if
        } // End for
        return false;
    }
//============================================================================================    
    /**
    * Retrieves all entries that are in this collection.
    *
    * @return A newly allocated array of all the entries in the collection. 
    * Note: If the collection is empty, the returned array is empty.
    */
    public Object[] toArray() {
        // Object array for returning after list is converted
        Object[] outputArray = new Object[numberOfEntries];
        // If list is empty, return null
        if(numberOfEntries == 0){
                return null;
        } // End if
        // For each item in th elist, copy it to the array
        for(int i = 0; i < numberOfEntries; i++) {
            outputArray[i] = (Object) list[i+1];
        } // End for
        return outputArray;
    } // End toArray
}
