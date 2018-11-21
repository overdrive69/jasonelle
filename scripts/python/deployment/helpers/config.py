# coding: utf-8

directories = ["celljs", "website", "stjs", "jasonette", "scripts", "docs"]
files = [".gitignore", ".travis.yml", "README.md", "LICENSE"]

cascades = {
    "website" :  "scripts/deployment/cascades/website.py",
    "docs" : "scripts/deployment/cascades/docs.py"
}