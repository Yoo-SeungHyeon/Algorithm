import java.util.Scanner;
import java.lang.StringBuilder;

class Solution
{
	public static void main(String args[]) throws Exception {
		Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder("");
		String input=sc.nextLine();
        sc.close();
        int len = input.length();
        char splitChar;
		for (int i = 0; i < len; i++){
            splitChar = input.charAt(i);
            if (97 <= splitChar && splitChar <= 122){
                splitChar -= 32;
                sb.append(splitChar);
            }else{
                sb.append(splitChar);
            }
        }
        System.out.println(sb);
	}
}