'''
This scipt save the feature vectors into a file.

mari wahl @ 2014
'''

import time



def save_feature(path_to_output, feature_value, feature_name):
    ''' 
       Save the feature vectors into a output file.
    '''
    file_feature = open(path_to_output, 'a')
    file_feature.write(feature_name + ': ')
    file_feature.write(feature_value + '\n') 
    file_feature.close()

