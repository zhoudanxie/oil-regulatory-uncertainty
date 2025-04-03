clear

/* dataset used in VAR */
use data_2024

/* Set time variable */
tsset monthly

/*dummy variable dum=1 when republicns are in power*/
gen dummyoilregunc2024 = dum*oilregunc2024
gen dum1=1-dum
gen dummy1oilregunc2024 = dum1*oilregunc2024

/*baseline*/
/*oil regulatory uncertainty with oil production*/
quiet var oilregunc2024 logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var1, step(60) set(myirf, replace)
/*oil regulatory uncertainty with oil drilling*/
quiet var oilregunc2024 logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var2, step(60) 

/*plotting figures*/
set scheme s1color

/* Figure 5: with Oil Production */
irf graph oirf, irf(var1) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logprodoil) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figure5.eps", replace

/* Figure 6: with Oil Drilling */
irf graph oirf, irf(var2) impulse(oilregunc2024) response(ffr logcpi logipm logworldprodoil kilianindex_100 logstock logrwti logdrill) level(68) yline(0,lcolor(black)) xlabel(0(10)60) byopts(yrescale) plotregion(fcolor(white)) graphregion(color(white)) subtitle(, nobexpand nobox fcolor(white)) byopts(colfirst legend(off) ixaxes ixtitle) plot1opts(lcolor(black)) xtitle(Month)
graph export "figure6.eps", replace


/*different political*/
quiet var dum dummyoilregunc2024 dummy1oilregunc2024 logstock ffr logcpi logprodoil logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var3, step(60)
quiet var dum dummyoilregunc2024 dummy1oilregunc2024 logstock ffr logcpi logdrill logipm logworldprodoil kilianindex_100 logrwti, lags(1/12) dfk small
irf create var4, step(60)

/* Figure 7: under Different Political Parties*/
irf cgraph (var3 dummyoilregunc2024 logprodoil oirf,subtitle("Under Republications") lc(black) lw(medthick) ysc(r(0.01 -0.01))) (var3 dummy1oilregunc2024 logprodoil oirf,subtitle("Under Democrats") lc(black) lw(medthick) ysc(r(0.01 -0.01))),level(68) xlabel(0(10)60) legend(off) xtitle(Month) iscale(.45)
graph export "figure7a.eps", replace
irf cgraph (var4 dummyoilregunc2024 logdrill oirf,subtitle("Under Republications") lc(black) lw(medthick) ysc(r(0.04 -0.04))) (var4 dummy1oilregunc2024 logdrill oirf,subtitle("Under Democrats") lc(black) lw(medthick) ysc(r(0.04 -0.04))),level(68) xlabel(0(10)60) legend(off) xtitle(Month) iscale(.45)
graph export "figure7b.eps", replace


/*with state unemployment*/
quiet var oilregunc2024 logstock ffr logcpi logprodoil logipm logrwti caur, lags(1/12) dfk small
irf create var5, step(60) 
quiet var oilregunc2024 logstock ffr logcpi logprodoil logipm logrwti nyur, lags(1/12) dfk small
irf create var6, step(60) 
quiet var oilregunc2024 logstock ffr logcpi logprodoil logipm logrwti txur, lags(1/12) dfk small
irf create var7, step(60) 
quiet var oilregunc2024 logstock ffr logcpi logprodoil logipm logrwti nmur, lags(1/12) dfk small
irf create var8, step(60) 

/*Figure 8: state effects*/
irf cgraph (var5 oilregunc2024 caur oirf,subtitle("CA Unemployment to Oil Reg U") lc(black) lw(medthick) ysc(r(0.1 -0.1))) (var6 oilregunc2024 nyur oirf,subtitle("NY Unemployment to Oil Reg U") lc(black) lw(medthick) ysc(r(0.1 -0.1))) (var7 oilregunc2024 txur oirf,subtitle("TX Unemployment to Oil Reg U") lc(black) lw(medthick) ysc(r(0.1 -0.1))) (var8 oilregunc2024 nmur oirf,subtitle("NM Unemployment to Oil Reg U") lc(black) lw(medthick) ysc(r(0.1 -0.1))),level(68) xlabel(0(10)60) legend(off) xtitle(Month) iscale(.45)
graph export "figure8.eps", replace