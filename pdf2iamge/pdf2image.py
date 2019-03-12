#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x

from pdf2image import convert_from_path
import tempfile


def main(filename, outputDir):
    print('filename=', filename)
    print('outputDir=', outputDir)
    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path(filename)
        for index, img in enumerate(images):
            img.save('%s/page_%s.png' % (outputDir, index))


if __name__ == "__main__":
    main(r'D:\learn\pdf2iamge\5.pdf', '/home/pdfimage/b')
