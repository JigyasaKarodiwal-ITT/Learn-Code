public class KaprekarSolver {
    public static int stepCount(int num) {
        int count = 0;

        while (num != Constants.kaprekarConstant && num != 0) {
            int nextStep = KaprekarCalculator.calculateDifference(num);
            System.out.println(num + " -> " + nextStep);
            num = nextStep;

            if (num == 0) {
                break;
            }

            count++;
        }

        return count;
    }
}
