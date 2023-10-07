from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_houses_house import MainHousesHouse


T = TypeVar("T", bound="MainHousesHouses")


@_attrs_define
class MainHousesHouses:
    """
    Attributes:
        guildhall_list (Union[Unset, List['MainHousesHouse']]):
        house_list (Union[Unset, List['MainHousesHouse']]):
        town (Union[Unset, str]):
        world (Union[Unset, str]):
    """

    guildhall_list: Union[Unset, List["MainHousesHouse"]] = UNSET
    house_list: Union[Unset, List["MainHousesHouse"]] = UNSET
    town: Union[Unset, str] = UNSET
    world: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guildhall_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.guildhall_list, Unset):
            guildhall_list = []
            for guildhall_list_item_data in self.guildhall_list:
                guildhall_list_item = guildhall_list_item_data.to_dict()

                guildhall_list.append(guildhall_list_item)

        house_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.house_list, Unset):
            house_list = []
            for house_list_item_data in self.house_list:
                house_list_item = house_list_item_data.to_dict()

                house_list.append(house_list_item)

        town = self.town
        world = self.world

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guildhall_list is not UNSET:
            field_dict["guildhall_list"] = guildhall_list
        if house_list is not UNSET:
            field_dict["house_list"] = house_list
        if town is not UNSET:
            field_dict["town"] = town
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_houses_house import MainHousesHouse

        d = src_dict.copy()
        guildhall_list = []
        _guildhall_list = d.pop("guildhall_list", UNSET)
        for guildhall_list_item_data in _guildhall_list or []:
            guildhall_list_item = MainHousesHouse.from_dict(guildhall_list_item_data)

            guildhall_list.append(guildhall_list_item)

        house_list = []
        _house_list = d.pop("house_list", UNSET)
        for house_list_item_data in _house_list or []:
            house_list_item = MainHousesHouse.from_dict(house_list_item_data)

            house_list.append(house_list_item)

        town = d.pop("town", UNSET)

        world = d.pop("world", UNSET)

        main_houses_houses = cls(
            guildhall_list=guildhall_list,
            house_list=house_list,
            town=town,
            world=world,
        )

        main_houses_houses.additional_properties = d
        return main_houses_houses

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
