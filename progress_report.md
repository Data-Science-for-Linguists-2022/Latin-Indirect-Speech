# Progress Report

## 2022-15-02
Created repo, added all startup files, downloaded PROIEL Treebank corpus.

## 1st Progress Report
I wrote a Python script to gather the type of sentence I'm looking for, [/annotations/annotate.py].
Right now, it may ignore some types of sentence (those involving the XOBJ and XADV syntactic relations),
but it gets a majority of what I need.
(I will update the code to account for the missing sentences.)

I also made a basic presentation file, [/overview.ipynb].
Right now, it just gives, as the name suggests, an overview of some of the data.
This will eventually be fleshed out into a main analysis file.

With regards to the sharing of my data, I decided not to commit my XML files, as they can be generated simply
by running the Python script in 'automatic' mode.
If I end up needing to manually correct them, I will probably commit my changes.
I did make a small portion available in the [/data_samples/] folder.
