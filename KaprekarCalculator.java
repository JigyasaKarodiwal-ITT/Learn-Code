import java.util.Arrays;

public class KaprekarCalculator {
    public static int calculateDifference(int num) {
        int[] digits = new int[4];
        for (int i = 3; i >= 0; --i) {
            digits[i] = num % 10;
            num /= 10;
        }

        Arrays.sort(digits);
        int ascending = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3];
        int descending = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0];

        return descending - ascending;
    }
}
