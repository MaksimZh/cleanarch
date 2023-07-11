from api import *

m = new() \
    .bind(move(100)) \
    .bind(turn(-90)) \
    .bind(set_state("soap")) \
    .bind(start()) \
    .bind(move(50)) \
    .bind(stop())

m.eval()
