from enum import Enum


class GetV3HighscoresWorldCategoryVocationPageVocation(str, Enum):
    ALL = "all"
    DRUIDS = "druids"
    KNIGHTS = "knights"
    PALADINS = "paladins"
    SORCERERS = "sorcerers"

    def __str__(self) -> str:
        return str(self.value)
