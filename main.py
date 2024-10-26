# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load
import json
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, TextStreamer
import torch
from accelerate import infer_auto_device_map
import gc
from IPython.display import Markdown, display

#Boolean Face
from dataclasses import dataclass
from enum import Enum
import logging
from typing import List, Dict, Tuple, Optional, Set
from collections import defaultdict
import itertools

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Custom files
from src.utils.utils import load_and_log_first_task
from src.faces.llm_llama3_2_3B import generate_llama_response
from src.utils.prompt_library import PromptTemplates

# Option 1 (Recommended for T4 x2): Enable tokenizer parallelism
# T4s have enough memory and processing power to benefit from parallel tokenization
os.environ["TOKENIZERS_PARALLELISM"] = "true"

# Enable CUDA memory optimizations
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

# Clear GPU memory before loading model
gc.collect()
torch.cuda.empty_cache()

# Load data

practice_path = 'data/practice_training_challenge.json'
# kaggle_path = 'kaggle/input/arc-prize-2024/arc-agi_training_challenges.json'
# Load challenges and log the first task
challenge_tasks = load_and_log_first_task(practice_path)

# When processing a task
if challenge_tasks:
    first_task_id = next(iter(challenge_tasks))
    first_task_data = challenge_tasks[first_task_id]

    # Get first training pair
    first_pair = first_task_data['train'][0]

    # Initialize PromptTemplates
    prompt_lib = PromptTemplates()

    # Define analysis types
    analysis_types = [
        ('boolean', 'pattern_analysis'),
        ('visual', 'pattern_analysis'),
        ('program', 'synthesis')
    ]

    # Generate prompts and responses for each analysis type
    for category, name in analysis_types:
        messages = prompt_lib.get_prompt(
            category=category,
            name=name,
            input_grid=str(first_pair['input']),
            output_grid=str(first_pair['output'])
        )
        
        # Combine messages into a single string for the LLM
        combined_message = "\n\n".join([f"{msg['role'].upper()}:\n{msg['content']}" for msg in messages])
        
        # Generate response using the LLM
        response = generate_llama_response(combined_message)
        print(f"\nResponse for {category} {name}:\n{response}")

else:
    print("Failed to load challenge tasks.")

