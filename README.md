# elden-ring-theorycrafting
A collection of optimization algorithms, tabulated data, and scripts to assist the process of designing character builds in Elden Ring. 

## Setup
Utility scripts are included to handle the process of scraping data from Fextralife, setting up a local SQLite database, and migrating scraped data to a local SQLite database.  

It is assumed that the Nix project manager will be used to obtain project dependencies.

## Usage
Examine files in the`theorycraft` directory; the public API is self-documented. 

## Roadmap 
This is intended to be an exploratory prototype; it is unlikely this will be maintained in the long term.

Python was chosen with the assumption that existing libraries are sufficient.  However, it does not have a maintained Datalog implementation to provide deductive database queries. This is especially important for the primary use-case of providing introspective insights.  Of course, this could be implemented from scratch, but it invalidates one of strongest arguments to use Python. 


