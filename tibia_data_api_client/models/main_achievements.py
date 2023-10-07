from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainAchievements")


@_attrs_define
class MainAchievements:
    """
    Attributes:
        grade (Union[Unset, int]):
        name (Union[Unset, str]):
        secret (Union[Unset, bool]):
    """

    grade: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    secret: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grade = self.grade
        name = self.name
        secret = self.secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grade is not UNSET:
            field_dict["grade"] = grade
        if name is not UNSET:
            field_dict["name"] = name
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        grade = d.pop("grade", UNSET)

        name = d.pop("name", UNSET)

        secret = d.pop("secret", UNSET)

        main_achievements = cls(
            grade=grade,
            name=name,
            secret=secret,
        )

        main_achievements.additional_properties = d
        return main_achievements

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
