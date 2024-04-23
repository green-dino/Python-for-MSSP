
# Define dictionaries for authors and tags

authors = {
    "Recipe Author": "Rain",
    "Tutorial Author": "Kate"
}

tags = {
    "Recipe Name": "recipe, example",
    "Tutorial Title": "tutorial, guide"
}

# Define functions to generate documents
def generate_recipe(name, author, tags):
    template = """
=========== 
{}
=========== 

:Author: {} 
:Tags: {}

## Abstract

Write here a small abstract about your recipe.

.. contents :: 
 
## Audience

Explain here who is the target readership.

## Prerequisites

Write the list of prerequisites for implementing this recipe. This can be additional documents, software, specific libraries, environment settings, or just anything that is required beyond the obvious language interpreter.

## Problem

Explain the problem that this recipe is trying to solve.

## Solution

Give a solution to the problem explained earlier. This is the core of a recipe.

## References

Put references, and links to other documents here.
""".format(name, author, tags)
    return template

def generate_tutorial(title, author, tags):
    template = """
# {}

- **Author:** {}
- **Tags:** {}

## Description

Write here a small abstract about your tutorial.

## Who Should Read This?

Explain here who should read this tutorial.

## Prerequisites

List any prerequisites for this tutorial, such as other documents to read or software to install.

## Tutorial

The main text of the tutorial goes here, providing step-by-step instructions on how to use the feature of the application.

## References

Put references and links to other documents here.
""".format(title, author, tags)
    return template

# Example usage
recipe = generate_recipe("Recipe Name", authors["Recipe Author"], tags["Recipe Name"])
tutorial = generate_tutorial("Tutorial Title", authors["Tutorial Author"], tags["Tutorial Title"])

print("Recipe Document:")
print(recipe)

print("\nTutorial Document:")
print(tutorial)
