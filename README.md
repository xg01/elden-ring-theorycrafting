# elden-ring-theorycrafting
A collection of optimization algorithms, tabulated data, and scripts to assist the process of designing character builds in Elden Ring. 

## Setup
Utility scripts are included to handle the process of scraping data from Fextralife, setting up a local SQLite database, and migrating scraped data to a local SQLite database 

It is assumed that the Nix project manager will be used to obtain project dependencies.

## Usage
- Pre-scraped, tabulated data can be found under `data/csv`.
- Self-documented API can be found under `theorycraft`

## Roadmap 
This was mostly intended to be prototype API design for a theorcrafting environment; it currently is missing many implenentations, which shouldn't be done in Python for performance reasons. Google OR-Tools does handle some intended use cases, but it's API is less than ideal, and while it's possible to wrap C and C++ code, it unlikely is worth the effort. 

Python was used with the assumption that existing libraries are sufficient.  However, it does not have a maintained Datalog implementation to provide deductive database queries. This is especially important for the primary use-case of providing introspective insights.  Of course, this could be implemented from scratch, but it invalidates one of strongest arguments to use Python. 


