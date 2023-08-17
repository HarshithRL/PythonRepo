import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
def runner_up(l):
    l=[int(x) for x in l]
    score=list(set(l))
    score.sort()
    logging.info(score[-2])