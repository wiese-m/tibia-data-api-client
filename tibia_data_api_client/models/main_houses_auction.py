from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainHousesAuction")


@_attrs_define
class MainHousesAuction:
    """
    Attributes:
        current_bid (Union[Unset, int]):
        finished (Union[Unset, bool]):
        time_left (Union[Unset, str]):
    """

    current_bid: Union[Unset, int] = UNSET
    finished: Union[Unset, bool] = UNSET
    time_left: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_bid = self.current_bid
        finished = self.finished
        time_left = self.time_left

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_bid is not UNSET:
            field_dict["current_bid"] = current_bid
        if finished is not UNSET:
            field_dict["finished"] = finished
        if time_left is not UNSET:
            field_dict["time_left"] = time_left

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_bid = d.pop("current_bid", UNSET)

        finished = d.pop("finished", UNSET)

        time_left = d.pop("time_left", UNSET)

        main_houses_auction = cls(
            current_bid=current_bid,
            finished=finished,
            time_left=time_left,
        )

        main_houses_auction.additional_properties = d
        return main_houses_auction

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
