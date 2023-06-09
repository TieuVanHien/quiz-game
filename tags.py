class Tags:
    def __init__(self, tag):
        categories = ["Linux", "Bash", "PHP", "Docker", "HTML", "MySQL", "Wordpress", "Laravel", "Kubernetes", "JavScript", "DevOps"]
        if tag in categories:
            self.tag = tag
        else:
            raise ValueError("Invalid tag. Please choose a tag from the specified categories.")