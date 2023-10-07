from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainKillers")


@_attrs_define
class MainKillers:
    """
    Attributes:
        name (Union[Unset, str]):
        player (Union[Unset, bool]):
        summon (Union[Unset, str]):
        traded (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    player: Union[Unset, bool] = UNSET
    summon: Union[Unset, str] = UNSET
    traded: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        player = self.player
        summon = self.summon
        traded = self.traded

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if player is not UNSET:
            field_dict["player"] = player
        if summon is not UNSET:
            field_dict["summon"] = summon
        if traded is not UNSET:
            field_dict["traded"] = traded

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        player = d.pop("player", UNSET)

        summon = d.pop("summon", UNSET)

        traded = d.pop("traded", UNSET)

        main_killers = cls(
            name=name,
            player=player,
            summon=summon,
            traded=traded,
        )

        main_killers.additional_properties = d
        return main_killers

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
