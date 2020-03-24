-- Type the text at the system level
on print(readLine)
  tell application "System Events"
    keystroke readLine
    delay (random number from 0.1 to 0.3)
  end tell
end print

on run argv
  -- Read File
  set fromFile to (item 1 of argv)
  set toFile to (item 2 of argv)
  set base64File to do shell script "cat " & fromFile & " | base64"

  -- -- Change to "Citrix Viewer" Window
  activate application "Citrix Viewer"

  -- Copy File
  print("echo '")
  print(base64File)
  print("' | base64 -d > " & toFile & "\n")
end run

