
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.discriminant_analysis import StandardScaler

class LoggingStandardScaler(StandardScaler):
    logged = False

    def fit(self, X, y=None):
        if not LoggingStandardScaler.logged:
            LoggingStandardScaler.logged = True
        super().fit(X,y)
        return self


class DebugStep(BaseEstimator, TransformerMixin):

    def transform(self, X):
        print(type(X))
        print(pd.DataFrame(X).head())
        print(X.shape)
        return X

    def fit(self, X, y=None, **fit_params):
        return self


def extract_params(prefix: str, params: dict) -> dict:
    selected_params = {}
    prefix = prefix + "__"
    for (k, v) in params.items():
        if k.startswith(prefix):
            k = k.replace(prefix, "")
            selected_params[k] = v
    return selected_params
