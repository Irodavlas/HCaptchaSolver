from handlers import solver
from models import florence2, bert
from models import utils
class NumberSolver(solver.NewCaptchaSolver):
    def __init__(self, images_path, challenge_prompt, challenge_image_path, captcha_type, model: florence2.NewFlorence2Model):
        super().__init__(images_path, challenge_prompt, challenge_image_path, captcha_type)
        self.model = model
    def solveChallenge(self):
        super().solveChallenge()
        descriptions = []
        response = dict()
        #challenge descriptions
        
        for path in self.images:
            descriptions.append(utils.parse_number(self.model.predict_caption(path)))
        print(descriptions)
        key = 0 if "greater" in self.prompt else 1
        prompt = utils.parse_number(self.model.predict_caption(self.challenge_image))
        print(prompt)
        response = dict()
        for i, num in enumerate(descriptions):
            if key == 0:
                response[i] = "yes" if num > prompt else "no"
            elif key == 1:
                response[i] = "yes" if num < prompt else "no"
            else:
                response[i] = "no"

        
        return response