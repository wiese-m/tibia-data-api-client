from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_spell import MainSpell


T = TypeVar("T", bound="MainSpells")


@_attrs_define
class MainSpells:
    """
    Attributes:
        spell_list (Union[Unset, List['MainSpell']]):
        spells_filter (Union[Unset, str]):
    """

    spell_list: Union[Unset, List["MainSpell"]] = UNSET
    spells_filter: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spell_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.spell_list, Unset):
            spell_list = []
            for spell_list_item_data in self.spell_list:
                spell_list_item = spell_list_item_data.to_dict()

                spell_list.append(spell_list_item)

        spells_filter = self.spells_filter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spell_list is not UNSET:
            field_dict["spell_list"] = spell_list
        if spells_filter is not UNSET:
            field_dict["spells_filter"] = spells_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_spell import MainSpell

        d = src_dict.copy()
        spell_list = []
        _spell_list = d.pop("spell_list", UNSET)
        for spell_list_item_data in _spell_list or []:
            spell_list_item = MainSpell.from_dict(spell_list_item_data)

            spell_list.append(spell_list_item)

        spells_filter = d.pop("spells_filter", UNSET)

        main_spells = cls(
            spell_list=spell_list,
            spells_filter=spells_filter,
        )

        main_spells.additional_properties = d
        return main_spells

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
