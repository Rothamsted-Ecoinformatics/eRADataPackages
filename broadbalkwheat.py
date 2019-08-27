'''
Created on 22 Aug 2017

@author: ostlerr
'''
from datapackage import Package

package = Package()
package.infer('Hackathon data/BroadbalkWheatData/broadbalkWheatData.csv')

package.descriptor['resources'][0]['schema']['fields'][0]['type']='year'
package.descriptor['resources'][0]['schema']['fields'][0]['description']='year of harvest'

package.descriptor['resources'][0]['schema']['fields'][1]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][1]['description']='the experiment strip'

package.descriptor['resources'][0]['schema']['fields'][2]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][2]['description']='the experiment section'

package.descriptor['resources'][0]['schema']['fields'][3]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][3]['description']='number of years since last non wheat crop    '

package.descriptor['resources'][0]['schema']['fields'][4]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][4]['description']='the previous years crop'

package.descriptor['resources'][0]['schema']['fields'][5]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][5]['description']='the wheat variety grown'

package.descriptor['resources'][0]['schema']['fields'][6]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][6]['description']='the fertilizer code - see columns for rates'

package.descriptor['resources'][0]['schema']['fields'][7]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][7]['description']='number of fertiliser applications, see fertilizer code for the rate ratio if multiple applications are applied.'

package.descriptor['resources'][0]['schema']['fields'][8]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][8]['description']='total kg N/ha applied'

package.descriptor['resources'][0]['schema']['fields'][9]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][9]['description']='total kg P/ha applied'

package.descriptor['resources'][0]['schema']['fields'][10]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][10]['description']='total kg K/ha applied'

package.descriptor['resources'][0]['schema']['fields'][11]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][11]['description']='total kg Mg/ha applied'

package.descriptor['resources'][0]['schema']['fields'][12]['type']='number,'
package.descriptor['resources'][0]['schema']['fields'][12]['description']='Amount of farmyard manure applied, tonnes/ha'

package.descriptor['resources'][0]['schema']['fields'][13]['type']='string'
package.descriptor['resources'][0]['schema']['fields'][13]['description']='notes'

package.descriptor['resources'][0]['schema']['fields'][14]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][14]['description']='Yield of total grain at 85% dry matter'

package.descriptor['resources'][0]['schema']['fields'][15]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][15]['description']='Yield of total straw at 85% dry matter'

package.descriptor['resources'][0]['schema']['fields'][16]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][16]['description']='Hagberg Falling Number in seconds'

package.descriptor['resources'][0]['schema']['fields'][17]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][17]['description']='Hectolitre weight of grain, kg/hl'

package.descriptor['resources'][0]['schema']['fields'][18]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][18]['description']='Thousand grain weight in grams'

package.descriptor['resources'][0]['schema']['fields'][19]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][19]['description']='% N in grain'

package.descriptor['resources'][0]['schema']['fields'][20]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][20]['description']='% N in straw'

package.descriptor['resources'][0]['schema']['fields'][21]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][21]['description']='% P in grain'

package.descriptor['resources'][0]['schema']['fields'][22]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][22]['description']='% P in straw'

package.descriptor['resources'][0]['schema']['fields'][23]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][23]['description']='% S in grain'

package.descriptor['resources'][0]['schema']['fields'][24]['type']='number'
package.descriptor['resources'][0]['schema']['fields'][24]['description']='% S in straw'

package.descriptor['description']='Winter wheat grain, nutrient and fertiliser data for continuous wheat (section 1) and first wheat in rotation (sections 2, 3, 4, 5, 7). Winter wheat varities selected primarily for their yield potential and also for breadmaking qualities. Herbicides and pesticides are applied as required, including spring and summer fungicides. The plots are regularly limed. grain and straw nutrients are no measured for every year. 2015 was sown to spring wheat and is not included'
package.descriptor['version']='1.0'

licence = {'name':'CC-BY-4.0','path':'https://creativecommons.org/licenses/by/4.0/','title':'Creative Commons Attribution 4.0 International'}
publisher = {'name':'Rothamsted Research'}
maintainer = {'name':'Richard Ostler','email':'richard.ostler@rothamsted.ac.uk'}
contributor = {'name':'Margaret Glending','email':'margaret.glendining@rothamsted.ac.uk'}
source = {'name':'Rothamsted electronic archive (e-RA)','web':'http://www.era.rothamsted.ac.uk/Broadbalk'}

package.descriptor['licenses']=[licence]
package.descriptor['publishers']=[publisher]
package.descriptor['maintainers']=[maintainer]
package.descriptor['contributors']=[contributor]
package.descriptor['sources']=[source]
package.descriptor['latitude']='51.809450'
package.descriptor['longitude']='-0.372898'
package.descriptor['altitude']='130'
package.descriptor['startYear']='1968'
package.descriptor['endYear']='2018'

package.commit()
package.valid
print('done')
package.save('broadbalkWheatData.zip')