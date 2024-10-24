#!/bin/bash

for i in {1..30}; do 
    quarto render prova_comput_1.qmd 
    file_name="prova_1_${i}.pdf"
    mv prova_comput_1.pdf $file_name
done
