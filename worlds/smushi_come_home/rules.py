from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.smushi_come_home import SmushiWorld

from BaseClasses import CollectionState
from worlds.smushi_come_home.data import *


def can_mine(world, state: CollectionState):
    return state.has("Tool of Mining", world.player)

def can_hm01(world, state: CollectionState):
    return state.has("Blade of Power", world.player)

def is_shroom_nerd(world, state: CollectionState):
    return state.has("Mycology Journal", world.player)

def can_burn(world, state: CollectionState):
    return state.has("Firestarter Kit", world.player)

def is_pitch_black_baby(world, state: CollectionState):
    return state.has("Headlamp", world.player)

def can_screw_glass(world, state: CollectionState):
    return state.has("Screwdriver", world.player)

def can_go_water(world, state: CollectionState):
    return state.has("Essence of Water", world.player)

def can_hail_magic_conch(world, state: CollectionState):
    return state.has("Conch Shell", world.player)

def can_fly(world, state: CollectionState):
    return state.has("Leaf Glider", world.player)

def has_climb_level(world, state: CollectionState, level):
    return state.has("Progressive Hooks", world.player, level)

def is_literate(world, state: CollectionState):
    return state.has("Tool of Writing", world.player)

def is_stretchy(world, state: CollectionState):
    return state.has("Band of Elasticity", world.player)

def is_rich(world, state: CollectionState):
    return state.has("Ancient Relic", world.player, 2)

def is_thicc(world, state: CollectionState):
    return state.has("Blueberry", world.player, 2)

def is_member(world, state: CollectionState):
    return state.has("Secret Password", world.player)

def can_boom(world, state: CollectionState):
    return state.has("Explosive Powder", world.player, 2) and can_burn(world, state)

def can_has_lamp(world, state: CollectionState):
    return state.has("Container of Light", world.player)

def has_a_secret(world, state: CollectionState):
    return state.has("Secret Opener", world.player)

def can_save_chungus(world, state: CollectionState):
    return state.has("Old String", world.player)

def can_glue(world, state: CollectionState):
    return state.has("Band Aid", world.player)

def has_basics(world, state: CollectionState):
    return state.has("Progressive Hooks", world.player, 1) and state.has("Leaf Glider", world.player)

def has_tools(world, state: CollectionState):
    return state.has("Progressive Hooks", world.player, 1) and (state.has("Leaf Glider", world.player)
    and state.has("Tool of Mining", world.player))

def is_uncle_iroh(world, state: CollectionState):
    return state.has("Lotus Flower", world.player, 5)

def get_advanced_rules(world):
    rules = {
        "locations": {
        },
        "entrances": {
        }
    }
    return rules

