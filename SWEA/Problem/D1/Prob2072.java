package SWEA.Problem.D1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 100ms 18740KB

public class Prob2072 {
    public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {

			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int sum = 0;

			for (int j = 0; j < 10; j++) {

				int num = Integer.parseInt(st.nextToken());

				if (num % 2 == 1) sum += num; 
			}

			sb.append("#" + (i+1) + " " + sum + "\n");
		}

		System.out.println(sb);
		br.close();
	}
}
