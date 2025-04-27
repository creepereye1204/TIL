class Classifier:
    @staticmethod
    def run(**kwargs):

        try:
            from src.utils import load_file, get_user_input, predict
            model = load_file(*kwargs['model'])
            questions = load_file(*kwargs['questions'])
            answers = load_file(*kwargs['answers'])
            skaler = load_file(
                *kwargs['skaler']) if 'skaler' in kwargs else None
            responses = get_user_input(
                questions=questions, limit=kwargs['limit'])
            predict(model=model, answers=answers,
                    responses=responses, scaler=skaler)
        except Exception as e:
            print(f"오류 발생: {e}")
            exit(0)
