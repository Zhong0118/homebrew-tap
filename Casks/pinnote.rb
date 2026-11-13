cask "pinnote" do
  version "1.3.8"
  sha256 "99199fd9c8f8a9721e6438cee342f706e8f5280d3614089c6ba3bbe6d8a876f7"

  url "https://github.com/Zhong0118/PinNote/releases/download/v#{version}/PinNote_#{version}_universal.dmg"
  name "PinNote"
  desc "Desktop Markdown sticky notes with screen-edge docking"
  homepage "https://zhong0118.github.io/PinNote/"

  auto_updates true

  app "PinNote.app"
end
