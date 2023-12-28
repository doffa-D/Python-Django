tell application "Finder"
    activate
    display dialog "Do you really want to shut down your computer?" buttons {"Cancel", "Shut Down"} default button "Shut Down"
    
    if button returned of the result is "Shut Down" then
        do shell script "sudo shutdown -h now" with administrator privileges
    end if
end tell
