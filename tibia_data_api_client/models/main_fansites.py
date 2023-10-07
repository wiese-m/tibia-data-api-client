from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_fansite import MainFansite


T = TypeVar("T", bound="MainFansites")


@_attrs_define
class MainFansites:
    """
    Attributes:
        promoted (Union[Unset, List['MainFansite']]):
        supported (Union[Unset, List['MainFansite']]):
    """

    promoted: Union[Unset, List["MainFansite"]] = UNSET
    supported: Union[Unset, List["MainFansite"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        promoted: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.promoted, Unset):
            promoted = []
            for promoted_item_data in self.promoted:
                promoted_item = promoted_item_data.to_dict()

                promoted.append(promoted_item)

        supported: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.supported, Unset):
            supported = []
            for supported_item_data in self.supported:
                supported_item = supported_item_data.to_dict()

                supported.append(supported_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promoted is not UNSET:
            field_dict["promoted"] = promoted
        if supported is not UNSET:
            field_dict["supported"] = supported

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_fansite import MainFansite

        d = src_dict.copy()
        promoted = []
        _promoted = d.pop("promoted", UNSET)
        for promoted_item_data in _promoted or []:
            promoted_item = MainFansite.from_dict(promoted_item_data)

            promoted.append(promoted_item)

        supported = []
        _supported = d.pop("supported", UNSET)
        for supported_item_data in _supported or []:
            supported_item = MainFansite.from_dict(supported_item_data)

            supported.append(supported_item)

        main_fansites = cls(
            promoted=promoted,
            supported=supported,
        )

        main_fansites.additional_properties = d
        return main_fansites

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
