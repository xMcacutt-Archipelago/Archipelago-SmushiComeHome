from __future__ import annotations
from worlds.smushi_come_home import *
from BaseClasses import MultiWorld, Region, Entrance
from typing import List, Dict

from worlds.smushi_come_home.locations import create_locations
from worlds.smushi_come_home.data import *


class Ty1Region(Region):
    subregions: List[Region] = []


def connect_regions(world: SmushiWorld, from_name: str, to_name: str, entrance_name: str) -> Entrance:
    entrance_region = world.multiworld.get_region(from_name, world.player)
    exit_region = world.multiworld.get_region(to_name, world.player)
    return entrance_region.connect(exit_region, entrance_name)


def create_region(world: SmushiWorld, name: str):
    reg = Region(name, world.player, world.multiworld)
    create_locations(world, reg)
    world.multiworld.regions.append(reg)


def create_regions(world: SmushiWorld):
    create_region(world, "Menu")
    create_region(world, SMUSHI_HOME)
    create_region(world, WINTER)

    # Garden of Spring
    create_region(world, GARDEN)
    create_region(world, CRYSTAL_CAVES)
    create_region(world, MYCENA_ENTRY)
    create_region(world, ANCIENT_PASSAGE) # -> FALL
    create_region(world, MYRTLE_POOLS)
    create_region(world, ANEMONE_WOODS)
    create_region(world, BOLETE_BEACH)

    # Forest of Fall
    create_region(world, FOREST)
    create_region(world, WAXCAP_FALLS)
    create_region(world, WAXCAP_FALLS_WATER_CAVE)
    create_region(world, RESTLESS_STREAM) # -> LAKE
    create_region(world, MAPLE_SANCTUARY)
    create_region(world, CRYPTIC_CAVERNS)
    create_region(world, DARK_CAVE)

    # Lake of Bloom
    create_region(world, LAKE) # -> HOME or GROVE
    create_region(world, TWIN_BEACH)
    create_region(world, HIDDEN_LOTUS)
    create_region(world, CHUNGY_CAVE)
    create_region(world, DIVERS_LOCUS)
    create_region(world, INDIGO_ISLAND)
    create_region(world, SACRED_HOLM)

    #Grove of Life
    create_region(world, GROVE)
    create_region(world, ELDERS_HOME)
    create_region(world, TRANQUIL_GARDEN)
    create_region(world, SACRED_TREE)
    create_region(world, LIMINAL_WOODS)
    create_region(world, BRILLIANT_BEACH)
    create_region(world, FIREFLIES)


def connect_all_regions(world: SmushiWorld):
    connect_regions(world, "Menu", GARDEN, f"Menu -> {GARDEN}")
    connect_regions(world, GARDEN, WINTER, f"{GARDEN} -> {WINTER}")
    connect_regions(world, GARDEN, CRYSTAL_CAVES, f"{GARDEN} -> {CRYSTAL_CAVES}")
    connect_regions(world, GARDEN, MYCENA_ENTRY, f"{GARDEN} -> {MYCENA_ENTRY}")
    connect_regions(world, GARDEN, ANCIENT_PASSAGE, f"{GARDEN} -> {ANCIENT_PASSAGE}")
    connect_regions(world, GARDEN, MYRTLE_POOLS, f"{GARDEN} -> {MYRTLE_POOLS}")
    connect_regions(world, GARDEN, ANEMONE_WOODS, f"{GARDEN} -> {ANEMONE_WOODS}")
    connect_regions(world, GARDEN, BOLETE_BEACH, f"{GARDEN} -> {BOLETE_BEACH}")
    connect_regions(world, ANCIENT_PASSAGE, FOREST, f"{ANCIENT_PASSAGE} -> {FOREST}")
    connect_regions(world, FOREST, WAXCAP_FALLS, f"{FOREST} -> {WAXCAP_FALLS}")
    connect_regions(world, WAXCAP_FALLS, WAXCAP_FALLS_WATER_CAVE, f"{WAXCAP_FALLS} -> {WAXCAP_FALLS_WATER_CAVE}")
    connect_regions(world, FOREST, RESTLESS_STREAM, f"{FOREST} -> {RESTLESS_STREAM}")
    connect_regions(world, WAXCAP_FALLS, MAPLE_SANCTUARY, f"{WAXCAP_FALLS} -> {MAPLE_SANCTUARY}")
    connect_regions(world, RESTLESS_STREAM, CRYPTIC_CAVERNS, f"{RESTLESS_STREAM} -> {CRYPTIC_CAVERNS}")
    connect_regions(world, CRYPTIC_CAVERNS, DARK_CAVE, f"{CRYPTIC_CAVERNS} -> {DARK_CAVE}")
    connect_regions(world, RESTLESS_STREAM, LAKE, f"{RESTLESS_STREAM} -> {LAKE}")
    connect_regions(world, LAKE, TWIN_BEACH, f"{LAKE} -> {TWIN_BEACH}")
    connect_regions(world, LAKE, HIDDEN_LOTUS, f"{LAKE} -> {HIDDEN_LOTUS}")
    connect_regions(world, HIDDEN_LOTUS, CHUNGY_CAVE, f"{HIDDEN_LOTUS} -> {CHUNGY_CAVE}")
    connect_regions(world, LAKE, DIVERS_LOCUS, f"{LAKE} -> {DIVERS_LOCUS}")
    connect_regions(world, LAKE, INDIGO_ISLAND, f"{LAKE} -> {INDIGO_ISLAND}")
    connect_regions(world, LAKE, SACRED_HOLM, f"{LAKE} -> {SACRED_HOLM}")
    connect_regions(world, LAKE, SMUSHI_HOME, f"{LAKE} -> {SMUSHI_HOME}")
    connect_regions(world, LAKE, ELDERS_HOME, f"{LAKE} -> {ELDERS_HOME}")
    connect_regions(world, ELDERS_HOME, GROVE, f"{ELDERS_HOME} -> {GROVE}")
    connect_regions(world, GROVE, TRANQUIL_GARDEN, f"{GROVE} -> {TRANQUIL_GARDEN}")
    connect_regions(world, GROVE, SACRED_TREE, f"{GROVE} -> {SACRED_TREE}")
    connect_regions(world, GROVE, LIMINAL_WOODS, f"{GROVE} -> {LIMINAL_WOODS}")
    connect_regions(world, GROVE, BRILLIANT_BEACH, f"{GROVE} -> {BRILLIANT_BEACH}")
    connect_regions(world, BRILLIANT_BEACH, FIREFLIES, f"{BRILLIANT_BEACH} -> {FIREFLIES}")


