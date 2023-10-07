from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_information import MainInformation
    from ..models.main_news_item import MainNewsItem


T = TypeVar("T", bound="MainNewsListResponse")


@_attrs_define
class MainNewsListResponse:
    """
    Attributes:
        information (Union[Unset, MainInformation]):
        news (Union[Unset, List['MainNewsItem']]):
    """

    information: Union[Unset, "MainInformation"] = UNSET
    news: Union[Unset, List["MainNewsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.information, Unset):
            information = self.information.to_dict()

        news: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.news, Unset):
            news = []
            for news_item_data in self.news:
                news_item = news_item_data.to_dict()

                news.append(news_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if information is not UNSET:
            field_dict["information"] = information
        if news is not UNSET:
            field_dict["news"] = news

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_information import MainInformation
        from ..models.main_news_item import MainNewsItem

        d = src_dict.copy()
        _information = d.pop("information", UNSET)
        information: Union[Unset, MainInformation]
        if isinstance(_information, Unset):
            information = UNSET
        else:
            information = MainInformation.from_dict(_information)

        news = []
        _news = d.pop("news", UNSET)
        for news_item_data in _news or []:
            news_item = MainNewsItem.from_dict(news_item_data)

            news.append(news_item)

        main_news_list_response = cls(
            information=information,
            news=news,
        )

        main_news_list_response.additional_properties = d
        return main_news_list_response

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
