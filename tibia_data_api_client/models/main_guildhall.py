from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainGuildhall")


@_attrs_define
class MainGuildhall:
    """
    Attributes:
        name (Union[Unset, str]):
        paid_until (Union[Unset, str]): Town      string `json:"town"`       // We can collect that from cached info?
                            Status    string `json:"status"`     // rented (but maybe also auctioned)
                            Owner     string `json:"owner"`      // We can collect that from cached info?
                            HouseID   int    `json:"houseid"`    // We can collect that from cached info?
        world (Union[Unset, str]): Maybe duplicate info? Guild can only be on one world..
    """

    name: Union[Unset, str] = UNSET
    paid_until: Union[Unset, str] = UNSET
    world: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        paid_until = self.paid_until
        world = self.world

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if paid_until is not UNSET:
            field_dict["paid_until"] = paid_until
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        paid_until = d.pop("paid_until", UNSET)

        world = d.pop("world", UNSET)

        main_guildhall = cls(
            name=name,
            paid_until=paid_until,
            world=world,
        )

        main_guildhall.additional_properties = d
        return main_guildhall

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
