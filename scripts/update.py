"""Refresh the cask from the latest public stable PinNote release."""
import json
import re
from pathlib import Path
from urllib.request import urlopen

with urlopen("https://api.github.com/repos/Zhong0118/PinNote/releases/latest", timeout=30) as response:
    release = json.load(response)
tag = release["tag_name"]
if release["draft"] or release["prerelease"] or not re.fullmatch(r"v\d+\.\d+\.\d+", tag):
    raise ValueError("Expected a stable semantic version")
version = tag[1:]
name = f"PinNote_{version}_universal.dmg"
asset, = [item for item in release["assets"] if item["name"] == name and item["state"] == "uploaded"]
digest = asset["digest"]
if not re.fullmatch(r"sha256:[a-f0-9]{64}", digest):
    raise ValueError("Release DMG has no SHA-256 digest")
Path("Casks/pinnote.rb").write_text(f'''cask "pinnote" do
  version "{version}"
  sha256 "{digest[7:]}"

  url "https://github.com/Zhong0118/PinNote/releases/download/v#{{version}}/PinNote_#{{version}}_universal.dmg"
  name "PinNote"
  desc "Desktop Markdown sticky notes with screen-edge docking"
  homepage "https://zhong0118.github.io/PinNote/"

  auto_updates true

  app "PinNote.app"
end
''')
