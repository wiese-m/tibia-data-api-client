from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_house_status import MainHouseStatus


T = TypeVar("T", bound="MainHouse")


@_attrs_define
class MainHouse:
    """
    Attributes:
        beds (Union[Unset, int]):
        houseid (Union[Unset, int]):
        img (Union[Unset, str]):
        name (Union[Unset, str]):
        rent (Union[Unset, int]):
        size (Union[Unset, int]):
        status (Union[Unset, MainHouseStatus]):
        town (Union[Unset, str]):
        type (Union[Unset, str]):
        world (Union[Unset, str]):
    """

    beds: Union[Unset, int] = UNSET
    houseid: Union[Unset, int] = UNSET
    img: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    rent: Union[Unset, int] = UNSET
    size: Union[Unset, int] = UNSET
    status: Union[Unset, "MainHouseStatus"] = UNSET
    town: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    world: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        beds = self.beds
        houseid = self.houseid
        img = self.img
        name = self.name
        rent = self.rent
        size = self.size
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        town = self.town
        type = self.type
        world = self.world

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if beds is not UNSET:
            field_dict["beds"] = beds
        if houseid is not UNSET:
            field_dict["houseid"] = houseid
        if img is not UNSET:
            field_dict["img"] = img
        if name is not UNSET:
            field_dict["name"] = name
        if rent is not UNSET:
            field_dict["rent"] = rent
        if size is not UNSET:
            field_dict["size"] = size
        if status is not UNSET:
            field_dict["status"] = status
        if town is not UNSET:
            field_dict["town"] = town
        if type is not UNSET:
            field_dict["type"] = type
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_house_status import MainHouseStatus

        d = src_dict.copy()
        beds = d.pop("beds", UNSET)

        houseid = d.pop("houseid", UNSET)

        img = d.pop("img", UNSET)

        name = d.pop("name", UNSET)

        rent = d.pop("rent", UNSET)

        size = d.pop("size", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MainHouseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MainHouseStatus.from_dict(_status)

        town = d.pop("town", UNSET)

        type = d.pop("type", UNSET)

        world = d.pop("world", UNSET)

        main_house = cls(
            beds=beds,
            houseid=houseid,
            img=img,
            name=name,
            rent=rent,
            size=size,
            status=status,
            town=town,
            type=type,
            world=world,
        )

        main_house.additional_properties = d
        return main_house

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
