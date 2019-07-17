#!/usr/bin/env bash
Dim yanshi,dspbt_bj,dspyx_bj,jg,bjmz,dspxy
yanshi = 1500
bjmz = "请输入短视频标题以及短视频的坐标位置"
UI.NewLayout (bjmz)
UI.SetOnShow(bjmz, 布局显示事件)
UI.Show (bjmz)
dspbt_bj = UI.GetValue("dspbt")
dspyx_bj = UI.GetValue("dspxy")
Function 布局显示事件()
    UI.AddTextView bjmz, "文字框1", "短视频标题："
    UI.AddEditText bjmz, "dspbt", "我刚刚发布一段短视频，快来看看吧！", 300, 50
    UI.AddTextView(bjmz, "文字框2", "短视频1-6：")
    UI.AddEditText bjmz, "dspxy", "6", 100
End Function
Do
    If CmpColorEx("338|1235|E3E923,334|1251|FFFFFF,338|1267|E5EB23,376|1235|5F3CF4,380|1251|FFFFFF,376|1267|613DF6",0.9) = 1 Then
        TracePrint "抖音初始界面"
        Delay yanshi
        Tap 518, 1255 //消息
        Delay yanshi
        Tap 355,1251 //发布
    ElseIf CmpColorEx("35|55|FFFFFF,101|56|D8D56A,356|1209|552CFE,359|1278|FFFFFF",0.9) = 1 Then
        TracePrint "拍摄界面"
        Delay yanshi
        Tap 626,1187 //上传
        Delay yanshi
    ElseIf CmpColorEx("9|30|EFEFEE,0|140|15CEFA,186|113|483F3D,347|49|B0ADAC,360|139|FFFFFF,691|57|E7E7E7",0.9) = 1 Then
        TracePrint "选择视频" // 120,291, 351|278|  605|277|  127|511|  365|507|  578|515|
        Delay yanshi
        dspxy = dspyx_bj["dspxy"]
        TracePrint dspxy
        If Int(dspxy) = 1 Then
            Tap 120, 291 //选择第1个视频
        ElseIf Int(dspxy) = 2 Then
            Tap 351,278 //选择第2个视频
        ElseIf Int(dspxy) = 3 Then
            Tap 605,277 //选择第3个视频
        ElseIf Int(dspxy) = 4 Then
            Tap 127,511 //选择第4个视频
        ElseIf Int(dspxy) = 5 Then
            Tap 365,507 //选择第5个视频
        ElseIf Int(dspxy) = 6 Then
            Tap 578,515 //选择第6个视频
        End If
        Delay yanshi
    ElseIf CmpColorEx("619|8|7454F5,705|44|5437DB,620|44|552CFE,705|8|5A3CDE,48|1155|15CEFA,53|1229|12C6F2",0.9) = 1 Then
        TracePrint "剪辑界面"
        Delay yanshi
        Tap 664,28 //下一步
        Delay yanshi
    ElseIf CmpColorEx("35|27|DEDDDC,47|79|F6F5F4,617|41|FFFFFF,605|51|FFFFFF,616|60|FFFFFF,627|1209|552CFE,703|1242|5F3EDC,626|1242|5E3FDE,702|1208|5F3FDE",0.9) = 1 Then
        TracePrint "剪辑完成界面"
        Delay yanshi
        Tap 665, 1224 //下一步
        Delay yanshi
    ElseIf CmpColorEx("464|1162|FEFEFF,464|1161|6C49FE,33|1065|3B3130,33|1064|1A0F0E,346|55|1A0F0E,346|56|B5B2B1",0.9) = 1 Then
        TracePrint "最终发布"
        Delay yanshi
        //InputText "我刚刚发布一段短视频，快来看看吧！"
        jg = UTF8.Len(dspbt_bj["dspbt"])
        For i = 1 To jg
            Delay 50
            KeyPress UTF8.StrGetAt(dspbt_bj["dspbt"], i)
        Next
        Delay yanshi
        Tap 463,1170 //最终发布
        Delay yanshi
    Else
        TracePrint 0
    End If
    Delay yanshi
    Sys.ClearMemory() //释放内存
Loop