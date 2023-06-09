class Tags:
    def __init__(self, tag):
        categories = ["Linux", "Bash", "PHP", "Docker", "HTML", "MySQL", "Wordpress", "Laravel", "Kubernetes", "JavaScript", "DevOps"]
        lowercase_categories = [category.lower() for category in categories]
        lowercase_tag = tag.lower()
        if lowercase_tag in lowercase_categories:
            self.tag = lowercase_tag
        else:
            raise ValueError("Invalid tag. Please choose a tag from the specified categories.")
