from client import StoerWagnerMinCut

def main():
    print("=== Stoer-Wagner Global Min Cut ===")
    solver = StoerWagnerMinCut()
    # Triangle graph where each edge has weight 2 -> any vertex partition cuts 2 edges = weight 4
    w_mat = [
        [0, 2, 2],
        [2, 0, 2],
        [2, 2, 0]
    ]

    res = solver.find_min_cut(3, w_mat)
    print("Min Cut Result:", res)
    assert res["global_min_cut_weight"] == 4

    print("Stoer-Wagner Min Cut verified successfully!")

if __name__ == "__main__":
    main()
