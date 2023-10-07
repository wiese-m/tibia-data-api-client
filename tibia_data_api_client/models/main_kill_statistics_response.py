from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_information import MainInformation
    from ..models.main_kill_statistics import MainKillStatistics


T = TypeVar("T", bound="MainKillStatisticsResponse")


@_attrs_define
class MainKillStatisticsResponse:
    """
    Attributes:
        information (Union[Unset, MainInformation]):
        killstatistics (Union[Unset, MainKillStatistics]):
    """

    information: Union[Unset, "MainInformation"] = UNSET
    killstatistics: Union[Unset, "MainKillStatistics"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.information, Unset):
            information = self.information.to_dict()

        killstatistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.killstatistics, Unset):
            killstatistics = self.killstatistics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if information is not UNSET:
            field_dict["information"] = information
        if killstatistics is not UNSET:
            field_dict["killstatistics"] = killstatistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_information import MainInformation
        from ..models.main_kill_statistics import MainKillStatistics

        d = src_dict.copy()
        _information = d.pop("information", UNSET)
        information: Union[Unset, MainInformation]
        if isinstance(_information, Unset):
            information = UNSET
        else:
            information = MainInformation.from_dict(_information)

        _killstatistics = d.pop("killstatistics", UNSET)
        killstatistics: Union[Unset, MainKillStatistics]
        if isinstance(_killstatistics, Unset):
            killstatistics = UNSET
        else:
            killstatistics = MainKillStatistics.from_dict(_killstatistics)

        main_kill_statistics_response = cls(
            information=information,
            killstatistics=killstatistics,
        )

        main_kill_statistics_response.additional_properties = d
        return main_kill_statistics_response

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
