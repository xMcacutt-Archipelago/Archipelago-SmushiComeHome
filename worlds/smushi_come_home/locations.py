from __future__ import annotations
from enum import EnumType, Enum
from typing import TYPE_CHECKING, NamedTuple, Any
from BaseClasses import Location, Region
from BaseClasses import Location, Region, LocationProgressType

from worlds.smushi_come_home import *
from worlds.smushi_come_home.data import *


class SmushiLocation(Location):
    game: str = "Smushi Come Home"


class LocData:
    def __init__(self, code: int, region: str):
        """
        Represents a location with associated conditions.

        :param code: A unique identifier for the location.
        :param region: Name of the containing region.
        """
        self.code = code
        self.region = region


def create_location(player: int, reg: Region, name: str, code: int):
    location = SmushiLocation(player, name, code, reg)
    reg.locations.append(location)


def create_locations_from_dict(loc_dict, reg, player):
    for (key, data) in loc_dict.items():
        if data.region != reg.name:
            continue
        create_location(player, reg, key, data.code)


def create_locations(world: SmushiWorld, reg: Region):
    create_locations_from_dict(progress_locations, reg, world.player)
    create_locations_from_dict(mycology_locations, reg, world.player)
    create_locations_from_dict(augmenter_locations, reg, world.player)


progress_locations = {
    "Tools of the Explorer Found":  LocData(0x100, WINTER),
    "Tool of Mining Found":         LocData(0x101, WINTER),

    "Garden Map Found":             LocData(0x202, MYCENA_ENTRY),
    "Yellow Shrine Energy Spore":   LocData(0x203, MYCENA_ENTRY),
    "Pink Shrine Energy Spore":     LocData(0x205, BOLETE_BEACH),
    "Blue Shrine Energy Spore":     LocData(0x206, BOLETE_BEACH),
    "Blade of Power Purchase":      LocData(0x207, BOLETE_BEACH),
    "Anemone Woods Wind Essence":   LocData(0x208, ANEMONE_WOODS),
    "Mycology Journal Unlock":      LocData(0x209, MYCENA_ENTRY),
    "Band of Elasticity Found":     LocData(0x20A, ANEMONE_WOODS),
    "Myrtle Pools Wind Essence":    LocData(0x20B, MYRTLE_POOLS),
    "Myrtle Pools Blueberry":       LocData(0x20C, MYRTLE_POOLS),
    "Ancient Relic 1 Found":        LocData(0x20D, MYRTLE_POOLS),
    "Ancient Relic 2 Found":        LocData(0x20E, MYRTLE_POOLS),
    "Crystal Cave Blueberry":       LocData(0x20F, CRYSTAL_CAVES),

    "Forest Map Found":             LocData(0x300, WAXCAP_FALLS),
    "Sturdy Hooks Purchase":         LocData(0x301, WAXCAP_FALLS),
    "Nectar Collector":             LocData(0x302, WAXCAP_FALLS),
    "Explosive Powder 1 Found":     LocData(0x303, CRYPTIC_CAVERNS),
    "Explosive Powder 2 Found":     LocData(0x304, DARK_CAVE),
    "Secret Password Found":        LocData(0x305, MAPLE_SANCTUARY),
    "Super Essence Found":          LocData(0x306, MAPLE_SANCTUARY),
    "Firestarter Kit Found":        LocData(0x307, MAPLE_SANCTUARY),
    "Maple Sanctuary Energy Spore": LocData(0x308, MAPLE_SANCTUARY),
    "Cryptic Caverns Wind Essence": LocData(0x309, CRYPTIC_CAVERNS),
    "Brick Chimney Wind Essence":   LocData(0x30A, MAPLE_SANCTUARY),
    "Restless Stream Energy Spore": LocData(0x30B, RESTLESS_STREAM),
    "Container of Light Found":     LocData(0x30C, CRYPTIC_CAVERNS),
    "Headlamp Acquired":            LocData(0x30D, CRYPTIC_CAVERNS),
    "Dark Cave Energy Spore":       LocData(0x30E, DARK_CAVE),

    "Lake Map Found":               LocData(0x400, TWIN_BEACH),
    "Essence of Water Purchase":    LocData(0x401, DIVERS_LOCUS),
    "Old String Found":             LocData(0x402, CHUNGY_CAVE),
    "Chungy Saved":                 LocData(0x403, HIDDEN_LOTUS),
    "Sacred Orb Found":             LocData(0x404, SACRED_HOLM),
    "Indigo Island Energy Spore":   LocData(0x405, INDIGO_ISLAND),
    "Indigo Island Wind Essence":   LocData(0x406, INDIGO_ISLAND),
    "Secret Opener Found":          LocData(0x407, INDIGO_ISLAND),

    "Grove Map Found":              LocData(0x500, GROVE),
    "Screwdriver Found":            LocData(0x501, GROVE),
    "Band Aid Found":               LocData(0x502, GROVE),
    "Ring of Truth Found":          LocData(0x503, GROVE),
    "Ring of Youth Found":          LocData(0x504, GROVE),
    "Ring of Love Found":           LocData(0x505, GROVE),
    "Ring of Prosperity Found":     LocData(0x506, FIREFLIES),
    "Ring of Spirit Found":         LocData(0x507, BRILLIANT_BEACH),
    "Sacred Streamer 1 Obtained":   LocData(0x508, GROVE),
    "Sacred Streamer 2 Obtained":   LocData(0x509, TRANQUIL_GARDEN),
    "Sacred Streamer 3 Obtained":   LocData(0x50A, BRILLIANT_BEACH),
    "Sacred Streamer 4 Obtained":   LocData(0x50B, BRILLIANT_BEACH),

}

