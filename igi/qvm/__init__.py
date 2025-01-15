from pathlib import Path

from rich import print
from typer import Typer

from igi.qvm.models import QVM
from igi.settings import settings

app = Typer()


@app.command()
def files(
    source_dir: Path = settings.game_dir,
    target_dir: Path = settings.data_dir,
    glob: str = "**/*.qvm",
    skip: int = 0,
    pick: int = None,
    stop: int = None,
    show_source_file: bool = True,
    show_target_file: bool = False,
    show_target_data: bool = False,
    save_target_data: bool = False,
):
    if pick is not None:
        stop = skip + pick

    for iteration, source_file in enumerate(source_dir.glob(glob), 1):
        if iteration <= skip:
            continue

        if stop is not None and iteration >= stop + 1:
            break

        target_file = target_dir.joinpath(source_file.relative_to(source_dir).with_suffix(".qsc")).absolute()

        if show_source_file:
            print(f'[#00af87]Source [{iteration:>05}]: "{source_file.as_posix()}"[/#00af87]')

        if show_target_file:
            print(f'[#d7af00]Target [{iteration:>05}]: "{target_file.as_posix()}"[/#d7af00]')

        if show_target_data or save_target_data:
            target_data = QVM.model_validate_file(source_file).get_statement_list().get_token()

            if show_target_data:
                print("# Decompiled QSC file start")
                print(target_data)
                print("# Decompiled QSC file end")

            if save_target_data:
                target_file.parent.mkdir(parents=True, exist_ok=True)
                target_file.write_text(target_data)
