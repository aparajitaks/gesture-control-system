import subprocess

class VolumeController:
    def volume_up(self):
        subprocess.call([
            "osascript",
            "-e",
            "set volume output volume ((output volume of (get volume settings)) + 6)"
        ])

    def volume_down(self):
        subprocess.call([
            "osascript",
            "-e",
            "set volume output volume ((output volume of (get volume settings)) - 6)"
        ])

    def mute_toggle(self):
        subprocess.call([
            "osascript",
            "-e",
            "set volume output muted not (output muted of (get volume settings))"
        ])
