# Prompt Engineering with PaLM API
This repository contains the sample code for experimenting with various prompting methods, including the following:

  1. Zero-shot Prompting
  2. Few-shot Prompting
  3. Chain-of-Thought (CoT)
  4. Self-consistency
  5. Generated Knowledge Prompting

The project is setup based on the Google's [PaLM API](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/overview).

# Project Setup

### Step 1 - Create a credential JSON file on Google Cloud

  1. Create and download the service account key
  2. If you want to keep this file in the project root directory, rename it to `sa.json` to prevent it being tracked by Git

### Step 2 - Create a `.env` file from the `.env.template`

  1. Set the `PROJECT` to your Google Cloud Project ID
  2. Set the `LOCATION` to your Vertex AI Location
  3. Set the `GOOGLE_APPLICATION_CREDENTIALS` to the absolute path to the credential JSON file

### Step 3 - Create a virtual environment
In this project, I used `mamba` to create a virtual environment. You can run `source create_env.sh` if you would like to use 
`mamba`, on a Linux or MacOS. If you would like to use other tools to create the virtual environment, you can install all the 
dependencies listed in `pip` section of the `environment.yaml` file.

### Step 4 - Export environment variable

To export the environment variable, you can use the bash script by running `source set_env.sh`. Or you can export all the variables
defined in the `.env` file. This isolates the project setup and credentials with the code.

### Step 5 - Run script

To execute an example, you can run the following command:

```
python prompt_engineering/chain_of_thought.py
```

# File Structure

The `models` is a python module contains a wrapper class on top of Vertex AI `TextGenerationModel`. You can create an instance of the
class to access the model, and use the `predict` method to get a response for your prompt.  

The `prompt_engineering` contains the sample code.

The `prompts` folder contains a set of prompts that are used by the sample code.

The `sample_outputs` folder contains the response for the prompts defined in the `prompts` folder. You might not get the exact same 
result as the sample responses shown in the folder.