mycology_locations = {
    "Mycena Haematopus":          LocData(0x600, GARDEN),
    "Volvopluteus Gloiocephalus": LocData(0x601, GARDEN),
    "Hypholoma Capnoides":        LocData(0x602, GARDEN),
    "Macrolepiota Procera":       LocData(0x603, GARDEN),
    "Entoloma Hochstetteri":      LocData(0x604, GARDEN),
    "Chalciporus Piperatus":      LocData(0x605, GARDEN),
    "Coprinus Comatus":           LocData(0x606, WAXCAP_FALLS_WATER_CAVE),
    "Mycena Chlorophos":          LocData(0x607, DARK_CAVE),
    "Cantharellus Cibarius":      LocData(0x608, CRYPTIC_CAVERNS),
    "Hygrocybe flavescens":       LocData(0x609, FOREST),
    "Daedaleopsis Tricolor":      LocData(0x60A, CRYPTIC_CAVERNS),
    "Amanita Muscaria":           LocData(0x60B, FOREST),
    "Exsudoporus Frostii":        LocData(0x60C, MAPLE_SANCTUARY),
    "Clavaria Zollingeri":        LocData(0x60D, LAKE),
    "Hygrocybe Conica":           LocData(0x60E, SACRED_HOLM),
    "Lactarius Indigo":           LocData(0x60F, LAKE),
    "Psathyrella Aquatica":       LocData(0x610, LAKE),
    "Hygrocybe Miniata":          LocData(0x611, GROVE),
    "Coprinellus Disseminatus":   LocData(0x612, ELDERS_HOME),
    "Phallus Indusiatus":         LocData(0x613, GROVE),
    "Laccaria Amethystina":       LocData(0x614, GROVE),
    "Coprinellus Domesticus":     LocData(0x615, GROVE),
    "Heart of the Forest":        LocData(0x616, GROVE),
}


augmenter_locations = {
    "Purple Augmenter":        LocData(0x700, MYCENA_ENTRY),
    "Strawberry Augmenter":    LocData(0x701, ANEMONE_WOODS),
    "Flower Augmenter":        LocData(0x702, MYCENA_ENTRY),
    "Secret Augmenter":        LocData(0x703, ANCIENT_PASSAGE),
    "Verdant Augmenter":       LocData(0x704, MAPLE_SANCTUARY),
    "Pelagic Augmenter":       LocData(0x705, DARK_CAVE),
    "Honey Augmenter":         LocData(0x706, WAXCAP_FALLS),
    "Sparkle Augmenter":       LocData(0x707, WAXCAP_FALLS_WATER_CAVE),
    "Clavaria Augmenter":      LocData(0x708, DIVERS_LOCUS),
    "Ink Augmenter":           LocData(0x709, CHUNGY_CAVE),
    "Precious Augmenter":      LocData(0x70A, BRILLIANT_BEACH),
    "Rainbow Augmenter":       LocData(0x70B, BRILLIANT_BEACH),
    "Veiled Augmenter":        LocData(0x70C, TRANQUIL_GARDEN),
    "Sacred Augmenter":        LocData(0x70D, SACRED_TREE),
}


smushi_location_table = {
    **progress_locations,
    **mycology_locations,
    **augmenter_locations,
}
