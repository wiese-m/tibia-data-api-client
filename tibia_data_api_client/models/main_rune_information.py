from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainRuneInformation")


@_attrs_define
class MainRuneInformation:
    """
    Attributes:
        damage_type (Union[Unset, str]):
        group_attack (Union[Unset, bool]):
        group_healing (Union[Unset, bool]):
        group_support (Union[Unset, bool]):
        level (Union[Unset, int]):
        magic_level (Union[Unset, int]):
        vocation (Union[Unset, List[str]]):
    """

    damage_type: Union[Unset, str] = UNSET
    group_attack: Union[Unset, bool] = UNSET
    group_healing: Union[Unset, bool] = UNSET
    group_support: Union[Unset, bool] = UNSET
    level: Union[Unset, int] = UNSET
    magic_level: Union[Unset, int] = UNSET
    vocation: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        damage_type = self.damage_type
        group_attack = self.group_attack
        group_healing = self.group_healing
        group_support = self.group_support
        level = self.level
        magic_level = self.magic_level
        vocation: Union[Unset, List[str]] = UNSET
        if not isinstance(self.vocation, Unset):
            vocation = self.vocation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if damage_type is not UNSET:
            field_dict["damage_type"] = damage_type
        if group_attack is not UNSET:
            field_dict["group_attack"] = group_attack
        if group_healing is not UNSET:
            field_dict["group_healing"] = group_healing
        if group_support is not UNSET:
            field_dict["group_support"] = group_support
        if level is not UNSET:
            field_dict["level"] = level
        if magic_level is not UNSET:
            field_dict["magic_level"] = magic_level
        if vocation is not UNSET:
            field_dict["vocation"] = vocation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        damage_type = d.pop("damage_type", UNSET)

        group_attack = d.pop("group_attack", UNSET)

        group_healing = d.pop("group_healing", UNSET)

        group_support = d.pop("group_support", UNSET)

        level = d.pop("level", UNSET)

        magic_level = d.pop("magic_level", UNSET)

        vocation = cast(List[str], d.pop("vocation", UNSET))

        main_rune_information = cls(
            damage_type=damage_type,
            group_attack=group_attack,
            group_healing=group_healing,
            group_support=group_support,
            level=level,
            magic_level=magic_level,
            vocation=vocation,
        )

        main_rune_information.additional_properties = d
        return main_rune_information

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
