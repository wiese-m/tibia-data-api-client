from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainOtherCharacters")


@_attrs_define
class MainOtherCharacters:
    """
    Attributes:
        deleted (Union[Unset, bool]): don't know how to do that yet..
        main (Union[Unset, bool]):
        name (Union[Unset, str]):
        status (Union[Unset, str]): online/offline
        traded (Union[Unset, bool]):
        world (Union[Unset, str]):
    """

    deleted: Union[Unset, bool] = UNSET
    main: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    traded: Union[Unset, bool] = UNSET
    world: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deleted = self.deleted
        main = self.main
        name = self.name
        status = self.status
        traded = self.traded
        world = self.world

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if main is not UNSET:
            field_dict["main"] = main
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if traded is not UNSET:
            field_dict["traded"] = traded
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deleted = d.pop("deleted", UNSET)

        main = d.pop("main", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        traded = d.pop("traded", UNSET)

        world = d.pop("world", UNSET)

        main_other_characters = cls(
            deleted=deleted,
            main=main,
            name=name,
            status=status,
            traded=traded,
            world=world,
        )

        main_other_characters.additional_properties = d
        return main_other_characters

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
