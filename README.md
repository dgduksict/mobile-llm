# MobileLLM-R1 Android App

An open-source Android application for offline inference using Meta's MobileLLM-R1-950M model, designed for non-commercial research purposes. The app supports solving mathematical, programming (Python/C++), and scientific problems with step-by-step reasoning and multi-turn chat capabilities.

This project is based on the [local-llms-on-android](https://github.com/dineshsoudagar/local-llms-on-android) repository (Apache 2.0 licensed) and integrates the MobileLLM-R1-950M model, which is licensed under the [FAIR Noncommercial Research License v1](LICENSE).

## Features

- Offline inference with MobileLLM-R1-950M (quantized to int4 for efficiency).
- Single-turn QA for math, coding, and scientific queries.
- Multi-turn chat with streaming responses.
- Toggle for step-by-step reasoning mode.
- Optimized for Android devices with ≥4 GB RAM and ARM64 architecture.

## License

- **Model License**: The MobileLLM-R1-950M model is subject to the [FAIR Noncommercial Research License v1](LICENSE). This restricts usage to non-commercial research purposes only. You must include the license with any distribution and ensure compliance.
- **Project License**: The codebase is licensed under the [Apache 2.0 License](LICENSE-APACHE), except for the model files, which remain under the FAIR license.

## Prerequisites

- **Hardware**: Android device with ≥4 GB RAM, ARM64 architecture.
- **Development**:
  - Python 3.8+ (for model export).
  - Android Studio (latest stable version).
  - Git for cloning the repository.
- **Model Files**: Exported ONNX model and tokenizer (see Setup).

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dgduksict/mobile-llm.git
cd mobile-llm
```

### 2. Export the Model to ONNX

0. Create a new virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Export the MobileLLM-R1-950M model to ONNX with int4 quantization:
   ```bash
   optimum-cli export onnx --model facebook/MobileLLM-R1-950M --task causal-lm --quantize awq --bits 4 mobilellm_r1_950m_onnx/
   ```
   - This generates `mobilellm_r1_950m_onnx/model_quantized.onnx` and `tokenizer.json`.
   - If int4 fails, try int8: `--quantize int8 --bits 8`, or FP16: omit `--quantize` and use `--dtype fp16`.
3. Copy `model_quantized.onnx` (rename to `model.onnx`) and `tokenizer.json` to `app/src/main/assets/` in the project.

### 3. Set Up Android Project

1. Open the project in Android Studio.
2. Ensure the ONNX Runtime dependency is in `app/build.gradle`:
   ```gradle
   dependencies {
       implementation 'com.microsoft.onnxruntime:onnxruntime-android:1.19.2'
   }
   ```
3. Sync the project.

### 4. Configure Model Settings

In `app/src/main/java/com/example/MainActivity.kt`, set the model configuration:

```kotlin
val modelconfigmobilellm = ModelConfig(
    precision = Precision.FP16,  // Or INT4 if quantized
    promptStyle = PromptStyle.QWEN,
    kvOverrides = true,
    eosTokenId = 128001,  // From tokenizer.json
    temperature = 0.7f,
    repetitionPenalty = 1.1f,
    maxTokens = 512
)
```

Update system prompts for reasoning or coding as needed (see [Model Card](https://huggingface.co/facebook/MobileLLM-R1-950M)).

### 5. Build and Run

1. Connect an Android device (enable USB debugging).
2. Build and run the app in Android Studio.
3. Test with a sample query: "Compute: 1-2+3-4+5-...+99-100".

## Usage

- **Input**: Enter a math, coding, or scientific question in the text field.
- **Reasoning Mode**: Toggle for step-by-step answers.
- **Output**: View responses in real-time (streaming enabled).
- **Examples**:
  - Math: "Compute: 1-2+3-4+5-...+99-100"
  - Python: "Write a function that returns the square of a number."
  - C++: "Write a C++ program that prints 'Hello, World!'."

## Contributing

Contributions are welcome! Please:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Ensure all contributions comply with the FAIR Noncommercial Research License for the model.

## Citation

If you use MobileLLM-R1-950M in your research, please cite:

```bibtex
@misc{mobilellm_r1_2025,
  title={MobileLLM-R1: Model Card},
  author={Zechun Liu*, Ernie Chang*, Changsheng Zhao*, Chia-Jung Chang, Wei Wen, Chen Lai, Rick Cao, Yuandong Tian, Raghuraman Krishnamoorthi, Yangyang Shi, Vikas Chandra},
  year={2025},
  url = {https://huggingface.co/mobilellm-r1}
}
```

## Contact

For issues or questions, open a GitHub issue or contact:

- Zechun Liu (zechunliu@meta.com)
- Ernie Chang (erniecyc@meta.com)
- Changsheng Zhao (cszhao@meta.com)

## Acknowledgments

- Based on [local-llms-on-android](https://github.com/dineshsoudagar/local-llms-on-android).
- Model by Meta's FAIR team.
