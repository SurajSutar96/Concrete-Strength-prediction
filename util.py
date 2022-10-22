import numpy as np
import pickle
import json

class ConcreteStrength():
    def __init__(self,a,b,c,d,e,f,g,h):
        self.Cement=a
        self.Blast_Furnace_Slag=b
        self.Fly_Ash=c
        self.Water=d
        self.Superplasticizer=e
        self.Coarse_Aggregate=f
        self.Fine_Aggregate=g
        self.Age=h
    def data(self):
        with open("concrete_strenth_model.pkl",'rb')as f:
            self.model=pickle.load(f)
        with open("concrete_strenth_data.json",'r')as f:
            self.data=json.load(f)
    def predict(self):
        self.data()
        array=np.zeros(len(self.data['Columns']))
        array[0]=self.Cement
        array[1]=self.Blast_Furnace_Slag
        array[2]=self.Fly_Ash
        array[3]=self.Water
        array[4]=self.Superplasticizer
        array[5]=self.Coarse_Aggregate
        array[6]=self.Fine_Aggregate
        array[7]=self.Age
        pred=self.model.predict([array])[0].round(2)
        print("Predicted Strength of concrete is:-",pred)
        return pred
if __name__=="__main__":
    Cement=540.0
    Blast_Furnace_Slag=2
    Fly_Ash=1
    Water=162.0
    Superplasticizer=2.5
    Coarse_Aggregate=1040.0
    Fine_Aggregate=676.0
    Age=111.0
    obj=ConcreteStrength(Cement,Blast_Furnace_Slag,Fly_Ash,Water,Superplasticizer,Coarse_Aggregate,Fine_Aggregate,Age)
    obj.predict()
