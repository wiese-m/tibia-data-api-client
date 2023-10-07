from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_online_players import MainOnlinePlayers


T = TypeVar("T", bound="MainWorld")


@_attrs_define
class MainWorld:
    """
    Attributes:
        battleye_date (Union[Unset, str]): BattlEye Status: null if since release / else show date?
        battleye_protected (Union[Unset, bool]): BattlEye Status: true if protected / false if "Not protected by
            BattlEye."
        creation_date (Union[Unset, str]): Creation Date: -> convert to YYYY-MM
        game_world_type (Union[Unset, str]): Game World Type: regular / experimental / tournament (if Tournament World
            Type exists)
        location (Union[Unset, str]): Location:
        name (Union[Unset, str]):
        online_players (Union[Unset, List['MainOnlinePlayers']]):
        players_online (Union[Unset, int]): Players Online:
        premium_only (Union[Unset, bool]): Premium Type: premium = true / else: false
        pvp_type (Union[Unset, str]): PvP Type:
        record_date (Union[Unset, str]): Online Record:
        record_players (Union[Unset, int]): Online Record:
        status (Union[Unset, str]): Status:
        tournament_world_type (Union[Unset, str]): Tournament World Type: "" (default?) / regular / restricted
        transfer_type (Union[Unset, str]): Transfer Type: regular (if not present) / locked / blocked
        world_quest_titles (Union[Unset, List[str]]): World Quest Titles:
    """

    battleye_date: Union[Unset, str] = UNSET
    battleye_protected: Union[Unset, bool] = UNSET
    creation_date: Union[Unset, str] = UNSET
    game_world_type: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    online_players: Union[Unset, List["MainOnlinePlayers"]] = UNSET
    players_online: Union[Unset, int] = UNSET
    premium_only: Union[Unset, bool] = UNSET
    pvp_type: Union[Unset, str] = UNSET
    record_date: Union[Unset, str] = UNSET
    record_players: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    tournament_world_type: Union[Unset, str] = UNSET
    transfer_type: Union[Unset, str] = UNSET
    world_quest_titles: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        battleye_date = self.battleye_date
        battleye_protected = self.battleye_protected
        creation_date = self.creation_date
        game_world_type = self.game_world_type
        location = self.location
        name = self.name
        online_players: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.online_players, Unset):
            online_players = []
            for online_players_item_data in self.online_players:
                online_players_item = online_players_item_data.to_dict()

                online_players.append(online_players_item)

        players_online = self.players_online
        premium_only = self.premium_only
        pvp_type = self.pvp_type
        record_date = self.record_date
        record_players = self.record_players
        status = self.status
        tournament_world_type = self.tournament_world_type
        transfer_type = self.transfer_type
        world_quest_titles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.world_quest_titles, Unset):
            world_quest_titles = self.world_quest_titles

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if battleye_date is not UNSET:
            field_dict["battleye_date"] = battleye_date
        if battleye_protected is not UNSET:
            field_dict["battleye_protected"] = battleye_protected
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if game_world_type is not UNSET:
            field_dict["game_world_type"] = game_world_type
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if online_players is not UNSET:
            field_dict["online_players"] = online_players
        if players_online is not UNSET:
            field_dict["players_online"] = players_online
        if premium_only is not UNSET:
            field_dict["premium_only"] = premium_only
        if pvp_type is not UNSET:
            field_dict["pvp_type"] = pvp_type
        if record_date is not UNSET:
            field_dict["record_date"] = record_date
        if record_players is not UNSET:
            field_dict["record_players"] = record_players
        if status is not UNSET:
            field_dict["status"] = status
        if tournament_world_type is not UNSET:
            field_dict["tournament_world_type"] = tournament_world_type
        if transfer_type is not UNSET:
            field_dict["transfer_type"] = transfer_type
        if world_quest_titles is not UNSET:
            field_dict["world_quest_titles"] = world_quest_titles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_online_players import MainOnlinePlayers

        d = src_dict.copy()
        battleye_date = d.pop("battleye_date", UNSET)

        battleye_protected = d.pop("battleye_protected", UNSET)

        creation_date = d.pop("creation_date", UNSET)

        game_world_type = d.pop("game_world_type", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        online_players = []
        _online_players = d.pop("online_players", UNSET)
        for online_players_item_data in _online_players or []:
            online_players_item = MainOnlinePlayers.from_dict(online_players_item_data)

            online_players.append(online_players_item)

        players_online = d.pop("players_online", UNSET)

        premium_only = d.pop("premium_only", UNSET)

        pvp_type = d.pop("pvp_type", UNSET)

        record_date = d.pop("record_date", UNSET)

        record_players = d.pop("record_players", UNSET)

        status = d.pop("status", UNSET)

        tournament_world_type = d.pop("tournament_world_type", UNSET)

        transfer_type = d.pop("transfer_type", UNSET)

        world_quest_titles = cast(List[str], d.pop("world_quest_titles", UNSET))

        main_world = cls(
            battleye_date=battleye_date,
            battleye_protected=battleye_protected,
            creation_date=creation_date,
            game_world_type=game_world_type,
            location=location,
            name=name,
            online_players=online_players,
            players_online=players_online,
            premium_only=premium_only,
            pvp_type=pvp_type,
            record_date=record_date,
            record_players=record_players,
            status=status,
            tournament_world_type=tournament_world_type,
            transfer_type=transfer_type,
            world_quest_titles=world_quest_titles,
        )

        main_world.additional_properties = d
        return main_world

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
