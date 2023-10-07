from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainSpell")


@_attrs_define
class MainSpell:
    """
    Attributes:
        formula (Union[Unset, str]):
        group_attack (Union[Unset, bool]):
        group_healing (Union[Unset, bool]):
        group_support (Union[Unset, bool]):
        level (Union[Unset, int]):
        mana (Union[Unset, int]):
        name (Union[Unset, str]):
        premium_only (Union[Unset, bool]):
        price (Union[Unset, int]):
        spell_id (Union[Unset, str]):
        type_instant (Union[Unset, bool]):
        type_rune (Union[Unset, bool]):
    """

    formula: Union[Unset, str] = UNSET
    group_attack: Union[Unset, bool] = UNSET
    group_healing: Union[Unset, bool] = UNSET
    group_support: Union[Unset, bool] = UNSET
    level: Union[Unset, int] = UNSET
    mana: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    premium_only: Union[Unset, bool] = UNSET
    price: Union[Unset, int] = UNSET
    spell_id: Union[Unset, str] = UNSET
    type_instant: Union[Unset, bool] = UNSET
    type_rune: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        formula = self.formula
        group_attack = self.group_attack
        group_healing = self.group_healing
        group_support = self.group_support
        level = self.level
        mana = self.mana
        name = self.name
        premium_only = self.premium_only
        price = self.price
        spell_id = self.spell_id
        type_instant = self.type_instant
        type_rune = self.type_rune

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if formula is not UNSET:
            field_dict["formula"] = formula
        if group_attack is not UNSET:
            field_dict["group_attack"] = group_attack
        if group_healing is not UNSET:
            field_dict["group_healing"] = group_healing
        if group_support is not UNSET:
            field_dict["group_support"] = group_support
        if level is not UNSET:
            field_dict["level"] = level
        if mana is not UNSET:
            field_dict["mana"] = mana
        if name is not UNSET:
            field_dict["name"] = name
        if premium_only is not UNSET:
            field_dict["premium_only"] = premium_only
        if price is not UNSET:
            field_dict["price"] = price
        if spell_id is not UNSET:
            field_dict["spell_id"] = spell_id
        if type_instant is not UNSET:
            field_dict["type_instant"] = type_instant
        if type_rune is not UNSET:
            field_dict["type_rune"] = type_rune

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        formula = d.pop("formula", UNSET)

        group_attack = d.pop("group_attack", UNSET)

        group_healing = d.pop("group_healing", UNSET)

        group_support = d.pop("group_support", UNSET)

        level = d.pop("level", UNSET)

        mana = d.pop("mana", UNSET)

        name = d.pop("name", UNSET)

        premium_only = d.pop("premium_only", UNSET)

        price = d.pop("price", UNSET)

        spell_id = d.pop("spell_id", UNSET)

        type_instant = d.pop("type_instant", UNSET)

        type_rune = d.pop("type_rune", UNSET)

        main_spell = cls(
            formula=formula,
            group_attack=group_attack,
            group_healing=group_healing,
            group_support=group_support,
            level=level,
            mana=mana,
            name=name,
            premium_only=premium_only,
            price=price,
            spell_id=spell_id,
            type_instant=type_instant,
            type_rune=type_rune,
        )

        main_spell.additional_properties = d
        return main_spell

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
