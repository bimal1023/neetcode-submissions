class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for op in operations:
            if op=="+":
                new_score=record[-1]+record[-2]
                record.append(new_score)
            elif op=="D":
                new_score=record[-1]*2
                record.append(new_score)
            elif op=="C":
                record.pop()
            else:
                record.append(int(op))
        return sum(record)
