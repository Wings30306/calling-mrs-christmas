/** Adapted from Days Until Christmas Countdown 1 
 * Powered by https://www.days-until-christmas.co.uk
 * Free to use as long as this notice is kept in place.
 * Created: 17/04/2010
 * Modified: 03/02/2018 
 * Original Script: https://www.days-until-christmas.co.uk/webcounts/xcd3248.js
 */

let t = new Date(),
  td = t.getDate(),
  tm = t.getMonth(), // index starts at 0 for January, ends at 11 for December
  xy = t.getFullYear();
11 == tm && td > 25 && xy++;
let xd = new Date(xy, 11, 25), 
  msd = 86400000, // milliseconds in a day
  tl = xd.getTime() - t.getTime(),
  dl = tl / msd,
  wdl = Math.ceil(dl); 
0 == wdl
  ?  htmlString = "<div style='font-size:16px;left:2px;top:62px;'>Merry<br>Christmas!</div>"
  : 1 == wdl
  ?  htmlString = "<div style='font-size:12px;left:2px;top:66px;'>It's<br>Christmas Eve!</div>"
  : htmlString = "<div style='font-size:28px;top:65px;'>" + wdl + "</div>";
  document.getElementById("xcd3248").innerHTML = htmlString;

/* End of Christmas Countdown script */


/**
 * Activate all tooltips
 * Function from the Bootstrap documentation, hence why it's using jQuery
 * https://getbootstrap.com/docs/4.4/components/tooltips/#example-enable-tooltips-everywhere
 */
$("[data-toggle='tooltip']").tooltip();

/**
 * Get current year for copyright statement in footer 
 */
document.getElementById("current-year").innerHTML = new Date().getFullYear()

/**
 * Highlight current day in contact page - opening hours.
 * Script adapted from: 
 * https://github.com/BlackrockDigital/startbootstrap-business-casual/blob/master/store.html
 * Changed to make sure Monday is index 0, Sunday is index 6. Original table started at Sunday.
 */
today = new Date().getDay() - 1
if (today === -1) {
  today = 6
}
$('.list-hours li').eq(today).addClass('today');