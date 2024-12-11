import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from matplotlib.figure import Figure

from src.data_export import insert_content
from src.data_preperation import prepare_data, prepare_plots
from src.dataloader import load_test_data

app = FastAPI()


@app.get("/report")
def get_report():
    prepare_report()
    return FileResponse(
        path="report_final.docx",  # Assuming this is the path where your document is saved
        filename="report.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


def prepare_report():
    unproccessed_data = load_test_data()
    proccessed_data = prepare_data(unproccessed_data)
    figures: list[Figure] = prepare_plots(proccessed_data)

    test_dict = {
        "week": "1.2.2024-7.2.2024",
        "Wochenbericht": "Das ist ein Test",
        "Vergleich zur vorherigen Woche": "Das ist ein zweiter Test",
    }

    insert_content(content_dict=test_dict, image=figures[0])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
