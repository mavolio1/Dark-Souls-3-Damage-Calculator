class Weapon:
    def __init__(self, d):
        for k, v in d.items():
            setattr(self, k, v)

    def __repr__(self):
        pprint = ''
        pprint += f'+-------' + f'{self.name:40}'.replace(' ', '-') + '------------------+\n'
        pprint += f'|WEAPON TYPE                    :         ' + f'{self.weapon_type:20}'       + '   |\n'
        pprint += f'|ATTACK TYPE                    :         ' + f'{self.attack_type:20}'       + '   |\n'
        pprint += f'+----------------------------------------------------------------+\n'
        pprint += f'|PHYSICAL ATK                   :               ' + f'{str(self.phys_atk):3}'      + '              |\n'
        pprint += f'|MAGICAL ATK                    :               ' + f'{str(self.magic_atk):3}'     + '              |\n'
        pprint += f'|FIRE ATK                       :               ' + f'{str(self.fire_atk):3}'      + '              |\n'
        pprint += f'|LIGHTNING ATK                  :               ' + f'{str(self.lightning_atk):3}' + '              |\n'
        pprint += f'|DARK ATK                       :               ' + f'{str(self.dark_atk):3}'      + '              |\n'
        pprint += f'+----------------------------------------------------------------+\n'
        pprint += f'|STR SCALING                    :               ' + f'{self.str_scale}' + '                |\n'
        pprint += f'|DEX SCALING                    :               ' + f'{self.dex_scale}' + '                |\n'
        pprint += f'|INT SCALING                    :               ' + f'{self.int_scale}' + '                |\n'
        pprint += f'|FAITH SCALING                  :               ' + f'{self.faith_scale}' + '                |\n'
        pprint += f'+----------------------------------------------------------------+'

        return pprint