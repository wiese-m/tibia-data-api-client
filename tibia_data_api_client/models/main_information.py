from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainInformation")


@_attrs_define
class MainInformation:
    """
    Attributes:
        api_version (Union[Unset, int]):
        timestamp (Union[Unset, str]):
    """

    api_version: Union[Unset, int] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_version = self.api_version
        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_version is not UNSET:
            field_dict["api_version"] = api_version
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_version = d.pop("api_version", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        main_information = cls(
            api_version=api_version,
            timestamp=timestamp,
        )

        main_information.additional_properties = d
        return main_information

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
