clear
graph drop _all
cap drop all
use data_2024.dta
describe
summarize

tsset monthly


*logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti

gen doilregunc = d.oilregunc2024

gen dlprodoil = d.logprodoil
gen dldrill = d.logdrill

gen dlstock = d.logstock
gen dffr = d.ffr
gen dlcpi = d.logcpi
gen dlipm = d.logipm
gen dlworldprodoil = d.logworldprodoil
gen dkilianindex_100 = d.kilianindex_100
gen dlrwti = d.logrwti

* Choose impulse response horizon
local hmax = 60

* Cumulative
forvalues h = 0/`hmax' {
	gen prodoil_c`h' = f`h'.logprodoil - l.logprodoil 
}

forvalues h = 0/`hmax' {
	gen drill_c`h' = f`h'.logdrill - l.logdrill
	gen drill_`h' = f`h'.logdrill
}

forvalues h = 0/`hmax' {
	gen stock_c`h' = f`h'.logstock - l.logstock
	gen stock_`h' = f`h'.logstock
}

forvalues h = 0/`hmax' {
	gen ffr_c`h' = f`h'.ffr - l.ffr
	gen ffr_`h' = f`h'.ffr
}

forvalues h = 0/`hmax' {
	gen cpi_c`h' = f`h'.logcpi - l.logcpi
	gen cpi_`h' = f`h'.logcpi
}

forvalues h = 0/`hmax' {
	gen ipm_c`h' = f`h'.logipm - l.logipm
	gen ipm_`h' = f`h'.logipm
}

forvalues h = 0/`hmax' {
	gen worldprodoil_c`h' = f`h'.logworldprodoil - l.logworldprodoil
	gen worldprodoil_`h' = f`h'.logworldprodoil
}

forvalues h = 0/`hmax' {
	gen wti_c`h' = f`h'.logrwti - l.logrwti
	gen wti_`h' = f`h'.logrwti
}

forvalues h = 0/`hmax' {
	gen kilian_c`h' = f`h'.kilianindex_100 - l.kilianindex_100
	gen kilian_`h' = f`h'.kilianindex_100
}


