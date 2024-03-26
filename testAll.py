import pickle

N=float(("90"))
P=float(("42"))
K=float(("43"))
temp=float(("20.7"))
Hum=float(("82"))
Ph=float(("6"))
Rain=float(("202"))

model=pickle.load(open("model.pkl",'rb'))
names = ["K-Nearest Neighbors", "SVM",
         "Decision Tree", "Random Forest",
         "Naive Bayes","ExtraTreesClassifier","VotingClassifier"]
for i in range(len(model)):
    print(names[i])
    test_prediction = model[i].predict([[N,P,K,temp,Hum,Ph,Rain]])
    print(test_prediction[0])