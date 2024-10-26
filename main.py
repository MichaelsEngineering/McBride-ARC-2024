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

from src.utils.utils import load_and_log_first_task


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

if challenge_tasks:
    # Get the first task ID and data
        # Load all task IDs into an array
    task_ids = list(challenge_tasks.keys())
    first_task_id = next(iter(challenge_tasks))
    first_task_data = challenge_tasks[first_task_id]

    # Now you can work with the first task
    print(f"Working with task ID: {first_task_id}")

    # If you want to process all tasks, you can still do so:
    # for task_id, task_data in challenge_tasks.items():
    #     result = solve_arc_task(task_data)
    #     # Process or store the result as needed
else:
    print("Failed to load challenge tasks.")