from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_overview_creature import MainOverviewCreature


T = TypeVar("T", bound="MainCreaturesContainer")


@_attrs_define
class MainCreaturesContainer:
    """
    Attributes:
        boosted (Union[Unset, MainOverviewCreature]):
        creature_list (Union[Unset, List['MainOverviewCreature']]):
    """

    boosted: Union[Unset, "MainOverviewCreature"] = UNSET
    creature_list: Union[Unset, List["MainOverviewCreature"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boosted: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boosted, Unset):
            boosted = self.boosted.to_dict()

        creature_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.creature_list, Unset):
            creature_list = []
            for creature_list_item_data in self.creature_list:
                creature_list_item = creature_list_item_data.to_dict()

                creature_list.append(creature_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boosted is not UNSET:
            field_dict["boosted"] = boosted
        if creature_list is not UNSET:
            field_dict["creature_list"] = creature_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_overview_creature import MainOverviewCreature

        d = src_dict.copy()
        _boosted = d.pop("boosted", UNSET)
        boosted: Union[Unset, MainOverviewCreature]
        if isinstance(_boosted, Unset):
            boosted = UNSET
        else:
            boosted = MainOverviewCreature.from_dict(_boosted)

        creature_list = []
        _creature_list = d.pop("creature_list", UNSET)
        for creature_list_item_data in _creature_list or []:
            creature_list_item = MainOverviewCreature.from_dict(creature_list_item_data)

            creature_list.append(creature_list_item)

        main_creatures_container = cls(
            boosted=boosted,
            creature_list=creature_list,
        )

        main_creatures_container.additional_properties = d
        return main_creatures_container

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
