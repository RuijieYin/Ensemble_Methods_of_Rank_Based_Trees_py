#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ruijie Yin (ruijieyin428@gmail.com), Chen Ye (cxy364@miami.edu) and Min Lu (m.lu6@umiami.edu)
# Description:
# Fast computing an ensemble of rank-based trees via boosting or random forest on binary and multi-class problems.
# It converts continuous gene expression profiles into ranked gene pairs,
# for which the variable importance indices are computed and adopted
# for dimension reduction.

from setuptools import setup, find_packages

setup(
    name="ranktreeEnsemble",
    version="0.1.3",
    keywords=["ensemble", "rank trees"],
    description="Fast computing an ensemble of rank-based trees via boosting or random forest on binary and multi-class problems. It converts continuous gene expression profiles into ranked gene pairs, for which the variable importance indices are computed and adopted for dimension reduction.",
    license="MIT License",
    url="https://github.com/RuijieYin/Ensemble_Methods_of_Rank_Based_Trees_py",
    author=["Ruijie Yin", "Ye Chen", "Min Lu"],
    author_email="ruijieyin428@gmail.com",
    maintainer="Ruijie Yin",
    maintainer_email="ruijieyin428@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="OS Independent",
    install_requires=[
        "pandas", "sklearn", "numpy==1.18.1", "shap-hypetune", "lightgbm"
    ],
    python_requires=">=3.6",
    long_description="Fast computing an ensemble of rank-based trees via boosting or random forest on binary and multi-class problems. It converts continuous gene expression profiles into ranked gene pairs, for which the variable importance indices are computed and adopted for dimension reduction.",
    long_description_content_type='text/markdown',
)