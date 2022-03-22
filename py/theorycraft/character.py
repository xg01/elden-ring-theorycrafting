from dataclasses import dataclass

# Motivation for using dataclasses:
# https://stackoverflow.com/questions/49002/prefer-composition-over-inheritance 

@dataclass
class MainStats:
    vigor: int
    mind: int 
    endurance: int 
    strength: int 
    dexerity: int 
    intelligence:int 
    faith: int 
    arcane: int 

@dataclass 
class DefensiveStats:
    immunity: int 
    robustness: int 
    focus: int 
    vitality: int 
    physical_def: float
    strike_def: float 
    slash_def: float 
    pierce_def: float 
    magic_def: float 
    fire_def: float 
    lightning_def: float 
    holy_def: float

@dataclass
class OffensiveStats:
    physical_atk_dmg: int
    magic_atk_dmg: int 
    fire_atk_dmg: int 
    lightning_atk_dmg: int 
    holy_atk_dmg: int 
    critical_atk_dmg: int 
    sorcery_scaling: int 
    incant_scaling: int 

@dataclass
class GeneralStats:
    hp: int 
    fp: int 
    stamina: float
    equip_load: float
    poise: int
    discovery: int
    memory_slots: int 

class CombinatorialOptimization:
    """ A mixin to provide combinatoral optimization functionality. Intended to be used with the Character class. """

    def find_equipment(self, general_stats):
        """ Generates all combinations of equipment that provides the requested character stats threshold. """
        raise NotImplementedError

    def find_equipment_with_damage_reduction(self, dmg_reduction_percent):
        """ Generate all combinations of equipment that provide the requested damage reduction threshold. """
        raise NotImplementedError

    def find_equipment_with_defense(self, equipment_def_stats):
        """ Generate all combinations of equipment that provide the requested damage reduction threshold. """
        raise NotImplementedError

class Character(CombinatorialOptimization):
    def __init__(self, main_stats, defensive_stats, offensive_stats):
        self.__main_stats = main_stats
        self.__defenses = defensive_stats
        self.__offensive_stats = offensive_stats
        # self.__general_stats = __compute_general_stats() -- implementation pending

    def __compute_general_stats(self):
        """ Uses main stats, defensive stats, and offensive stats to determine general stats. """
        raise NotImplementedError

    # Note: Data need to be obtained from testing combinations in-game.  
    # Mathematical analysis can be applied to this data to reasonably approximate damage formulas.
    def compute_attack_rating(self):
        """ Implementation is pending on discovery of defense formulas. Additional empirical testing is required. """
        raise NotImplementedError

    def compute_damage_reduction(self, incoming_dmg): 
        """ Implementation is pending on discovery of defense formulas. Additional empirical testing is required. """
        raise NotImplementedError
