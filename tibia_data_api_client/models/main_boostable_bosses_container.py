from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_overview_boostable_boss import MainOverviewBoostableBoss


T = TypeVar("T", bound="MainBoostableBossesContainer")


@_attrs_define
class MainBoostableBossesContainer:
    """
    Attributes:
        boostable_boss_list (Union[Unset, List['MainOverviewBoostableBoss']]):
        boosted (Union[Unset, MainOverviewBoostableBoss]):
    """

    boostable_boss_list: Union[Unset, List["MainOverviewBoostableBoss"]] = UNSET
    boosted: Union[Unset, "MainOverviewBoostableBoss"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boostable_boss_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.boostable_boss_list, Unset):
            boostable_boss_list = []
            for boostable_boss_list_item_data in self.boostable_boss_list:
                boostable_boss_list_item = boostable_boss_list_item_data.to_dict()

                boostable_boss_list.append(boostable_boss_list_item)

        boosted: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boosted, Unset):
            boosted = self.boosted.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boostable_boss_list is not UNSET:
            field_dict["boostable_boss_list"] = boostable_boss_list
        if boosted is not UNSET:
            field_dict["boosted"] = boosted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_overview_boostable_boss import MainOverviewBoostableBoss

        d = src_dict.copy()
        boostable_boss_list = []
        _boostable_boss_list = d.pop("boostable_boss_list", UNSET)
        for boostable_boss_list_item_data in _boostable_boss_list or []:
            boostable_boss_list_item = MainOverviewBoostableBoss.from_dict(boostable_boss_list_item_data)

            boostable_boss_list.append(boostable_boss_list_item)

        _boosted = d.pop("boosted", UNSET)
        boosted: Union[Unset, MainOverviewBoostableBoss]
        if isinstance(_boosted, Unset):
            boosted = UNSET
        else:
            boosted = MainOverviewBoostableBoss.from_dict(_boosted)

        main_boostable_bosses_container = cls(
            boostable_boss_list=boostable_boss_list,
            boosted=boosted,
        )

        main_boostable_bosses_container.additional_properties = d
        return main_boostable_bosses_container

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
