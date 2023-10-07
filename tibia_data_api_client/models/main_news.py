from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainNews")


@_attrs_define
class MainNews:
    """
    Attributes:
        category (Union[Unset, str]):
        content (Union[Unset, str]):
        content_html (Union[Unset, str]):
        date (Union[Unset, str]):
        id (Union[Unset, int]):
        title (Union[Unset, str]):
        type (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    category: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    content_html: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        content = self.content
        content_html = self.content_html
        date = self.date
        id = self.id
        title = self.title
        type = self.type
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if content is not UNSET:
            field_dict["content"] = content
        if content_html is not UNSET:
            field_dict["content_html"] = content_html
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category", UNSET)

        content = d.pop("content", UNSET)

        content_html = d.pop("content_html", UNSET)

        date = d.pop("date", UNSET)

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        main_news = cls(
            category=category,
            content=content,
            content_html=content_html,
            date=date,
            id=id,
            title=title,
            type=type,
            url=url,
        )

        main_news.additional_properties = d
        return main_news

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
