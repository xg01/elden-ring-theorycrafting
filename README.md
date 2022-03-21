# elden-ring-theorycrafting
A collection of automation scripts, optimization algorithms, and tabulated stats for assistance for build customization. 

## Ad-hoc Setup
Various scripts are included to handle the process of scraping data from Fextralife, setting up a local SQLite database, and migrating scraped data to the local SQLite database.  

## Assumptions
- It is assumed that the Nix project manager will be used to obtain project dependencies. Traditional dependency management could be included later,
- Python does not have a maintained Datalog implementation, nor does it have metaprogramming on par with Ruby/Lisp/etc, which increases the friction to implement features I envisioned.
