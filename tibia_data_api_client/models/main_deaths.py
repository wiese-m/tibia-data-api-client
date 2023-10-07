from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_killers import MainKillers


T = TypeVar("T", bound="MainDeaths")


@_attrs_define
class MainDeaths:
    """
    Attributes:
        assists (Union[Unset, List['MainKillers']]):
        killers (Union[Unset, List['MainKillers']]):
        level (Union[Unset, int]):
        reason (Union[Unset, str]):
        time (Union[Unset, str]):
    """

    assists: Union[Unset, List["MainKillers"]] = UNSET
    killers: Union[Unset, List["MainKillers"]] = UNSET
    level: Union[Unset, int] = UNSET
    reason: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assists: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assists, Unset):
            assists = []
            for assists_item_data in self.assists:
                assists_item = assists_item_data.to_dict()

                assists.append(assists_item)

        killers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.killers, Unset):
            killers = []
            for killers_item_data in self.killers:
                killers_item = killers_item_data.to_dict()

                killers.append(killers_item)

        level = self.level
        reason = self.reason
        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assists is not UNSET:
            field_dict["assists"] = assists
        if killers is not UNSET:
            field_dict["killers"] = killers
        if level is not UNSET:
            field_dict["level"] = level
        if reason is not UNSET:
            field_dict["reason"] = reason
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_killers import MainKillers

        d = src_dict.copy()
        assists = []
        _assists = d.pop("assists", UNSET)
        for assists_item_data in _assists or []:
            assists_item = MainKillers.from_dict(assists_item_data)

            assists.append(assists_item)

        killers = []
        _killers = d.pop("killers", UNSET)
        for killers_item_data in _killers or []:
            killers_item = MainKillers.from_dict(killers_item_data)

            killers.append(killers_item)

        level = d.pop("level", UNSET)

        reason = d.pop("reason", UNSET)

        time = d.pop("time", UNSET)

        main_deaths = cls(
            assists=assists,
            killers=killers,
            level=level,
            reason=reason,
            time=time,
        )

        main_deaths.additional_properties = d
        return main_deaths

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
