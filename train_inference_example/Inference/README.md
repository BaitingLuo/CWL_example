# Inference Workflow Description 
The following description will tell the user how to prepare and execute the workflow for a succesfull
repreat of the original experiment.

## Environment
For the execution environment, you are going to need a linux based machine with [cwltool](https://github.com/common-workflow-language/cwltool)
installed on it. Additionally, you will also need [docker](https://docs.docker.com/engine/install/) installed to be able to run
the containerized computing elements.

## Description

### Inference


### Required inputs
 - Test_Data : 
 - Trained_Model : 


### Generated outputs
 - Testing_Results : 


## Execution
To run the workflow, you need to give the following command:
```
cwltool  --custom-net "host" --no-match-user --no-read-only --tmpdir $PWD --preserve-environment LEAP_CLI_DIR Inference.cwl.json --Test_Data ... --Trained_Model ... 
```