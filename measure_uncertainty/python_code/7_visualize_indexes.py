import pandas as pd
import os
import numpy as np
from datetime import datetime

# Plotting Packages
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino Linotype']})

import matplotlib
matplotlib.use('TkAgg')

colors=['#033C5A','#AA9868','#0190DB','#FFC72C','#A75523','#008364','#78BE20','#C9102F',
        '#033C5A','#AA9868','#0190DB','#FFC72C','#A75523','#008364','#78BE20','#C9102F']

# %%
# Get directory
directory=os.path.dirname(os.path.realpath(__file__))

# %%
# Create output folder if not existing
output_path=f'{directory}/../output'
if not os.path.exists(output_path):
        os.makedirs(output_path)
else:
        pass

#%%---------------------------------------------------------------------------------------------------------------------
#---------------------------------------Plot Oil Regulatory Uncertainty Index-------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# Oil regulatory uncertainty index
regIndex=pd.read_csv(f'{directory}/../data/oil_regulatory_uncertainty_index.csv')

regIndex['Year-Month']=regIndex['Year'].map(str)+'-'+regIndex['Month'].map(str)
regIndex['date']=regIndex['Year-Month'].astype('datetime64[ns]').dt.date

# Rolling mean
regIndex['RegUncertaintyIndexMean'] = regIndex['RegUncertaintyIndex'].rolling(window=12,center=True).mean()
# print(regIndex.head())

#%%-----------------------------------------------------------------------------------------------------------------------
# Plot monthly uncertainty index with rolling mean
x=regIndex['date']
y1=regIndex['RegUncertaintyIndex']
y2=regIndex['RegUncertaintyIndexMean']

fig, ax = plt.subplots(1, figsize=(16,9))
ax.plot(x,y1,color="#808080",label='Oil Regulatory Uncertainty Index')
ax.plot(x,y2,color="black",linewidth=2.5,linestyle='dashed',label='12-Month Rolling Mean')

# events
ax.axvspan(datetime(1990,6,1),datetime(1991,4,1),alpha=0.1, lw=0, color='#0000FF')
ax.axvspan(datetime(1995,2,1),datetime(1995,11,1),alpha=0.1, lw=0, color='#0000FF')
ax.axvspan(datetime(2001,6,1),datetime(2001,11,1),alpha=0.1, lw=0, color='#0000FF')
ax.axvspan(datetime(2004,7,1),datetime(2006,2,1),alpha=0.1, lw=0, color='#0000FF')
ax.axvspan(datetime(2008,4,1),datetime(2011,5,1),alpha=0.1, lw=0, color='#0000FF')
ax.axvspan(datetime(2016,2,1),datetime(2016,11,1),alpha=0.1, lw=0, color='#0000FF')

ax.text(datetime(1989,7,1), 1.08, 'Natural Gas Wellhead\nDecontrol Act of 1989',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(1990,1,1), 1.15, 'Natural Gas Market\nDeregulation (1978-1992)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(1990,11,1), 1, 'Clean Air Act\nAmendments of 1990',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(1992,10,1), 0.96, 'Energy Policy Act of 1992',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(1996,1,1), 1.03, 'Electricity Market\nDeregulation (1992-1999)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2001,7,1), 0.92, 'California Energy\nCrisis (2000-2001)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2001,9,1), 1, '9/11\n(2001)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2005,3,1), 0.85, 'Clean Air Interstate\nRule (2005)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2005,8,1), 1.07, 'Energy Policy Act of 2005',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2005,12,1), 0.98, 'Regional Greenhouse\nGas Initiative\nMemorandum (2005)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2007,4,1), 1.17, 'Massachusetts\nv. EPA (2007)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2009,2,1), 0.9, 'American Recovery\nand Reinvestment\nAct of 2009',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2009,12,1), 1.1, 'EPA’s GHG Endangerment\nFinding (2009)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2011,12,1), 1, 'Mercury and Air\nToxics Standards (2011)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2015,8,1), 1.05, 'Clean Power Plan\n(2015)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2016,9,1), 0.95, 'U.S. Joining the\nParis Agreement (2016)',
        fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2020,11,1), 0.85, '2020 Presidential\nElection',
        fontsize=12,horizontalalignment='center',color='#0000FF')

# format the ticks
years = mdates.YearLocator(2)   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y-%m')

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)

# round to nearest years.
datemin = np.datetime64(x.iloc[0], 'Y')
datemax = np.datetime64(x.iloc[-1], 'Y') + np.timedelta64(1, 'Y')
ax.set_xlim(datemin, datemax)

