from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainOverviewBoostableBoss")


@_attrs_define
class MainOverviewBoostableBoss:
    """
    Attributes:
        featured (Union[Unset, bool]):
        image_url (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    featured: Union[Unset, bool] = UNSET
    image_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        featured = self.featured
        image_url = self.image_url
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if featured is not UNSET:
            field_dict["featured"] = featured
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        featured = d.pop("featured", UNSET)

        image_url = d.pop("image_url", UNSET)

        name = d.pop("name", UNSET)

        main_overview_boostable_boss = cls(
            featured=featured,
            image_url=image_url,
            name=name,
        )

        main_overview_boostable_boss.additional_properties = d
        return main_overview_boostable_boss

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
