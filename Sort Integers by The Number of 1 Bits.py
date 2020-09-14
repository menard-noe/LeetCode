from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dict_number_bits = dict()
        arr = sorted(arr)

        dict_memo_count_bits = {0: 0, 1: 1}

        def count_bits(val: int):
            if val in dict_memo_count_bits:
                return dict_memo_count_bits[val]
            else:
                if val % 2 == 1:
                    dict_memo_count_bits[val] = count_bits(val // 2) + 1
                    return dict_memo_count_bits[val]
                else:
                    dict_memo_count_bits[val] = count_bits(val // 2)
                    return dict_memo_count_bits[val]

        for val in arr:
            queue_values = dict_number_bits.get(count_bits(val), [])
            queue_values.append(val)
            dict_number_bits[count_bits(val)] = queue_values

        res = []
        sorted_key = sorted(dict_number_bits)
        for key in sorted_key:
            res.extend(dict_number_bits[key])
        return res


if __name__ == "__main__":
    arr = [10,100,1000,10000]
    solution = Solution()
    print(solution.sortByBits(arr))