* Cumulative
/*us oil drilling*/
*est sto clear
cap drop b u d Years Zero
gen Years = _n-1 if _n<=`hmax'
gen Zero =  0    if _n<=`hmax'
gen b=0
gen u=0
gen d=0
forv h = 0/`hmax' {
	 *baseline
     newey drill_c`h' doilregunc l(1/12).doilregunc l(1/12).dlstock l(1/12).dffr l(1/12).dlcpi l(1/12).dldrill l(1/12).dlipm l(1/12).dlworldprodoil l(1/12).dkilianindex_100 l(1/12).dlrwti if tin(1985m1,2021m12), lag(`h')
	 replace b = _b[doilregunc]                     if _n == `h'+1
	 replace u = _b[doilregunc] + 1* _se[doilregunc]  if _n == `h'+1
	 replace d = _b[doilregunc] - 1* _se[doilregunc]  if _n == `h'+1
}
* nois esttab , se nocons keep(dgs1)
gen b_oildrill=b

set scheme s1color
twoway (rarea u d Years, fcolor(gs13) lcolor(gs13) lw(none) lpattern(solid)) (line b_oildrill Years, lcolor(black) lpattern(solid) lwidth(thick)) (line Zero Years, lcolor(black)), legend(off) title("U.S. Oil Drilling", color(black)) xtitle("Month") graphregion(color(white)) plotregion(fcolor(white)) xlabel(0(10)60)
gr rename fig_oildrill,replace

/*stock*/
est sto clear
cap drop b u d Years Zero
gen Years = _n-1 if _n<=`hmax'
gen Zero =  0    if _n<=`hmax'
gen b=0
gen u=0
gen d=0
forv h = 0/`hmax' {
	 *baseline
     newey stock_c`h' doilregunc l(1/12).doilregunc l(1/12).dlstock l(1/12).dffr l(1/12).dlcpi l(1/12).dldrill l(1/12).dlipm l(1/12).dlworldprodoil l(1/12).dkilianindex_100 l(1/12).dlrwti if tin(1985m1,2021m12), lag(`h')
	 replace b = _b[doilregunc]                     if _n == `h'+1
	 replace u = _b[doilregunc] + 1* _se[doilregunc]  if _n == `h'+1
	 replace d = _b[doilregunc] - 1* _se[doilregunc]  if _n == `h'+1
}
* nois esttab , se nocons keep(dgs1)
gen b_stock=b
twoway (rarea u d Years, fcolor(gs13) lcolor(gs13) lw(none) lpattern(solid)) (line b_stock Years, lcolor(black) lpattern(solid) lwidth(thick)) (line Zero Years, lcolor(black)), legend(off) title("S&P 500 Index", color(black)) xtitle("Month") graphregion(color(white)) plotregion(fcolor(white)) xlabel(0(10)60)
gr rename fig_stock,replace

/*federal funds rate*/
est sto clear
cap drop b u d Years Zero
gen Years = _n-1 if _n<=`hmax'
gen Zero =  0    if _n<=`hmax'
gen b=0
gen u=0
gen d=0
forv h = 0/`hmax' {
	 *baseline
     newey ffr_c`h' doilregunc l(1/12).doilregunc l(1/12).dlstock l(1/12).dffr l(1/12).dlcpi l(1/12).dldrill l(1/12).dlipm l(1/12).dlworldprodoil l(1/12).dkilianindex_100 l(1/12).dlrwti if tin(1985m1,2021m12), lag(`h')
	 replace b = _b[doilregunc]                     if _n == `h'+1
	 replace u = _b[doilregunc] + 1* _se[doilregunc]  if _n == `h'+1
	 replace d = _b[doilregunc] - 1* _se[doilregunc]  if _n == `h'+1
}
* nois esttab , se nocons keep(dgs1)
gen b_ffr=b
twoway (rarea u d Years, fcolor(gs13) lcolor(gs13) lw(none) lpattern(solid)) (line b_ffr Years, lcolor(black) lpattern(solid) lwidth(thick)) (line Zero Years, lcolor(black)), legend(off) title("Federal Funds Rate", color(black)) xtitle("Month") graphregion(color(white)) plotregion(fcolor(white)) xlabel(0(10)60)
gr rename fig_ffr,replace

/*industrial production*/
est sto clear
cap drop b u d Years Zero
gen Years = _n-1 if _n<=`hmax'
gen Zero =  0    if _n<=`hmax'
gen b=0
gen u=0
gen d=0
forv h = 0/`hmax' {
	 *baseline
     newey ipm_c`h' doilregunc l(1/12).doilregunc l(1/12).dlstock l(1/12).dffr l(1/12).dlcpi l(1/12).dldrill l(1/12).dlipm l(1/12).dlworldprodoil l(1/12).dkilianindex_100 l(1/12).dlrwti if tin(1985m1,2021m12), lag(`h')
	 replace b = _b[doilregunc]                     if _n == `h'+1
	 replace u = _b[doilregunc] + 1* _se[doilregunc]  if _n == `h'+1
	 replace d = _b[doilregunc] - 1* _se[doilregunc]  if _n == `h'+1
}
* nois esttab , se nocons keep(dgs1)
gen b_ipm=b
twoway (rarea u d Years, fcolor(gs13) lcolor(gs13) lw(none) lpattern(solid)) (line b_ipm Years, lcolor(black) lpattern(solid) lwidth(thick)) (line Zero Years, lcolor(black)), legend(off) title("Industrial Production", color(black)) xtitle("Month") graphregion(color(white)) plotregion(fcolor(white)) xlabel(0(10)60)
gr rename fig_ipm,replace

/*world economic activity*/
est sto clear
cap drop b u d Years Zero
gen Years = _n-1 if _n<=`hmax'
gen Zero =  0    if _n<=`hmax'
gen b=0
gen u=0
gen d=0
forv h = 0/`hmax' {
	 *baseline
     newey kilian_c`h' doilregunc l(1/12).doilregunc l(1/12).dlstock l(1/12).dffr l(1/12).dlcpi l(1/12).dldrill l(1/12).dlipm l(1/12).dlworldprodoil l(1/12).dkilianindex_100 l(1/12).dlrwti if tin(1985m1,2021m12), lag(`h')
	 replace b = _b[doilregunc]                     if _n == `h'+1
	 replace u = _b[doilregunc] + 1* _se[doilregunc]  if _n == `h'+1
	 replace d = _b[doilregunc] - 1* _se[doilregunc]  if _n == `h'+1
}
* nois esttab , se nocons keep(dgs1)
gen b_kilian=b
twoway (rarea u d Years, fcolor(gs13) lcolor(gs13) lw(none) lpattern(solid)) (line b_kilian Years, lcolor(black) lpattern(solid) lwidth(thick)) (line Zero Years, lcolor(black)), legend(off) title("World Economic Activity", color(black)) xtitle("Month") graphregion(color(white)) plotregion(fcolor(white)) xlabel(0(10)60)
gr rename fig_wea,replace

/*world oil production*/
est sto clear
cap drop b u d Years Zero
gen Years = _n-1 if _n<=`hmax'
gen Zero =  0    if _n<=`hmax'
gen b=0
gen u=0
gen d=0
forv h = 0/`hmax' {
	 *baseline
     newey worldprodoil_c`h' doilregunc l(1/12).doilregunc l(1/12).dlstock l(1/12).dffr l(1/12).dlcpi l(1/12).dldrill l(1/12).dlipm l(1/12).dlworldprodoil l(1/12).dkilianindex_100 l(1/12).dlrwti if tin(1985m1,2021m12), lag(`h')
	 replace b = _b[doilregunc]                     if _n == `h'+1
	 replace u = _b[doilregunc] + 1* _se[doilregunc]  if _n == `h'+1
	 replace d = _b[doilregunc] - 1* _se[doilregunc]  if _n == `h'+1
}
* nois esttab , se nocons keep(dgs1)
gen b_wop=b
twoway (rarea u d Years, fcolor(gs13) lcolor(gs13) lw(none) lpattern(solid)) (line b_wop Years, lcolor(black) lpattern(solid) lwidth(thick)) (line Zero Years, lcolor(black)), legend(off) title("World Oil Production", color(black)) xtitle("Month") graphregion(color(white)) plotregion(fcolor(white)) xlabel(0(10)60)
gr rename fig_wop,replace

/*price level*/
est sto clear
cap drop b u d Years Zero
gen Years = _n-1 if _n<=`hmax'
gen Zero =  0    if _n<=`hmax'
gen b=0
gen u=0
gen d=0
forv h = 0/`hmax' {
	 *baseline
     newey cpi_c`h' doilregunc l(1/12).doilregunc l(1/12).dlstock l(1/12).dffr l(1/12).dlcpi l(1/12).dldrill l(1/12).dlipm l(1/12).dlworldprodoil l(1/12).dkilianindex_100 l(1/12).dlrwti if tin(1985m1,2021m12), lag(`h')
	 replace b = _b[doilregunc]                     if _n == `h'+1
	 replace u = _b[doilregunc] + 1* _se[doilregunc]  if _n == `h'+1
	 replace d = _b[doilregunc] - 1* _se[doilregunc]  if _n == `h'+1
}
* nois esttab , se nocons keep(dgs1)
gen b_cpi=b
twoway (rarea u d Years, fcolor(gs13) lcolor(gs13) lw(none) lpattern(solid)) (line b_cpi Years, lcolor(black) lpattern(solid) lwidth(thick)) (line Zero Years, lcolor(black)), legend(off) title("Price Level", color(black)) xtitle("Month") graphregion(color(white)) plotregion(fcolor(white)) xlabel(0(10)60)
gr rename fig_cpi,replace

/*oil prices*/
est sto clear
cap drop b u d Years Zero
gen Years = _n-1 if _n<=`hmax'
gen Zero =  0    if _n<=`hmax'
gen b=0
gen u=0
gen d=0
forv h = 0/`hmax' {
	 *baseline
     newey wti_c`h' doilregunc l(1/12).doilregunc l(1/12).dlstock l(1/12).dffr l(1/12).dlcpi l(1/12).dldrill l(1/12).dlipm l(1/12).dlworldprodoil l(1/12).dkilianindex_100 l(1/12).dlrwti if tin(1985m1,2021m12), lag(`h')
	 replace b = _b[doilregunc]                     if _n == `h'+1
	 replace u = _b[doilregunc] + 1* _se[doilregunc]  if _n == `h'+1
	 replace d = _b[doilregunc] - 1* _se[doilregunc]  if _n == `h'+1
}
* nois esttab , se nocons keep(dgs1)
gen b_wti=b
twoway (rarea u d Years, fcolor(gs13) lcolor(gs13) lw(none) lpattern(solid)) (line b_wti Years, lcolor(black) lpattern(solid) lwidth(thick)) (line Zero Years, lcolor(black)), legend(off) title("Oil Prices", color(black)) xtitle("Month") graphregion(color(white)) plotregion(fcolor(white)) xlabel(0(10)60)
gr rename fig_wti,replace

gr combine fig_ffr fig_ipm fig_stock fig_wea fig_oildrill fig_wop fig_cpi fig_wti, graphregion(color(white)) plotregion(color(white)) note("Note: 68% confidence bands displayed",size(small))

graph export "figureH2.eps", replace
/* THE END */
