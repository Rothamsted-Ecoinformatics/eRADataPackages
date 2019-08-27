'''
Created on 22 Aug 2017

@author: ostlerr
'''
from datapackage import Package

package = Package()
package.infer('Hackathon data/BroadbalkChemistry/broadbalkNitrateLeachingData.csv')

package.descriptor['resources'][0]['schema']['fields'][0]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][0]['description']='Season'

package.descriptor['resources'][0]['schema']['fields'][1]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][1]['description']='Strip is the section 9 plot'

package.descriptor['resources'][0]['schema']['fields'][2]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][2]['description']='Fertilisers regime'

package.descriptor['resources'][0]['schema']['fields'][3]['type']='text'
package.descriptor['resources'][0]['schema']['fields'][3]['description']='N rate'

package.descriptor['resources'][0]['schema']['fields'][4]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][4]['description']='Farmyard manure rate'

package.descriptor['resources'][0]['schema']['fields'][5]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][5]['description']='N leached KgN/ha'

package.descriptor['resources'][0]['schema']['fields'][6]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][6]['description']='Rainfall in mm'

package.descriptor['resources'][0]['schema']['fields'][7]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][7]['description']='Rainfall difference from 30 year mean.'

package.descriptor['resources'][0]['schema']['fields'][8]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][8]['description']='through drainage'

package.descriptor['resources'][0]['schema']['fields'][9]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][9]['description']='through drainage difference from 30 year mean.'

package.descriptor['description']='roadbalk % Soil Organic Carbon, % Nitrogen and Olsen P (plant available P) in top-soil (0-23cm). Data are the means of all holes in each strip (up to 1944) and of all sections in 1966; and then of specific sections from 1966.'
package.descriptor['version']='1.0'

licence = {'name':'CC-BY-4.0','path':'https://creativecommons.org/licenses/by/4.0/','title':'Creative Commons Attribution 4.0 International'}
publisher = {'name':'Rothamsted Research'}
maintainer = {'name':'Richard Ostler','email':'richard.ostler@rothamsted.ac.uk'}
contributor = {'name':'Margaret Glending','email':'margaret.glendining@rothamsted.ac.uk'}
source = {'name':'Rothamsted electronic archive (e-RA)','web':'http://www.era.rothamsted.ac.uk/Broadbalk'}
notes = [{'noteId':'2','note':'Mean of those sections equivalent to modern (post-1968) Sections 1, 6 & 9 i.e. those sections in Continuous (or almost continuous) wheat; see cropping plans.'},
          {'noteId':'3','note':'Mean of Sections 1 & 9 only.'},
          {'noteId':'4','note':'Mean of Sections 1, 6 & 9.'},
          {'noteId':'5','note':'Mean of Sections 2, 3, 4, 5 & 7 (sampled in 1988, 1988, 1987, 1988 & 1987 respectively).'},
          {'noteId':'6','note':'Mean of Sections 2, 3, 4, 5 & 7 (sampled in 1996, 1996, 1993, 1994 & 1992 respectively)'},
          {'noteId':'7','note':'Mean of Sections 2, 3, 4, 5 & 7 (sampled in 2000)'},
          {'noteId':'8','note':'Mean of Sections 2, 3, 4, 5 & 7 (sampled in 2006, 2005, 2006, 2006 & 2006 respectively)'},
          {'noteId':'9','note':'mean of Sections 2, 3, 4, 5 & 7 (sampled in 2011, 2010, 2008, 2009 & 2012 respectively)'},
          {'noteId':'10','note':'Mean of  Sections 2, 3, 4, 5 & 7 i.e. those sections in rotations since 1968'},
          {'noteId':'11','note':'Mean of Sections 2, 3, 4 & 5  (sampled in 2016, 2015, 2013 & 2014 respectively)'},
          {'noteId':'','note':'Note that P was not applied to many plots from 2001 due to very high Olsen-P values'},
          {'noteId':'','note':'Continuous wheat data for plot 01 are from Section 6 only.'},
          {'noteId':'','note':'Note that strip 20 only extends over Sections 0 and 1.'}          
          ]

analysis = [{'method':'Analysis of air-dried soil ground to < 2mm'},
          {'method':'Selected treatments from 1881, 1893, 1914, 1936 and 1944 were re-analysed in 2001-4 for Total C and Total N by combustion (LECO) and for CaCO3-C by manometry'}, 
          {'method':'Organic C values given above are Total C minus CaCO3-C: all available holes (samples) from each treatment were re-analysed.'},
          {'method':'Data for 1865 are derived from original Soda Lime analyses (for Total N) and C:N ratios for 1893 (for Organic C): see 1865 data sheets'},
          {'method':'Data for 1966 are corrected Walkey-Black values for Organic C (W-B x 1.3 is equivalent to org C by Tinsley or total C by combustion minus CaCO3-C) and Kjeldahl for Total N.'},
          {'method':'Data for 1987/88 are Tinsley for Organic C and Kjeldahl for Total N.'},
          {'method':'C & N Data for 1992, 1997, 2000, 2005 are by combustion and manometry. '},
          {'method':'Selected treatments from 1881, 1893, 1914, 1936 and 1944 were analysed in 2001-4 for Olsen P; all available holes (samples) from each treatment were analysed.'}
            ]

package.descriptor['licenses']=[licence]
package.descriptor['publishers']=[publisher]
package.descriptor['maintainers']=[maintainer]
package.descriptor['contributors']=[contributor]
package.descriptor['sources']=[source]
package.descriptor['latitude']='51.809450'
package.descriptor['longitude']='-0.372898'
package.descriptor['altitude']='130'
package.descriptor['startYear']='1843'
package.descriptor['endYear']='2018'
package.descriptor['notes']=notes
package.descriptor['techicalInfo']=analysis


package.commit()
package.valid
print('done')
package.save('broadbalkSoilChemistryData.zip')