# 1. 인접행렬 구성
# 2. 각 라운드에서 새로운 중간 node 설정(N라운드라면, N번 노드가 mid_node)
# 3. 더 짧은 길이 선택
# -> 위와 같은 과정은 N번 라운드에 거쳐 실행

# for(int i = 1; i<=n; i++){
#     for(int j =1; j<=n; j++){
#         if (i == j) dist[i][j] = 0;
#         else if (adj[i][j]) dist[i][j] = adj[i][j];
#         else dist[i][j] = INF;
#     }
# }

# for(int k = 1; k<= n; k++){
#     for(int i = 1; i <= n; i++){
#         for(int j = 1; j<=n; j++){
#             dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]);
#         }
#     }
# }