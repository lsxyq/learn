var loadSize = function () {
  var t, l, w, h
  if (document.documentElement && document.documentElement.scrollTop) {
    t = document.documentElement.scrollTop
    l = document.documentElement.scrollLeft
    w = document.documentElement.scrollWidth
    h = document.documentElement.scrollHeight
  } else if (document.body) {
    t = document.body.scrollTop
    l = document.body.scrollLeft
    w = document.body.scrollWidth
    h = document.body.scrollHeight
  }
  alert(t, l, w, h)
}

var t = document.documentElement.scrollTop
var h = document.documentElement.scrollHeight
var d_height = {}
var current = t + d_height
if (current > h) {
  window.scrollTo(0, document.documentElement.clientHeight)
} else {
  window.scrollTo(0, current)
}
