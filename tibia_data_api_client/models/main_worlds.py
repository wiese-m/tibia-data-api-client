from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_world import MainWorld


T = TypeVar("T", bound="MainWorlds")


@_attrs_define
class MainWorlds:
    """
    Attributes:
        world (Union[Unset, MainWorld]):
    """

    world: Union[Unset, "MainWorld"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        world: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.world, Unset):
            world = self.world.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_world import MainWorld

        d = src_dict.copy()
        _world = d.pop("world", UNSET)
        world: Union[Unset, MainWorld]
        if isinstance(_world, Unset):
            world = UNSET
        else:
            world = MainWorld.from_dict(_world)

        main_worlds = cls(
            world=world,
        )

        main_worlds.additional_properties = d
        return main_worlds

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
