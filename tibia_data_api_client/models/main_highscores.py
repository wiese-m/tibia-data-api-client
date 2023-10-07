from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_highscore import MainHighscore
    from ..models.main_highscore_page import MainHighscorePage


T = TypeVar("T", bound="MainHighscores")


@_attrs_define
class MainHighscores:
    """
    Attributes:
        category (Union[Unset, str]):
        highscore_age (Union[Unset, int]):
        highscore_list (Union[Unset, List['MainHighscore']]):
        highscore_page (Union[Unset, MainHighscorePage]):
        vocation (Union[Unset, str]):
        world (Union[Unset, str]):
    """

    category: Union[Unset, str] = UNSET
    highscore_age: Union[Unset, int] = UNSET
    highscore_list: Union[Unset, List["MainHighscore"]] = UNSET
    highscore_page: Union[Unset, "MainHighscorePage"] = UNSET
    vocation: Union[Unset, str] = UNSET
    world: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        highscore_age = self.highscore_age
        highscore_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.highscore_list, Unset):
            highscore_list = []
            for highscore_list_item_data in self.highscore_list:
                highscore_list_item = highscore_list_item_data.to_dict()

                highscore_list.append(highscore_list_item)

        highscore_page: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.highscore_page, Unset):
            highscore_page = self.highscore_page.to_dict()

        vocation = self.vocation
        world = self.world

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if highscore_age is not UNSET:
            field_dict["highscore_age"] = highscore_age
        if highscore_list is not UNSET:
            field_dict["highscore_list"] = highscore_list
        if highscore_page is not UNSET:
            field_dict["highscore_page"] = highscore_page
        if vocation is not UNSET:
            field_dict["vocation"] = vocation
        if world is not UNSET:
            field_dict["world"] = world

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.main_highscore import MainHighscore
        from ..models.main_highscore_page import MainHighscorePage

        d = src_dict.copy()
        category = d.pop("category", UNSET)

        highscore_age = d.pop("highscore_age", UNSET)

        highscore_list = []
        _highscore_list = d.pop("highscore_list", UNSET)
        for highscore_list_item_data in _highscore_list or []:
            highscore_list_item = MainHighscore.from_dict(highscore_list_item_data)

            highscore_list.append(highscore_list_item)

        _highscore_page = d.pop("highscore_page", UNSET)
        highscore_page: Union[Unset, MainHighscorePage]
        if isinstance(_highscore_page, Unset):
            highscore_page = UNSET
        else:
            highscore_page = MainHighscorePage.from_dict(_highscore_page)

        vocation = d.pop("vocation", UNSET)

        world = d.pop("world", UNSET)

        main_highscores = cls(
            category=category,
            highscore_age=highscore_age,
            highscore_list=highscore_list,
            highscore_page=highscore_page,
            vocation=vocation,
            world=world,
        )

        main_highscores.additional_properties = d
        return main_highscores

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
