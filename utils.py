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
        print(f'+-------' + f'{self.name:40}'.replace(' ', '-') + '-------+')
        print(f'|PHYSICAL ATK                   :       ' + f'{str(self.phys_atk):3}'      + '            |')
        print(f'|MAGICAL ATK                    :       ' + f'{str(self.magic_atk):3}'     + '            |')
        print(f'|FIRE ATK                       :       ' + f'{str(self.fire_atk):3}'      + '            |')
        print(f'|LIGHTNING ATK                  :       ' + f'{str(self.lightning_atk):3}' + '            |')
        print(f'|DARK ATK                       :       ' + f'{str(self.dark_atk):3}'      + '            |')
        print(f'+------------------------------------------------------+')
        return ''