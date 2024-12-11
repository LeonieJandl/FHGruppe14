from matplotlib.figure import Figure

from src.data_export import insert_content
from src.data_preperation import prepare_data, prepare_plots
from src.dataloader import load_test_data

unproccessed_data = load_test_data()
proccessed_data = prepare_data(unproccessed_data)
figures: list[Figure] = prepare_plots(proccessed_data)

test_dict = {
    "week": "1.2.2024-7.2.2024",
    "Wochenbericht": "Das ist ein Test",
    "Vergleich zur vorherigen Woche": "Das ist ein zweiter Test",
}

insert_content(content_dict=test_dict, image=figures[0])
