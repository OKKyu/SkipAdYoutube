' ����
' �V���[�g�J�b�g��
' �����N�쐬��
' �����N�쐬��

Set ws = CreateObject("WScript.Shell")

dim scFileName :scFileName = WScript.Arguments(0)
dim linkMoto   :linkMoto   = WScript.Arguments(1)
dim bat        :bat        = WScript.Arguments(2)
dim args       :args       = WScript.Arguments(3)
dim linkSaki   :linkSaki   = WScript.Arguments(4)

' �V���[�g�J�b�g�쐬
WScript.Echo linkSaki + "\" + scFileName + ".lnk"
Set shortcut = ws.CreateShortcut(linkSaki + "\" + scFileName + ".lnk")
With shortcut
    .TargetPath = linkMoto + "\" + bat
    .Arguments = args
    .WorkingDirectory = linkMoto
    .WindowStyle = 7
End With
shortcut.Save
