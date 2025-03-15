import java.util.Scanner;
import java.io.IOException;

class Solution{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.close();
        for(int i = 1; i <= T; i++){
            System.out.print("#");
        }
    }
}