import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure


def prepare_data(data: pd.DataFrame) -> pd.DataFrame:
    # Prepare the data for week differenz
    data["Woche"] = data["Woche"].astype(str)
    data["Datum_parsed"] = data["Datum"].apply(
        lambda x: pd.to_datetime(
            x.replace(" ", "").split("-")[0].strip(), format="%d.%m.%Y"
        )
    )
    # Calculate the week difference
    data["Wochen_Differenz"] = (
        data["Datum_parsed"] - data["Datum_parsed"].shift(1)
    ).dt.days / 7

    # Calculate Yield per week
    data["Ertrag (€)"] = (
        data["Gesamtverkäufe (€)"]
        - data["Rückgaben (€)"]
        - data["Beschädigte Ware (€)"]
    )

    # Calculate Profit per week
    data["Gewinn (€)"] = data["Ertrag (€)"] - data["Kosten (€)"]

    # Calculate Percentage Changes from previous week
    data["Ertrag_Prozent_Änderung"] = data["Ertrag (€)"].pct_change() * 100
    data["Gewinn_Prozent_Änderung"] = data["Gewinn (€)"].pct_change() * 100
    data["Gesamtverkäufe_Prozent_Änderung"] = (
        data["Gesamtverkäufe (€)"].pct_change() * 100
    )
    data["Kosten_Prozent_Änderung"] = data["Kosten (€)"].pct_change() * 100
    data["Anzahl_Verkäufe_Prozent_Änderung"] = (
        data["Anzahl der Verkäufe"].pct_change() * 100
    )
    data["Rückgaben_Prozent_Änderung"] = data["Rückgaben (€)"].pct_change() * 100
    data["Beschädigte_Ware_Prozent_Änderung"] = (
        data["Beschädigte Ware (€)"].pct_change() * 100
    )

    return data


def prepare_plots(data: pd.DataFrame) -> list[Figure]:
    figures = []

    # Close any existing figures to prevent memory issues
    plt.close("all")

    # Process each week except the first one
    for i in range(1, len(data)):
        current_week = data.iloc[i]
        previous_week = data.iloc[i - 1]

        fig, ax = plt.subplots(figsize=(12, 8))
        ax.grid(True, linestyle="--", alpha=0.7, axis="y")

        # Set up the bar positions
        labels = [
            "Gesamtverkäufe (€)",
            "Kosten (€)",
            "Ertrag (€)",
            "Gewinn (€)",
            "Anzahl der Verkäufe",
            "Rückgaben (€)",
            "Beschädigte Ware (€)",
        ]
        x = range(len(labels))
        bar_width = 0.35

        # Plot each label for previous and current week
        for j, label in enumerate(labels):
            ax.bar(
                j - bar_width / 2,
                previous_week[label],
                bar_width,
                label=f"{label} (Vorherige Woche)" if i == 1 else "",
                edgecolor="black",
                linewidth=1,
            )
            ax.bar(
                j + bar_width / 2,
                current_week[label],
                bar_width,
                label=f"{label} (Aktuelle Woche)" if i == 1 else "",
                edgecolor="black",
                linewidth=1,
            )

        # Add title and labels
        ax.set_title(
            f'Woche {current_week["Woche"]}\n'
            # f'Ertrag Änderung: {current_week["Ertrag_Prozent_Änderung"]:.1f}%\n'
            # f'Gewinn Änderung: {current_week["Gewinn_Prozent_Änderung"]:.1f}%'
        )

        ax.set_ylabel("Betrag (€)")
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=45, ha="right")

        # Add value labels on the bars
        for idx, week in enumerate([previous_week, current_week]):
            for j, label in enumerate(labels):
                ax.text(
                    j - bar_width / 2 if idx % 2 == 0 else j + bar_width / 2,
                    week[label],
                    f"{week[label]:,.2f}€",
                    ha="center",
                    va="bottom",
                )

        # Add legend with removal of duplicate labels
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys())

        plt.tight_layout()
        figures.append(fig)

    return figures