def get_standard_rules(world):
    rules = {
        "locations": {
            "Tools of the Explorer Found":
                lambda state: can_mine(world, state),

            "Tool of Mining Found":
                lambda state: has_tools(world, state),

            "Purple Augmenter":
                lambda state: state.can_reach_location("Orange Shrine Completed", world.player),

            "Pink Shrine Energy Spore":
                lambda state: state.can_reach_location("Pink Shrine Completed", world.player),

            "Blue Shrine Energy Spore":
                lambda state: state.can_reach_location("Blue Shrine Completed", world.player),

            "Flower Augmenter":
                lambda state: state.has("Flower Shrine Completed", world.player, 4),

            "Secret Augmenter":
                lambda state: has_a_secret(world, state),

            "Blade of Power Purchase":
                lambda state: can_mine(world, state),

            "Anemone Woods Wind Essence":
                lambda state: can_fly(world, state),

            "Strawberry Augmenter":
                lambda state: can_fly(world, state) and is_stretchy(world, state),

            "Mycology Journal Unlock":
                lambda state: is_literate(world, state),

            "Myrtle Pools Wind Essence":
                lambda state: can_fly(world, state),

            "Ancient Relic 1 Found":
                lambda state: has_tools(world, state),

            "Ancient Relic 2 Found":
                lambda state: has_tools(world, state),

            "Myrtle Pools Blueberry Purchase":
                lambda state: can_mine(world, state),

            "Crystal Cave Blueberry Found":
                lambda state: has_basics(world, state),

            "Sturdy Hooks Purchase":
                lambda state: can_mine(world, state),

            "Explosive Powder 1 Found":
                lambda state: is_member(world, state),

            "Super Essence Found":
                lambda state: can_fly(world, state),

            "Firestarter Kit Purchase":
                lambda state: can_mine(world, state),

            "Maple Sanctuary Energy Spore":
                lambda state: can_burn(world, state),

            "Cryptic Caverns Wind Essence":
                lambda state: has_basics(world, state),

            "Brick Chimney Wind Essence":
                lambda state: can_hm01(world, state) and can_fly(world, state),

            "Restless Stream Energy Spore":
                lambda state: can_hm01(world, state) and has_climb_level(world, state, 1),

            "Container of Light Found":
                lambda state: has_climb_level(world, state, 2) and can_fly(world, state),

            "Headlamp Acquired":
                lambda state: can_has_lamp(world, state),

            "Dark Cave Energy Spore":
                lambda state: can_burn(world, state),

            "Pelagic Augmenter":
                lambda state: can_burn(world, state) and can_hm01(world, state),

            "Mycena Chlorophos":
                lambda state: can_hm01(world, state) and is_shroom_nerd(world, state),

            "Essence of Water Purchase":
                lambda state: can_mine(world, state),

            "Psathyrella Aquatica":
                lambda state: can_go_water(world, state) and is_shroom_nerd(world, state),

            "Clavaria Augmenter":
                lambda state: can_go_water(world, state),

            "Ink Augmenter":
                lambda state: can_hm01(world, state),

            "Old String Found":
                lambda state: can_go_water(world, state) and can_burn(world, state),

            "Chungy Saved":
                lambda state: can_burn(world, state) and can_save_chungus(world, state),

            "Indigo Island Energy Spore":
                lambda state: can_mine(world, state),

            "Indigo Island Wind Essence":
                lambda state: can_mine(world, state),

            "Secret Opener Found":
                lambda state: can_fly(world, state) and can_burn(world, state)
                              and has_climb_level(world, state, 2),

            "Screwdriver Purchase":
                lambda state: can_mine(world, state) and has_climb_level(1),

            "Ring of Truth Found":
                lambda state: can_fly(world, state) and can_hm01(world, state) and has_climb_level(world, state, 1) and can_fly(world, state),

            "Ring of Love Found":
                lambda state: can_fly(world, state) and has_climb_level(world, state, 2)
                              and can_screw_glass(world, state),

            "Sacred Streamer 1 Obtained":
                lambda state: has_climb_level(world, state, 2) and can_mine(world, state),

            "Sacred Streamer 2 Obtained":
                lambda state: can_hm01(world, state) and can_glue(world, state),

            "Band Aid Found":
                lambda state: can_fly(world, state) and has_climb_level(world, state, 2) and can_hm01(world, state),

            "Ring of Youth Found":
                lambda state: can_hm01(world, state),

            "Veiled Augmenter":
                lambda state: can_fly(world, state) and has_climb_level(world, state, 2) and can_hm01(world, state),

            "Ring of Spirit Found":
                lambda state: can_burn(world, state) and can_go_water(world, state),

            "Sacred Streamer 3 Obtained":
                lambda state: state.has("Ring Returned", world.player, 1)
                              and can_fly(world, state) and can_burn(world, state) and can_go_water(world, state)
                              and has_climb_level(world, state, 2),

            "Sparkle Augmenter":
                lambda state: has_climb_level(world, state, 2) and can_fly(world, state) and state.has("Energy Spore", world.player, 2),

            "Mycena Haematopus":
                lambda state: is_shroom_nerd(world, state),

            "Volvopluteus Gloiocephalus":
                lambda state: is_shroom_nerd(world, state),

            "Hypholoma Capnoides":
                lambda state: is_shroom_nerd(world, state),

            "Macrolepiota Procera":
                lambda state: is_shroom_nerd(world, state) and can_fly(world, state),

            "Entoloma Hochstetteri":
                lambda state: is_shroom_nerd(world, state),

            "Chalciporus Piperatus":
                lambda state: is_shroom_nerd(world, state),

            "Coprinus Comatus":
                lambda state: is_shroom_nerd(world, state),

            "Cantharellus Cibarius":
                lambda state: is_shroom_nerd(world, state),

            "Hygrocybe Flavescens":
                lambda state: is_shroom_nerd(world, state),

            "Daedaleopsis Tricolor":
                lambda state: is_shroom_nerd(world, state),

            "Amanita Muscaria":
                lambda state: is_shroom_nerd(world, state),

            "Exsudoporus Frostii":
                lambda state: is_shroom_nerd(world, state),

            "Clavaria Zollingeri":
                lambda state: is_shroom_nerd(world, state),

            "Hygrocybe Conica":
                lambda state: is_shroom_nerd(world, state),

            "Lactarius Indigo":
                lambda state: is_shroom_nerd(world, state),

            "Hygrocybe Miniata":
                lambda state: is_shroom_nerd(world, state),

            "Coprinellus Disseminatus":
                lambda state: is_shroom_nerd(world, state),

            "Phallus Indusiatus":
                lambda state: is_shroom_nerd(world, state),

            "Laccaria Amethystina":
                lambda state: is_shroom_nerd(world, state),

            "Coprinellus Domesticus":
                lambda state: is_shroom_nerd(world, state),

            "Heart of the Forest":
                lambda state: is_shroom_nerd(world, state),

            "Sacred Streamer 4 Obtained":
                lambda state: state.has("Ring Returned", world.player, 3),

            "Rainbow Augmenter":
                lambda state: can_fly(world, state) and has_climb_level(world, state, 2),

            "Sharp Augmenter":
                lambda state: can_fly(world, state) and has_climb_level(world, state, 2)
                              and can_burn(world, state) and can_screw_glass(world, state),

            "Precious Augmenter":
                lambda state: state.has("Ring Returned", world.player, 5),

            "Sacred Augmenter":
                lambda state: state.has("Sacred Streamer", world.player, 4),


        },
        "entrances": {
            f"{GARDEN} -> {CRYSTAL_CAVES}":
                lambda state: can_hm01(world, state),
            f"{ANCIENT_PASSAGE} -> {FOREST}":
                lambda state: is_thicc(world, state),
            f"{WAXCAP_FALLS} -> {MAPLE_SANCTUARY}":
                lambda state: has_climb_level(world, state, 2),
            f"{RESTLESS_STREAM} -> {CRYPTIC_CAVERNS}":
                lambda state: can_fly(world, state) or has_climb_level(world, state, 1),
            f"{CRYPTIC_CAVERNS} -> {DARK_CAVE}":
                lambda state: is_pitch_black_baby(world, state) and has_basics(world, state),
            f"{WAXCAP_FALLS} -> {WAXCAP_FALLS_WATER_CAVE}":
                lambda state: can_go_water(world, state),
            f"{RESTLESS_STREAM} -> {LAKE}":
                lambda state: can_boom(world, state),
            f"{LAKE} -> {ELDERS_HOME}":
                lambda state: is_uncle_iroh(world, state),
            f"{HIDDEN_LOTUS} -> {CHUNGY_CAVE}":
                lambda state: can_go_water(world, state) and can_fly(world, state) and is_pitch_black_baby(world, state)
                              and has_climb_level(world, state, 2),
            f"{LAKE} -> {SACRED_HOLM}":
                lambda state: has_climb_level(world, state, 2) and can_fly(world, state) and can_mine(world, state),
            f"{ELDERS_HOME} -> {GROVE}":
                lambda state: can_go_water(world, state) and can_fly(world, state) and can_screw_glass(world, state)
                              and has_climb_level(world, state, 2),
            f"{GROVE} -> {TRANQUIL_GARDEN}":
                lambda state: can_burn(world, state),
            f"{BRILLIANT_BEACH} -> {FIREFLIES}":
                lambda state: can_fly(world, state) and state.has("Ring Returned", world.player, 1),
            f"{LAKE} -> {SMUSHI_HOME}":
                lambda state: state.has("Lake Capybara Reunited", world.player, 2),
        }
    }
    return rules



