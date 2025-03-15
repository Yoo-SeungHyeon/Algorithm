import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
        int target;
        int year;
        int month;
        int day;
        
        for(int test_case = 1; test_case <= T; test_case++)
		{
			target = sc.nextInt();
            year = target/10000;
            month = (target%10000)/100;
            day = (target%10000)%100;
            switch(month){
                case 2:
                    if(01<=day&&day<=28){
                     	System.out.printf("#%d %04d/%02d/%02d\n",test_case,year,month,day);   
                        break;
                    }else{
                    	System.out.printf("#%d -1\n",test_case);
                        break;
                    }
                case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                     if(01<=day&&day<=31){
                     	System.out.printf("#%d %04d/%02d/%02d\n",test_case,year,month,day);   
                        break;
                    }else{
                    	System.out.printf("#%d -1\n",test_case);
                    	break;
                    }
                case 4: case 6: case 9: case 11:
                     if(01<=day&&day<=28){
                     	System.out.printf("#%d %04d/%02d/%02d\n",test_case,year,month,day);   
                        break;
                    }else{
                    	System.out.printf("#%d -1\n",test_case);
                        break;
                    }
                default:
                    System.out.printf("#%d -1\n",test_case);
            }
		}
	}
}