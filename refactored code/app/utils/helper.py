from datetime import datetime

def get_current_timestamp():
    return datetime.utcnow().isoformat()

def compare_answers(user_answers: list, correct_answers: list) -> bool:
    return sorted(user_answers) == sorted(correct_answers)
