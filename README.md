# elden-ring-theorycrafting
A collection of scripts, tabulated data, and optimization APIs to assist the process of designing character builds in Elden Ring. 

Utility scripts are included to handle the process of scraping data from Fextralife, setting up a local SQLite database, and migrating scraped data to a local SQLite database 

The Nix project manager was used to obtain project dependencies.

## Roadmap 
This was mostly intended to be quick prototype for API design of a theorycrafting environment.  It currently is missing many implenentation details, which could be done in Python but require extraneous effort to manage performance concerns and implement custom libraries are existing libraries are insufficent.  Google OR-Tools does handle some intended use cases, but it's API for bin-packing problems obfuscates desired solver data, A maintained Datalog implementation to provide deductive database queries does not exist. This is especially important for the primary use-case of providing introspective insights.  Of course, all of this could be implemented from scratch, but it invalidates one of strongest arguments to use Python. 


