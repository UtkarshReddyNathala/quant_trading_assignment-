from statsmodels.tsa.stattools import coint


def find_best_pair(price_df):

    instruments = price_df.columns

    best_pair = None
    best_pvalue = 1

    for i in range(len(instruments)):
        for j in range(i + 1, len(instruments)):

            s1 = price_df[instruments[i]]
            s2 = price_df[instruments[j]]

            score, pvalue, _ = coint(s1, s2)

            if pvalue < best_pvalue:

                best_pvalue = pvalue
                best_pair = (instruments[i], instruments[j])

    return best_pair
