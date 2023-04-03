function solution(n, computers) {
  let answer = 0;
  const visited = Array.from({ length: n }, () => false);

  function bfs(i) {
    const queue = [];
    queue.push(i);

    while (queue.length) {
      x = queue.shift();
      visited[x] = true;
      for (let j = 0; j < n; j++) {
        if (!visited[j] && computers[x][j] && computers[j][x] && x !== j) {
          queue.push(j);
        }
      }
    }
  }
  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      bfs(i);
      answer++;
    }
  }
  return answer;
}
