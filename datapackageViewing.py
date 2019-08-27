'''
Created on 22 Aug 2017

@author: ostlerr
'''
from datapackage import Package, Profile

package = Package('dp3.zip')
package.get_resource('parkgrass-species').table.read(keyed=True)
print(package.get_resource('parkgrass-species').table.read(keyed=True))


