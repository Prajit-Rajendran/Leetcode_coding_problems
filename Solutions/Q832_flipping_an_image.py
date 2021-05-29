class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        flipped_img = []
        for row in image:
            new_row = []
            row = list(reversed(row))
            for c in row:
                if c == 0:
                    new_row.append(1)
                else:
                    new_row.append(0)
            flipped_img.append(new_row)
        return flipped_img
        