from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_highscores import MainHighscores
    from ..models.main_information import MainInformation


T = TypeVar("T", bound="MainHighscoresResponse")


@_attrs_define
class MainHighscoresResponse:
    """
    Attributes:
        highscores (Union[Unset, MainHighscores]):
        information (Union[Unset, MainInformation]):
    """

    highscores: Union[Unset, "MainHighscores"] = UNSET
    information: Union[Unset, "MainInformation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        highscores: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.highscores, Unset):
            highscores = self.highscores.to_dict()

        information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.information, Unset):
            information = self.information.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if highscores is not UNSET:
            field_dict["highscores"] = highscores
        if information is not UNSET:
            field_dict["information"] = information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_highscores import MainHighscores
        from ..models.main_information import MainInformation

        d = src_dict.copy()
        _highscores = d.pop("highscores", UNSET)
        highscores: Union[Unset, MainHighscores]
        if isinstance(_highscores, Unset):
            highscores = UNSET
        else:
            highscores = MainHighscores.from_dict(_highscores)

        _information = d.pop("information", UNSET)
        information: Union[Unset, MainInformation]
        if isinstance(_information, Unset):
            information = UNSET
        else:
            information = MainInformation.from_dict(_information)

        main_highscores_response = cls(
            highscores=highscores,
            information=information,
        )

        main_highscores_response.additional_properties = d
        return main_highscores_response

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
