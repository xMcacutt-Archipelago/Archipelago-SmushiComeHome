from __future__ import annotations
from typing import Dict, Optional, TYPE_CHECKING
from worlds.smushi_come_home import *
from typing import Dict, Optional
from BaseClasses import Item, ItemClassification, MultiWorld, Location
from worlds.smushi_come_home.options import SmushiOptions


class SmushiItem(Item):
    game: str = "Smushi Come Home"


def get_random_item_names(rand, k: int, weights: dict[str, int]) -> str:
    random_items = rand.choices(
        list(weights.keys()),
        weights=list(weights.values()),
        k=k)
    return random_items


def create_single(name: str, world: SmushiWorld, item_class: ItemClassification = None) -> None:
    classification = smushi_item_table[name].classification if item_class is None else item_class
    world.itempool.append(SmushiItem(name, classification, smushi_item_table[name].code, world.player))


def create_multiple(name: str, amount: int, world: SmushiWorld, item_class: ItemClassification = None):
    for i in range(amount):
        create_single(name, world, item_class)


def create_items(world: SmushiWorld):
    total_location_count: int = len(world.multiworld.get_unfilled_locations(world.player))

    # Generic
    create_multiple("Energy Spore", 7, world)
    create_multiple("Wind Essence", 5, world)
    create_single("Leaf Glider", world)
    create_multiple("Progressive Hooks", 2, world)
    create_single("Tool of Mining", world)
    create_single("Tool of Writing", world)
    create_single("Band of Elasticity", world)
    create_single("Blade of Power", world)
    create_multiple("Ancient Relic", 2, world)
    create_multiple("Blueberry", 2, world)
    create_single("Mycology Journal", world)
    create_single("Firestarter Kit", world)
    create_single("Secret Password", world)
    create_multiple("Explosive Powder", 2, world)
    create_single("Container of Light", world)
    create_single("Headlamp", world)
    create_single("Essence of Water", world)
    create_single("Sacred Orb", world)
    create_single("Secret Opener", world)
    create_single("Old String", world)
    create_single("Screwdriver", world)
    create_single("Band Aid", world)
    create_single("Ring of Love", world)
    create_single("Ring of Youth", world)
    create_single("Ring of Truth", world)
    create_single("Ring of Prosperity", world)
    create_single("Ring of Spirit", world)
    create_single("Conch Shell", world)
    create_multiple("Sacred Streamer", 4, world)
    create_single("Super Spore", world)
    create_single("Super Essence", world)
    create_multiple("Lotus Flower", 5, world)

    # Junk
    remaining_locations: int = total_location_count - len(world.itempool)
    # trap_count: int = round(remaining_locations * options.trap_fill_percentage / 100)
    junk_count: int = remaining_locations # - trap_count
    junk = get_random_item_names(world.random, junk_count, junk_weights)
    for name in junk:
        create_single(name, world)
    # traps = get_random_item_names(world.random, trap_count, trap_weights)
    # for name in traps:
        # create_single(name, world)
    world.multiworld.itempool += world.itempool


class ItemData:
    def __init__(self, code: Optional[int], classification: Optional[ItemClassification]):
        self.code = code
        self.classification = classification


smushi_item_table: Dict[str, ItemData] = {
    "Energy Spore":           ItemData(0x1, ItemClassification.progression),
    "Wind Essence":           ItemData(0x2, ItemClassification.progression),
    "Leaf Glider":            ItemData(0x3, ItemClassification.progression),
    "Progressive Hooks":      ItemData(0x4, ItemClassification.progression),
    "Tool of Mining":         ItemData(0x5, ItemClassification.progression),
    "Tool of Writing":        ItemData(0x6, ItemClassification.progression),
    "Band of Elasticity":     ItemData(0x7, ItemClassification.progression),
    "Blade of Power":         ItemData(0x8, ItemClassification.progression),
    "Ancient Relic":          ItemData(0x9, ItemClassification.progression),
    "Blueberry":              ItemData(0xA, ItemClassification.progression),
    "Mycology Journal":       ItemData(0xB, ItemClassification.progression),
    "Firestarter Kit":        ItemData(0xC, ItemClassification.progression),
    "Secret Password":        ItemData(0xD, ItemClassification.progression),
    "Explosive Powder":       ItemData(0xE, ItemClassification.progression),
    "Container of Light":     ItemData(0xF, ItemClassification.progression),
    "Headlamp":               ItemData(0x10, ItemClassification.progression),
    "Essence of Water":       ItemData(0x11, ItemClassification.progression),
    "Sacred Orb":             ItemData(0x12, ItemClassification.progression),
    "Secret Opener":          ItemData(0x13, ItemClassification.progression),
    "Old String":             ItemData(0x14, ItemClassification.progression),
    "Screwdriver":            ItemData(0x15, ItemClassification.progression),
    "Band Aid":               ItemData(0x16, ItemClassification.progression),
    "Ring of Love":           ItemData(0x17, ItemClassification.progression),
    "Ring of Youth":          ItemData(0x18, ItemClassification.progression),
    "Ring of Truth":          ItemData(0x19, ItemClassification.progression),
    "Ring of Prosperity":     ItemData(0x1A, ItemClassification.progression),
    "Ring of Spirit":         ItemData(0x1B, ItemClassification.progression),
    "Conch Shell":            ItemData(0x1C, ItemClassification.progression),
    "Sacred Streamer":        ItemData(0x1D, ItemClassification.progression),
    "Super Spore":            ItemData(0x1E, ItemClassification.useful),
    "Super Essence":          ItemData(0x1F, ItemClassification.useful),
    "Lotus Flower":           ItemData(0x20, ItemClassification.progression),

    "Classic Shroomie":       ItemData(0x100, ItemClassification.filler),
    "Amethyst Shroomie":      ItemData(0x100, ItemClassification.filler),
    "Strawberry Shroomie":    ItemData(0x100, ItemClassification.filler),
    "Flower Shroomie":        ItemData(0x100, ItemClassification.filler),
    "SHO Bowl":               ItemData(0x100, ItemClassification.filler),
    "Verdant Shroomie":       ItemData(0x100, ItemClassification.filler),
    "Pelagic Shroomie":       ItemData(0x100, ItemClassification.filler),
    "Honey Shroomie":         ItemData(0x100, ItemClassification.filler),
    "Sparkle Shroomie":       ItemData(0x100, ItemClassification.filler),
    "Clavaria Shroomie":      ItemData(0x100, ItemClassification.filler),
    "Inkcap Shroomie":        ItemData(0x100, ItemClassification.filler),
    "Sharp Shroomie":         ItemData(0x10B, ItemClassification.filler),
    "Precious Shroomie":      ItemData(0x10C, ItemClassification.filler),
    "Rainbow Shroomie":       ItemData(0x10D, ItemClassification.filler),
    "Veiled Shroomie":        ItemData(0x10E, ItemClassification.filler),
    "Sacred Shroomie":        ItemData(0x10F, ItemClassification.filler),

    "Purple Crystal":         ItemData(0x200, ItemClassification.filler)
}



junk_weights = {
    "Purple Crystal": 1
}


trap_weights = {
}