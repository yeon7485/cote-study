import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫 줄에 n(노드 개수)과 m(간선 개수) 입력받기
        int city = Integer.parseInt(br.readLine());
        int bus = Integer.parseInt(br.readLine());

        // 간선 정보를 저장할 리스트
        List<Map<Integer, Integer>> edges = new ArrayList<>();
        for(int i = 0; i < city; i++) {
            edges.add(new HashMap<>());
        }

        StringTokenizer st;
        // 간선 정보 입력받기
        for (int i = 0; i < bus; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            if(edges.get(u-1).containsKey(v - 1)) {
                if(edges.get(u-1).get(v - 1) <= w) {
                    continue;
                }
            }
            edges.get(u - 1).put(v - 1, w);
        }

        // 출발점과 도착점 입력받기
        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        BOJ_1916 boj = new BOJ_1916(city);
        System.out.println(boj.findPath(edges, start, end));
    
    }
}

class BOJ_1916 {

    private final int INF = Integer.MAX_VALUE;
    boolean[] visited;
    int[] costs;

    public BOJ_1916(int nodeCount) {
        visited = new boolean[nodeCount];
        costs = new int[nodeCount];

        Arrays.fill(visited, false);
        Arrays.fill(costs, INF);
    }

    public int findPath(List<Map<Integer, Integer>> edges, int start, int end) {

        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        pq.offer(new int[]{start - 1, 0});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            if(visited[cur[0]]) {
                continue;
            }
            visited[cur[0]] = true;
            costs[cur[0]] = cur[1];
            for(int next : edges.get(cur[0]).keySet()) {
                int newCost = edges.get(cur[0]).get(next) + cur[1];
                pq.offer(new int[]{next, newCost});
            }
        }

        return costs[end-1];

    }
}