# format the coords message box
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = lambda x: '$%1.2f' % x
fig.autofmt_xdate()

# Set tick and label format
ax.tick_params(axis='both',which='major',labelsize=14,color='#9a9a9a')
ax.set_ylabel('Oil Regulatory Uncertainty',fontsize=16)
ax.set_yticks(np.arange(round(min(y1),1)-0.4,round(max(y1),1)+0.4,0.1))
ax.set_ylim(bottom=round(min(y1),1)-0.1)

# Borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#9a9a9a')
ax.spines['bottom'].set_color('#9a9a9a')

# Legend
fig.legend(loc='lower center', ncol=2, fontsize=16)
fig.subplots_adjust(bottom=0.15)

plt.savefig(f'{directory}/../output/figure1.jpg', bbox_inches='tight')
plt.close()
print(f'Figure 1 saved in /measure_uncertainty/output.')

#%%-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------Plot Oil Supply Uncertainty Index----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# Oil supply uncertainty index
monthlyIndex=pd.read_csv(f'{directory}/../data/oil_supply_uncertainty_index.csv')

monthlyIndex['Year-Month']=monthlyIndex['Year'].map(str)+'-'+monthlyIndex['Month'].map(str)
monthlyIndex['date']=monthlyIndex['Year-Month'].astype('datetime64[ns]').dt.date

monthlyIndex['UncertaintyIndexMean'] = monthlyIndex['UncertaintyIndex'].rolling(window=12,center=True).mean()
# print(monthlyIndex.head())

#%%-----------------------------------------------------------------------------------------------------------------------
# Plot monthly uncertainty index with rolling mean
x=monthlyIndex['date']
y1=monthlyIndex['UncertaintyIndex']
y2=monthlyIndex['UncertaintyIndexMean']

fig, ax = plt.subplots(1, figsize=(16,9))
ax.plot(x,y1,color="#808080",label='Oil Supply Uncertainty Index')
ax.plot(x,y2,color="black",linewidth=2.5,linestyle='dashed',label='12-Month Rolling Mean')

# events
ax.axvspan(datetime(1989,3,31),datetime(1989,4,30),alpha=0.1,lw=0, color='#0000FF')
ax.text(datetime(1989,3,1), 0.78, 'Exxon Valdez\nOil Spill\n(1989)', fontsize=12,horizontalalignment='center',color='#0000FF')

ax.axvspan(datetime(1990,7,31),datetime(1991,1,31),alpha=0.1,lw=0, color='#0000FF')
ax.text(datetime(1990,11,1), 0.85, 'First Gulf War\n(1990-1991)', fontsize=12,horizontalalignment='center',color='#0000FF')

ax.axvspan(datetime(2003,2,28),datetime(2003,6,30),alpha=0.1,lw=0, color='#0000FF')
ax.text(datetime(2003,2,1), 0.73, 'Venezuela General\nStrike (2002-2003)', fontsize=12,horizontalalignment='center',color='#0000FF')
ax.text(datetime(2003,3,1), 0.77, 'Beginning of\nSecond Gulf War (2003-2011)', fontsize=12,horizontalalignment='center',color='#0000FF')

ax.axvspan(datetime(2004,5,31),datetime(2004,8,31),alpha=0.1,lw=0, color='#0000FF')
ax.text(datetime(2004,9,1), 0.84, 'Atlantic Hurricanes\n(2004)', fontsize=12,horizontalalignment='center',color='#0000FF')

ax.axvspan(datetime(2005,8,31),datetime(2005,9,30),alpha=0.1,lw=0, color='#0000FF')
ax.text(datetime(2005,8,1), 0.8, 'Hurricane Katrina\n(2005)', fontsize=12,horizontalalignment='center',color='#0000FF')

ax.text(datetime(2008,1,1), 0.88, 'Shale Revolution (2005-2010)', fontsize=12,horizontalalignment='center',color='#0000FF')

ax.axvspan(datetime(2008,5,31),datetime(2008,6,30),alpha=0.1,lw=0, color='#0000FF')
ax.text(datetime(2008,6,1), 0.7, 'Oil Price Peak\n(2008)', fontsize=12,horizontalalignment='center',color='#0000FF')

ax.axvspan(datetime(2010,4,30),datetime(2010,5,31),alpha=0.1,lw=0, color='#0000FF')
ax.text(datetime(2010,4,1), 0.77, 'Deepwater Horizon\nOil Spill (2010)', fontsize=12,horizontalalignment='center',color='#0000FF')

