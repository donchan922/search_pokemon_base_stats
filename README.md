# search_pokemon_base_stats
This is a command line tool to search base stats of POKEMON.

## Requirements
- Python 2.x

## Usage
Clone software:
```bash
$ cd
$ git clone https://github.com/donchan922/search_pokemon_base_stats.git
```

Execute following command:
```bash
$ python ~/search_pokemon_base_stats/source/search_base_stats.py POKEMON_NAME
```

For Example:
```bash
$ python ~/search_pokemon_base_stats/source/search_base_stats.py ピカチュウ

No.,ポケモン名,HP,攻撃,防御,特攻,特防,素早,合計
025,ピカチュウ,35,55,40,50,50,90,320
```

```bash
$ python ~/search_pokemon_base_stats/source/search_base_stats.py メガルカリオ ジャローダ

No.,ポケモン名,HP,攻撃,防御,特攻,特防,素早,合計
497,ジャローダ,75,75,95,75,95,113,528
448,メガルカリオ,70,145,88,140,70,112,625
```

## License
This software is released under the MIT License, see LICENSE.
