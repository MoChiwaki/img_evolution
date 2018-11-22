# pokemonの進化を学習させ、画像を進化させます


## 学習するには
```
python ./pix2pix-tensorflow/pix2pix.py --mode train --output_dir pixelart_train --max_epochs 100 --input_dir ./pixelart/train --which_direction BtoA
```

## 実行するには
```
python ./pix2pix-tensorflow/pix2pix.py --mode test --output_dir ./pixelart_test --input_dir ./levelUpTestData --checkpoint pixelart_train
```

## フォーマットに使える
- createTestData.py
 1枚の進化させたい画像を実行用フォーマットに合わせます

- levelUp.py  
 pixelartに学習用のフォーマット画像を作ります  
 input用ディレクトリ、output用ディレクトリを引数にして学習用フォーマット作ります

- split.py  
　学習用のフォーマット画像をtrainとvalに振り分ける