ax.axvspan(datetime(2020,3,31),datetime(2020,4,30),alpha=0.1,lw=0, color='#0000FF')
ax.text(datetime(2020,4,1), 0.7, 'COVID-19 Outbreak\nin the US (2020)', fontsize=12,horizontalalignment='center',color='#0000FF')

# format the ticks
years = mdates.YearLocator(2)   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y-%m')

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
# ax.xaxis.set_minor_locator(months)

# round to nearest years.
datemin = np.datetime64(monthlyIndex['date'].iloc[0], 'Y')
datemax = np.datetime64(monthlyIndex['date'].iloc[-1], 'Y') + np.timedelta64(1, 'Y')
ax.set_xlim(datemin, datemax)

# format the coords message box
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = lambda x: '$%1.2f' % x
fig.autofmt_xdate()

# Set tick and label format
ax.tick_params(axis='both',which='major',labelsize=14,color='#9a9a9a')
ax.set_ylabel('Oil Supply Uncertainty',fontsize=16)
ax.set_yticks(np.arange(round(min(y1),1)-0.1,round(max(y1),1)+0.3,0.1))
ax.set_ylim(bottom=round(min(y1),1)-0.1)

# Borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#9a9a9a')
ax.spines['bottom'].set_color('#9a9a9a')

# Legend
fig.legend(loc='lower center', ncol=2, fontsize=16)
fig.subplots_adjust(bottom=0.15)

plt.savefig(f'{directory}/../output/figure3.jpg', bbox_inches='tight')
plt.close()
print(f'Figure 3 saved in /measure_uncertainty/output.')

#%% -----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------Compare with journal-based measure--------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

#%% Function to standardize index
def normalize_data(data_col):
        data_col_std =(data_col - data_col.mean()) / data_col.std()
        return data_col_std

#%% Journal-based measure
regIndex['RegUncertaintyIndexMean_Journal'] = regIndex['RegUncertaintyIndex_Journal'].rolling(window=12,center=True).mean()

#%% Plot
regIndex2=regIndex[regIndex['RegUncertaintyIndex_Journal'].notnull()]

x=regIndex2['date']
y1=normalize_data(regIndex2['RegUncertaintyIndex'])
y2=y1.rolling(window=12,center=True).mean()
y3=normalize_data(regIndex2['RegUncertaintyIndex_Journal'])
y4=y3.rolling(window=12,center=True).mean()

fig, ax = plt.subplots(1, figsize=(16,9))
ax.plot(x,y1,color="#808080",label='Oil Regulatory Uncertainty Index')
ax.plot(x,y2,color="black",linewidth=2.5,linestyle='dashed',label='12-Month Rolling Mean (Baseline)')
ax.plot(x,y3,color="#6699CC",label='Journal-based Oil Regulatory Uncertainty Index')
ax.plot(x,y4,color="#0000FF",linewidth=2.5,linestyle='dashed',label='12-Month Rolling Mean (Journal-based)')

# Shading
ax.axvspan(datetime(1995,2,1),datetime(1995,11,1),alpha=0.1, lw=0, color='#0000FF')
ax.axvspan(datetime(2001,6,1),datetime(2001,11,1),alpha=0.1, lw=0, color='#0000FF')
ax.axvspan(datetime(2004,7,1),datetime(2006,2,1),alpha=0.1, lw=0, color='#0000FF')
ax.axvspan(datetime(2008,4,1),datetime(2011,5,1),alpha=0.1, lw=0, color='#0000FF')
ax.axvspan(datetime(2016,2,1),datetime(2016,11,1),alpha=0.1, lw=0, color='#0000FF')

# format the ticks
years = mdates.YearLocator(2)   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y-%m')

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)

# round to nearest years.
datemin = np.datetime64(x.iloc[0], 'Y')
datemax = np.datetime64(x.iloc[-1], 'Y') + np.timedelta64(1, 'Y')
ax.set_xlim(datemin, datemax)

# format the coords message box
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = lambda x: '$%1.2f' % x
fig.autofmt_xdate()

# Set tick and label format
ax.tick_params(axis='both',which='major',labelsize=14,color='#9a9a9a')
ax.set_ylabel('Standard Deviations',fontsize=16)
ax.set_yticks(np.arange(-4,5,1))

# Borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#9a9a9a')
ax.spines['bottom'].set_color('#9a9a9a')

