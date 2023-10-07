from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainHighscorePage")


@_attrs_define
class MainHighscorePage:
    """
    Attributes:
        current_page (Union[Unset, int]): Current page
        total_pages (Union[Unset, int]): Total page count
        total_records (Union[Unset, int]): Total highscore records
    """

    current_page: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET
    total_records: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_page = self.current_page
        total_pages = self.total_pages
        total_records = self.total_records

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if total_records is not UNSET:
            field_dict["total_records"] = total_records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_page = d.pop("current_page", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        total_records = d.pop("total_records", UNSET)

        main_highscore_page = cls(
            current_page=current_page,
            total_pages=total_pages,
            total_records=total_records,
        )

        main_highscore_page.additional_properties = d
        return main_highscore_page

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
