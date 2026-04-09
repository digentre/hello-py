"""
A simple greeting program that asks for the user's name and provides a personalized hello message.

This script demonstrates basic input handling, error management, and user interaction
with graceful fallbacks for edge cases like empty input or interruption.
"""

def get_name() -> str:
    """Get user's name with error handling."""
    try:
        # Prompt user for their name
        name = input("What's your name? ")
        # Handle empty or whitespace-only input
        if not name.strip():
            return "Anonymous"
        # Return cleaned input (remove leading/trailing whitespace)
        return name.strip()
    except (EOFError, KeyboardInterrupt):
        # Handle EOF (no input available) or user interruption (Ctrl+C)
        return "Anonymous"

def greet(name: str) -> None:
    """Print greeting message."""
    # Display personalized greeting with the provided name
    print(f'Hello {name} from Claude Code!')

def main() -> None:
    """Main function that orchestrates the greeting process."""
    # Get the user's name (with fallback handling)
    name = get_name()
    # Display the greeting
    greet(name)

# Only run main() if this script is executed directly (not imported)
if __name__ == "__main__":
    main()