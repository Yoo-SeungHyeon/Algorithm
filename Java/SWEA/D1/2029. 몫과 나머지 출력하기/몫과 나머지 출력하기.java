import java.util.Scanner;
import java.io.IOException;

class Solution {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 1; i <= T; i++){
            int A = sc.nextInt();
            int B = sc.nextInt();

            System.out.printf("#%d %d %d\n", i, A/B, A%B);
        }
    }
}