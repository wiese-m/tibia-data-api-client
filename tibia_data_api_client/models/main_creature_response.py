from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_creature import MainCreature
    from ..models.main_information import MainInformation


T = TypeVar("T", bound="MainCreatureResponse")


@_attrs_define
class MainCreatureResponse:
    """
    Attributes:
        creature (Union[Unset, MainCreature]):
        information (Union[Unset, MainInformation]):
    """

    creature: Union[Unset, "MainCreature"] = UNSET
    information: Union[Unset, "MainInformation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creature: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.creature, Unset):
            creature = self.creature.to_dict()

        information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.information, Unset):
            information = self.information.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creature is not UNSET:
            field_dict["creature"] = creature
        if information is not UNSET:
            field_dict["information"] = information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_creature import MainCreature
        from ..models.main_information import MainInformation

        d = src_dict.copy()
        _creature = d.pop("creature", UNSET)
        creature: Union[Unset, MainCreature]
        if isinstance(_creature, Unset):
            creature = UNSET
        else:
            creature = MainCreature.from_dict(_creature)

        _information = d.pop("information", UNSET)
        information: Union[Unset, MainInformation]
        if isinstance(_information, Unset):
            information = UNSET
        else:
            information = MainInformation.from_dict(_information)

        main_creature_response = cls(
            creature=creature,
            information=information,
        )

        main_creature_response.additional_properties = d
        return main_creature_response

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
