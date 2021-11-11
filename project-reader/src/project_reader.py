from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        p = toml.loads(content)
        print()
        print(p)
        print()
        l = []
        l2 = []
        for item in p["tool"]["poetry"]["dependencies"]:
            l.append(item)
        for item in p["tool"]["poetry"]["dev-dependencies"]:
            l2.append(item)
        return Project(p["tool"]["poetry"]["name"], p["tool"]["poetry"]["description"], l,l2)
