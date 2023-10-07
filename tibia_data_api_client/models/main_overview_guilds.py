from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_overview_guild import MainOverviewGuild


T = TypeVar("T", bound="MainOverviewGuilds")


@_attrs_define
class MainOverviewGuilds:
    """
    Attributes:
        active (Union[Unset, List['MainOverviewGuild']]):
        formation (Union[Unset, List['MainOverviewGuild']]):
        world (Union[Unset, str]):
    """

    active: Union[Unset, List["MainOverviewGuild"]] = UNSET
    formation: Union[Unset, List["MainOverviewGuild"]] = UNSET
    world: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.active, Unset):
            active = []
            for active_item_data in self.active:
                active_item = active_item_data.to_dict()

                active.append(active_item)

        formation: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.formation, Unset):
            formation = []
            for formation_item_data in self.formation:
                formation_item = formation_item_data.to_dict()

                formation.append(formation_item)

        world = self.world

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if formation is not UNSET:
            field_dict["formation"] = formation
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_overview_guild import MainOverviewGuild

        d = src_dict.copy()
        active = []
        _active = d.pop("active", UNSET)
        for active_item_data in _active or []:
            active_item = MainOverviewGuild.from_dict(active_item_data)

            active.append(active_item)

        formation = []
        _formation = d.pop("formation", UNSET)
        for formation_item_data in _formation or []:
            formation_item = MainOverviewGuild.from_dict(formation_item_data)

            formation.append(formation_item)

        world = d.pop("world", UNSET)

        main_overview_guilds = cls(
            active=active,
            formation=formation,
            world=world,
        )

        main_overview_guilds.additional_properties = d
        return main_overview_guilds

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
