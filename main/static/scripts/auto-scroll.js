hei = window.screen.height;

function myFunction() {
    setTimeout(function () {
        var scrollPos = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
        if (scrollPos < 50) {
            //window.scrollBy(0, hei / 1.37);
            //--start--for safari
            var to = (hei / 1.3);
            var i = 0;
            if (i < to) {
                var int = setInterval(function () {
                    if (i > (to - 20)) i += 1;
                    else if (i > (to - 70)) i += 2;
                    else if (i > (to - 90)) i += 3;
                    else if (i > (to - 160)) i += 7;
                    else if (i > (to - 250)) i += 13;
                    else if (i > (to - 410)) i += 25;
                    else if (i > (to - 660)) i += 50;
                    else i += 100;
                    window.scroll(0, i);
                    if (i >= to) clearInterval(int);
                });
            }
            //--and--
        }
    },500);
}
myFunction();