// Back to Top Start
let calcScrollValue = () => {
  let scrollProgress = document.querySelector(".progress");
  let scrollProgressValue = document.querySelector(".progress_value");
  let position = document.documentElement.scrollTop;
//   console.log("Position = " + position);
  let calcHeight =
    document.documentElement.scrollHeight -
    document.documentElement.clientHeight;
  let scrollValue = Math.round((position * 100) / calcHeight);
//   console.log("Scrolling = " + scrollValue + "%")
  document.querySelector('.present').innerHTML = `${scrollValue}%`
  if (position > 100) {
    scrollProgress.style.display = "grid";
  } else {
    scrollProgress.style.display = "none";
  }
  scrollProgress.addEventListener("click", () => {
    document.documentElement.scrollTop = 0;
  });
  scrollProgress.style.background = `conic-gradient(#03cc65 ${scrollValue}%, #d7d7d7 ${scrollValue}%)`;
  let bottom_header = document.querySelector(".bottom_header");
  let mobile_header = document.querySelector(".mobile_header");
  // Sticky Navbar
  if (position > 20) {
    bottom_header.style.position = 'fixed'
    bottom_header.style.top = "0";
    bottom_header.style.width = '100%'
  } else {
    bottom_header.style.position = 'relative'
    bottom_header.style.top = "";
    bottom_header.style.width = ""
  };
  if (position > 40) {
    mobile_header.style.position = "fixed";
    mobile_header.style.top = "0";
    mobile_header.style.width = "100%";
  } else {
    mobile_header.style.position = "relative";
    mobile_header.style.top = "";
    mobile_header.style.width = "";
  }
};
window.onscroll = calcScrollValue;
window.onload = calcScrollValue;
// Back to Top End

// offcanvas_navbar
let toggler_btn = document.querySelector(".toggler_btn");
let offcanvas_header = document.querySelector(".offcanvas_header");
let close_btn = document.querySelector(".close_btn");

toggler_btn.addEventListener("click", () => {
  offcanvas_header.style.display = "block";
  offcanvas_header.style.transform = "translate(0px)";
});
close_btn.addEventListener("click", () => {
  offcanvas_header.style.transform = "translate(-100%)";
  offcanvas_header.style.display = "none";
});
// popup search
let popup_search = document.querySelector(".popup_search");

function popup() {
  popup_search.style.display = "grid";
}

function popupClose() {
  popup_search.style.display = "none";
}

// dropdown
function dropdown(e) {
  let dropdown_content = document.querySelectorAll(".dropdown_content");
  dropdown_content[e].classList.toggle("dropdown_content_show");
}
