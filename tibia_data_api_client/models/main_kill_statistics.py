from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_entry import MainEntry
    from ..models.main_total import MainTotal


T = TypeVar("T", bound="MainKillStatistics")


@_attrs_define
class MainKillStatistics:
    """
    Attributes:
        entries (Union[Unset, List['MainEntry']]):
        total (Union[Unset, MainTotal]):
        world (Union[Unset, str]):
    """

    entries: Union[Unset, List["MainEntry"]] = UNSET
    total: Union[Unset, "MainTotal"] = UNSET
    world: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()

                entries.append(entries_item)

        total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        world = self.world

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if total is not UNSET:
            field_dict["total"] = total
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_entry import MainEntry
        from ..models.main_total import MainTotal

        d = src_dict.copy()
        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = MainEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        _total = d.pop("total", UNSET)
        total: Union[Unset, MainTotal]
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = MainTotal.from_dict(_total)

        world = d.pop("world", UNSET)

        main_kill_statistics = cls(
            entries=entries,
            total=total,
            world=world,
        )

        main_kill_statistics.additional_properties = d
        return main_kill_statistics

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
