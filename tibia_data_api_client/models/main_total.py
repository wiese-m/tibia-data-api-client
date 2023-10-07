from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainTotal")


@_attrs_define
class MainTotal:
    """
    Attributes:
        last_day_killed (Union[Unset, int]):
        last_day_players_killed (Union[Unset, int]):
        last_week_killed (Union[Unset, int]):
        last_week_players_killed (Union[Unset, int]):
    """

    last_day_killed: Union[Unset, int] = UNSET
    last_day_players_killed: Union[Unset, int] = UNSET
    last_week_killed: Union[Unset, int] = UNSET
    last_week_players_killed: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_day_killed = self.last_day_killed
        last_day_players_killed = self.last_day_players_killed
        last_week_killed = self.last_week_killed
        last_week_players_killed = self.last_week_players_killed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_day_killed is not UNSET:
            field_dict["last_day_killed"] = last_day_killed
        if last_day_players_killed is not UNSET:
            field_dict["last_day_players_killed"] = last_day_players_killed
        if last_week_killed is not UNSET:
            field_dict["last_week_killed"] = last_week_killed
        if last_week_players_killed is not UNSET:
            field_dict["last_week_players_killed"] = last_week_players_killed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_day_killed = d.pop("last_day_killed", UNSET)

        last_day_players_killed = d.pop("last_day_players_killed", UNSET)

        last_week_killed = d.pop("last_week_killed", UNSET)

        last_week_players_killed = d.pop("last_week_players_killed", UNSET)

        main_total = cls(
            last_day_killed=last_day_killed,
            last_day_players_killed=last_day_players_killed,
            last_week_killed=last_week_killed,
            last_week_players_killed=last_week_players_killed,
        )

        main_total.additional_properties = d
        return main_total

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
