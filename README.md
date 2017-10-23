# Prisma-Photo-Editor

Prisma is a photo editing app that transforms your photos into works of art using the styles of famous artists. A unique combination of neural networks and artificial intelligence helps you turn memorable moments into timeless art.

## Style Transfer using TensorFlow

This project adds styles from given 6 pre-trained models to any photo in about 8-10 seconds. 

## Documentation
### Training Style Transfer Networks
Use `style.py` to train a new style transfer network. Run `python style.py` to view all the possible parameters. Training takes 4-6 hours roughly. **Before you run this, you should run `setup.sh`**. Example usage:

    python style.py --style path/to/style/img.jpg \
      --checkpoint-dir checkpoint/path \
      --test path/to/test/img.jpg \
      --test-dir path/to/test/dir \
      --content-weight 1.5e1 \
      --checkpoint-iterations 1000 \
      --batch-size 20

### Evaluating Style Transfer Networks
Use `evaluate.py` to evaluate a style transfer network. Run `python evaluate.py` to view all the possible parameters. Evaluation takes 8-10 seconds.**Models for evaluation are [located here](https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ?usp=sharing)**. Example usage:

    python evaluate.py --checkpoint path/to/style/model.ckpt \
      --in-path dir/of/test/imgs/ \
      --out-path dir/for/results/


The file `livefeed.py` acts as a GUI for this project. It captures a photo from the webcam, displays available styles to choose from, and upon selecting the style, it displays the edited picture.

### Requirements
- TensorFlow 0.11.0
- Python 2.7.9, Pillow 3.4.2, scipy 0.18.1, numpy 1.11.2
- If you want to train :
  - A decent GPU
  - All the required NVIDIA software to run TF on a GPU (cuda, etc)

### Citation
```
  @misc{engstrom2016faststyletransfer,
    author = {Logan Engstrom},
    title = {Fast Style Transfer},
    year = {2016},
    howpublished = {\url{https://github.com/lengstrom/fast-style-transfer/}},
    note = {commit xxxxxxx}
  }
  
  
 


