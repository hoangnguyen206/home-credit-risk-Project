import pandas as pd

from home_credit_risk.validation import check_unique_key

def test_check_unique_key_returns_true_when_unique():
    df = pd.read_csv('tests/fixtures/application_small.csv')
    assert check_unique_key(df, 'sk_id_curr') is True

def test_check_unique_key_returns_false_when_duplicated():
    df = pd.DataFrame({"sk_id_curr": [1, 1, 2], "target": [0, 1, 0]})
    assert check_unique_key(df, 'sk_id_curr') is False