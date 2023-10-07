from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainHouses")


@_attrs_define
class MainHouses:
    """
    Attributes:
        houseid (Union[Unset, int]):
        name (Union[Unset, str]):
        paid (Union[Unset, str]):
        town (Union[Unset, str]):
    """

    houseid: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    paid: Union[Unset, str] = UNSET
    town: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        houseid = self.houseid
        name = self.name
        paid = self.paid
        town = self.town

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if houseid is not UNSET:
            field_dict["houseid"] = houseid
        if name is not UNSET:
            field_dict["name"] = name
        if paid is not UNSET:
            field_dict["paid"] = paid
        if town is not UNSET:
            field_dict["town"] = town

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        houseid = d.pop("houseid", UNSET)

        name = d.pop("name", UNSET)

        paid = d.pop("paid", UNSET)

        town = d.pop("town", UNSET)

        main_houses = cls(
            houseid=houseid,
            name=name,
            paid=paid,
            town=town,
        )

        main_houses.additional_properties = d
        return main_houses

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
