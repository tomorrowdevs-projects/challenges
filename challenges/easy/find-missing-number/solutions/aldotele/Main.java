public class Main {
    int[] incomingArr;
    int[] sortedArr;
    Integer missing;  // can be either a number or null

    public Main(int[] a) {
        incomingArr = a;
    }

    public void sortArr(int[] arr) {
        // nested loop to sort the provided Array in ascending order
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] > arr[j]) {
                    int temp = arr[i];  // variable used to store and switch
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        this.sortedArr = arr;
    }

    public Integer findMissing(int[] arr) {
        Integer missing = null;  // using Integer as it allows returning null (in case of no missing number)
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[i-1] + 1) {
                // if the following number is not equal to the previous plus 1, then there is a missing number
                missing = arr[i-1] + 1;
            }
        }
        this.missing = missing;
        return missing;
    }

    public static void main(String[] args) {
        int[] arr = {230, 222, 220, 224, 229, 221, 225, 223, 228, 226};  // change this to test with other arrays
        Main myArr = new Main(arr);
        myArr.sortArr(myArr.incomingArr);  // provided array gets sorted and stored
        myArr.findMissing(myArr.sortedArr);  // looking for missing numbers in sorted array
        
        if (myArr.missing != null) {
            System.out.println(myArr.missing);
        } else {
            System.out.println("no missing number.");
        }
    }
}
