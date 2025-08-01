# LunarRegolith
This repository contains details on the reanalysis of lunar-grown plant data performed for a NASA GeneLab project, conducted in collaboration between the Causal Inference and Lunar Regolith subgroups. 

Below, you can find a step-by-step instruction on what I've done so far.

## Introduction

### Data

This reanalysis pertains to the [OSD-476 study available via the NASA Open Science Data Repository (OSDR)](https://osdr.nasa.gov/bio/repo/data/studies/OSD-476). The data used in this reanalysis consists of four images grown in lunar regolith simulant and lunar regolith. 

### Goal of the study

The goal of this study is to identify the genes that have a causal relationship with the change in the phenotype of plants grown on lunar regolith from Apollo 11, 12, and 17 missions in comparison to those grown on lunar regolith simulant. 

## Analysis

### Step 1: Creation of single-plant images

To properly proceed with the next step, each image must contain only one plant. Since the images available in OSDR have seven plants each, I had to manually remove all but one plant for each photo. To achieve this, I used [Photoroom's AI retouch feature](https://www.photoroom.com/tools/remove-object-from-photo). This way, I ended up with 4 × 7 = 28 photos. You can see the original and edited images in SOAPP/images. 

### Step 2: SOAPP analysis

To perform a detailed analysis of the sizes and color compositions of the plants, I used SOAPP. You can find detailed instructions on how to run SOAPP [here](https://github.com/lvbauer/soapp-tutorial/blob/main/soapp-guide.md). It's easy, don't be afraid! I used Docker. I chose custom settings for each image. 

#### Output 

I saved all the outputs in two csv files. You can find them in the SOAPP/output directory. Here's an explanation of what is in them:
* **Results.csv** contains all the data regarding the size of the plants.
* **Color_results.csv** contains all the data regarding the color of the plants.

### Step 3: Matching SOAPP output with differential gene expression data

SOAPP/output/images_to_sequencing.csv is the file that matches SOAPP output with differential gene expression data, i.e., the GSM numbers.

**How did I match them?**

I downloaded the metadata zip file (OSD-476_metadata_OSD-476-ISA.zip) from the [OSDR repository](https://osdr.nasa.gov/bio/repo/data/studies/OSD-476). The s_OSD-476.txt file allowed me to associate the GSM numbers with their corresponding lunar regolith type (JSC-1A, Apollo 11, Apollo 12, and Apollo 17). This enabled me to link the Apollo regolith samples directly to their GSM identifiers, but I still didn't know which JSC-1A plant was sequenced in each case. To resolve this, I studied [Figure 3](https://www.nature.com/articles/s42003-022-03334-8/figures/3) from [the associated paper](https://www.nature.com/articles/s42003-022-03334-8), and i_Investigation.txt metadata file (from OSD-476_metadata_OSD-476-ISA.zip). That file includes the note: 

"_In Figure 3 [...] one can see the full designation of each plant used in the transcriptomes, so “P1J4JSC1A” means Plate 1, JSC plant 4, (JSC spelled out just to clarify for figure) and correlates to ‘Col-0, Leaves, JSC-1A, replicate 1’ in the transcriptome data set._"

It also states:

"_Although there were four representative JSC1A plants on each plate, only one of those plants (the plant in position 4 in each plate) was used from each plate for the transcriptome analyses._"

Based on this information, I inferred that the JSC-1A 4 plants were sequenced in each case (check SOAPP/images/original_images/LSDS-12_morphometric-photography_Lunar_plate_map.jpg or below image for reference).  


<p align="center">
  <img src="https://github.com/AnnaLew/LunarRegolith/blob/main/SOAPP/images/original_images/LSDS-12_morphometric-photography_Lunar_plate_map.jpg?raw=true" alt="Plate map" width="500"/>
</p>


**Why are there only 16 sequences available when 28 plants were grown?**

Only one plant per regolith type was sequenced on each of the four plates, resulting in:

- 4 × JSC-1A (position 4)
- 4 × Apollo 11
- 4 × Apollo 12
- 4 × Apollo 17

  = 16 sequenced samples

Note: An additional four samples associated with JSC-1A-grown plants were sequenced (GSM5691027, GSM5691028, GSM5691029, GSM5691030), but their exact plant origin could not be confidently determined from the available metadata.

### Step 4: CRISP analysis 

TBD


