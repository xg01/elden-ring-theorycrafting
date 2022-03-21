# elden-ring-theorycrafting
A collection of scripts, tabulated data, and optimization APIs to assist the process of designing character builds in Elden Ring. 

## Setup
Utility scripts are included to handle the process of scraping data from Fextralife, setting up a local SQLite database, and migrating scraped data to a local SQLite database 

It is assumed that the Nix project manager will be used to obtain project dependencies.

## Usage
- Pre-scraped, tabulated data can be found under `data/csv`.
- Self-documented API can be found under `theorycraft`

## Roadmap 
This was mostly intended to be quick prototype for API design of a theorycrafting environment.  It currently is missing many implenentation details, which could be done in Python but require a lot of effort to manage performance concerns. In addition, existing libraries are insufficent: Google OR-Tools does handle some intended use cases, but it's API for bin-packing problems hides away obfuscates desired data; a maintained Datalog implementation to provide deductive database queries does not exist. This is especially important for the primary use-case of providing introspective insights.  Of course, this could be implemented from scratch, but it invalidates one of strongest arguments to use Python. 


