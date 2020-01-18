/* Adapted from Days Until Christmas Countdown 1 
Powered by https://www.days-until-christmas.co.uk
Free to use as long as this notice is kept in place.
Created: 17/04/2010
Modified: 03/02/2018 
Original Script: https://www.days-until-christmas.co.uk/webcounts/xcd3248.js */

document.write(); var t = new Date(), td = t.getDate(), tm = t.getMonth(), xy = t.getFullYear(); 11 == tm && td > 25 && xy++; var xd = new Date(xy, 11, 25), msd = 86400000, tl = (xd.getTime() - t.getTime()), dl = tl / msd, wdl = Math.ceil(dl), a = document.getElementById('xcda3248'); 0 == wdl ? document.write("<div style='font-size:16px;left:2px;top:62px;'>Merry<br>Christmas!</div>") : 1 == wdl ? document.write("<div style='font-size:12px;left:2px;top:66px;'>It's<br>Christmas Eve!</div>") : document.write("<div style='font-size:28px;top:65px;'>" + wdl + "</div>"); (!a || a.href.indexOf("www.days-until-christmas.co.uk") < 0) && (document.getElementById("xcd3248").innerHTML = "");