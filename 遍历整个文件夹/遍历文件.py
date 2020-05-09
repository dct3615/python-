# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('C:\\Users\\00124175\\Desktop\\python'):
    for filename in filenames:
        print(os.path.join(dirname, filename))