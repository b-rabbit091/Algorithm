class Solutions(object):

    def find_permutation(self, elems, nums, index, res):

        res.append(elems[:])

        if index == len(nums):
            return

        for i in range(index, len(nums)):
            elems.append(nums[i])
            self.find_permutation(elems, nums, i + 1, res)
            elems.pop()
        return

    def driver(self):
        nums = [1, 2, 3]
        elems = []
        res = []
        self.find_permutation(elems, nums, 0, res)
        print(res)


obj = Solutions()
obj.driver()
