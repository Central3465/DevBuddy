from modules import getcommit

def getcommit():
    commit = getcommit.getcommit()
    assert len(commit) == 40