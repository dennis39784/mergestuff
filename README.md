# mergestuff
merge poc for Per
script is written in the Python 3.5 environment

merge script to merge a server property file with a default property file
Each property file has many lines of properties, one property per line, in the format of:
  attribute = value
 
Merge logic is to produce a merged file with:
  - for each attribute in the default file, if that attribute is also listed in server specific property file, then use the value from the server file in the final output file
  - for each attribute in the default file, if that attribute does NOT exist in the server specific file, then include the attribute and value from the default file into the target file
  - if there are attributes in the server specific file but not in the default file, then add such server specific attribute and value into the target file.   Note: due to avoidance of N*N loop, missing attributes/values will be added to the end of the target file and not in the same location as in the server file
  
Run this script as:
  % python mergepoc.py <server filename>
 
Output writes to a file named "envTarget" in the current working directory, and will create envTarget is none is found.  This also means existing envTarget file will get overwritten.  Not an issue for this quick and dirty POC.

There are some "print" statements currently to help identify the intermediate dictionary values.  They can be commented out, but be careful here as I used the print to file function to write the envTarget file, so don't comment that out.

In additon to the merge script, there's a envDefault file with default properties, and 3 test scenrios files included in this commit.

Scenario 1 (envfile1): same set of properties as the default set, with a couple of updated values in envfile1
Scenario 2 (envfile2): only has two properties in this file, each property exists in default, but values are updated.
Scenario 3 (envfile3): has more attributes than default.  Merged file should be the superset, with all updated values from the server specific file.

To do:
1) refactor to use functions for cleaner code.  Need one for creating dictionaries from property files, another for merging dictionaries and output to target file, and another for finding and appending the server specific properties into the target file.
2) add time or random bits to envTarget filenames so each run's output is unique.
3) add a wrapper to run against a set of env input files to produce a set of output files
4) add template parsing functionaltiy for "???" so default can have masked fields (e.g. attribute=???)
