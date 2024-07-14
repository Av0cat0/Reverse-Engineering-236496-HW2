from itertools import permutations,combinations


numbers = range(1, 13)
print(numbers)
combinations_of_4 = combinations(numbers, 4)
valid_combinations = [comb for comb in combinations_of_4 if sum(comb) == 26]

def find_disjoint_pairs(comb_list):
    disjoint_pairs = []
    for comb1, comb2 in combinations(comb_list, 2):
        if not set(comb1) & set(comb2):  # Check if intersection is empty
            disjoint_pairs.append((comb1, comb2))
    return disjoint_pairs

disjoint_pairs = find_disjoint_pairs(valid_combinations)
groups = [[set(pair[0]), set(pair[1])] for pair in disjoint_pairs]
groups.extend([[set(pair[1]), set(pair[0])] for pair in disjoint_pairs])
print(groups)
all_numbers = set(range(12))
for group_idx, group in enumerate(groups, start=1):
    for perm1 in permutations(group[0]):
        for perm2 in permutations(group[1]):
            combined_set = group[0] | group[1]
            missing_numbers = list(all_numbers - combined_set)
            for perm in permutations(missing_numbers):
                if perm[0]+perm1[1]+perm[1]+perm2[0] == 26 and \
                        perm1[2]+perm[0]+perm[2]+perm2[3] == 26 and \
                        perm2[1]+perm[1]+perm1[0]+perm[3] == 26 and \
                        perm2[2]+perm[2]+perm1[3]+perm[3] == 26 and \
                        perm[0]+perm[3]+perm1[0]+perm2[0]+perm1[3]+perm2[3] == 26:
                    print(f"{perm[0]} {perm1} {perm[1]} {perm[2]} {perm2} {perm[3]}")
