import re

class TagManipulator():    
    def parse_string(self, tags, regex=","):
        result = []

        tempResult = re.split( regex, tags )
        for item in tempResult:
            if len(item.strip())>0:
                result.append(item.strip())

        return result