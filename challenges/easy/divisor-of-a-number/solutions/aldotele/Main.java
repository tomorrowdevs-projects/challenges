public class Main {
    int number;

    public Main(int n) {
        number = n;
    }

    public int countDivisors() {
        int d = 0;
        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                d++;
            }
        }
        return d;
    }
    public static void main(String[] args) {
        Main myNum = new Main(5);  // change parameters here
        System.out.println(myNum.countDivisors());
    }
}
