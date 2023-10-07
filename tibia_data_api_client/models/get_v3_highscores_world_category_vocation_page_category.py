from enum import Enum


class GetV3HighscoresWorldCategoryVocationPageCategory(str, Enum):
    ACHIEVEMENTS = "achievements"
    AXEFIGHTING = "axefighting"
    BOSSPOINTS = "bosspoints"
    CHARMPOINTS = "charmpoints"
    CLUBFIGHTING = "clubfighting"
    DISTANCEFIGHTING = "distancefighting"
    DROMESCORE = "dromescore"
    EXPERIENCE = "experience"
    FISHING = "fishing"
    FISTFIGHTING = "fistfighting"
    GOSHNARSTAINT = "goshnarstaint"
    LOYALTYPOINTS = "loyaltypoints"
    MAGICLEVEL = "magiclevel"
    SHIELDING = "shielding"
    SWORDFIGHTING = "swordfighting"

    def __str__(self) -> str:
        return str(self.value)
