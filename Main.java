public class Main {
    public static void main(String[] args) {
        int num = UserInput.takeNumber();

        if (num < 1000 || num > 9999) {
            System.out.println("Please enter a valid 4-digit number.");
            System.exit(1);
        }

        int steps = KaprekarSolver.stepCount(num);
        ResultDisplay.show(steps);
    }
}
