import random

comparison_count = 0

def min_max_dc(arr, low, high):
    global comparison_count
    # Base case: single element
    if low == high:
        return arr[low], arr[low]
    
    # Base case: two elements
    if high - low == 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    # Divide
    mid = (low + high) // 2
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)
    
    # Conquer: combine with 2 comparisons
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin
    
    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax
    
    return overall_min, overall_max

def min_max_naive(arr):
    if not arr:
        return None, None, 0
    mn, mx = arr[0], arr[0]
    comps = 0
    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x
        else:
            comps += 1
            if x > mx:
                mx = x
    return mn, mx, comps

# Demonstration on small array
arr = [3, 1, 7, 4, 9, 2, 3, 5, 6, 0]
comparison_count = 0
mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc_comps = comparison_count
naive_mn, naive_mx, naive_comps = min_max_naive(arr)

print(f"Array: {arr}")
print(f"Min: {mn}, Max: {mx}")
print(f"D&C Comparisons: {dc_comps}")
print(f"Naive Comparisons: {naive_comps}")

# Performance Analysis
print(f"\n{ 'Size':>8} {'DC Comps':>12} {'Naive Comps':>14} {'Formula 3n/2-2':>16}")
print("-" * 56)
for size in [10, 100, 1000, 10000]:
    arr_rand = [random.randint(1, 10000) for _ in range(size)]
    comparison_count = 0
    mn, mx = min_max_dc(arr_rand, 0, len(arr_rand) - 1)
    dc = comparison_count
    _, _, naive = min_max_naive(arr_rand)
    form = int(3 * size / 2 - 2)
    print(f"{size:>8} {dc:>12} {naive:>14} {form:>16}")
