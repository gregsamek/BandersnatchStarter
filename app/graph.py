from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    return Chart(
        df, 
        title=f"{y} by {x} for {target}",
        background="#252525",
        padding={"left": 10, "top": 10, "right": 10, "bottom": 10}
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list()),
    ).configure_title(
        fontSize=20,
        color="#aaaaaa"
    ).configure_axis(
        labelColor="#aaaaaa",
        titleColor="#aaaaaa",
        labelFontSize=14,  # Set font size for axis labels
        titleFontSize=14  # Set font size for axis titles
    ).configure_legend(
        labelColor="#aaaaaa",
        titleColor="#aaaaaa",
        labelFontSize=12,
        titleFontSize=12  # Set font size for legend title
    ).properties(
        width=500,
        height=400
    ).interactive()