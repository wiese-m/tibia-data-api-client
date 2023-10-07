from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainHouseRental")


@_attrs_define
class MainHouseRental:
    """
    Attributes:
        moving_date (Union[Unset, str]):
        owner (Union[Unset, str]):
        owner_sex (Union[Unset, str]):
        paid_until (Union[Unset, str]):
        transfer_accept (Union[Unset, bool]):
        transfer_price (Union[Unset, int]):
        transfer_receiver (Union[Unset, str]):
    """

    moving_date: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    owner_sex: Union[Unset, str] = UNSET
    paid_until: Union[Unset, str] = UNSET
    transfer_accept: Union[Unset, bool] = UNSET
    transfer_price: Union[Unset, int] = UNSET
    transfer_receiver: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        moving_date = self.moving_date
        owner = self.owner
        owner_sex = self.owner_sex
        paid_until = self.paid_until
        transfer_accept = self.transfer_accept
        transfer_price = self.transfer_price
        transfer_receiver = self.transfer_receiver

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if moving_date is not UNSET:
            field_dict["moving_date"] = moving_date
        if owner is not UNSET:
            field_dict["owner"] = owner
        if owner_sex is not UNSET:
            field_dict["owner_sex"] = owner_sex
        if paid_until is not UNSET:
            field_dict["paid_until"] = paid_until
        if transfer_accept is not UNSET:
            field_dict["transfer_accept"] = transfer_accept
        if transfer_price is not UNSET:
            field_dict["transfer_price"] = transfer_price
        if transfer_receiver is not UNSET:
            field_dict["transfer_receiver"] = transfer_receiver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        moving_date = d.pop("moving_date", UNSET)

        owner = d.pop("owner", UNSET)

        owner_sex = d.pop("owner_sex", UNSET)

        paid_until = d.pop("paid_until", UNSET)

        transfer_accept = d.pop("transfer_accept", UNSET)

        transfer_price = d.pop("transfer_price", UNSET)

        transfer_receiver = d.pop("transfer_receiver", UNSET)

        main_house_rental = cls(
            moving_date=moving_date,
            owner=owner,
            owner_sex=owner_sex,
            paid_until=paid_until,
            transfer_accept=transfer_accept,
            transfer_price=transfer_price,
            transfer_receiver=transfer_receiver,
        )

        main_house_rental.additional_properties = d
        return main_house_rental

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
