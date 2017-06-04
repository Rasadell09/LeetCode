class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        res = []
        decomStr = []
        contres = []
        aa = {}
        index = 0
        for i in range(len(paths)):
            tmp = paths[i].split(" ")
            for j in range(len(tmp)):
                if j != 0:
                    decomStr.append([])
                    decomStr[index].append(tmp[0])
                    decomStr[index].append(tmp[j])
                    index += 1
        for i in range(len(decomStr)):
            tmp = decomStr[i][1][decomStr[i][1].index('(') + 1:decomStr[i][1].index(')')]
            if tmp in aa:
                aa[tmp] += 1
            else:
                aa[tmp] = 1
        for k in aa.keys():
            if aa[k] != 1:
                contres.append(k)
                res.append([])
        for x in range(len(decomStr)):
            cont = decomStr[x][1][decomStr[x][1].index('(') + 1:decomStr[x][1].index(')')]
            decomStr[x][1] = decomStr[x][1][:decomStr[x][1].index('(')]
            for i in range(len(contres)):
                if cont == contres[i]:
                    res[contres.index(cont)].append("/".join(decomStr[x]))
        print res


s = Solution()
s.findDuplicate(["root/a 1.txt(abc) 2.txt(egh)", "root/c 3.txt(cd)", "root/c/d 4.txt(eh)", "root 4.txt(g)"])
