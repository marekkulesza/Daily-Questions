package codewars;

public class forLoopIntList{

    public static int grow(int[] x) {
        int counter = 1;

        for (int i : x) {
            counter *= i;
        }
        return counter;
    }

    public static void main(String[] args) {
        System.out.println(grow(new int[]{1,2,3}));
    }
}