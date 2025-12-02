from dataclasses import dataclass

from Options import Choice, Range, Toggle, OptionGroup, PerGameCommonOptions


class Goal(Choice):
    """
    Determines the goal of the seed

    Home: Complete base game and help Smushi return home

    Grove: Complete DLC and restore the Heart of the Forest
    """
    display_name = "Goal"
    option_home = 0
    option_grove = 1
    default = 0


class LogicDifficulty(Choice):
    """
    Standard: (RECOMMENDED) Basic logic, no sequence breaks needed

    Advanced: Uses out of bounds glitches
    """
    display_name = "Logic Difficulty"
    option_standard = 0
    option_advanced = 1
    default = 0


smushi_option_groups = [
    OptionGroup("Goal Options", [
        Goal,
    ]),
    OptionGroup("Logic Options", [
        LogicDifficulty
    ]),
]


@dataclass
class SmushiOptions(PerGameCommonOptions):
    goal: Goal
    logic_difficulty: LogicDifficulty
