from dataclasses import dataclass


@dataclass
class ScrapedFileDTO:
    def __init__(self, name, complexity, issue_count, issue_map):
        self.name = name
        self.complexity = complexity
        self.issue_count = issue_count
        self.issue_map = issue_map

    def __str__(self):
        ans = (
            f"" + self.name + "\ncomplexity: " + str(self.complexity) + ", issue_count: " + str(self.issue_count) + "\n"
        )
        for key in self.issue_map:
            ans += str(self.issue_map[key]) + " : " + key + "\n"
        return ans
