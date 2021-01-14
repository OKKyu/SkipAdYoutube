' 引数
' ショートカット名
' リンク作成元
' リンク作成先

Set ws = CreateObject("WScript.Shell")

dim scFileName :scFileName = WScript.Arguments(0)
dim linkMoto   :linkMoto   = WScript.Arguments(1)
dim bat        :bat        = WScript.Arguments(2)
dim args       :args       = WScript.Arguments(3)
dim linkSaki   :linkSaki   = WScript.Arguments(4)

' ショートカット作成
WScript.Echo linkSaki + "\" + scFileName + ".lnk"
Set shortcut = ws.CreateShortcut(linkSaki + "\" + scFileName + ".lnk")
With shortcut
    .TargetPath = linkMoto + "\" + bat
    .Arguments = args
    .WorkingDirectory = linkMoto
    .WindowStyle = 7
End With
shortcut.Save
