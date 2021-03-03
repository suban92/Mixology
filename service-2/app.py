from flask import Flask, Response, request
import random
app = Flask(__name__)

@app.route('/spirit', methods=['GET'])
def spirit():
    spirit = ("vodka", "gin", "rum", "whiskey", "cognac", "Tequila","Jenever", "liquers")
    return Response(random.choices(spirit), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
 


#@app.route('/mixer', methods=['POST'])
#def mixer():
 #   mixer = request.data.decode('UTF-8')
  #  if spirit == "whiskey":
   #     mixer = "cola"
    #elif spirit == "vodka":
    #    mixer = "redbull"
    #elif spirit == "gin":
    #    mixer = "lemonade"
    #else:  spirit == "rum":
     #   mixer = "coke"
    #return  Response(noise, mimetype= "text/plain")
#@app.route('/mixer', methods=['GET'])
#def mixer():
#    mixer = ("schweppes tonic water", "redbull","coca-cola", "ginger ale", "bitter lemonade", "orange soda", "appletizer")
#    return Response(random.choices(mixer), mimetype="text ")

if __name__ == "__main__":  
    app.run(debug=True, host='0.0.0.0', port=5001)