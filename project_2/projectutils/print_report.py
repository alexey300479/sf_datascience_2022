from IPython.display import Markdown as md


def print_report(reports: dict, title: str, topic: int):
    """
    Печатает последовательно все отчеты из словаря reports,
    относящиеся к разделу topic, озаглавленные title.

    Args:
        reports (dict): словарь отчетов
        title (str): Заголовок отчета
        topic (int): Номер раздела
    """
    report = f"""<h1>Раздел проекта: {topic}. {title}</h1><br>
    <div class='report'>
    """

    for key, value in reports.items():
        if key.startswith(f"report_{topic}"):
            report += "<br>"
            report += f"<h4>{value}</h4>"
    report += "</div>"

    return md(report)
