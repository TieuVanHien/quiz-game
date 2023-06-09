class Tags:
    def __init__(self, tag):
        categories = ["Linux", "Bash", "PHP", "Docker", "HTML", "MySQL", "Wordpress", "Laravel", "Kubernetes", "JavaScript", "DevOps"]
        lowercase_tag = tag.lower()
        if lowercase_tag in [category.lower() for category in categories]:
            self.tag = lowercase_tag
        else:
            raise ValueError("Invalid tag. Please choose a tag from the specified categories.")
