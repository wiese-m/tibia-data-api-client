from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_content_type import MainContentType
    from ..models.main_social_media import MainSocialMedia


T = TypeVar("T", bound="MainFansite")


@_attrs_define
class MainFansite:
    """
    Attributes:
        contact (Union[Unset, str]):
        content_type (Union[Unset, MainContentType]):
        fansite_item (Union[Unset, bool]):
        fansite_item_url (Union[Unset, str]):
        homepage (Union[Unset, str]):
        languages (Union[Unset, List[str]]):
        logo_url (Union[Unset, str]):
        name (Union[Unset, str]):
        social_media (Union[Unset, MainSocialMedia]):
        specials (Union[Unset, List[str]]):
    """

    contact: Union[Unset, str] = UNSET
    content_type: Union[Unset, "MainContentType"] = UNSET
    fansite_item: Union[Unset, bool] = UNSET
    fansite_item_url: Union[Unset, str] = UNSET
    homepage: Union[Unset, str] = UNSET
    languages: Union[Unset, List[str]] = UNSET
    logo_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    social_media: Union[Unset, "MainSocialMedia"] = UNSET
    specials: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact = self.contact
        content_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.to_dict()

        fansite_item = self.fansite_item
        fansite_item_url = self.fansite_item_url
        homepage = self.homepage
        languages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.languages, Unset):
            languages = self.languages

        logo_url = self.logo_url
        name = self.name
        social_media: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.social_media, Unset):
            social_media = self.social_media.to_dict()

        specials: Union[Unset, List[str]] = UNSET
        if not isinstance(self.specials, Unset):
            specials = self.specials

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if fansite_item is not UNSET:
            field_dict["fansite_item"] = fansite_item
        if fansite_item_url is not UNSET:
            field_dict["fansite_item_url"] = fansite_item_url
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if languages is not UNSET:
            field_dict["languages"] = languages
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if social_media is not UNSET:
            field_dict["social_media"] = social_media
        if specials is not UNSET:
            field_dict["specials"] = specials

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_content_type import MainContentType
        from ..models.main_social_media import MainSocialMedia

        d = src_dict.copy()
        contact = d.pop("contact", UNSET)

        _content_type = d.pop("content_type", UNSET)
        content_type: Union[Unset, MainContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = MainContentType.from_dict(_content_type)

        fansite_item = d.pop("fansite_item", UNSET)

        fansite_item_url = d.pop("fansite_item_url", UNSET)

        homepage = d.pop("homepage", UNSET)

        languages = cast(List[str], d.pop("languages", UNSET))

        logo_url = d.pop("logo_url", UNSET)

        name = d.pop("name", UNSET)

        _social_media = d.pop("social_media", UNSET)
        social_media: Union[Unset, MainSocialMedia]
        if isinstance(_social_media, Unset):
            social_media = UNSET
        else:
            social_media = MainSocialMedia.from_dict(_social_media)

        specials = cast(List[str], d.pop("specials", UNSET))

        main_fansite = cls(
            contact=contact,
            content_type=content_type,
            fansite_item=fansite_item,
            fansite_item_url=fansite_item_url,
            homepage=homepage,
            languages=languages,
            logo_url=logo_url,
            name=name,
            social_media=social_media,
            specials=specials,
        )

        main_fansite.additional_properties = d
        return main_fansite

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
