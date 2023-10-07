from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_houses_auction import MainHousesAuction


T = TypeVar("T", bound="MainHousesHouse")


@_attrs_define
class MainHousesHouse:
    """
    Attributes:
        auction (Union[Unset, MainHousesAuction]):
        auctioned (Union[Unset, bool]):
        house_id (Union[Unset, int]):
        name (Union[Unset, str]):
        rent (Union[Unset, int]):
        rented (Union[Unset, bool]):
        size (Union[Unset, int]):
    """

    auction: Union[Unset, "MainHousesAuction"] = UNSET
    auctioned: Union[Unset, bool] = UNSET
    house_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    rent: Union[Unset, int] = UNSET
    rented: Union[Unset, bool] = UNSET
    size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auction, Unset):
            auction = self.auction.to_dict()

        auctioned = self.auctioned
        house_id = self.house_id
        name = self.name
        rent = self.rent
        rented = self.rented
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auction is not UNSET:
            field_dict["auction"] = auction
        if auctioned is not UNSET:
            field_dict["auctioned"] = auctioned
        if house_id is not UNSET:
            field_dict["house_id"] = house_id
        if name is not UNSET:
            field_dict["name"] = name
        if rent is not UNSET:
            field_dict["rent"] = rent
        if rented is not UNSET:
            field_dict["rented"] = rented
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_houses_auction import MainHousesAuction

        d = src_dict.copy()
        _auction = d.pop("auction", UNSET)
        auction: Union[Unset, MainHousesAuction]
        if isinstance(_auction, Unset):
            auction = UNSET
        else:
            auction = MainHousesAuction.from_dict(_auction)

        auctioned = d.pop("auctioned", UNSET)

        house_id = d.pop("house_id", UNSET)

        name = d.pop("name", UNSET)

        rent = d.pop("rent", UNSET)

        rented = d.pop("rented", UNSET)

        size = d.pop("size", UNSET)

        main_houses_house = cls(
            auction=auction,
            auctioned=auctioned,
            house_id=house_id,
            name=name,
            rent=rent,
            rented=rented,
            size=size,
        )

        main_houses_house.additional_properties = d
        return main_houses_house

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
