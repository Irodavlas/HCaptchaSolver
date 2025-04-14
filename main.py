from flask import Flask, jsonify, request
from flask_cors import CORS
import handlers.cosineSimilarity
import handlers.numbers
import handlers.yesnoAnswering
from models import florence2,utils, bert, miniLM
import handlers
app = Flask(__name__)
CORS(app)
import asyncio

@app.route("/",methods=["POST"])
def solve_captcha():
    #image = "974ad16a3cfb36d5dc58c9e949c112cac5b579b7308f38751c8128f790036dc7.png"
    
    captcha_type = "yesno"
    challenge_prompt = "Click the numbers greater than the one shown in the picture"
    content = request.json
    images_path = []
    print(content.values()) 
    '''
    for key in content:
        images_path.append(utils.downloadImage(content[key])) #downloads and return the path to image
    '''
    #test 
    for key in content:
        images_path.append(content[key])
    #end test
    
    if captcha_type == "similarity":
        handler = handlers.cosineSimilarity.CosineSimilaritySolver(images_path[:-1], challenge_prompt, images_path[-1], captcha_type, Florence, MiniLM, 0.43)
        response = handler.solveChallenge()
    elif captcha_type == "numbers":
        handler = handlers.numbers.NumberSolver(images_path[:-1], challenge_prompt, images_path[-1], "number", Florence)
        response = handler.solveChallenge()
    elif captcha_type == "yesno":
        handler = handlers.yesnoAnswering.YesNowQuestionSolver(images_path[:-1], challenge_prompt, images_path[-1], "yesno", Florence, Bert)
        response = handler.solveChallenge()
    print(response)
    return jsonify(response)

    
if __name__ == "__main__":
    Florence = florence2.NewFlorence2Model() 
    Bert = bert.NewYesNoPredictor()
    MiniLM = miniLM.NewMiniLM()

    print("running:",app.run(port=4000))
