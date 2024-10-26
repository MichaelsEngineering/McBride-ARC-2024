from typing import Dict, List, Any

class PromptTemplates:
    """Stores and manages specialized prompts for ARC analysis"""
    
    def __init__(self):
        # Core templates dictionary storing all prompts by category and name
        self.templates = {
            'boolean': {
                'pattern_analysis': {
                    'system': """You are an expert at analyzing boolean logic patterns in ARC Challenge tasks. Your role is to:
1. Identify potential boolean operations (AND, OR, XOR, NOT) between input grids or grid regions
2. Analyze cell-wise boolean relationships between input and output
3. Detect pattern propagation using boolean logic
4. Recognize boolean masks and their applications
5. Identify composite boolean transformations""",
                    'user': """Analyze the boolean logic patterns in this ARC task:

Input Grid:
{input_grid}

Output Grid:
{output_grid}

Focus on:
1. What boolean operations could transform the input to output?
2. Are there any boolean masks or templates being applied?
3. What cell-wise or regional boolean patterns do you observe?"""
                },
                'transformation': {
                    'system': """You are an expert at implementing boolean transformations in ARC tasks. Your role is to:
1. Suggest specific boolean operations to transform input to output
2. Identify the sequence of operations needed
3. Consider edge cases and pattern boundaries
4. Propose efficient boolean implementations""",
                    'user': """Given the input and output grids, suggest boolean transformations:

Input Grid:
{input_grid}

Output Grid:
{output_grid}

Provide:
1. Specific boolean operations needed
2. Order of operations
3. Any edge cases to handle"""
                }
            },
            'visual': {
                'pattern_analysis': {
                    'system': """You are an expert at analyzing visual patterns in ARC tasks. Focus on:
1. Spatial relationships and transformations
2. Shape recognition and manipulation
3. Pattern repetition and symmetry
4. Color relationships and changes""",
                    'user': """Analyze the visual patterns in this task:

Input Grid:
{input_grid}

Output Grid:
{output_grid}

Describe:
1. Visual transformations observed
2. Spatial relationships
3. Pattern rules"""
                }
            },
            'program': {
                'synthesis': {
                    'system': """You are an expert at program synthesis for ARC tasks. Your role is to:
1. Identify algorithmic patterns
2. Suggest implementation approaches
3. Consider edge cases and generalization
4. Propose efficient solutions""",
                    'user': """Analyze this task for program synthesis:

Input Grid:
{input_grid}

Output Grid:
{output_grid}

Provide:
1. Algorithmic approach
2. Implementation steps
3. Edge cases to handle"""
                }
            }
        }

    def get_prompt(self, category: str, name: str, **kwargs) -> List[Dict[str, str]]:
        """
        Get a formatted prompt by category and name
        
        Args:
            category: Main category (e.g., 'boolean', 'visual', 'program')
            name: Specific prompt name (e.g., 'pattern_analysis')
            **kwargs: Format arguments for the prompt (e.g., input_grid, output_grid)
            
        Returns:
            List of formatted message dictionaries ready for LLM
        """
        try:
            template = self.templates[category][name]
            return [
                {"role": "system", "content": template['system']},
                {"role": "user", "content": template['user'].format(**kwargs)}
            ]
        except KeyError:
            raise ValueError(f"Prompt template not found for category '{category}' and name '{name}'")

    def list_prompts(self) -> Dict[str, List[str]]:
        """List all available prompts by category"""
        return {
            category: list(prompts.keys())
            for category, prompts in self.templates.items()
        }

# Example usage
if __name__ == "__main__":
    # Initialize prompt library
    prompt_lib = PromptTemplates()
    
    # Example task data
    test_input = [[0, 1], [1, 0]]
    test_output = [[1, 0], [0, 1]]
    
    # Get boolean analysis prompt
    messages = prompt_lib.get_prompt(
        category='boolean',
        name='pattern_analysis',
        input_grid=str(test_input),
        output_grid=str(test_output)
    )
    
    # Show available prompts
    print("Available prompts:")
    for category, names in prompt_lib.list_prompts().items():
        print(f"\n{category}:")
        for name in names:
            print(f"  - {name}")
            
    # Show formatted prompt
    print("\nExample formatted prompt:")
    for message in messages:
        print(f"\n{message['role'].upper()}:")
        print(message['content'])