public class Main {
    public static void main(String[] args) {
        int num = Input.takeNumber();

        if (num < Constants.MIN_VALID || num > Constants.MAX_VALID) {
            System.out.println("Please enter a valid 4-digit number.");
            System.exit(1);
        }

        int steps = KaprekarSolver.stepCount(num);
        ResultDisplay.show(steps);
    }
}
