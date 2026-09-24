def judge(question: str, expects: str, answer: str, results) -> bool:
    if not expects:
        return False
    return expects.lower().strip() in (answer or "".lower)