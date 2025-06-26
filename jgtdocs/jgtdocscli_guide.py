import argparse
from pathlib import Path

try:
    from jgtpy.jgtpy_guide_for_agent import (
        list_sections as jgtpy_list_sections,
        read_section as jgtpy_read_section,
        list_scripts as jgtpy_list_scripts,
        read_script as jgtpy_read_script,
        show_script_examples as jgtpy_examples,
        install_scripts as jgtpy_install_scripts,
    )
    JGTPY_AVAILABLE = True
except Exception:  # pragma: no cover - optional dependency
    JGTPY_AVAILABLE = False

DOCS_DIR = Path(__file__).resolve().parent.parent / 'book'
DEFAULT_FILE = DOCS_DIR / 'core_principles.md'


def read_markdown(path: Path) -> str:
    if not path.exists():
        return f"Documentation file not found: {path}"
    return path.read_text()


def list_docs() -> list:
    files = [p for p in DOCS_DIR.glob('**/*.md') if p.is_file()]
    return files


def main():
    parser = argparse.ArgumentParser(description='JGTDocs CLI Guide')
    parser.add_argument('--list', action='store_true', help='List available documentation files')
    parser.add_argument('--doc', type=str, help='Display a specific documentation file by name')
    parser.add_argument('--principles', action='store_true', help='Show core principles documentation')
    parser.add_argument('--all', action='store_true', help='Display all documentation files')
    parser.add_argument('--deps', action='store_true', help='Show dependency overview')
    parser.add_argument('--info-request', action='store_true', help='Show pending information requests')

    # jgtpy integration
    parser.add_argument('--jgtpy-list', action='store_true', help='List jgtpy documentation sections')
    parser.add_argument('--jgtpy-section', type=str, help='Display a specific jgtpy section')
    parser.add_argument('--jgtpy-scripts', action='store_true', help='List available jgtpy scripts')
    parser.add_argument('--jgtpy-script', type=str, help='Show a specific jgtpy script')
    parser.add_argument('--jgtpy-examples', action='store_true', help='Show jgtpy script usage examples')
    parser.add_argument('--jgtpy-install-scripts', type=str, nargs='?', const='current',
                        help='Install jgtpy scripts to directory (default: current)')
    parser.add_argument('--jgtpy-overwrite', action='store_true', help='Overwrite files when installing jgtpy scripts')
    args = parser.parse_args()

    if args.list:
        for f in list_docs():
            print(f.relative_to(DOCS_DIR))
        return

    if args.principles:
        print(read_markdown(DEFAULT_FILE))
        return

    if args.doc:
        target = DOCS_DIR / args.doc
        print(read_markdown(target))
        return

    if args.all:
        for f in list_docs():
            print(read_markdown(f))
            print()
        return

    if args.deps:
        target = DOCS_DIR / 'sections' / 'dependencies.md'
        print(read_markdown(target))
        return

    if args.info_request:
        target = DOCS_DIR / 'sections' / 'info_request.md'
        print(read_markdown(target))
        return

    if args.jgtpy_list:
        if JGTPY_AVAILABLE:
            for sec in jgtpy_list_sections():
                print(sec)
        else:
            print('jgtpy documentation not available')
        return

    if args.jgtpy_section:
        if JGTPY_AVAILABLE:
            print(jgtpy_read_section(args.jgtpy_section))
        else:
            print('jgtpy documentation not available')
        return

    if args.jgtpy_scripts:
        if JGTPY_AVAILABLE:
            for s in jgtpy_list_scripts():
                print(s)
        else:
            print('jgtpy scripts not available')
        return

    if args.jgtpy_script:
        if JGTPY_AVAILABLE:
            print(jgtpy_read_script(args.jgtpy_script))
        else:
            print('jgtpy scripts not available')
        return

    if args.jgtpy_examples:
        if JGTPY_AVAILABLE:
            print(jgtpy_examples())
        else:
            print('jgtpy examples not available')
        return

    if args.jgtpy_install_scripts is not None:
        if JGTPY_AVAILABLE:
            target = None if args.jgtpy_install_scripts == 'current' else args.jgtpy_install_scripts
            installed, failed = jgtpy_install_scripts(target, args.jgtpy_overwrite)
            if installed:
                print('Installed scripts:')
                for s in installed:
                    print(f'  {s}')
            if failed:
                print('Failed to install:')
                for s in failed:
                    print(f'  {s}')
        else:
            print('jgtpy scripts not available')
        return

    parser.print_help()


if __name__ == '__main__':
    main()
