import numpy as np
import json
import logging
from typing import Dict, List, Optional, Any

logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_and_log_first_task(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Load the JSON file, log the first task, and print its first matrix.
    
    Args:
        file_path (str): Path to the JSON file.
    
    Returns:
        dict: The entire loaded JSON data.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        if data:
            first_task_id = next(iter(data))
            first_task = data[first_task_id]
            
            logger.info(f"First task ID: {first_task_id}")
            logger.info("First task content:")
            logger.info(json.dumps(first_task, indent=2))
            
            # Print the first matrix of the first task
            if 'train' in first_task and first_task['train']:
                first_matrix = first_task['train'][0]['input']
                logger.info("First matrix of the first task:")
                for row in first_matrix:
                    logger.info(' '.join(map(str, row)))
            else:
                logger.warning("No training data found in the first task.")
        else:
            logger.warning("The loaded JSON file is empty.")
        
        return data
    except Exception as e:
        logger.error(f"An error occurred while loading the file: {str(e)}")
        return None
    
    
def format_submission(task_results: Dict[str, List[List[List[int]]]]) -> Dict[str, List[Dict[str, List[List[int]]]]]:
    """
    Format results according to competition submission requirements.
    Handles multiple test cases per task.
    """
    submission = {}
    
    for task_id, predictions in task_results.items():
        # Create list of predictions for each test case
        submission[task_id] = [
            {
                "attempt_1": pred,
                "attempt_2": pred  
            }
            for pred in predictions
        ]
    
    return submission