from handlers import solver
from models import florence2, miniLM

class CosineSimilaritySolver(solver.NewCaptchaSolver):
    def __init__(self, images_path, challenge_prompt, challenge_image_path, captcha_type, model: florence2.NewFlorence2Model, similarity_model: miniLM.NewMiniLM, threshold):
        super().__init__(images_path, challenge_prompt, challenge_image_path, captcha_type)
        self.model = model
        self.similarity_model = similarity_model
        self.threshold = threshold
    def solveChallenge(self):
        #logic
        super().solveChallenge()
        descriptions = []
        response = dict()
        #challenge descriptions
        for path in self.images:
            descriptions.append(self.model.predict_caption(path))
        #prompt image description 
        prompt_description = self.model.predict_caption(self.challenge_image)
        prompt_embedding = self.similarity_model.encode_embedding(prompt_description)
        for i, desc in enumerate(descriptions):
            similarity =self.similarity_model.cosine_similarity(prompt_embedding, self.similarity_model.encode_embedding(desc))
            similarity = float(similarity)
            if similarity > self.threshold:
                answer = "yes"
            else:
                answer = "no"
            response[i] = answer

        return response
        
        
