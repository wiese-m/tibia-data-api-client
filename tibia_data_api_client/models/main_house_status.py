from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_house_auction import MainHouseAuction
    from ..models.main_house_rental import MainHouseRental


T = TypeVar("T", bound="MainHouseStatus")


@_attrs_define
class MainHouseStatus:
    """
    Attributes:
        auction (Union[Unset, MainHouseAuction]):
        is_auctioned (Union[Unset, bool]):
        is_moving (Union[Unset, bool]):
        is_rented (Union[Unset, bool]):
        is_transfering (Union[Unset, bool]):
        original (Union[Unset, str]):
        rental (Union[Unset, MainHouseRental]):
    """

    auction: Union[Unset, "MainHouseAuction"] = UNSET
    is_auctioned: Union[Unset, bool] = UNSET
    is_moving: Union[Unset, bool] = UNSET
    is_rented: Union[Unset, bool] = UNSET
    is_transfering: Union[Unset, bool] = UNSET
    original: Union[Unset, str] = UNSET
    rental: Union[Unset, "MainHouseRental"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auction, Unset):
            auction = self.auction.to_dict()

        is_auctioned = self.is_auctioned
        is_moving = self.is_moving
        is_rented = self.is_rented
        is_transfering = self.is_transfering
        original = self.original
        rental: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rental, Unset):
            rental = self.rental.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auction is not UNSET:
            field_dict["auction"] = auction
        if is_auctioned is not UNSET:
            field_dict["is_auctioned"] = is_auctioned
        if is_moving is not UNSET:
            field_dict["is_moving"] = is_moving
        if is_rented is not UNSET:
            field_dict["is_rented"] = is_rented
        if is_transfering is not UNSET:
            field_dict["is_transfering"] = is_transfering
        if original is not UNSET:
            field_dict["original"] = original
        if rental is not UNSET:
            field_dict["rental"] = rental

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_house_auction import MainHouseAuction
        from ..models.main_house_rental import MainHouseRental

        d = src_dict.copy()
        _auction = d.pop("auction", UNSET)
        auction: Union[Unset, MainHouseAuction]
        if isinstance(_auction, Unset):
            auction = UNSET
        else:
            auction = MainHouseAuction.from_dict(_auction)

        is_auctioned = d.pop("is_auctioned", UNSET)

        is_moving = d.pop("is_moving", UNSET)

        is_rented = d.pop("is_rented", UNSET)

        is_transfering = d.pop("is_transfering", UNSET)

        original = d.pop("original", UNSET)

        _rental = d.pop("rental", UNSET)
        rental: Union[Unset, MainHouseRental]
        if isinstance(_rental, Unset):
            rental = UNSET
        else:
            rental = MainHouseRental.from_dict(_rental)

        main_house_status = cls(
            auction=auction,
            is_auctioned=is_auctioned,
            is_moving=is_moving,
            is_rented=is_rented,
            is_transfering=is_transfering,
            original=original,
            rental=rental,
        )

        main_house_status.additional_properties = d
        return main_house_status

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
