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

I saved all the outputs in two csv files. You can find them in SOAPP/output. Here's an explanation of what is in them:
* **Results.csv** contains all the data regarding the size of the plants.
* **Color_results.csv** contains all the data regarding the color of the plants.

### Step 3: Matching SOAPP output with differential gene expression data

TBD

### Step 4: CRISP analysis 

TBD


