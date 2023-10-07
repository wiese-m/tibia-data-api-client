from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_overview_world import MainOverviewWorld


T = TypeVar("T", bound="MainOverviewWorlds")


@_attrs_define
class MainOverviewWorlds:
    """
    Attributes:
        players_online (Union[Unset, int]): Calculated value
        record_date (Union[Unset, str]): Overall Maximum:
        record_players (Union[Unset, int]): Overall Maximum:
        regular_worlds (Union[Unset, List['MainOverviewWorld']]):
        tournament_worlds (Union[Unset, List['MainOverviewWorld']]):
    """

    players_online: Union[Unset, int] = UNSET
    record_date: Union[Unset, str] = UNSET
    record_players: Union[Unset, int] = UNSET
    regular_worlds: Union[Unset, List["MainOverviewWorld"]] = UNSET
    tournament_worlds: Union[Unset, List["MainOverviewWorld"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        players_online = self.players_online
        record_date = self.record_date
        record_players = self.record_players
        regular_worlds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regular_worlds, Unset):
            regular_worlds = []
            for regular_worlds_item_data in self.regular_worlds:
                regular_worlds_item = regular_worlds_item_data.to_dict()

                regular_worlds.append(regular_worlds_item)

        tournament_worlds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tournament_worlds, Unset):
            tournament_worlds = []
            for tournament_worlds_item_data in self.tournament_worlds:
                tournament_worlds_item = tournament_worlds_item_data.to_dict()

                tournament_worlds.append(tournament_worlds_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if players_online is not UNSET:
            field_dict["players_online"] = players_online
        if record_date is not UNSET:
            field_dict["record_date"] = record_date
        if record_players is not UNSET:
            field_dict["record_players"] = record_players
        if regular_worlds is not UNSET:
            field_dict["regular_worlds"] = regular_worlds
        if tournament_worlds is not UNSET:
            field_dict["tournament_worlds"] = tournament_worlds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_overview_world import MainOverviewWorld

        d = src_dict.copy()
        players_online = d.pop("players_online", UNSET)

        record_date = d.pop("record_date", UNSET)

        record_players = d.pop("record_players", UNSET)

        regular_worlds = []
        _regular_worlds = d.pop("regular_worlds", UNSET)
        for regular_worlds_item_data in _regular_worlds or []:
            regular_worlds_item = MainOverviewWorld.from_dict(regular_worlds_item_data)

            regular_worlds.append(regular_worlds_item)

        tournament_worlds = []
        _tournament_worlds = d.pop("tournament_worlds", UNSET)
        for tournament_worlds_item_data in _tournament_worlds or []:
            tournament_worlds_item = MainOverviewWorld.from_dict(tournament_worlds_item_data)

            tournament_worlds.append(tournament_worlds_item)

        main_overview_worlds = cls(
            players_online=players_online,
            record_date=record_date,
            record_players=record_players,
            regular_worlds=regular_worlds,
            tournament_worlds=tournament_worlds,
        )

        main_overview_worlds.additional_properties = d
        return main_overview_worlds

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
