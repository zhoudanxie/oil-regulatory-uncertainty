clear

/* dataset used in VAR */
use data_2024

/* Set time variable */
tsset monthly

/*oil uncertainty journal based*/


/*Appendix E.2: oil uncertainty econ-adjusted*/
quiet var oilregunc2024econ logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var1, step(60) set(myirfrobust, replace)
quiet var oilregunc2024econ logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var2, step(60) 

/*Figures E.2.1 and E.2.2*/
set scheme s1color
irf graph oirf, irf(var1) impulse(oilregunc2024econ) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logprodoil) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureE21.eps", replace

irf graph oirf, irf(var2) impulse(oilregunc2024econ) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logdrill) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureE22.eps", replace


/*Appendix G.1: oil uncertainty ordered as the last variable*/
quiet var logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti oilregunc2024, lags(1/12) dfk small
irf create var1a, step(60) 
quiet var logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti oilregunc2024, lags(1/12) dfk small
irf create var2a, step(60) 

/*Figurs G.1.1 and G.1.2*/
irf graph oirf, irf(var1a) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logprodoil) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG11.eps", replace

irf graph oirf, irf(var2a) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logdrill) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG12.eps", replace


/*Appendix G.2: with 24 lags*/
quiet var oilregunc2024 logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti, lags(1/24) dfk small
irf create var1b, step(60)
quiet var oilregunc2024 logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti, lags(1/24) dfk small
irf create var2b, step(60) 

/*Figures G.2.1 and G.2.2*/
irf graph oirf, irf(var1b) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logprodoil) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG21.eps", replace

irf graph oirf, irf(var2b) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logdrill) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG22.eps", replace


/*Appendix G.3: with aggregate uncertainty*/
quiet var jurado oilregunc2024 logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var1c, step(60) 
quiet var jurado oilregunc2024 logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var2c, step(60) 

/*Figures G.3.1 and G.3.2*/
irf graph oirf, irf(var1c) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logprodoil) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG31.eps", replace

irf graph oirf, irf(var2c) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logdrill) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG32.eps", replace


/*Appendix G.4: with EPU*/
quiet var epu oilregunc2024 logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var1d, step(60)
quiet var epu oilregunc2024 logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var2d, step(60) 

/*Figures G.4.1 and G.4.2*/
irf graph oirf, irf(var1d) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logprodoil) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG41.eps", replace

irf graph oirf, irf(var2d) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logdrill) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG42.eps", replace


/*Appendix G.5: with EPU regulation*/
quiet var epureg oilregunc2024 logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var1e, step(60)
quiet var epureg oilregunc2024 logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var2e, step(60) 

/*Figures G.5.1 and G.5.2*/
irf graph oirf, irf(var1e) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logprodoil) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG51.eps", replace

irf graph oirf, irf(var2e) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logdrill) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG52.eps", replace


/*Appendix G.6: with CPU*/
quiet var cpu oilregunc2024 logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var1f, step(60)
quiet var cpu oilregunc2024 logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var2f, step(60) 

/*Figures G.6.1 and G.6.2*/
irf graph oirf, irf(var1f) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logprodoil) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG61.eps", replace

irf graph oirf, irf(var2f) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logdrill) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG62.eps", replace


/*Appendix G.7: with GPR*/
quiet var gpr oilregunc2024 logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var1g, step(60)
quiet var gpr oilregunc2024 logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var2g, step(60) 

/*Figures G.7.1 and G.7.2*/
irf graph oirf, irf(var1g) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logprodoil) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG71.eps", replace

irf graph oirf, irf(var2g) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logdrill) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureG72.eps", replace


/*Appendix E.1: oil uncertainty journal-based*/
quiet var oilregunc_journal logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var1h, step(60) 
quiet var oilregunc_journal logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var2h, step(60) 

/*Figures E.1.1 and E.1.2*/
irf graph oirf, irf(var1h) impulse(oilregunc_journal) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logprodoil) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureE11.eps", replace

irf graph oirf, irf(var2h) impulse(oilregunc_journal) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logdrill) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figureE12.eps", replace

/*subtitle("Federal Funds Rate" "Price Level" "Industrial Production" "World Oil Production" "World Economic Activity" "S&P 500 Index" "Oil Prices" "U.S. Oil Production")