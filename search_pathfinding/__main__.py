from multiprocessing.managers import Value

import rich_click as click
import random


def generate_grid(grid_size) -> list:
    """
    Generate the grid using some randomness
    :param grid_size: The size of the grid to generate
    :return: Returns the newly generated grid
    """
    grid = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            if random.randint(0, 10) < 5:
                row.append("*")
            else:
                row.append(".")
        grid.append(row)
    return grid


def render_grid(grid) -> None:
    """
    Render the grid as required
    :param grid:
    :return:
    """
    for row in grid:
        for col in row:
            print(col, end=" ")


def dfs(current, end, grid, visited, path):
    """

    :param current:
    :param end:
    :param grid:
    :param visited:
    :param path:
    :return:
    """
    if current == end:
        path.append(current)
        return path

    nodes_available = []

    visited.add(current)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            neighbour = (current[0] + i - 1, current[0] + j - 1)
            if not neighbour:
                raise ValueError("The neighbour is invalid or null")

        path = dfs(nodes_available.pop(), end, grid, visited, [*path])


def traverse(grid: list[list], start: tuple[int, int], end: tuple[int, int]):
    dfs(start, end, grid, set(), [])


@click.group(help="The base command-line interface for the tool.")
@click.option("--grid-size", type=int, default=16, help="The size of the grid to generate.")
@click.pass_context
def cli(context: click.Context, grid_size: int) -> None:
    """

    :param grid_size:
    :param context:
    :return:
    """
    if not context:
        raise ValueError("The click context is invalid.")

    context.ensure_object(dict)
    context.obj["grid_size"] = int(context.params["grid_size"])
    context.exit(0)


@cli.command("generate-grid", help="Generate a randomized grid to traverse")
def cli_generate(ctx: click.Context) -> None:
    """

    :param ctx:
    :return:
    """
    if not ctx:
        raise ValueError("The click context is invalid.")
    grid = generate_grid(ctx.obj["grid_size"])
    render_grid(grid)


@cli.command("bfs", help="The best-first search algorithm")
def cli_bfs(ctx: click.Context) -> None:
    """

    :param ctx:
    :return:
    """
    if not ctx:
        raise ValueError("The click context is invalid.")
    grid = generate_grid(ctx.obj["grid_size"])
    path = traverse(grid, (0, 0), (ctx.obj["grid_size"] - 1, ctx.obj["grid_size"] - 1))


@cli.command("dfs", help="The depth-first search algorithm")
def cli_dfs(ctx: click.Context) -> None:
    """

    :param ctx:
    :return:
    """
    if not ctx:
        raise ValueError("The click context is invalid.")


if __name__ == "__main__":
    try:
        cli()
    except Exception as exc:
        pass
