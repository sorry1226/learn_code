
def minMutation( start, end, bank):
    """
    :type  start: str, end: str, bank: List[str]
    :rtype: n: int
    """
    if end not in bank: return -1
    front = {start}
    back = {end}
    dist = 0
    geneList = set(bank)
    gene_len = len(start)

    while front:
        dist += 1
        next_front = set()
        for gene in front:
            for i in range(gene_len):
                for c in ['A','C','G','T']:
                    if c != gene[i]:
                        new_gene = gene[:i] + c + gene[i+1:]
                        if new_gene in back:
                            return dist
                        if new_gene in geneList:
                            next_front.add(new_gene)
                            geneList.remove(new_gene)

        front = next_front
        if len(back) < len(front):
            front, back = back, front
    return -1


if __name__ == '__main__':
    start= "AAAAACCC"
    end= "AACCCCCC"
    bank= ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    print(minMutation(start, end, bank))
