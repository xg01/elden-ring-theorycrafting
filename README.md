# elden-ring-theorycrafting
A collection of automation scripts, optimization algorithms, and tabulated stats for assistance for build customization. 

## Setup
Various scripts are included to handle the process of scraping data from Fextralife, setting up a local SQLite database, and migrating scraped data to a local SQLite database.  

It is assumed that the Nix project manager will be used to obtain project dependencies.

## Usage
Examine files in the`theorycraft` directory to view the API provided for each 

## Roadmap 
This is an exploratory prototype and will not be maintained in the long-term.

Python was chosen with the assumption that existing libraries are sufficient.  However, it does not have a maintained Datalog implementation to provide deductive database queries. This is especially important for the primary use-case of providing introspective insights.  Of course, this can be implenented from scratch, but it defeats the purpose of Python in the first place.

