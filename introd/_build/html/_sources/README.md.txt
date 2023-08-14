# VQuant量化方案 
## Environment

```bash
conda create -n vquant python==3.8
conda activate vquant
conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c nvidia
pip install pytorchcv==0.0.51
```


## Quantization Rules
1. The weight and activation should be quantized correctly when inference.
    - Weight is per-(output) channel quantization.
      - Affine quantzation, same as ZeroQ and GDFQ.
      - For all results of VQuant, we only set the min/max as the quantization range.
    - Activation (input) must be per-tensor quantization: all elements must have ONE quantization range.
      - The clip method is a BN-based method from DFQ with a wider clip range.
      - All models have the same range setting (alpha) of the BN-based method under the same bit-width (similar with [ACIQ (alpha)](https://github.com/submission2019/AnalyticalScaleForIntegerQuantization/blob/3246ee8cbfb747d7ef821c8cecc50283a73eaf92/pytorch_quantizer/quantization/qtypes/int_quantizer.py#L10)).
    - The first layer input does not need quantization. 
      - Same as other frameworks, such as ZeroQ and GDFQ.
    - The last layer (FC) input uses 8bit quantization. 
      - Lower bit-width than other frameworks, such as ZeroQ and GDFQ.
      - Note that other frameworks didn't quantize the FC input activation after average pooling.


2. The quantization procedure MUST not involve any real dataset information. (data-free)
    - Weight quantization should finish before the inference without training/validation dataset.
    - Activation can only quantize in inference runtime. However, its quantization range should be set before inference without a training/validation dataset.

3. Test all models
    - All models use the same hyperparameters under the same bit-width.
    - The results should fit the results (with $\pm 0.2$ error) presented in the manuscript.

3. Ablation study
    - Reproduce the same results as in the manuscript.

