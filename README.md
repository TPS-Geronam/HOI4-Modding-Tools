# HOI4-Modding-Tools
### Duplicate loc key remover:
Comments out duplicate loc keys by first letting you select the `text.log` (auto-generated by hoi4, can be found inside `\Documents\Paradox Interactive\Hearts of Iron IV\logs`) and then the localisation folder. Notice that the program removes the first duplicate it can find and then moves on to the next key. In case of more than two duplicates than of the same key the program can be run again.

### python (2.7) scripts are inside `/res/python_scripts/`
- deleteprovinceidfrom.py : deletes given province ID's from a file
- replacestatetype.py : replaces state type of states inside a folder
- replacemanpower.py : replaces manpower of states inside a folder
- copyflagdummy.py : copies a dummy flag with given TAG's
- deletestate.py : deletes a state inside history/states with ID (optimized for MapGen, change syntax if in need)
- blankallfiles.py : blanks all files inside current directory
- religionscrapper.py : (only usable on eoanb) gets all religions of adjacent country history files into output txt
- removereligion.py : (only usable on eoanb) removes all religions from adjacent country history files