# Legend
fig.legend(loc='lower center', ncol=2, fontsize=16)
fig.subplots_adjust(bottom=0.2)

plt.savefig(f'{directory}/../output/appendixC.jpg', bbox_inches='tight')
plt.close()
print(f'Appendix C saved in /measure_uncertainty/output.')

#%% -----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------Compare with other measures----------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

#%% Other indexes
# Climate policy uncertainty index
df_cpu=pd.read_csv(f"{directory}/../data/supplementary_data/cpu_index.csv",skiprows=4)
df_cpu['Year-Month']=[datetime.strptime(x,'%b-%y').strftime('%Y-%m') for x in df_cpu['date']]
df_cpu['Year']=df_cpu['Year-Month'].astype('datetime64[ns]').dt.year
df_cpu['Month']=df_cpu['Year-Month'].astype('datetime64[ns]').dt.month
# Merge
regIndex=regIndex.merge(df_cpu[['Year','Month','cpu_index']],on=['Year','Month'],how='left')

# EPU Regulation index
df_repu=pd.read_excel(f"{directory}/../data/supplementary_data/categorical_epu_index.xlsx")
df_repu=df_repu[df_repu['Month'].notnull()][['Year','Month','8. Regulation']].\
        rename(columns={'8. Regulation':'REPU'})
# Merge
regIndex=regIndex.merge(df_repu,on=['Year','Month'],how='left')

# Geopolitical risk index
df_gpr=pd.read_excel(f"{directory}/../data/supplementary_data/gpr_index.xls")
df_gpr=df_gpr[['month','GPR']]
df_gpr['Year']=df_gpr['month'].astype('datetime64[ns]').dt.year
df_gpr['Month']=df_gpr['month'].astype('datetime64[ns]').dt.month
# Merge
regIndex=regIndex.merge(df_gpr,on=['Year','Month'],how='left')

# Merge with oil supply uncertainty index
regIndex=regIndex.merge(monthlyIndex[['Year','Month','UncertaintyIndex']],on=['Year','Month'],how='left')

#%% Plot all indexes
def plot_subplot(ax,x,y1,y2,y_label,y_color="#0000FF"):
        ax.plot(x, y1, color="black", linewidth=1, label='Oil Regulatory Uncertainty Index')
        ax.plot(x, y2, color=y_color, linewidth=1, label=y_label)

        # format the ticks
        years = mdates.YearLocator(2)  # every year
        months = mdates.MonthLocator()  # every month
        years_fmt = mdates.DateFormatter('%Y-%m')

        datemin = np.datetime64(x.iloc[0], 'Y')
        datemax = np.datetime64(x.iloc[-1], 'Y') + np.timedelta64(1, 'Y')

        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(years_fmt)

        # round to nearest years
        ax.set_xlim(datemin, datemax)

        # Set tick and label format
        ax.tick_params(axis='both', which='major', labelsize=11, color='#9a9a9a')
        ax.tick_params(axis='x', rotation=30)
        ax.set_yticks(np.arange(-2,10,2))
        ax.set_ylabel('Standard Deviations', fontsize=12)
        ax.tick_params(labelbottom=True)

        # Borders
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#9a9a9a')
        ax.spines['bottom'].set_color('#9a9a9a')

        # Legend
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=12)

        return

# Plot
fig, axes = plt.subplots(3, 1, figsize=(10,15),
                         sharex=False, sharey=False
                         )

x = regIndex['date']
y1=normalize_data(regIndex['RegUncertaintyIndex'])

y_vars=['REPU','GPR','cpu_index']
y_labels=['Economic Policy Uncertainty Index: Regulation',
          'Geopolitical Risk Index',
          'Climate Policy Uncertainty Index']
y_colors=["#0000FF","#F400A1","#FF4500"]

for i, ax in enumerate(axes.flatten()):
        y2 = normalize_data(regIndex[y_vars[i]])
        plot_subplot(ax,x, y1, y2, y_labels[i],y_colors[i])

# Add events to subplot 1
axes[0].axvspan(datetime(1990,11,1),datetime(1990,12,1),alpha=0.5, color='#d3d3d3')
axes[0].text(datetime(1990,11,1), 6.5, '1990 CAA\nAmendments',
        fontsize=9,horizontalalignment='center',color='#0000FF')

axes[0].axvspan(datetime(1991,1,1),datetime(1991,2,1),alpha=0.5, color='#d3d3d3')
axes[0].text(datetime(1991,1,1), 5, 'Gulf War I', fontsize=9, color=y_colors[0],horizontalalignment='center')

