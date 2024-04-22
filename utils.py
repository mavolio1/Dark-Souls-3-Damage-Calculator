class Weapon:
    def __init__(self, name, weapon_type, attack_type, phys_atk,
                  magic_atk, fire_atk, ligthning_atk, dark_atk,
                  str_scale, dex_scale, int_scale, faith_scale):
        self.name = name
        self.weapon_type = weapon_type
        self.attack_type = attack_type
        self.phys_atk = phys_atk
        self.magic_atk = magic_atk
        self.fire_atk = fire_atk
        self.lightning_atk = ligthning_atk
        self.dark_atk = dark_atk
        self.str_scale = str_scale
        self.dex_scale = dex_scale
        self.int_scale = int_scale
        self.faith_scale = faith_scale

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