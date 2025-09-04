from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

from . import core

app = typer.Typer(
    add_completion=False, help="Conversor de Medidas (CLI bonita com Typer + Rich)"
)
console = Console()


def _header():
    console.print(
        Panel.fit(
            "[bold cyan]Conversor de Medidas[/bold cyan] • Typer + Rich",
            border_style="cyan",
        )
    )


@app.command()
def menu():
    """
    Menu interativo (setas não são necessárias; escolha por número).
    """
    _header()
    table = Table(title="Escolha uma conversão", show_lines=True)
    table.add_column("#", justify="right", style="bold")
    table.add_column("Conversão")
    table.add_row("1", "Celsius → Fahrenheit")
    table.add_row("2", "Fahrenheit → Celsius")
    table.add_row("3", "Celsius → Kelvin")
    table.add_row("4", "Kelvin → Celsius")
    table.add_row("5", "Quilômetros → Milhas")
    table.add_row("6", "Milhas → Quilômetros")
    table.add_row("7", "Quilos → Libras")
    table.add_row("8", "Libras → Quilos")
    console.print(table)

    escolha = Prompt.ask(
        "[bold]Digite o número[/bold]", choices=[str(i) for i in range(1, 9)]
    )
    valor_str = Prompt.ask("[bold]Digite o valor[/bold]")
    try:
        valor = float(valor_str.replace(",", "."))
    except ValueError:
        console.print("[red]Valor inválido.[/red]")
        raise typer.Exit(code=1)

    mapa = {
        "1": ("°C", "°F", core.celsius_para_fahrenheit),
        "2": ("°F", "°C", core.fahrenheit_para_celsius),
        "3": ("°C", "K", core.celsius_para_kelvin),
        "4": ("K", "°C", core.kelvin_para_celsius),
        "5": ("km", "mi", core.km_para_milhas),
        "6": ("mi", "km", core.milhas_para_km),
        "7": ("kg", "lb", core.kg_para_lb),
        "8": ("lb", "kg", core.lb_para_kg),
    }

    de, para, func = mapa[escolha]
    resultado = func(valor)

    console.print(
        Panel.fit(
            f"[green]{valor:g} {de}[/green] → [bold yellow]{resultado:.6g} {para}[/bold yellow]",
            border_style="green",
        )
    )


@app.command()
def c2f(c: float = typer.Argument(..., help="Temperatura em °C")):
    """Conversão direta: Celsius para Fahrenheit."""
    console.print(core.celsius_para_fahrenheit(c))


@app.command()
def km2mi(km: float):
    """Conversão direta: km para milhas."""
    console.print(core.km_para_milhas(km))


@app.command()
def kg2lb(kg: float):
    """Conversão direta: kg para lb."""
    console.print(core.kg_para_lb(kg))


if __name__ == "__main__":
    app()
