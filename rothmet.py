'''
Created on 22 Aug 2017

@author: ostlerr
'''
from datapackage import Package

package = Package()


#package.descriptor['licenses'][0]['name']='CC-BY-4.0'
#package.descriptor['licenses'][0]['path']='https://creativecommons.org/licenses/by/4.0/'
#package.descriptor['licenses'][0]['title']='Creative Commons Attribution 4.0 International'
#package.descriptor['publishers'][0]='Rothamsted Research'
#package.descriptor['maintainers'][0]['name']='Richard Ostler'
#package.descriptor['maintainers'][0]['email']='richard.ostler@rothamsted.ac.uk'
#package.descriptor['sources'][0]['name']='Rothamsted electronic archive (e-RA)'
#package.descriptor['sources'][0]['web']='http://www.era.rothamsted.ac.uk'
#package.descriptor['location']='s'
#package.descriptor['location']['latitude']='51.806720'
#package.descriptor['location']['longitude']='-0.360120'
#package.descriptor['location']['altitude']='128'
#package.descriptor['temporalCoverage']['startYear']='1968'


package.infer('Hackathon data/rothmet/Rothmet.csv')

package.descriptor['resources'][0]['schema']['fields'][0]['type']='date'
package.descriptor['resources'][0]['schema']['fields'][0]['description']='observation date'

package.descriptor['resources'][0]['schema']['fields'][1]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][1]['description']='daily maximum temperature in degrees celsius'

package.descriptor['resources'][0]['schema']['fields'][2]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][2]['description']='daily minimum temperature in degrees celsius'

package.descriptor['resources'][0]['schema']['fields'][3]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][3]['description']='rainfall from original 5 inch guage, in mm'

package.descriptor['resources'][0]['schema']['fields'][4]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][4]['description']='daily hours of sunshine'

package.descriptor['resources'][0]['schema']['fields'][5]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][5]['description']='Run of wind 0900 to 0900 GMT at 2m in km'

package.descriptor['resources'][0]['schema']['fields'][6]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][6]['description']='dry bulb temperature in degrees celsius'

package.descriptor['resources'][0]['schema']['fields'][7]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][7]['description']='wet bulb temperature in degrees celsius'

package.descriptor['resources'][0]['schema']['fields'][8]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][8]['description']='total daily solar radiation in J/cm2'

package.descriptor['resources'][0]['schema']['fields'][9]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][9]['description']='Relative humidity at 0900 GMT derived from dry and wet bulb until 2013 in %'

package.descriptor['resources'][0]['schema']['fields'][10]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][10]['description']='grass minimum temperature in degrees celsius'

package.descriptor['resources'][0]['schema']['fields'][11]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][11]['description']='soil temperature under grass at 10cm in degrees celsius'

package.descriptor['resources'][0]['schema']['fields'][12]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][12]['description']='soil temperature under grass at 20cm in degrees celsius'

package.descriptor['resources'][0]['schema']['fields'][13]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][13]['description']='soil temperature under bare soil at 10cm in degrees celsius'

package.descriptor['resources'][0]['schema']['fields'][14]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][14]['description']='soil temperature under bare soil at 20cm in degrees celsius'

package.descriptor['description']='Daily weather data from the Rothamsted Met station, 1968 to 2018. Prepared for Agri-tech East Hackathon, Cambridge, 5-7 July 2019.'
package.descriptor['version']='1.0'

licence = {'name':'CC-BY-4.0','path':'https://creativecommons.org/licenses/by/4.0/','title':'Creative Commons Attribution 4.0 International'}
publisher = {'name':'Rothamsted Research'}
maintainer = {'name':'Richard Ostler','email':'richard.ostler@rothamsted.ac.uk'}

source = {'name':'Rothamsted electronic archive (e-RA)','web':'http://www.era.rothamsted.ac.uk/Met'}

package.descriptor['licenses']=[licence]
package.descriptor['publishers']=[publisher]
package.descriptor['maintainers']=[maintainer]
package.descriptor['sources']=[source]
package.descriptor['latitude']='51.806720'
package.descriptor['longitude']='-0.360120'
package.descriptor['altitude']='128'
package.descriptor['startYear']='1968'
package.descriptor['endYear']='2018'

package.commit()
package.valid
print('done')
package.save('rothmetData.zip')