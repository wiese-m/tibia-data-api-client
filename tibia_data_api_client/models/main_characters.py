from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_account_badges import MainAccountBadges
    from ..models.main_account_information import MainAccountInformation
    from ..models.main_achievements import MainAchievements
    from ..models.main_character import MainCharacter
    from ..models.main_deaths import MainDeaths
    from ..models.main_other_characters import MainOtherCharacters


T = TypeVar("T", bound="MainCharacters")


@_attrs_define
class MainCharacters:
    """
    Attributes:
        account_badges (Union[Unset, List['MainAccountBadges']]):
        account_information (Union[Unset, MainAccountInformation]):
        achievements (Union[Unset, List['MainAchievements']]):
        character (Union[Unset, MainCharacter]):
        deaths (Union[Unset, List['MainDeaths']]):
        other_characters (Union[Unset, List['MainOtherCharacters']]):
    """

    account_badges: Union[Unset, List["MainAccountBadges"]] = UNSET
    account_information: Union[Unset, "MainAccountInformation"] = UNSET
    achievements: Union[Unset, List["MainAchievements"]] = UNSET
    character: Union[Unset, "MainCharacter"] = UNSET
    deaths: Union[Unset, List["MainDeaths"]] = UNSET
    other_characters: Union[Unset, List["MainOtherCharacters"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_badges: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.account_badges, Unset):
            account_badges = []
            for account_badges_item_data in self.account_badges:
                account_badges_item = account_badges_item_data.to_dict()

                account_badges.append(account_badges_item)

        account_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_information, Unset):
            account_information = self.account_information.to_dict()

        achievements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.achievements, Unset):
            achievements = []
            for achievements_item_data in self.achievements:
                achievements_item = achievements_item_data.to_dict()

                achievements.append(achievements_item)

        character: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.character, Unset):
            character = self.character.to_dict()

        deaths: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deaths, Unset):
            deaths = []
            for deaths_item_data in self.deaths:
                deaths_item = deaths_item_data.to_dict()

                deaths.append(deaths_item)

        other_characters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.other_characters, Unset):
            other_characters = []
            for other_characters_item_data in self.other_characters:
                other_characters_item = other_characters_item_data.to_dict()

                other_characters.append(other_characters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_badges is not UNSET:
            field_dict["account_badges"] = account_badges
        if account_information is not UNSET:
            field_dict["account_information"] = account_information
        if achievements is not UNSET:
            field_dict["achievements"] = achievements
        if character is not UNSET:
            field_dict["character"] = character
        if deaths is not UNSET:
            field_dict["deaths"] = deaths
        if other_characters is not UNSET:
            field_dict["other_characters"] = other_characters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_account_badges import MainAccountBadges
        from ..models.main_account_information import MainAccountInformation
        from ..models.main_achievements import MainAchievements
        from ..models.main_character import MainCharacter
        from ..models.main_deaths import MainDeaths
        from ..models.main_other_characters import MainOtherCharacters

        d = src_dict.copy()
        account_badges = []
        _account_badges = d.pop("account_badges", UNSET)
        for account_badges_item_data in _account_badges or []:
            account_badges_item = MainAccountBadges.from_dict(account_badges_item_data)

            account_badges.append(account_badges_item)

        _account_information = d.pop("account_information", UNSET)
        account_information: Union[Unset, MainAccountInformation]
        if isinstance(_account_information, Unset):
            account_information = UNSET
        else:
            account_information = MainAccountInformation.from_dict(_account_information)

        achievements = []
        _achievements = d.pop("achievements", UNSET)
        for achievements_item_data in _achievements or []:
            achievements_item = MainAchievements.from_dict(achievements_item_data)

            achievements.append(achievements_item)

        _character = d.pop("character", UNSET)
        character: Union[Unset, MainCharacter]
        if isinstance(_character, Unset):
            character = UNSET
        else:
            character = MainCharacter.from_dict(_character)

        deaths = []
        _deaths = d.pop("deaths", UNSET)
        for deaths_item_data in _deaths or []:
            deaths_item = MainDeaths.from_dict(deaths_item_data)

            deaths.append(deaths_item)

        other_characters = []
        _other_characters = d.pop("other_characters", UNSET)
        for other_characters_item_data in _other_characters or []:
            other_characters_item = MainOtherCharacters.from_dict(other_characters_item_data)

            other_characters.append(other_characters_item)

        main_characters = cls(
            account_badges=account_badges,
            account_information=account_information,
            achievements=achievements,
            character=character,
            deaths=deaths,
            other_characters=other_characters,
        )

        main_characters.additional_properties = d
        return main_characters

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
