import os
import shutil
import yaml
from src.templates import (
    RofiTemplate,
    FehbgTemplate,
    TerminatorTemplate,
    XresourcesTemplate,
    DunstTemplate,
)


class ThemeSetter:
    def __init__(self) -> None:
        self.root_folder = os.path.dirname(os.path.abspath(__file__))
        self.config = self.load_config_yaml()
        self.themes = self.config["themes"]
        self.home_path = f"/home/{os.getlogin()}/"
        self.wallpapers_path = os.path.join(self.root_folder, "wallpapers")

    def get_available_themes(self):
        themes = ""
        for i, theme in enumerate(self.themes):
            themes += f"\t{i}: {theme}\n"

        return "Available themes:\n" + themes

    def load_config_yaml(self):
        config_path = os.path.join(self.root_folder, "config.yaml")

        with open(config_path, "r") as stream:
            return yaml.safe_load(stream)

    def save_config_yaml(self):
        config_path = os.path.join(self.root_folder, "config.yaml")

        with open(config_path, "w") as config_file:
            return yaml.dump(self.config, config_file)

    def get_theme_name_from_idx(self, theme_name):
        if theme_name.isnumeric() and int(theme_name) < len(self.themes):
            return list(self.themes.keys())[int(theme_name)]
        return theme_name

    def load_theme(self, theme_name):
        theme_name = self.get_theme_name_from_idx(theme_name)

        if theme_name not in self.themes:
            raise Exception("Unknown theme!\n" + self.get_available_themes())

        theme = self.themes[theme_name]
        theme["image_path"] = os.path.join(self.wallpapers_path, theme["image_name"])

        return theme

    def copy_files(self):
        for file, path in self.config["files"].items():
            shutil.copy(
                os.path.join(self.root_folder, "files", file),
                os.path.join(self.home_path, path),
            )

    def generate_from_template(self, theme):
        for template in [
            RofiTemplate,
            FehbgTemplate,
            TerminatorTemplate,
            XresourcesTemplate,
            DunstTemplate,
        ]:
            content = template.template.format(**theme)
            with open(os.path.join(self.home_path, template.path), "w") as f:
                f.write(content)

    def save_theme(self, theme_name, theme):
        if theme_name not in self.themes:
            image_name = theme["image_path"].split("/")[-1]
            shutil.copy(theme.pop("image_path"), os.path.join(self.wallpapers_path, image_name))

            theme["image_name"] = image_name

            self.themes[theme_name] = theme
            self.save_config_yaml()
            print(f"Theme {theme_name} successfully saved! ")
        else:
            raise Exception(f"Theme with name {theme_name} already exists!")

    def reload_needed(self):
        os.system("xrdb ~/.Xresources")
        os.system("killall dunst >/dev/null 2>&1")
        os.system(f"{self.home_path}.fehbg")
        os.system(f"{self.home_path}{self.config['files']['launch_polybar.sh']} >/dev/null 2>&1")

    def set_theme(self, theme):
        self.copy_files()
        self.generate_from_template(theme)

        self.reload_needed()
