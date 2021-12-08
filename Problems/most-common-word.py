from typing import Counter, List


class Solution:
    def clean_text(self, paragraph):
        text_rmv = re.sub(
            "[-=+,#/\?:;^.@*\"※~ㆍ!』‘|\(\)\[\]`'…》\”\“\’·]", " ", paragraph
        )
        text_rmv = " ".join(text_rmv.split())
        return text_rmv

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        temp = self.clean_text(paragraph).lower().split()
        world_dict = dict(Counter(temp))
        for ban in banned:
            if ban in world_dict.keys():
                del world_dict[ban]
        return max(world_dict, key=lambda x: world_dict[x])
