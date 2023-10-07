from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainHouseAuction")


@_attrs_define
class MainHouseAuction:
    """
    Attributes:
        auction_end (Union[Unset, str]):
        auction_ongoing (Union[Unset, bool]):
        current_bid (Union[Unset, int]):
        current_bidder (Union[Unset, str]):
    """

    auction_end: Union[Unset, str] = UNSET
    auction_ongoing: Union[Unset, bool] = UNSET
    current_bid: Union[Unset, int] = UNSET
    current_bidder: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auction_end = self.auction_end
        auction_ongoing = self.auction_ongoing
        current_bid = self.current_bid
        current_bidder = self.current_bidder

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auction_end is not UNSET:
            field_dict["auction_end"] = auction_end
        if auction_ongoing is not UNSET:
            field_dict["auction_ongoing"] = auction_ongoing
        if current_bid is not UNSET:
            field_dict["current_bid"] = current_bid
        if current_bidder is not UNSET:
            field_dict["current_bidder"] = current_bidder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auction_end = d.pop("auction_end", UNSET)

        auction_ongoing = d.pop("auction_ongoing", UNSET)

        current_bid = d.pop("current_bid", UNSET)

        current_bidder = d.pop("current_bidder", UNSET)

        main_house_auction = cls(
            auction_end=auction_end,
            auction_ongoing=auction_ongoing,
            current_bid=current_bid,
            current_bidder=current_bidder,
        )

        main_house_auction.additional_properties = d
        return main_house_auction

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
