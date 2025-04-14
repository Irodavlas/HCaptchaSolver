from handlers import solver
from models import florence2, bert
from models import utils
class YesNowQuestionSolver(solver.NewCaptchaSolver):
    
    def __init__(self, images_path, challenge_prompt, challenge_image_path, captcha_type, model: florence2.NewFlorence2Model, question_model: bert.NewYesNoPredictor):
        super().__init__(images_path, challenge_prompt, challenge_image_path, captcha_type)
        self.model = model
        self.question_model = question_model
    def solveChallenge(self):
        super().solveChallenge()
        descriptions = []
        response = dict()
        #challenge descriptions
        for path in self.images:
            word = utils.get_first_noun(self.model.predict_caption(path))
            print(word)
            descriptions.append(word)
        prompt_label = utils.get_first_noun(self.model.predict_caption(self.challenge_image))
        
        for i, item in enumerate(descriptions):
            question = f"Do {item} fit inside a {prompt_label}"
            response[i] = self.question_model.predict(question)
        return response