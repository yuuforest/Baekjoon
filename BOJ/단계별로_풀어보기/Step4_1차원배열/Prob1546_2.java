package BOJ.단계별로_풀어보기.Step4_1차원배열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 132ms 14556KB

public class Prob1546_2 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int num = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer (br.readLine(), " ");

        float max = 0;
        float sum = 0;
        float[] floatArray = new float[num];

        for (int i = 0; i < num; i++) {
            floatArray[i] = Float.parseFloat(st.nextToken());

            if (max < floatArray[i]) {
                max = floatArray[i];
            }
        }

        for (int i = 0; i < num; i++) {
            sum += floatArray[i] / max * 100;
        }

        sb.append(sum/num);

        System.out.println(sb);

        br.close();
    }
}