from django.shortcuts import render
import itertools

# Class xử lý đồ thị
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = [[0] * num_vertices for _ in range(num_vertices)]  # Ma trận kề

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight  # Đồ thị vô hướng

    def find_hamiltonian_cycle(self):
        vertices = list(range(self.num_vertices))
        min_path = None
        min_cost = float("inf")

        # Tạo tất cả hoán vị bắt đầu từ đỉnh 0
        for perm in itertools.permutations(vertices[1:]):  
            path = [0] + list(perm) + [0]
            cost = sum(self.edges[path[i]][path[i+1]] for i in range(len(path) - 1))

            if cost < min_cost:
                min_cost = cost
                min_path = path

        return min_path, min_cost

# Xử lý request từ form
def index(request):
    if request.method == "POST":
        try:
            input_data = request.POST["graph_data"].strip().split("\n")
            num_vertices, num_edges = map(int, input_data[0].split())

            graph = Graph(num_vertices)

            for line in input_data[1:num_edges + 1]:  # Đọc các cạnh
                u, v, weight = map(int, line.split())
                graph.add_edge(u - 1, v - 1, weight)  # Chỉnh index từ 1-based → 0-based

            path, cost = graph.find_hamiltonian_cycle()

            if path:
                result = f"Path: {' → '.join(str(v + 1) for v in path)} (Cost: {cost})"
            else:
                result = "Không tìm thấy chu trình Hamilton."

            return render(request, "index.html", {"result": result})

        except Exception as e:
            return render(request, "index.html", {"error": str(e)})

    return render(request, "index.html")
