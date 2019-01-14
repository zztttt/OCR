rem 执行改批处理前先要目录下创建font_properties文件  

echo Run Tesseract for Training..  
tesseract  d.normal.exp0.tif d.normal.exp0  nobatch box.train
  
echo Compute the Character Set..  
unicharset_extractor d.normal.exp0.box  
mftraining -F font_properties -U unicharset -O d.unicharset d.normal.exp0.tr  
  
echo Clustering..  
cntraining.exe d.normal.exp0.tr  
  
echo Rename Files..  
rename normproto d.normproto  
rename inttemp d.inttemp  
rename pffmtable d.pffmtable  
rename shapetable d.shapetable   
  
echo Create Tessdata..  
combine_tessdata d.  

echo Delete useless file
del unicharset,d.unicharset,d.shapetable,d.pffmtable,d.normproto,d.normal.exp0.tr,d.inttemp