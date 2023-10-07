from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_rune_information import MainRuneInformation
    from ..models.main_spell_information import MainSpellInformation


T = TypeVar("T", bound="MainSpellData")


@_attrs_define
class MainSpellData:
    """
    Attributes:
        description (Union[Unset, str]):
        has_rune_information (Union[Unset, bool]):
        has_spell_information (Union[Unset, bool]):
        image_url (Union[Unset, str]):
        name (Union[Unset, str]):
        rune_information (Union[Unset, MainRuneInformation]):
        spell_id (Union[Unset, str]):
        spell_information (Union[Unset, MainSpellInformation]):
    """

    description: Union[Unset, str] = UNSET
    has_rune_information: Union[Unset, bool] = UNSET
    has_spell_information: Union[Unset, bool] = UNSET
    image_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    rune_information: Union[Unset, "MainRuneInformation"] = UNSET
    spell_id: Union[Unset, str] = UNSET
    spell_information: Union[Unset, "MainSpellInformation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        has_rune_information = self.has_rune_information
        has_spell_information = self.has_spell_information
        image_url = self.image_url
        name = self.name
        rune_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rune_information, Unset):
            rune_information = self.rune_information.to_dict()

        spell_id = self.spell_id
        spell_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spell_information, Unset):
            spell_information = self.spell_information.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if has_rune_information is not UNSET:
            field_dict["has_rune_information"] = has_rune_information
        if has_spell_information is not UNSET:
            field_dict["has_spell_information"] = has_spell_information
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if name is not UNSET:
            field_dict["name"] = name
        if rune_information is not UNSET:
            field_dict["rune_information"] = rune_information
        if spell_id is not UNSET:
            field_dict["spell_id"] = spell_id
        if spell_information is not UNSET:
            field_dict["spell_information"] = spell_information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_rune_information import MainRuneInformation
        from ..models.main_spell_information import MainSpellInformation

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        has_rune_information = d.pop("has_rune_information", UNSET)

        has_spell_information = d.pop("has_spell_information", UNSET)

        image_url = d.pop("image_url", UNSET)

        name = d.pop("name", UNSET)

        _rune_information = d.pop("rune_information", UNSET)
        rune_information: Union[Unset, MainRuneInformation]
        if isinstance(_rune_information, Unset):
            rune_information = UNSET
        else:
            rune_information = MainRuneInformation.from_dict(_rune_information)

        spell_id = d.pop("spell_id", UNSET)

        _spell_information = d.pop("spell_information", UNSET)
        spell_information: Union[Unset, MainSpellInformation]
        if isinstance(_spell_information, Unset):
            spell_information = UNSET
        else:
            spell_information = MainSpellInformation.from_dict(_spell_information)

        main_spell_data = cls(
            description=description,
            has_rune_information=has_rune_information,
            has_spell_information=has_spell_information,
            image_url=image_url,
            name=name,
            rune_information=rune_information,
            spell_id=spell_id,
            spell_information=spell_information,
        )

        main_spell_data.additional_properties = d
        return main_spell_data

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
