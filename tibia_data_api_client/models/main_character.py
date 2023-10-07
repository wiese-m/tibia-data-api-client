from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_character_guild import MainCharacterGuild
    from ..models.main_houses import MainHouses


T = TypeVar("T", bound="MainCharacter")


@_attrs_define
class MainCharacter:
    """
    Attributes:
        account_status (Union[Unset, str]):
        achievement_points (Union[Unset, int]):
        comment (Union[Unset, str]):
        deletion_date (Union[Unset, str]):
        former_names (Union[Unset, List[str]]):
        former_worlds (Union[Unset, List[str]]):
        guild (Union[Unset, MainCharacterGuild]):
        houses (Union[Unset, List['MainHouses']]):
        last_login (Union[Unset, str]):
        level (Union[Unset, int]):
        married_to (Union[Unset, str]):
        name (Union[Unset, str]):
        residence (Union[Unset, str]):
        sex (Union[Unset, str]):
        title (Union[Unset, str]):
        traded (Union[Unset, bool]):
        unlocked_titles (Union[Unset, int]):
        vocation (Union[Unset, str]):
        world (Union[Unset, str]):
    """

    account_status: Union[Unset, str] = UNSET
    achievement_points: Union[Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    deletion_date: Union[Unset, str] = UNSET
    former_names: Union[Unset, List[str]] = UNSET
    former_worlds: Union[Unset, List[str]] = UNSET
    guild: Union[Unset, "MainCharacterGuild"] = UNSET
    houses: Union[Unset, List["MainHouses"]] = UNSET
    last_login: Union[Unset, str] = UNSET
    level: Union[Unset, int] = UNSET
    married_to: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    residence: Union[Unset, str] = UNSET
    sex: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    traded: Union[Unset, bool] = UNSET
    unlocked_titles: Union[Unset, int] = UNSET
    vocation: Union[Unset, str] = UNSET
    world: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_status = self.account_status
        achievement_points = self.achievement_points
        comment = self.comment
        deletion_date = self.deletion_date
        former_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.former_names, Unset):
            former_names = self.former_names

        former_worlds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.former_worlds, Unset):
            former_worlds = self.former_worlds

        guild: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guild, Unset):
            guild = self.guild.to_dict()

        houses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.houses, Unset):
            houses = []
            for houses_item_data in self.houses:
                houses_item = houses_item_data.to_dict()

                houses.append(houses_item)

        last_login = self.last_login
        level = self.level
        married_to = self.married_to
        name = self.name
        residence = self.residence
        sex = self.sex
        title = self.title
        traded = self.traded
        unlocked_titles = self.unlocked_titles
        vocation = self.vocation
        world = self.world

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_status is not UNSET:
            field_dict["account_status"] = account_status
        if achievement_points is not UNSET:
            field_dict["achievement_points"] = achievement_points
        if comment is not UNSET:
            field_dict["comment"] = comment
        if deletion_date is not UNSET:
            field_dict["deletion_date"] = deletion_date
        if former_names is not UNSET:
            field_dict["former_names"] = former_names
        if former_worlds is not UNSET:
            field_dict["former_worlds"] = former_worlds
        if guild is not UNSET:
            field_dict["guild"] = guild
        if houses is not UNSET:
            field_dict["houses"] = houses
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if level is not UNSET:
            field_dict["level"] = level
        if married_to is not UNSET:
            field_dict["married_to"] = married_to
        if name is not UNSET:
            field_dict["name"] = name
        if residence is not UNSET:
            field_dict["residence"] = residence
        if sex is not UNSET:
            field_dict["sex"] = sex
        if title is not UNSET:
            field_dict["title"] = title
        if traded is not UNSET:
            field_dict["traded"] = traded
        if unlocked_titles is not UNSET:
            field_dict["unlocked_titles"] = unlocked_titles
        if vocation is not UNSET:
            field_dict["vocation"] = vocation
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_character_guild import MainCharacterGuild
        from ..models.main_houses import MainHouses

        d = src_dict.copy()
        account_status = d.pop("account_status", UNSET)

        achievement_points = d.pop("achievement_points", UNSET)

        comment = d.pop("comment", UNSET)

        deletion_date = d.pop("deletion_date", UNSET)

        former_names = cast(List[str], d.pop("former_names", UNSET))

        former_worlds = cast(List[str], d.pop("former_worlds", UNSET))

        _guild = d.pop("guild", UNSET)
        guild: Union[Unset, MainCharacterGuild]
        if isinstance(_guild, Unset):
            guild = UNSET
        else:
            guild = MainCharacterGuild.from_dict(_guild)

        houses = []
        _houses = d.pop("houses", UNSET)
        for houses_item_data in _houses or []:
            houses_item = MainHouses.from_dict(houses_item_data)

            houses.append(houses_item)

        last_login = d.pop("last_login", UNSET)

        level = d.pop("level", UNSET)

        married_to = d.pop("married_to", UNSET)

        name = d.pop("name", UNSET)

        residence = d.pop("residence", UNSET)

        sex = d.pop("sex", UNSET)

        title = d.pop("title", UNSET)

        traded = d.pop("traded", UNSET)

        unlocked_titles = d.pop("unlocked_titles", UNSET)

        vocation = d.pop("vocation", UNSET)

        world = d.pop("world", UNSET)

        main_character = cls(
            account_status=account_status,
            achievement_points=achievement_points,
            comment=comment,
            deletion_date=deletion_date,
            former_names=former_names,
            former_worlds=former_worlds,
            guild=guild,
            houses=houses,
            last_login=last_login,
            level=level,
            married_to=married_to,
            name=name,
            residence=residence,
            sex=sex,
            title=title,
            traded=traded,
            unlocked_titles=unlocked_titles,
            vocation=vocation,
            world=world,
        )

        main_character.additional_properties = d
        return main_character

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
