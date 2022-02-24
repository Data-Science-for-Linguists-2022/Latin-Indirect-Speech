# Project Plan

## Summary

This project will examine the use of indirect speech in Latin.
Indirect speech refers to the reporting of someone else's speech without direct quotation, as in the sentence
"She said *she would be here by noon*."
In the case of this project, this will also include some complement clauses, as the syntax in Latin is the same.

The project will examine differences in usage between authors, as well as between different time periods.
In earlier Latin, the standard construction was to use the accusative + infinitive: "*nūntiātum est adesse Scīpiōnem*" [1];
in this phrase, *nūntiātum est* means "it was reported", *adesse* "to be present", and *Scīpiōnem* the accusative form of the name Scipio.
Thus, the translation is "It was reported that Scipio was present/nearby."

However, in later texts, a new construction emerges: the use of the subordinating conjuction *quod* + a clause in the indicative or subjunctive.
This is also the form that survives in modern Romance languages. For example: in "*et vīdit Deus quod esset bonum*" [2],
*et vīdit Deus* means "and God saw", *esset bonum* "was good", and *quod* serves a function similar to the English *that* in the translation:
"And God saw that it was good."

## Data
For my data, I will use the PROIEL Treebank [3]. [Link](https://dev.syntacticus.org/proiel.html)
It contains 6 Latin texts, 3 from the 1st century BCE and 3 from the 4th-5th centuries CE, covering 5 authors and 225,064 tokens.
The data is already annotated with syntactic roles, parts of speech, and morphological information.
I will, however, need to mark all instances of indirect speech.

## Analysis
For my analyis, I'll first mark each instance of indirect speech with its type (accusative + infinitive or *quod*-clause),
as well as other information (what verb introduced the clause, its tense, tense of the subclause, etc.).
I'll then compare this information for different eras and authors.
My main hypothesis is that in later Latin, the *quod*-clause will have a clear trend of becoming more prevalent.

## Presentation
For presenting the data, I will use a Jupyter notebook that explains the code and includes relevant graphs and data.
I may also make a PowerPoint/Beamer presentation.

## Citations

1. Caesar, B.C. 3.36.1.
2. Vulgate, Gen. 1:10
3. Dag T. T. Haug and Marius L. Jøhndal. 2008. 'Creating a Parallel Treebank of the Old Indo-European Bible Translations'. In Caroline Sporleder and Kiril Ribarov (eds.). Proceedings of the Second Workshop on Language Technology for Cultural Heritage Data (LaTeCH 2008) (2008), pp. 27-34.