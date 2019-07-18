// if (oSession.uriContains('https://aweme.snssdk.com/aweme/v1/aweme/post/')) {
//   var sps = oSession.PathAndQuery.slice(-58,);
//   var strBody = oSession.GetResponseBodyAsString();
//   var dSessionId = oSession.id;
//
//   // 时间格式化
//   var date = new Date();
//   var month = date.getMonth() + 1;
//   var strDate = date.getDate();
//   var strHours = date.getHours();
//   var strMinutes = date.getMinutes();
//   var strSeconds = date.getSeconds();
//   var strMilliSeconds = date.getMilliseconds();
//
//   if (month >= 1 && month <= 9) {
//     month = '0' + month;
//   }
//   if (strDate >= 0 && strDate <= 9) {
//     strDate = '0' + strDate;
//   }
//   if (strHours >= 0 && strHours <= 9) {
//     strHours = '0' + strHours;
//   }
//   if (strMinutes >= 0 && strMinutes <= 9) {
//     strMinutes = '0' + strMinutes;
//   }
//   if (strSeconds >= 0 && strSeconds <= 9) {
//     strSeconds = '0' + strSeconds;
//   }
//   if (strMilliSeconds >= 0 && strMilliSeconds <= 9) {
//     strMilliSeconds = '00' + strMilliSeconds;
//   } else if (strMilliSeconds >= 10 && strMilliSeconds <= 99) {
//     strMilliSeconds = '0' + strMilliSeconds;
//   }
//
//   var currentdate = date.getFullYear() + month + strDate
//     + '_' + strHours + strMinutes + strSeconds + '_' + strMilliSeconds;
//
//   var filename = 'C:/Projects/learn/douyin/urls' + '/' + currentdate + '_' + dSessionId + '.json';
//   var curDate = new Date();
//   var sw: System.IO.StreamWriter;
//   if (System.IO.File.Exists(filename)) {
//     sw = System.IO.File.AppendText(filename);
//     sw.Write(strBody);
//   } else {
//     sw = System.IO.File.CreateText(filename);
//     sw.Write(strBody);
//   }
//
//   sw.Close();
//   sw.Dispose();
// }
// if (oSession.uriContains('https://api.amemv.com/aweme/v1/aweme/post/')) {
//   var strBody = oSession.GetResponseBodyAsString();
//   var sps = oSession.PathAndQuery.slice(-58,);
//   //FiddlerObject.alert(sps)
//   var dSessionId = oSession.id;
//
//   // 时间格式化
//   var date = new Date();
//   var month = date.getMonth() + 1;
//   var strDate = date.getDate();
//   var strHours = date.getHours();
//   var strMinutes = date.getMinutes();
//   var strSeconds = date.getSeconds();
//   var strMilliSeconds = date.getMilliseconds();
//
//   if (month >= 1 && month <= 9) {
//     month = '0' + month;
//   }
//   if (strDate >= 0 && strDate <= 9) {
//     strDate = '0' + strDate;
//   }
//   if (strHours >= 0 && strHours <= 9) {
//     strHours = '0' + strHours;
//   }
//   if (strMinutes >= 0 && strMinutes <= 9) {
//     strMinutes = '0' + strMinutes;
//   }
//   if (strSeconds >= 0 && strSeconds <= 9) {
//     strSeconds = '0' + strSeconds;
//   }
//   if (strMilliSeconds >= 0 && strMilliSeconds <= 9) {
//     strMilliSeconds = '00' + strMilliSeconds;
//   } else if (strMilliSeconds >= 10 && strMilliSeconds <= 99) {
//     strMilliSeconds = '0' + strMilliSeconds;
//   }
//
//   var currentdate = date.getFullYear() + month + strDate
//     + '_' + strHours + strMinutes + strSeconds + '_' + strMilliSeconds;
//
//   var filename = 'C:/Projects/learn/douyin/urls' + '/' + currentdate + '_' + dSessionId + '.json';
//   var curDate = new Date();
//   var s1: System.IO.StreamWriter;
//   if (System.IO.File.Exists(filename)) {
//     s1 = System.IO.File.AppendText(filename);
//     s1.Write(strBody);
//   } else {
//     s1 = System.IO.File.CreateText(filename);
//     s1.Write(strBody);
//   }
//
//   s1.Close();
//   s1.Dispose();
// }