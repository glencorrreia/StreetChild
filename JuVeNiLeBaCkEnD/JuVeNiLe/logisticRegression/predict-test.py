from sklearn.externals import joblib





# test_data = [0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0] #output = 0  (Lost and Found)




test_data = [0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0] #output  = -1 (NGO)

'''
test_data = [
    0, # criminal-record
    0, # lost-found
    0, # Hinduism
    0, # Islam
    1, # Christianity
    0, # Sikhism
    0, # Buddhism
    0, # Jainism
    0, # Other religions
    1, # age (above 10 or not)
    0, # male
    0, # female
    0, # transgender
    0, # orphan
    1, # parents-earning
    1, # has-siblings
    0, # goes-to-school
    1, # child-labour
    0, # safe-area
    0, # INC
    0, # BJP
    0, # CPI
    0, # NCP
    1, #BSP
    0 #AITC
] #output = 1 (ORPHAN)

'''




def getPrediction():
    classifier = joblib.load('logisticR_final.pkl')
    result = classifier.predict([test_data])
    print(result)
    return result


getPrediction()
