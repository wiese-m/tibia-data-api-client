from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_guild import MainGuild


T = TypeVar("T", bound="MainGuilds")


@_attrs_define
class MainGuilds:
    """
    Attributes:
        guild (Union[Unset, MainGuild]):
    """

    guild: Union[Unset, "MainGuild"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guild: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guild, Unset):
            guild = self.guild.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guild is not UNSET:
            field_dict["guild"] = guild

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_guild import MainGuild

        d = src_dict.copy()
        _guild = d.pop("guild", UNSET)
        guild: Union[Unset, MainGuild]
        if isinstance(_guild, Unset):
            guild = UNSET
        else:
            guild = MainGuild.from_dict(_guild)

        main_guilds = cls(
            guild=guild,
        )

        main_guilds.additional_properties = d
        return main_guilds

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
