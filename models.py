import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import FunctionTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

from features import *
from shared import *

cols_to_standardize = [
    "previous_qualification_grade", 
    "admission_grade", 
    "age_at_enrollment",
    "1st_sem_grade", 
    "1st_sem_enrolled",
    "1st_sem_evaluations",
    "1st_sem_approved",
    "1st_sem_without_evaluations",
    "1st_sem_credited",
    "2nd_sem_grade", 
    "2nd_sem_enrolled",
    "2nd_sem_evaluations",
    "2nd_sem_credited",
    "2nd_sem_approved",
    "2nd_sem_without_evaluations",
    "inflation_rate",
    "unemployment_rate",
    "gdp",
    "application_mode",
    "previous_qualification",
    "father_qualification",
    "mother_qualification",
    "father_occupation",
    "mother_occupation",
    "application_order",
    "course"
]

collapser = FunctionTransformer(
    func=collapse_hcard_features, 
    feature_names_out="one-to-one"
)

def logistic_sgd():
    param_grid = {
        "clf__random_state": [42],
        "clf__penalty": [None, "l1", "l2"],
        "clf__alpha": [0.0001, 0.001, 0.01],
        "clf__max_iter": np.power(10, np.arange(3, 5)),
        "clf__class_weight": [
            {0:0.5, 1:1},
            {0:1, 1:2},
        ],
        "selector__k": range(2,36,2)
    }
    
    def create_pipeline(params={}):
        column_transformer = ColumnTransformer(
            transformers=[
                ("scaler", LoggingStandardScaler(), cols_to_standardize)
            ], 
            remainder="passthrough", 
            verbose_feature_names_out=False
        )

        clf = SGDClassifier(
            loss="log_loss", 
            **extract_params("clf", params)
        )

        return  Pipeline(steps=[
            ("collapser", collapser),
            ("transformer", column_transformer),
            ("selector", SelectKBest(f_classif, **extract_params("selector", params))),
            ("clf", clf)
        ])

    return (create_pipeline, param_grid, True)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import MinMaxScaler

def knn():
    grid_params = {
        "clf__n_neighbors": [4,5,6,7],
        "clf__weights": ["uniform", "distance"],
        "kbest_selector__k": range(2,37,2)
    }

    def create_pipeline(params={}):
        pipe = Pipeline([
            ("collapser", collapser),
            ("scaler", MinMaxScaler((0,1))),
            ("kbest_selector", SelectKBest(f_classif, **extract_params("kbest_selector", params))),
            ("clf", KNeighborsClassifier(**extract_params("clf", params)))
        ])
        return pipe

    return (create_pipeline, grid_params,True)



def svm():
    probability = False
    grid_params = {
        "clf__probability": [probability],
        "clf__C": [1.5],
        "clf__kernel": ["poly", "rbf"],
        "clf__degree": [3,5],
        "clf__class_weight": [{0:1, 1:i} for i in range(3,6,1)],
        "kbest_selector__k": range(2,20,2)
    }

    def create_pipeline(params={}):
        pipe = Pipeline([
            ("collapser", collapser),
            ("scaler", MinMaxScaler((0,1))),
            ("kbest_selector", SelectKBest(f_classif, **extract_params("kbest_selector", params))),
            ("clf", SVC(**extract_params("clf", params)))
        ])
        return pipe

    return (create_pipeline, grid_params, probability)