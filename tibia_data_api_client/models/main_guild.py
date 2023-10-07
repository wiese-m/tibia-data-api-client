from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_guild_member import MainGuildMember
    from ..models.main_guildhall import MainGuildhall
    from ..models.main_invited_guild_member import MainInvitedGuildMember


T = TypeVar("T", bound="MainGuild")


@_attrs_define
class MainGuild:
    """
    Attributes:
        active (Union[Unset, bool]):
        description (Union[Unset, str]):
        disband_condition (Union[Unset, str]):
        disband_date (Union[Unset, str]):
        founded (Union[Unset, str]):
        guildhalls (Union[Unset, List['MainGuildhall']]):
        homepage (Union[Unset, str]):
        in_war (Union[Unset, bool]):
        invites (Union[Unset, List['MainInvitedGuildMember']]):
        logo_url (Union[Unset, str]):
        members (Union[Unset, List['MainGuildMember']]):
        members_invited (Union[Unset, int]):
        members_total (Union[Unset, int]):
        name (Union[Unset, str]):
        open_applications (Union[Unset, bool]):
        players_offline (Union[Unset, int]):
        players_online (Union[Unset, int]):
        world (Union[Unset, str]):
    """

    active: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    disband_condition: Union[Unset, str] = UNSET
    disband_date: Union[Unset, str] = UNSET
    founded: Union[Unset, str] = UNSET
    guildhalls: Union[Unset, List["MainGuildhall"]] = UNSET
    homepage: Union[Unset, str] = UNSET
    in_war: Union[Unset, bool] = UNSET
    invites: Union[Unset, List["MainInvitedGuildMember"]] = UNSET
    logo_url: Union[Unset, str] = UNSET
    members: Union[Unset, List["MainGuildMember"]] = UNSET
    members_invited: Union[Unset, int] = UNSET
    members_total: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    open_applications: Union[Unset, bool] = UNSET
    players_offline: Union[Unset, int] = UNSET
    players_online: Union[Unset, int] = UNSET
    world: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        description = self.description
        disband_condition = self.disband_condition
        disband_date = self.disband_date
        founded = self.founded
        guildhalls: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.guildhalls, Unset):
            guildhalls = []
            for guildhalls_item_data in self.guildhalls:
                guildhalls_item = guildhalls_item_data.to_dict()

                guildhalls.append(guildhalls_item)

        homepage = self.homepage
        in_war = self.in_war
        invites: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invites, Unset):
            invites = []
            for invites_item_data in self.invites:
                invites_item = invites_item_data.to_dict()

                invites.append(invites_item)

        logo_url = self.logo_url
        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()

                members.append(members_item)

        members_invited = self.members_invited
        members_total = self.members_total
        name = self.name
        open_applications = self.open_applications
        players_offline = self.players_offline
        players_online = self.players_online
        world = self.world

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if description is not UNSET:
            field_dict["description"] = description
        if disband_condition is not UNSET:
            field_dict["disband_condition"] = disband_condition
        if disband_date is not UNSET:
            field_dict["disband_date"] = disband_date
        if founded is not UNSET:
            field_dict["founded"] = founded
        if guildhalls is not UNSET:
            field_dict["guildhalls"] = guildhalls
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if in_war is not UNSET:
            field_dict["in_war"] = in_war
        if invites is not UNSET:
            field_dict["invites"] = invites
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if members is not UNSET:
            field_dict["members"] = members
        if members_invited is not UNSET:
            field_dict["members_invited"] = members_invited
        if members_total is not UNSET:
            field_dict["members_total"] = members_total
        if name is not UNSET:
            field_dict["name"] = name
        if open_applications is not UNSET:
            field_dict["open_applications"] = open_applications
        if players_offline is not UNSET:
            field_dict["players_offline"] = players_offline
        if players_online is not UNSET:
            field_dict["players_online"] = players_online
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_guild_member import MainGuildMember
        from ..models.main_guildhall import MainGuildhall
        from ..models.main_invited_guild_member import MainInvitedGuildMember

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        description = d.pop("description", UNSET)

        disband_condition = d.pop("disband_condition", UNSET)

        disband_date = d.pop("disband_date", UNSET)

        founded = d.pop("founded", UNSET)

        guildhalls = []
        _guildhalls = d.pop("guildhalls", UNSET)
        for guildhalls_item_data in _guildhalls or []:
            guildhalls_item = MainGuildhall.from_dict(guildhalls_item_data)

            guildhalls.append(guildhalls_item)

        homepage = d.pop("homepage", UNSET)

        in_war = d.pop("in_war", UNSET)

        invites = []
        _invites = d.pop("invites", UNSET)
        for invites_item_data in _invites or []:
            invites_item = MainInvitedGuildMember.from_dict(invites_item_data)

            invites.append(invites_item)

        logo_url = d.pop("logo_url", UNSET)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = MainGuildMember.from_dict(members_item_data)

            members.append(members_item)

        members_invited = d.pop("members_invited", UNSET)

        members_total = d.pop("members_total", UNSET)

        name = d.pop("name", UNSET)

        open_applications = d.pop("open_applications", UNSET)

        players_offline = d.pop("players_offline", UNSET)

        players_online = d.pop("players_online", UNSET)

        world = d.pop("world", UNSET)

        main_guild = cls(
            active=active,
            description=description,
            disband_condition=disband_condition,
            disband_date=disband_date,
            founded=founded,
            guildhalls=guildhalls,
            homepage=homepage,
            in_war=in_war,
            invites=invites,
            logo_url=logo_url,
            members=members,
            members_invited=members_invited,
            members_total=members_total,
            name=name,
            open_applications=open_applications,
            players_offline=players_offline,
            players_online=players_online,
            world=world,
        )

        main_guild.additional_properties = d
        return main_guild

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
