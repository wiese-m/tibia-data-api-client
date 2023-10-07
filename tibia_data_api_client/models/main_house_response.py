from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_house import MainHouse
    from ..models.main_information import MainInformation


T = TypeVar("T", bound="MainHouseResponse")


@_attrs_define
class MainHouseResponse:
    """
    Attributes:
        house (Union[Unset, MainHouse]):
        information (Union[Unset, MainInformation]):
    """

    house: Union[Unset, "MainHouse"] = UNSET
    information: Union[Unset, "MainInformation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        house: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.house, Unset):
            house = self.house.to_dict()

        information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.information, Unset):
            information = self.information.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if house is not UNSET:
            field_dict["house"] = house
        if information is not UNSET:
            field_dict["information"] = information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_house import MainHouse
        from ..models.main_information import MainInformation

        d = src_dict.copy()
        _house = d.pop("house", UNSET)
        house: Union[Unset, MainHouse]
        if isinstance(_house, Unset):
            house = UNSET
        else:
            house = MainHouse.from_dict(_house)

        _information = d.pop("information", UNSET)
        information: Union[Unset, MainInformation]
        if isinstance(_information, Unset):
            information = UNSET
        else:
            information = MainInformation.from_dict(_information)

        main_house_response = cls(
            house=house,
            information=information,
        )

        main_house_response.additional_properties = d
        return main_house_response

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
