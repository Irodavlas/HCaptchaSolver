
class NewCaptchaSolver():
    def __init__(self, images_path, challenge_prompt, challenge_image_path, captcha_type):
        print(f"initializing Captcha solver for:{captcha_type}")
        self.type = captcha_type
        self.images = images_path
        self.prompt = challenge_prompt
        self.challenge_image = challenge_image_path
    def solveChallenge(self):
        print(f"Trying to solve challenge, [TYPE]:{self.type}")
        pass