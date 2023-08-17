import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
def avg_marks(d,Student):
    for i,y in d.items():
        if Student==i:
            Percentage=sum(y)/len(y)
            logging.info("%.2f" % Percentage)
            break
        else:
            continue
    return Percentage

