from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainSpellInformation")


@_attrs_define
class MainSpellInformation:
    """
    Attributes:
        amount (Union[Unset, int]):
        city (Union[Unset, List[str]]):
        cooldown_alone (Union[Unset, int]):
        cooldown_group (Union[Unset, int]):
        damage_type (Union[Unset, str]):
        formula (Union[Unset, str]):
        group_attack (Union[Unset, bool]):
        group_healing (Union[Unset, bool]):
        group_support (Union[Unset, bool]):
        level (Union[Unset, int]):
        mana (Union[Unset, int]):
        premium_only (Union[Unset, bool]):
        price (Union[Unset, int]):
        soul_points (Union[Unset, int]):
        type_instant (Union[Unset, bool]):
        type_rune (Union[Unset, bool]):
        vocation (Union[Unset, List[str]]):
    """

    amount: Union[Unset, int] = UNSET
    city: Union[Unset, List[str]] = UNSET
    cooldown_alone: Union[Unset, int] = UNSET
    cooldown_group: Union[Unset, int] = UNSET
    damage_type: Union[Unset, str] = UNSET
    formula: Union[Unset, str] = UNSET
    group_attack: Union[Unset, bool] = UNSET
    group_healing: Union[Unset, bool] = UNSET
    group_support: Union[Unset, bool] = UNSET
    level: Union[Unset, int] = UNSET
    mana: Union[Unset, int] = UNSET
    premium_only: Union[Unset, bool] = UNSET
    price: Union[Unset, int] = UNSET
    soul_points: Union[Unset, int] = UNSET
    type_instant: Union[Unset, bool] = UNSET
    type_rune: Union[Unset, bool] = UNSET
    vocation: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        city: Union[Unset, List[str]] = UNSET
        if not isinstance(self.city, Unset):
            city = self.city

        cooldown_alone = self.cooldown_alone
        cooldown_group = self.cooldown_group
        damage_type = self.damage_type
        formula = self.formula
        group_attack = self.group_attack
        group_healing = self.group_healing
        group_support = self.group_support
        level = self.level
        mana = self.mana
        premium_only = self.premium_only
        price = self.price
        soul_points = self.soul_points
        type_instant = self.type_instant
        type_rune = self.type_rune
        vocation: Union[Unset, List[str]] = UNSET
        if not isinstance(self.vocation, Unset):
            vocation = self.vocation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if city is not UNSET:
            field_dict["city"] = city
        if cooldown_alone is not UNSET:
            field_dict["cooldown_alone"] = cooldown_alone
        if cooldown_group is not UNSET:
            field_dict["cooldown_group"] = cooldown_group
        if damage_type is not UNSET:
            field_dict["damage_type"] = damage_type
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
        if premium_only is not UNSET:
            field_dict["premium_only"] = premium_only
        if price is not UNSET:
            field_dict["price"] = price
        if soul_points is not UNSET:
            field_dict["soul_points"] = soul_points
        if type_instant is not UNSET:
            field_dict["type_instant"] = type_instant
        if type_rune is not UNSET:
            field_dict["type_rune"] = type_rune
        if vocation is not UNSET:
            field_dict["vocation"] = vocation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        city = cast(List[str], d.pop("city", UNSET))

        cooldown_alone = d.pop("cooldown_alone", UNSET)

        cooldown_group = d.pop("cooldown_group", UNSET)

        damage_type = d.pop("damage_type", UNSET)

        formula = d.pop("formula", UNSET)

        group_attack = d.pop("group_attack", UNSET)

        group_healing = d.pop("group_healing", UNSET)

        group_support = d.pop("group_support", UNSET)

        level = d.pop("level", UNSET)

        mana = d.pop("mana", UNSET)

        premium_only = d.pop("premium_only", UNSET)

        price = d.pop("price", UNSET)

        soul_points = d.pop("soul_points", UNSET)

        type_instant = d.pop("type_instant", UNSET)

        type_rune = d.pop("type_rune", UNSET)

        vocation = cast(List[str], d.pop("vocation", UNSET))

        main_spell_information = cls(
            amount=amount,
            city=city,
            cooldown_alone=cooldown_alone,
            cooldown_group=cooldown_group,
            damage_type=damage_type,
            formula=formula,
            group_attack=group_attack,
            group_healing=group_healing,
            group_support=group_support,
            level=level,
            mana=mana,
            premium_only=premium_only,
            price=price,
            soul_points=soul_points,
            type_instant=type_instant,
            type_rune=type_rune,
            vocation=vocation,
        )

        main_spell_information.additional_properties = d
        return main_spell_information

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
