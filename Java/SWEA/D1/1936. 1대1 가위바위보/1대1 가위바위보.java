import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		String[] input = sc.nextLine().split(" ");
		int A = Integer.parseInt(input[0]);
        int B = Integer.parseInt(input[1]);
        
        if(A > B){
        	System.out.print("A");
        } else {
        	System.out.print("B");
        }
	}
}