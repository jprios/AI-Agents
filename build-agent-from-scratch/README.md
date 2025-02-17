# AI Agent with Tool Selection

An intelligent AI assistant that can perform calculations, reverse strings, and answer general questions using either Ollama (for local LLMs) or OpenAI models. The agent automatically selects the appropriate tool based on user queries.

## Features

- 🧮 **Basic Calculator**: 
  - Performs arithmetic operations (add, subtract, multiply, divide)
  - Handles decimal numbers
  - Error handling for division by zero
  - Supports alternative operation words (plus/add, minus/subtract, etc.)

- 🔄 **String Reversal**: 
  - Reverses any given string
  - Input validation
  - Clean output formatting

- 💬 **General Q&A**: 
  - Handles general questions with direct responses
  - Provides informative responses about capabilities
  - Friendly conversational interface

- 🔄 **Model Flexibility**: 
  - Local LLM support via Ollama (llama2, mistral, etc.)
  - Cloud-based support via OpenAI models
  - Temperature and stop token configuration

## Prerequisites

### 1. Python Environment Setup

#### Windows:
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation:
   - ✅ Check "Add Python to PATH"
   - Click "Install Now"
3. Verify installation:
   ```bash
   python --version
   pip --version
   ```

#### macOS/Linux:
Python usually comes pre-installed. If not:
```bash
# macOS (using Homebrew)
brew install python

# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### 2. Ollama Setup (for Local LLMs)

#### Installation:

```bash
# macOS/Linux
curl https://ollama.ai/install.sh | sh

# Windows (WSL2 required)
# 1. Install WSL2 first:
wsl --install

# 2. Then install Ollama:
curl https://ollama.ai/install.sh | sh

# 3. Or download Windows native version (beta) from:
# https://ollama.ai/download/windows
```

#### Pull and Run Models:
```bash
# Start Ollama server
ollama serve

# Pull the llama2 model
ollama pull llama2

# Verify installation
ollama list
```

### 3. OpenAI Setup (Optional)
If you want to use OpenAI models:

1. Create an account at [OpenAI](https://platform.openai.com/)
2. Get your API key
3. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-agent-tools.git
   cd ai-agent-tools
   ```

2. Install required packages:
   ```bash
   # For Ollama (Local LLM) setup
   pip install requests termcolor python-dotenv

   # For OpenAI setup (optional)
   pip install openai
   ```

3. If you prefer using requirements.txt:
   ```bash
   # Create requirements.txt
   cat > requirements.txt << EOL
   requests>=2.31.0
   termcolor>=2.3.0
   python-dotenv>=1.0.0
   # Optional: for OpenAI integration
   # openai>=1.3.0
   EOL

   # Install from requirements.txt
   pip install -r requirements.txt
   ```

Note: 
- For Ollama usage, only `requests`, `termcolor`, and `python-dotenv` are required
- Install `openai` package only if you plan to use OpenAI models
- Use `pip3` instead of `pip` on some Unix systems if you have both Python 2 and 3 installed

## Usage

### Example Queries:

1. **Calculator Operations:**
   ```
   Ask me anything: Calculate 15 plus 7
   Ask me anything: What is 100 divided by 5?
   Ask me anything: Multiply 23 and 4
   ```

2. **String Reversal:**
   ```
   Ask me anything: Reverse the word 'hello world'
   Ask me anything: What is the reverse of Python?
   Ask me anything: Reverse this: Programming
   ```

3. **General Questions:**
   ```
   Ask me anything: Who are you?
   Ask me anything: What can you help me with?
   Ask me anything: How are you today?
   ```

### Running with Different Models:

#### Ollama (Local LLM):
```python
model_service = OllamaModel
model_name = "llama2"  # or "mistral", "codellama", etc.
stop = "<|eot_id|>"
```

#### OpenAI:
```python
from openai import OpenAI
model_service = OpenAIModel
model_name = 'gpt-3.5-turbo'  # or 'gpt-4', etc.
stop = None
```

## Troubleshooting

1. **Ollama Connection Issues:**
   - Ensure Ollama server is running: `ollama serve`
   - Check available models: `ollama list`
   - Verify port 11434 is available and not blocked
   - Check Ollama logs: `journalctl -u ollama`

2. **Python Path Issues:**
   - Verify Python installation: `python --version`
   - Check PATH environment variable
   - Try using `python3` instead of `python` on Unix systems

3. **OpenAI Authentication:**
   - Verify API key in `.env` file
   - Check environment variable loading
   - Ensure OpenAI package is installed
   - Verify API key has sufficient credits

4. **Common Issues:**
   - "Connection refused" - Make sure Ollama server is running
   - "Model not found" - Run `ollama pull <model_name>` first
   - "ImportError" - Check all required packages are installed

## Version Compatibility

- Python: 3.8 or higher
- Ollama: Latest version recommended
- OpenAI API: Latest version
- Operating Systems: Windows 10/11, macOS, Linux

## Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and create pull requests.

## License

[Your chosen license]

## References

- [Ollama Official Documentation](https://ollama.ai/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python Installation Guide](https://www.python.org/downloads/)
