<!---
readme for pyscripts/resources/webdrivers.
--->
this directory was created to hold the geckodriver binary  
required by selenium (python3).  
might add more drivers, might remove it.

NOTE:
In most cases, this file will need to either
a) be moved to a directory in your environment's PATH variable.
b) add a new directory to your PATH; containing the driver.

I added it to my repo, as i do with a few other items, to
try to keep some obscure dependencies all in one place.
I don't remember where I got it, but it wasn't hard to find.
There was another repo on github hosting various, compressed
versions of geckodriver.

For now, I'm wondering if there is a way to add a path (with
sys.path?) to python temporarily. This would ideally be done
through/by the python script, itself, or perhaps using a
virtual environment (venv module).
