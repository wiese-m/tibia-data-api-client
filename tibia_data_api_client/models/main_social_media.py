from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainSocialMedia")


@_attrs_define
class MainSocialMedia:
    """
    Attributes:
        discord (Union[Unset, bool]):
        facebook (Union[Unset, bool]):
        instagram (Union[Unset, bool]):
        reddit (Union[Unset, bool]):
        twitch (Union[Unset, bool]):
        twitter (Union[Unset, bool]):
        youtube (Union[Unset, bool]):
    """

    discord: Union[Unset, bool] = UNSET
    facebook: Union[Unset, bool] = UNSET
    instagram: Union[Unset, bool] = UNSET
    reddit: Union[Unset, bool] = UNSET
    twitch: Union[Unset, bool] = UNSET
    twitter: Union[Unset, bool] = UNSET
    youtube: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        discord = self.discord
        facebook = self.facebook
        instagram = self.instagram
        reddit = self.reddit
        twitch = self.twitch
        twitter = self.twitter
        youtube = self.youtube

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discord is not UNSET:
            field_dict["discord"] = discord
        if facebook is not UNSET:
            field_dict["facebook"] = facebook
        if instagram is not UNSET:
            field_dict["instagram"] = instagram
        if reddit is not UNSET:
            field_dict["reddit"] = reddit
        if twitch is not UNSET:
            field_dict["twitch"] = twitch
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if youtube is not UNSET:
            field_dict["youtube"] = youtube

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        discord = d.pop("discord", UNSET)

        facebook = d.pop("facebook", UNSET)

        instagram = d.pop("instagram", UNSET)

        reddit = d.pop("reddit", UNSET)

        twitch = d.pop("twitch", UNSET)

        twitter = d.pop("twitter", UNSET)

        youtube = d.pop("youtube", UNSET)

        main_social_media = cls(
            discord=discord,
            facebook=facebook,
            instagram=instagram,
            reddit=reddit,
            twitch=twitch,
            twitter=twitter,
            youtube=youtube,
        )

        main_social_media.additional_properties = d
        return main_social_media

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