axes[0].axvspan(datetime(2001,9,1),datetime(2001,10,1),alpha=0.5, color='#d3d3d3')
axes[0].text(datetime(2001,9,1), 2.2, '9/11', fontsize=9, color=y_colors[0],horizontalalignment='center')

axes[0].axvspan(datetime(2008,9,1),datetime(2008,10,1),alpha=0.5, color='#d3d3d3')
axes[0].text(datetime(2008,9,1), 4.2, 'Lehman\nBrothers', fontsize=9, color=y_colors[0],horizontalalignment='center')

axes[0].axvspan(datetime(2010,3,1),datetime(2010,4,1),alpha=0.5, color='#d3d3d3')
axes[0].text(datetime(2010,3,1), 5.7, 'Obamacare', fontsize=9, color=y_colors[0],horizontalalignment='center')

axes[0].axvspan(datetime(2010,4,1),datetime(2010,5,1),alpha=0.5, color='#d3d3d3')
axes[0].text(datetime(2010,4,1), 6.5, 'Deepwater Horizon', fontsize=9, color=y_colors[0],horizontalalignment='center')

axes[0].axvspan(datetime(2010,7,1),datetime(2010,8,1),alpha=0.5, color='#d3d3d3')
axes[0].text(datetime(2010,7,1), 7.2, 'Dodd-Frank', fontsize=9, color=y_colors[0],horizontalalignment='center')

axes[0].axvspan(datetime(2011,8,1),datetime(2011,9,1),alpha=0.5, color='#d3d3d3')
axes[0].text(datetime(2011,9,1), 4, 'Debt\nCeiling\nDispute', fontsize=9, color=y_colors[0],horizontalalignment='center')

axes[0].axvspan(datetime(2016,11,1),datetime(2016,12,1),alpha=0.5, color='#d3d3d3')
axes[0].text(datetime(2016,11,1),3, '2016 Presidential\nElection', fontsize=9, color=y_colors[0],horizontalalignment='center')

axes[0].axvspan(datetime(2020,3,1),datetime(2020,4,1),alpha=0.5, color='#d3d3d3')
axes[0].text(datetime(2020,1,1), 4.7, 'Coronavirus\nOutbreak', fontsize=9, color=y_colors[0],horizontalalignment='center')

# Add events to subplot 2
axes[1].axvspan(datetime(1991,1,1),datetime(1991,2,1),alpha=0.5, color='#d3d3d3')
axes[1].text(datetime(1991,1,1), 7, 'Gulf War I', fontsize=9, color=y_colors[1],horizontalalignment='center')

axes[1].axvspan(datetime(2001,9,1),datetime(2001,10,1),alpha=0.5, color='#d3d3d3')
axes[1].text(datetime(2001,9,1), 9, '9/11',fontsize=9,color=y_colors[1],horizontalalignment='center')

axes[1].axvspan(datetime(2003,3,1),datetime(2003,4,1),alpha=0.5, color='#d3d3d3')
axes[1].text(datetime(2003,3,1), 6, 'Gulf War II', fontsize=9,color=y_colors[1],horizontalalignment='center')

# Add events to subplot 3
axes[2].axvspan(datetime(2016,11,1),datetime(2016,12,1),alpha=0.5, color='#d3d3d3')
axes[2].text(datetime(2016,11,1),4, '2016\nPresidential\nElection', fontsize=9, color=y_colors[2],horizontalalignment='center')

axes[2].axvspan(datetime(2020,11,1),datetime(2020,12,1),alpha=0.5, color='#d3d3d3')
axes[2].text(datetime(2020,11,1), 5, '2020\nPresidential\nElection',fontsize=9,horizontalalignment='center',color=y_colors[2])

axes[2].axvspan(datetime(2019,9,1),datetime(2019,10,1),alpha=0.5, color='#d3d3d3')
axes[2].text(datetime(2019,9,1), 6.7, 'UN Climate\nAction Summit',fontsize=9,horizontalalignment='center',color=y_colors[2])

axes[2].axvspan(datetime(2021,11,1),datetime(2021,12,1),alpha=0.5, color='#d3d3d3')
axes[2].text(datetime(2021,11,1),7.7, 'COP26',fontsize=9,horizontalalignment='center',color=y_colors[2])

# Save plot
plt.subplots_adjust(hspace=0.4)

plt.savefig(f'{directory}/../output/appendixD.jpg',bbox_inches='tight')
plt.close()
print(f'Appendix D saved in /measure_uncertainty/output.')