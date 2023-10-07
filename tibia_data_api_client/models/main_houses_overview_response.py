from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_houses_houses import MainHousesHouses
    from ..models.main_information import MainInformation


T = TypeVar("T", bound="MainHousesOverviewResponse")


@_attrs_define
class MainHousesOverviewResponse:
    """
    Attributes:
        houses (Union[Unset, MainHousesHouses]):
        information (Union[Unset, MainInformation]):
    """

    houses: Union[Unset, "MainHousesHouses"] = UNSET
    information: Union[Unset, "MainInformation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        houses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.houses, Unset):
            houses = self.houses.to_dict()

        information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.information, Unset):
            information = self.information.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if houses is not UNSET:
            field_dict["houses"] = houses
        if information is not UNSET:
            field_dict["information"] = information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_houses_houses import MainHousesHouses
        from ..models.main_information import MainInformation

        d = src_dict.copy()
        _houses = d.pop("houses", UNSET)
        houses: Union[Unset, MainHousesHouses]
        if isinstance(_houses, Unset):
            houses = UNSET
        else:
            houses = MainHousesHouses.from_dict(_houses)

        _information = d.pop("information", UNSET)
        information: Union[Unset, MainInformation]
        if isinstance(_information, Unset):
            information = UNSET
        else:
            information = MainInformation.from_dict(_information)

        main_houses_overview_response = cls(
            houses=houses,
            information=information,
        )

        main_houses_overview_response.additional_properties = d
        return main_houses_overview_response

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