def set_rules(world):
    from . import SmushiWorld
    world: SmushiWorld
    rules_lookup = get_standard_rules(world) if world.options.logic_difficulty.value == 0 else get_advanced_rules(world)

    world.create_event(MYCENA_ENTRY, "Flower Shrine Completed", "Yellow Shrine Completed")
    world.create_event(BOLETE_BEACH, "Flower Shrine Completed", "Blue Shrine Completed")
    world.get_location("Blue Shrine Completed").access_rule = \
        lambda state: has_climb_level(world, state, 1) or can_fly(world, state)
    world.create_event(BOLETE_BEACH, "Flower Shrine Completed", "Pink Shrine Completed")
    world.get_location("Pink Shrine Completed").access_rule = \
        lambda state: has_climb_level(world, state, 1) and can_hm01(world, state)
    world.create_event(MYCENA_ENTRY, "Flower Shrine Completed", "Orange Shrine Completed")
    world.get_location("Orange Shrine Completed").access_rule = \
        lambda state: has_climb_level(world, state, 1) and can_hm01(world, state)

    world.create_event(SACRED_HOLM, "Lake Capybara Reunited", "Sister Capybara Helped")
    world.get_location("Sister Capybara Helped").access_rule = \
        lambda state: can_burn(world, state) and can_hm01(world, state)
    world.create_event(HIDDEN_LOTUS, "Lake Capybara Reunited", "Brother Capybara Helped")
    world.get_location("Brother Capybara Helped").access_rule = \
        lambda state: state.can_reach_location("Chungy Saved", world.player)

    world.create_event(BRILLIANT_BEACH, "Ring Returned", "Ring of Truth Returned")
    world.get_location("Ring of Truth Returned").access_rule = lambda state: state.has("Ring of Truth", world.player)
    world.create_event(BRILLIANT_BEACH, "Ring Returned", "Ring of Youth Returned")
    world.get_location("Ring of Youth Returned").access_rule = lambda state: state.has("Ring of Youth", world.player)
    world.create_event(BRILLIANT_BEACH, "Ring Returned", "Ring of Love Returned")
    world.get_location("Ring of Youth Returned").access_rule = lambda state: state.has("Ring of Love", world.player)
    world.create_event(BRILLIANT_BEACH, "Ring Returned", "Ring of Prosperity Returned")
    world.get_location("Ring of Youth Returned").access_rule = lambda state: state.has("Ring of Prosperity", world.player)
    world.create_event(BRILLIANT_BEACH, "Ring Returned", "Ring of Spirit Returned")
    world.get_location("Ring of Youth Returned").access_rule = lambda state: state.has("Ring of Spirit", world.player)

    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError:
            print(f"Invalid Entrance specified in rules dictionary: {entrance_name}")
            pass
    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError:
            print(f"Invalid Location specified in rules dictionary: {location_name}")
            pass

    if world.options.goal.value == 0:
        world.create_event(SMUSHI_HOME, "Victory", "Victory")
    if world.options.goal.value == 1:
        world.create_event(SACRED_TREE, "Victory", "Victory")
        world.get_location("Victory").access_rule = lambda state: state.has("Sacred Streamer", world.player, 4)
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
