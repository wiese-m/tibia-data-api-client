from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainAccountBadges")


@_attrs_define
class MainAccountBadges:
    """
    Attributes:
        description (Union[Unset, str]):
        icon_url (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    icon_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        icon_url = self.icon_url
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        icon_url = d.pop("icon_url", UNSET)

        name = d.pop("name", UNSET)

        main_account_badges = cls(
            description=description,
            icon_url=icon_url,
            name=name,
        )

        main_account_badges.additional_properties = d
        return main_account_badges

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
