from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainGuildMember")


@_attrs_define
class MainGuildMember:
    """
    Attributes:
        joined (Union[Unset, str]):
        level (Union[Unset, int]):
        name (Union[Unset, str]):
        rank (Union[Unset, str]):
        status (Union[Unset, str]):
        title (Union[Unset, str]):
        vocation (Union[Unset, str]):
    """

    joined: Union[Unset, str] = UNSET
    level: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    rank: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    vocation: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        joined = self.joined
        level = self.level
        name = self.name
        rank = self.rank
        status = self.status
        title = self.title
        vocation = self.vocation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if joined is not UNSET:
            field_dict["joined"] = joined
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name
        if rank is not UNSET:
            field_dict["rank"] = rank
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if vocation is not UNSET:
            field_dict["vocation"] = vocation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        joined = d.pop("joined", UNSET)

        level = d.pop("level", UNSET)

        name = d.pop("name", UNSET)

        rank = d.pop("rank", UNSET)

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        vocation = d.pop("vocation", UNSET)

        main_guild_member = cls(
            joined=joined,
            level=level,
            name=name,
            rank=rank,
            status=status,
            title=title,
            vocation=vocation,
        )

        main_guild_member.additional_properties = d
        return main_guild_member

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
