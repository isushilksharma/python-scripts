$TimeToQuit = $false
$Signature = @'
    [DllImport("user32.dll", CharSet = CharSet.Auto, ExactSpelling = true, CallingConvention = CallingConvention.Winapi)] 
    public static extern short GetKeyState(int keyCode);
'@
Add-Type -AssemblyName System.Windows.Forms
Add-Type -MemberDefinition $Signature -Name Keyboard -Namespace WeakShell

#Write-Output "Starting Show As Active!"
#Write-Output "Turn on Caps Lock to quit."

do {
    # "(([int][WeakShell.Keyboard]::GetKeyState(0x14)) -band 0xffff) -eq 0" = True when CapsLock is off
    if ((([int][WeakShell.Keyboard]::GetKeyState(0x14)) -band 0xffff) -eq 0) {
        [System.Windows.Forms.SendKeys]::SendWait("{ScrollLock}")
	$Pos = [System.Windows.Forms.Cursor]::Position
  	$x = ($pos.X % 500) + 2
  	$y = ($pos.Y % 500) + 5
  	[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
        Start-Sleep -Seconds 1
    }
    else {
        $TimeToQuit = $true
        Write-Output "Caps Lock on, quiting"
    }
}while ($TimeToQuit -eq $false)
