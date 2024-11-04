import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		int c = scan.nextInt();
		System.out.println(a + b - c);

		String num = Integer.toString(a) + Integer.toString(b);
		System.out.println(Integer.parseInt(num) - c);
	}
}
