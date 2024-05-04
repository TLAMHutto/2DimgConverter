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


<h3>Conversion Stats Using DPTs Image Processor</h3>
<table><thead><tr><th>Image Type</th><th>Resolution</th><th>DPI</th><th>Bit Depth</th><th>File Size</th></tr></thead><tbody><tr><td>Non-depth</td><td>640 x 480</td><td>96 x 96 DPI</td><td>24 Bit</td><td>68.4 KB</td></tr><tr><td>Depth-Img</td><td>640 x 480</td><td>96 x 96 DPI</td><td>8 Bit</td><td>12.0 KB</td></tr></tbody></table>
<h3>Conversion Stats Using DPTs Model Prediction</h3>
<table><thead><tr><th>Image Type</th><th>Resolution</th><th>DPI</th><th>Bit Depth</th><th>File Size</th></tr></thead><tbody><tr><td>Non-Depth</td><td>360 x 540</td><td>96 x 96 DPI</td><td>24 Bit</td><td>35.9 KB</td></tr><tr><td>Depth-Img</td><td>360 x 540</td><td>96 x 96 DPI</td><td>8 Bit</td><td>7.12 KB</td></tr></tbody></table>