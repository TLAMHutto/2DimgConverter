"# 2DimgConverter"

---PYLibs needed/Dependencies---

        **Transformers**

            Hugging Face GitHub repository for transformers
                pip install -q git+https://github.com/huggingface/transformers.git

            Installing Transformer library
                pip install -q datasets transformers
    
        **ZoeDepth**

            git clone https://github.com/isl-org/ZoeDepth.git
     
        **Dependencies**

            pip install --upgrade timm==0.6.7 torch==2.0.1 torchvision==0.15.2 numpy==1.23.5 pillow==9.4.0

Conversion stats
    Depth-img using DPTs image processer
        Non-depth
            640 x 480
            96 x 96 DPI
            24 Bit Depth
            68.4 KB
        Depth-Img
            640 x 480
            96 x 96 DPI
            8 Bit Depth
            12.0 KB
    Depth-img using DPTs model prediction
        Non-Depth
            360 x 540
            96 x 96 DPI
            24 Bit Depth
            35.9 KB
        Depth-Img
            360 x 540
            96 x 96 DPI
            8 Bit Depth
            7.12 KB DPTs\photos