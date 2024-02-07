public class KaprekarSolver {
    public static int stepCount(int num) {
        final int kaprekarConst = 6174;
        int count = 0;

        while (num != kaprekarConst && num != 0) {
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
