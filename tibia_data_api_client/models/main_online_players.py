from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainOnlinePlayers")


@_attrs_define
class MainOnlinePlayers:
    """
    Attributes:
        level (Union[Unset, int]):
        name (Union[Unset, str]):
        vocation (Union[Unset, str]):
    """

    level: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    vocation: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        level = self.level
        name = self.name
        vocation = self.vocation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name
        if vocation is not UNSET:
            field_dict["vocation"] = vocation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        level = d.pop("level", UNSET)

        name = d.pop("name", UNSET)

        vocation = d.pop("vocation", UNSET)

        main_online_players = cls(
            level=level,
            name=name,
            vocation=vocation,
        )

        main_online_players.additional_properties = d
        return main_online_players

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
