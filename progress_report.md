# Progress Report

## 2022-15-02
Created repo, added all startup files, downloaded PROIEL Treebank corpus.

## 1st Progress Report
I wrote a Python script to gather the type of sentence I'm looking for, [/annotations/annotate.py].
Right now, it may ignore some types of sentence (those involving the XOBJ and XADV syntactic relations),
but it gets a majority of what I need.
(I will update the code to account for the missing sentences.)

I also made a basic presentation file, [overview.ipynb].
Right now, it just gives, as the name suggests, an overview of some of the data.
This will eventually be fleshed out into a main analysis file.

With regards to the sharing of my data, I decided not to commit my XML files, as they can be generated simply
by running the Python script in 'automatic' mode.
If I end up needing to manually correct them, I will probably commit my changes.
I did make a small portion available in the [data_samples/] folder.

## 2nd Progress report
I thought about how to organize my data, and settled on a dataframe with the following columns:

* **Id** - the sentence's ID, as assigned by PROIEL (some had no ID, in which case I generated one)
* **File** - the file the sentence came from
* **Author**
* **Era** - Either Classical or Late
* **Type** - One of the types of construction I identified
* **Text** - The unannotated text of the sentence

I then began working on the analysis, focusing mainly on frequency of type based on era and author to start.
I noticed that Jerome had a much higher proportion of subordinators than the others.
I realized this may reflect Jerome's tendency to emulate the syntax and structures of the languages he
translated (e.g. increased VSO word order in the Old Testament).
I'll need to look into this further, as it may taint the data (since it is not necessarily reflective of 'normal' Latin).

In addition, I added an [introduction to indirect speech](oo_introduction.md), since understanding the construction and how
it works is important to understanding the project.
I also updated README.md with some links to important files within the project.
