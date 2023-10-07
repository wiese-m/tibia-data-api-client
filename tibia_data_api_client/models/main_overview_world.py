from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainOverviewWorld")


@_attrs_define
class MainOverviewWorld:
    """
    Attributes:
        battleye_date (Union[Unset, str]): BattlEye Status: null if since release / else show date?
        battleye_protected (Union[Unset, bool]): BattlEye Status: true if protected / false if "Not protected by
            BattlEye."
        game_world_type (Union[Unset, str]): BattlEye Status: regular / experimental / tournament (if Tournament World
            Type exists)
        location (Union[Unset, str]): Location:
        name (Union[Unset, str]):
        players_online (Union[Unset, int]): Online:
        premium_only (Union[Unset, bool]): Additional Information: premium = true / else: false
        pvp_type (Union[Unset, str]): PvP Type:
        status (Union[Unset, str]): Online:
        tournament_world_type (Union[Unset, str]): BattlEye Status: null (default?) / regular / restricted
        transfer_type (Union[Unset, str]): Additional Information: regular (if not present) / locked / blocked
    """

    battleye_date: Union[Unset, str] = UNSET
    battleye_protected: Union[Unset, bool] = UNSET
    game_world_type: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    players_online: Union[Unset, int] = UNSET
    premium_only: Union[Unset, bool] = UNSET
    pvp_type: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    tournament_world_type: Union[Unset, str] = UNSET
    transfer_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        battleye_date = self.battleye_date
        battleye_protected = self.battleye_protected
        game_world_type = self.game_world_type
        location = self.location
        name = self.name
        players_online = self.players_online
        premium_only = self.premium_only
        pvp_type = self.pvp_type
        status = self.status
        tournament_world_type = self.tournament_world_type
        transfer_type = self.transfer_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if battleye_date is not UNSET:
            field_dict["battleye_date"] = battleye_date
        if battleye_protected is not UNSET:
            field_dict["battleye_protected"] = battleye_protected
        if game_world_type is not UNSET:
            field_dict["game_world_type"] = game_world_type
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if players_online is not UNSET:
            field_dict["players_online"] = players_online
        if premium_only is not UNSET:
            field_dict["premium_only"] = premium_only
        if pvp_type is not UNSET:
            field_dict["pvp_type"] = pvp_type
        if status is not UNSET:
            field_dict["status"] = status
        if tournament_world_type is not UNSET:
            field_dict["tournament_world_type"] = tournament_world_type
        if transfer_type is not UNSET:
            field_dict["transfer_type"] = transfer_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        battleye_date = d.pop("battleye_date", UNSET)

        battleye_protected = d.pop("battleye_protected", UNSET)

        game_world_type = d.pop("game_world_type", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        players_online = d.pop("players_online", UNSET)

        premium_only = d.pop("premium_only", UNSET)

        pvp_type = d.pop("pvp_type", UNSET)

        status = d.pop("status", UNSET)

        tournament_world_type = d.pop("tournament_world_type", UNSET)

        transfer_type = d.pop("transfer_type", UNSET)

        main_overview_world = cls(
            battleye_date=battleye_date,
            battleye_protected=battleye_protected,
            game_world_type=game_world_type,
            location=location,
            name=name,
            players_online=players_online,
            premium_only=premium_only,
            pvp_type=pvp_type,
            status=status,
            tournament_world_type=tournament_world_type,
            transfer_type=transfer_type,
        )

        main_overview_world.additional_properties = d
        return main_overview_world

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
