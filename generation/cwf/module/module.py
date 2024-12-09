from typing import List

from canvas import Color
from generation.cwf.ruleset.rule import WCFRule


class WCFModule:

    value: int
    content: Color

    rules: List[WCFRule] # List of rule for each neighbors


