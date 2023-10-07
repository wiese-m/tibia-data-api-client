from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainAccountInformation")


@_attrs_define
class MainAccountInformation:
    """
    Attributes:
        created (Union[Unset, str]):
        loyalty_title (Union[Unset, str]):
        position (Union[Unset, str]):
    """

    created: Union[Unset, str] = UNSET
    loyalty_title: Union[Unset, str] = UNSET
    position: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created = self.created
        loyalty_title = self.loyalty_title
        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if loyalty_title is not UNSET:
            field_dict["loyalty_title"] = loyalty_title
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = d.pop("created", UNSET)

        loyalty_title = d.pop("loyalty_title", UNSET)

        position = d.pop("position", UNSET)

        main_account_information = cls(
            created=created,
            loyalty_title=loyalty_title,
            position=position,
        )

        main_account_information.additional_properties = d
        return main_account_information

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
