import tsp

total_cost = []

def count_cost_rute(cost_rute, vertex, currentPos, n, count, cost):
    if count == n and cost_rute[currentPos][0]:
        total_cost.append(cost + cost_rute[currentPos][0])
        return
    for i in range(n):
        if (vertex[i] == False and cost_rute[currentPos][i]):
            vertex[i] = True
            count_cost_rute(cost_rute, vertex, i, n, count + 1, cost + cost_rute[currentPos][i])
            vertex[i] = False

if __name__ == "__main__":
    cost_rute = [[ 0,   100, 210, 100, 200 ],
                 [ 100, 0,   180, 80,  120 ],
                 [ 210, 180, 0,   125, 30  ],
                 [ 100, 80,  125, 0,   175 ],
                 [ 200, 120, 30,  175, 0   ]]
    v = [False for i in range(len(cost_rute))]
    v[0] = True
    count_cost_rute(cost_rute, v, 0, len(cost_rute), 1, 0)

    dcost = {(i,j): cost_rute[i][j] for i in range(len(cost_rute)) for j in range(len(cost_rute))}
    _, lintasan = tsp.tsp(range(len(cost_rute)), dcost)

    name_rute = {0: 'Gudang', 1: 'Toko A', 2: 'Toko B', 3: 'Toko C', 4: 'Toko D'}
    replacer = name_rute.get
    lintasan = [replacer(n, n) for n in lintasan]

    print("List Cost:", total_cost)
    print("Cost terendah adalah:", min(total_cost))
    print("Lintasan:", " -> ".join(lintasan), "-> Gudang")
