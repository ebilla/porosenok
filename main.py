import time
import os
import random
from colorama import init, Fore, Back, Style
import pygame

init(autoreset=True)

pygame.mixer.init()

def play_music(music_file):
    try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.25)
    except Exception as e:
        print(Fore.RED + f"Ошибка при воспроизведении музыки: {e}")

class MegaDancingPig:
    def __init__(self):
        self.width = os.get_terminal_size().columns
        self.height = os.get_terminal_size().lines
        self.frames = self._create_mega_frames()
        self.x = 0
        self.y = 5
        self.x_speed = 1
        self.y_speed = 0
        self.gravity = 0.1
        self.ground_level = self.height - 10
        self.energy = 100
        self.dance_styles = [
            "Великолепнейший", "Очаровательный", "Исключительный", "Умница",
            "Гениальный", "Талантливый", "Непревзойденный", "Блестящий", "Вдохновляющий",
            "Прекрасная душа"
        ]
        self.current_style = 0
        self.color_cycle = 0

    def _create_mega_frames(self):
        return [
            r"""
( ° ʖ °)
    """,
            r"""
(⊙ヮ⊙)
    """,
            r"""
¯\_(ツ)_/¯
    """,
            r"""
(ง ° ل °)ง
    """,
            r"""
( ° ʖ °)
    """,
            r"""
(ง ° ل °)ง
    """,
            r"""
ʕ•ᴥ•ʔ
    """,
            r"""
(ᵔᴥᵔ)
    """,
            r"""
(ಥ﹏ಥ)
    """,
            r"""
(ง°ل°)ง
    """,
            r"""
ᕦ(ò_óˇ)ᕤ
    """,
            r"""
┌( ಠ_ಠ)┘
    """,
            r"""
(ಠ_ಠ)
    """,
            r"""
(ಥ_ಥ)
    """,
            r"""
◘_◘
    """,
            r"""
ب_ب
    """,
            r"""
(✿｡✿)
""",
            r"""
⊙﹏⊙
""",
            r"""
◉◡◉
""",
            r"""
◉_◉
""",
            r"""
⊙︿⊙
""",
            r"""
ಠ▃ಠ
""",
            r"""
( ･_･)♡
""",
            r"""
( ﾟヮﾟ)
""",
            r"""
(¬‿¬)
""",
            r"""
(╥_╥)
""",
            r"""
(◕‿◕)
""",
            r"""
(ʘᗩʘ')
""",
            r"""
(✪㉨✪)
""",
            r"""
|◔◡◉|
""",
            r"""
(⊙ω⊙)
""",
            r"""
(◑‿◐)
""",
            r"""
(╯3╰)
""",
            r"""
┌( ಠ‿ಠ)┘
""",
            r"""
(ಠ╭╮ಠ)
""",
            r"""
╘[◉﹃◉]╕
""",
            r"""
o(╥﹏╥)o
""",
            r"""
\ (•◡•) /
"""]


    def _clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def _get_color(self):
        colors = [
            Fore.RED, Fore.GREEN, Fore.YELLOW,
            Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
            Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX
        ]
        self.color_cycle = (self.color_cycle + 1) % len(colors)
        return colors[self.color_cycle]


    def _update_physics(self):
        self.x += self.x_speed
        if self.x <= 0 or self.x >= self.width - 30:
            self.x_speed *= -1
            self.current_style = (self.current_style + 1) % len(self.dance_styles)

        self.y_speed += self.gravity
        self.y += self.y_speed

        if self.y >= self.ground_level:
            self.y = self.ground_level
            self.y_speed = -random.uniform(1.5, 3.0)  # Случайная сила прыжка
            self.energy = min(100, self.energy + 20)


    def dance(self, duration=100):
        start_time = time.time()
        frame_idx = 0

        try:
            while time.time() - start_time < duration:
                self._clear()
                self._update_physics()

                current_frame = self.frames[frame_idx % len(self.frames)]
                colored_pig = self._get_color() + current_frame

                output = []
                output.append(Fore.WHITE + f"≡≡≡ SUPER MEGA DANCING ≡≡≡".center(self.width))
                output.append("")
                output.append(Fore.CYAN + f"Ты сегодня: {self.dance_styles[self.current_style]} | "
                                          f"Уровень кринжа: {self.energy}% | "
                                          f"Время: {int(time.time() - start_time)} сек")
                output.append("")

                for _ in range(int(self.y)):
                    output.append("")

                pig_lines = colored_pig.split('\n')
                for line in pig_lines:
                    output.append(" " * int(self.x) + line)

                print('\n'.join(output))

                frame_idx += 1
                self.energy = max(0, self.energy - 0.5)
                time.sleep(0.25)

        except KeyboardInterrupt:
            print(Fore.GREEN + Style.BRIGHT + "\nMEGA PIG закончил шоу! Спасибо за просмотр!" + Style.RESET_ALL)


if __name__ == "__main__":
    # Запуск музыки
    music_file = "background.mp3"
    play_music(music_file)

    pig = MegaDancingPig()
    pig.dance()
