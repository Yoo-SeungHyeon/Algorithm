import java.util.Scanner;
import java.io.IOException;

class Solution {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        int P = sc.nextInt();
        int K = sc.nextInt();
        sc.close();
        int result = 0;
        if(P >= K) {
            result = P - K + 1;
        } else {
            result = 1000 + P - K + 1;
        }
        System.out.println(result);
    }
}