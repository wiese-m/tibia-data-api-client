from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_spell_data import MainSpellData


T = TypeVar("T", bound="MainSpellsContainer")


@_attrs_define
class MainSpellsContainer:
    """
    Attributes:
        spell (Union[Unset, MainSpellData]):
    """

    spell: Union[Unset, "MainSpellData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spell: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spell, Unset):
            spell = self.spell.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spell is not UNSET:
            field_dict["spell"] = spell

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_spell_data import MainSpellData

        d = src_dict.copy()
        _spell = d.pop("spell", UNSET)
        spell: Union[Unset, MainSpellData]
        if isinstance(_spell, Unset):
            spell = UNSET
        else:
            spell = MainSpellData.from_dict(_spell)

        main_spells_container = cls(
            spell=spell,
        )

        main_spells_container.additional_properties = d
        return main_spells_container

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
