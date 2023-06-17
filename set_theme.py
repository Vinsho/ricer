from src.ThemeSetter import ThemeSetter
from src.PaletteMaker import PaletteMaker

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Simple tool for ricing.")

    parser.add_argument("--theme", "-t", type=str, help="Select from exiting themes")
    parser.add_argument(
        "--display", "-d", help="Shows existing themes", action="store_true"
    )
    parser.add_argument("--image", "-i", type=str, help="Image to make a theme from.")
    parser.add_argument("--remove", "-r", type=str, help="Remove given theme.")
    parser.add_argument(
        "--save",
        "-s",
        type=str,
        help="Save created theme from image, provide it's name.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    setter = ThemeSetter()

    if args.display or not any(vars(args).values()):
        print(setter.get_available_themes())
    elif args.theme:
        theme = setter.load_theme(args.theme)
        setter.set_theme(theme)
    elif args.image:
        palette = PaletteMaker().make(args.image)
        palette["image_path"] = args.image

        setter.set_theme(palette)

        if args.save:
            setter.save_theme(theme_name=args.save, theme=palette)

    elif args.remove:
        setter.remove_theme(theme_name=args.remove)
