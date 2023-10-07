from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainNewsItem")


@_attrs_define
class MainNewsItem:
    """
    Attributes:
        category (Union[Unset, str]):
        date (Union[Unset, str]):
        id (Union[Unset, int]):
        news (Union[Unset, str]):
        type (Union[Unset, str]):
        url (Union[Unset, str]):
        url_api (Union[Unset, str]):
    """

    category: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    news: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    url_api: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        date = self.date
        id = self.id
        news = self.news
        type = self.type
        url = self.url
        url_api = self.url_api

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if news is not UNSET:
            field_dict["news"] = news
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url
        if url_api is not UNSET:
            field_dict["url_api"] = url_api

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category", UNSET)

        date = d.pop("date", UNSET)

        id = d.pop("id", UNSET)

        news = d.pop("news", UNSET)

        type = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        url_api = d.pop("url_api", UNSET)

        main_news_item = cls(
            category=category,
            date=date,
            id=id,
            news=news,
            type=type,
            url=url,
            url_api=url_api,
        )

        main_news_item.additional_properties = d
        return main_news_item

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
