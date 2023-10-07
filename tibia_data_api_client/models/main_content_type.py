from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainContentType")


@_attrs_define
class MainContentType:
    """
    Attributes:
        statistics (Union[Unset, bool]):
        texts (Union[Unset, bool]):
        tools (Union[Unset, bool]):
        wiki (Union[Unset, bool]):
    """

    statistics: Union[Unset, bool] = UNSET
    texts: Union[Unset, bool] = UNSET
    tools: Union[Unset, bool] = UNSET
    wiki: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        statistics = self.statistics
        texts = self.texts
        tools = self.tools
        wiki = self.wiki

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if texts is not UNSET:
            field_dict["texts"] = texts
        if tools is not UNSET:
            field_dict["tools"] = tools
        if wiki is not UNSET:
            field_dict["wiki"] = wiki

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        statistics = d.pop("statistics", UNSET)

        texts = d.pop("texts", UNSET)

        tools = d.pop("tools", UNSET)

        wiki = d.pop("wiki", UNSET)

        main_content_type = cls(
            statistics=statistics,
            texts=texts,
            tools=tools,
            wiki=wiki,
        )

        main_content_type.additional_properties = d
        return main_content_type

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
