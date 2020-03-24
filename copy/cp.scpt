-- Type the text at the system level
on print(readLine)
  tell application "System Events"
    keystroke readLine
    delay (random number from 0.1 to 0.3)
  end tell
end print

on run argv
  set fromFile to (item 1 of argv)
  set toFile to (item 2 of argv)

  set base64File to do shell script "cat " & fromFile & " | base64 | fold -w 100000"
  set md5 to do shell script "cat " & fromFile & " | md5sum | cut -d ' ' -f 1"
  set the_list to paragraphs of base64File

  -- -- Change to "Citrix Viewer" Window
  activate application "Citrix Viewer"

  print("BCP\n")
  delay (random number from 1.0 to 1.0)

  repeat with the_row in the_list
    set the clipboard to the_row
    delay (random number from 0.3 to 0.3)
    print("CCP\n")
    delay (random number from 0.3 to 0.3)
  end repeat

  delay (random number from 1.0 to 1.0)
  print("ACP " & toFile & " " & md5 & "\n")
end run

