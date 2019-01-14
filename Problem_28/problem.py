import unittest

def solve(case):
    '''
        result = []
        developing = ""
        current = ""
        the quick brown, distribute = 1
        fox jumps over, distribute = 2
        the lazy dog, distribute = 4

        split on line by space
        the, quick, brown --> Exclude last element
        the, quick
        if length == 1
        buffer on right
        elm[0] += ' ' * k - distribute

        fox, jumps, over
        fox, jumps, distribute 2
        i = 0
        while distribute > 0:
            elm[i] += ' '
            i++
            if i >= len(list)
                i = 0
            distribute --
            if distribute == 0
            break
        
            Complexity = O(n) for preprocessing and O(m*d) for spacing, O(n*m*d)
    '''
    string_list = case[0]
    k = case[1]
    
    resulting_list = []
    developing_word = ""

    distributor = []
    # Build resulting list
    for i in range(len(string_list)):
        if (len(developing_word) + len(string_list[i]) + 1) <= k:
            if len(developing_word) == 0:
                developing_word = string_list[i]
                continue
            developing_word += ' ' + string_list[i]
        else:
            distributor.append(k - len(developing_word))
            resulting_list.append(developing_word)
            developing_word = string_list[i]
    distributor.append(k - len(developing_word))
    resulting_list.append(developing_word)

    for idx, elm in enumerate(resulting_list):
        i = 0
        elm_split = elm.split(' ')
        elm_split = [elms + ' ' if idx < len(elm_split) - 1 else elms for idx, elms in enumerate(elm_split)]
        while distributor[idx] > 0:
            if i >= len(elm_split) - 1:
                i = 0
            elm_split[i] += ' '
            i += 1
            distributor[idx] -= 1
        resulting_list[idx] = ''.join(elm_split)

    return resulting_list

class Test(unittest.TestCase):

    data = [((["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16), ["the  quick brown",
                                                                        "fox  jumps  over", "the   lazy   dog"]),
            ((["the"], 5), ["the  "])]

    def test(self):
        for case, expected in self.data:
            actual = solve(case)
            self.assertEquals(actual, expected)

if __name__ == '__main__':
    unittest.main()