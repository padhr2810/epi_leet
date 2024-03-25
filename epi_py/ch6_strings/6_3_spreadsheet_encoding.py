import functools

#from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    print("##############################################")
    print(f"col = {col}")
    print(f"ord('A') + 1 = {ord('A') + 1}")
    print(f"ord(0) = {ord(0)}")
    
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)


if __name__ == '__main__':
    #exit(
    #    generic_test.generic_test_main('spreadsheet_encoding.py',
    #                                   'spreadsheet_encoding.tsv',
    #                                   ss_decode_col_id))
