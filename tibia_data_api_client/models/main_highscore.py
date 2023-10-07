from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainHighscore")


@_attrs_define
class MainHighscore:
    """
    Attributes:
        level (Union[Unset, int]): Level column
        name (Union[Unset, str]): Name column
        rank (Union[Unset, int]): Rank column
        title (Union[Unset, str]): Title column (when category: loyalty)
        value (Union[Unset, int]): Points/SkillLevel column
        vocation (Union[Unset, str]): Vocation column
        world (Union[Unset, str]): World column
    """

    level: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    rank: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    value: Union[Unset, int] = UNSET
    vocation: Union[Unset, str] = UNSET
    world: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        level = self.level
        name = self.name
        rank = self.rank
        title = self.title
        value = self.value
        vocation = self.vocation
        world = self.world

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name
        if rank is not UNSET:
            field_dict["rank"] = rank
        if title is not UNSET:
            field_dict["title"] = title
        if value is not UNSET:
            field_dict["value"] = value
        if vocation is not UNSET:
            field_dict["vocation"] = vocation
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        level = d.pop("level", UNSET)

        name = d.pop("name", UNSET)

        rank = d.pop("rank", UNSET)

        title = d.pop("title", UNSET)

        value = d.pop("value", UNSET)

        vocation = d.pop("vocation", UNSET)

        world = d.pop("world", UNSET)

        main_highscore = cls(
            level=level,
            name=name,
            rank=rank,
            title=title,
            value=value,
            vocation=vocation,
            world=world,
        )

        main_highscore.additional_properties = d
        return main_highscore

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
