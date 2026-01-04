import typing
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region, Location
from Utils import visualize_regions
from worlds.AutoWorld import WebWorld, World
from .items import SmushiItem, smushi_item_table, create_items, ItemData
from .locations import smushi_location_table, SmushiLocation
from .options import SmushiOptions, smushi_option_groups
from .regions import create_regions, connect_regions, connect_all_regions
from .rules import set_rules

class SmushiWeb(WebWorld):
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Smushi Come Home randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["xMcacutt", "Dashieswag92"]
    )

    tutorials = [setup_en]
    option_groups = smushi_option_groups

class SmushiWorld(World):
    """
    Play as a tiny lil' mushroom who's lost in the forest and can't find its way home.
    Explore unique areas freely at your own pace, chat with friendly inhabitants,
    and take on different adventures to get back home!
    """
    game = "Smushi Come Home"
    options_dataclass = SmushiOptions
    options: SmushiOptions
    topology_present = True
    item_name_to_id = {name: item.code for name, item in smushi_item_table.items()}
    location_name_to_id = {name: item.code for name, item in smushi_location_table.items()}

    web = SmushiWeb()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.itempool = []

    def fill_slot_data(self) -> id:
        from Utils import visualize_regions
        state = self.multiworld.get_all_state(False)
        state.update_reachable_regions(self.player)
        return {
            "ModVersion": "1.0.7",
            "Goal": self.options.goal.value,
            "LogicDifficulty": self.options.logic_difficulty.value
        }

    def generate_early(self) -> None:
        return

    def create_item(self, name: str) -> Item:
        item_info = smushi_item_table[name]
        return SmushiItem(name, item_info.classification, item_info.code, self.player)

    def create_items(self):
        create_items(self)

    def create_event(self, region_name: str, event_name: str, event_loc_name: str) -> None:
        region: Region = self.multiworld.get_region(region_name, self.player)
        loc: SmushiLocation = SmushiLocation(self.player, event_loc_name, None, region)
        loc.place_locked_item(SmushiItem(event_name, ItemClassification.progression, None, self.player))
        region.locations.append(loc)

    def create_regions(self):
        create_regions(self)
        connect_all_regions(self)

    def set_rules(self):
        set_rules(self)

    def extend_hint_information(self, hint_data: typing.Dict[int, typing.Dict[int, str]]):
        new_hint_data = {}

        for key, data in smushi_location_table.items():
            try:
                location: Location = self.multiworld.get_location(key, self.player)
            except KeyError:
                continue

            # new_hint_data[location.address] = f""

        hint_data[self.player] = new_hint_data

    # def generate_output(self, output_dir):
    #     visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml",
    #                       show_entrance_names=True,
    #                       regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
    #                           self.player])