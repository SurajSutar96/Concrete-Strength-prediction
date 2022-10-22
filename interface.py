from flask import Flask,jsonify,request,render_template
from util import ConcreteStrength

app=Flask(__name__)

@app.route('/')
def main():
    return jsonify({'Home':"We are at home page"})

@app.route('/Concrete_strength')
def base():
    data=request.form
    Cement=data['Cement']
    Blast_Furnace_Slag=data['Blast_Furnace_Slag']
    Fly_Ash=data['Fly_Ash']
    Water=data['Water']
    Superplasticizer=data['Superplasticizer']
    Coarse_Aggregate=data['Coarse_Aggregate']
    Fine_Aggregate=data['Fine_Aggregate']
    Age=data['Age']
    pred=ConcreteStrength(Cement,Blast_Furnace_Slag,Fly_Ash,Water,Superplasticizer,Coarse_Aggregate,Fine_Aggregate,Age)
    prediction=pred.predict()
    return jsonify({"OutPut":f"Predicted Strength of Concrete is {prediction} kn/sqm"})
if __name__=="__main__":
    app.run(port='3333',debug=True)
