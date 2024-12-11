from loguru import logger
from matplotlib.figure import Figure

from src.data_preperation import prepare_data, prepare_plots
from src.dataloader import load_test_data

unproccessed_data = load_test_data()
proccessed_data = prepare_data(unproccessed_data)
figures: list[Figure] = prepare_plots(proccessed_data)

# Display the figure
for i in range(len(figures)):
    figures[i].show()
input()
logger.info(proccessed_data)
