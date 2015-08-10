# pyinfra
# File: pyinfra/facts/git.py
# Desc: local git repo facts

from pyinfra.api.facts import FactBase


class GitBranch(FactBase):
    def command(self, name):
        return 'git -C {0} rev-parse --abbrev-ref HEAD'.format(name)
