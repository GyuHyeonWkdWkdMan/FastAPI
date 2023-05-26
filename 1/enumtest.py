from enum import Enum

class Skill(Enum):
    HTML = 1
    CSS = 2
    JS = 3

print(type(Skill.HTML))
print({Skill.HTML})
print(Skill.CSS.value)