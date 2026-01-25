// For more information on JavaDoc, visit: https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html


/**
 * This is a class documentation example.
 * Ideally you would put something very descriptive about the class here.
 *
 * @author Your Name
 * @version 1.0 <-- Not always used.
 * @since 2024-06-15 <-- Could be date or version.
 *
 */
public class JavaDoc {
    /**
     * This method adds two integers.
     *
     * @param a the first integer to add
     * @param b the second integer to add
     * @return the sum of a and b
     */
    public int add(int a, int b) {
        return a + b;
    }

    /**
     * This method subtracts one integer from another.
     *
     * @param a the integer to subtract from
     * @param b the integer to subtract
     * @return the result of a minus b
     */
    public int subtract(int a, int b) {
        return a - b;
    }

    /**
     * This method multiplies two integers.
     *
     * @param a the first integer to multiply
     * @param b the second integer to multiply
     * @return the product of a and b
     */
    public int multiply(int a, int b) {
        return a * b;
    }

    /**
     * This method divides one integer by another.
     *
     * @param a the integer to be divided
     * @param b the integer to divide by
     * @return the quotient of a divided by b
     * @throws ArithmeticException if b is zero <-- This is an example of a throw tag. Throwing is when there is an unrecoverable error or you want to halt the program in a harsh way.
     */
    public int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Division by zero is not allowed.");
        }

        return a / b;
    }
}