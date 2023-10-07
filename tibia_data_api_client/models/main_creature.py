from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainCreature")


@_attrs_define
class MainCreature:
    """
    Attributes:
        be_convinced (Union[Unset, bool]):
        be_paralysed (Union[Unset, bool]):
        be_summoned (Union[Unset, bool]):
        behaviour (Union[Unset, str]):
        convinced_mana (Union[Unset, int]):
        description (Union[Unset, str]):
        experience_points (Union[Unset, int]):
        featured (Union[Unset, bool]):
        healed (Union[Unset, List[str]]):
        hitpoints (Union[Unset, int]):
        image_url (Union[Unset, str]):
        immune (Union[Unset, List[str]]):
        is_lootable (Union[Unset, bool]):
        loot_list (Union[Unset, List[str]]):
        name (Union[Unset, str]):
        race (Union[Unset, str]):
        see_invisible (Union[Unset, bool]):
        strong (Union[Unset, List[str]]):
        summoned_mana (Union[Unset, int]):
        weakness (Union[Unset, List[str]]):
    """

    be_convinced: Union[Unset, bool] = UNSET
    be_paralysed: Union[Unset, bool] = UNSET
    be_summoned: Union[Unset, bool] = UNSET
    behaviour: Union[Unset, str] = UNSET
    convinced_mana: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    experience_points: Union[Unset, int] = UNSET
    featured: Union[Unset, bool] = UNSET
    healed: Union[Unset, List[str]] = UNSET
    hitpoints: Union[Unset, int] = UNSET
    image_url: Union[Unset, str] = UNSET
    immune: Union[Unset, List[str]] = UNSET
    is_lootable: Union[Unset, bool] = UNSET
    loot_list: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    race: Union[Unset, str] = UNSET
    see_invisible: Union[Unset, bool] = UNSET
    strong: Union[Unset, List[str]] = UNSET
    summoned_mana: Union[Unset, int] = UNSET
    weakness: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        be_convinced = self.be_convinced
        be_paralysed = self.be_paralysed
        be_summoned = self.be_summoned
        behaviour = self.behaviour
        convinced_mana = self.convinced_mana
        description = self.description
        experience_points = self.experience_points
        featured = self.featured
        healed: Union[Unset, List[str]] = UNSET
        if not isinstance(self.healed, Unset):
            healed = self.healed

        hitpoints = self.hitpoints
        image_url = self.image_url
        immune: Union[Unset, List[str]] = UNSET
        if not isinstance(self.immune, Unset):
            immune = self.immune

        is_lootable = self.is_lootable
        loot_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.loot_list, Unset):
            loot_list = self.loot_list

        name = self.name
        race = self.race
        see_invisible = self.see_invisible
        strong: Union[Unset, List[str]] = UNSET
        if not isinstance(self.strong, Unset):
            strong = self.strong

        summoned_mana = self.summoned_mana
        weakness: Union[Unset, List[str]] = UNSET
        if not isinstance(self.weakness, Unset):
            weakness = self.weakness

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if be_convinced is not UNSET:
            field_dict["be_convinced"] = be_convinced
        if be_paralysed is not UNSET:
            field_dict["be_paralysed"] = be_paralysed
        if be_summoned is not UNSET:
            field_dict["be_summoned"] = be_summoned
        if behaviour is not UNSET:
            field_dict["behaviour"] = behaviour
        if convinced_mana is not UNSET:
            field_dict["convinced_mana"] = convinced_mana
        if description is not UNSET:
            field_dict["description"] = description
        if experience_points is not UNSET:
            field_dict["experience_points"] = experience_points
        if featured is not UNSET:
            field_dict["featured"] = featured
        if healed is not UNSET:
            field_dict["healed"] = healed
        if hitpoints is not UNSET:
            field_dict["hitpoints"] = hitpoints
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if immune is not UNSET:
            field_dict["immune"] = immune
        if is_lootable is not UNSET:
            field_dict["is_lootable"] = is_lootable
        if loot_list is not UNSET:
            field_dict["loot_list"] = loot_list
        if name is not UNSET:
            field_dict["name"] = name
        if race is not UNSET:
            field_dict["race"] = race
        if see_invisible is not UNSET:
            field_dict["see_invisible"] = see_invisible
        if strong is not UNSET:
            field_dict["strong"] = strong
        if summoned_mana is not UNSET:
            field_dict["summoned_mana"] = summoned_mana
        if weakness is not UNSET:
            field_dict["weakness"] = weakness

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        be_convinced = d.pop("be_convinced", UNSET)

        be_paralysed = d.pop("be_paralysed", UNSET)

        be_summoned = d.pop("be_summoned", UNSET)

        behaviour = d.pop("behaviour", UNSET)

        convinced_mana = d.pop("convinced_mana", UNSET)

        description = d.pop("description", UNSET)

        experience_points = d.pop("experience_points", UNSET)

        featured = d.pop("featured", UNSET)

        healed = cast(List[str], d.pop("healed", UNSET))

        hitpoints = d.pop("hitpoints", UNSET)

        image_url = d.pop("image_url", UNSET)

        immune = cast(List[str], d.pop("immune", UNSET))

        is_lootable = d.pop("is_lootable", UNSET)

        loot_list = cast(List[str], d.pop("loot_list", UNSET))

        name = d.pop("name", UNSET)

        race = d.pop("race", UNSET)

        see_invisible = d.pop("see_invisible", UNSET)

        strong = cast(List[str], d.pop("strong", UNSET))

        summoned_mana = d.pop("summoned_mana", UNSET)

        weakness = cast(List[str], d.pop("weakness", UNSET))

        main_creature = cls(
            be_convinced=be_convinced,
            be_paralysed=be_paralysed,
            be_summoned=be_summoned,
            behaviour=behaviour,
            convinced_mana=convinced_mana,
            description=description,
            experience_points=experience_points,
            featured=featured,
            healed=healed,
            hitpoints=hitpoints,
            image_url=image_url,
            immune=immune,
            is_lootable=is_lootable,
            loot_list=loot_list,
            name=name,
            race=race,
            see_invisible=see_invisible,
            strong=strong,
            summoned_mana=summoned_mana,
            weakness=weakness,
        )

        main_creature.additional_properties = d
        return main_creature

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
