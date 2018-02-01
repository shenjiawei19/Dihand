from .txodds import tasks as tx
from .example import tasks as ex

tasks = {
    'txodds': tx.__all__,
    'exodds': ex.__all__
}
