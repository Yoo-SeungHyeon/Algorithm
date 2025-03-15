import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
        String T;
		T=sc.nextLine();
        sc.close();
        int num = 0;
		for(int i = 0; i < T.length(); i++)
		{
            num = T.charAt(i) - 64;
            System.out.print(num + " ");
        }
	}
}