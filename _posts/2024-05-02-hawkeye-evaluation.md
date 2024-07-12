---
layout: post
title: "HawkEye Evaluation"
date: 2024-05-02 00:00:00 -0700
description: Ocean Color Remote Sensing at UNCW
img: hawkeye.png
tags: [water quality, remote sensing, oceanography, satellite imagery, environmental monitoring]
categories: research
---

### Introduction
This project at UNCW evaluates the efficacy of the HawkEye satellite sensor in capturing ocean color (OC) imagery, specifically focusing on the Cape Fear River Estuary (CFRE) in southeastern North Carolina. Coastal and estuarine environments, which are vital for biodiversity and local economies, present unique challenges for remote sensing due to their optically complex waters. This research involves detailed comparisons of in-situ measurements with data from HawkEye and other satellite sensors to refine and enhance marine conservation and management strategies.

![Study Site](/mitchtorkelson/assets/img/for_posts/studysite_mosaic_presentation.png)  
*Sampling overview of the Cape Fear River Estuary and Masonboro Inlet Area we collected in-situ water quality measurements with the R/V Cape Fear (transect lines) and where we acquired satellite-derived measurements*

### Methodology
Our approach leverages a multi-sensor strategy that combines HawkEye satellite data with an array of other satellite-derived and in-situ "sea-truthing" chlorophyll a measurements from the CFRE. This integration allows us to assess the accuracy and utility of HawkEye in estimating chlorophyll a concentrations, which are crucial for understanding estuarine primary productivity dynamics.

![Satellite-derived chl mosaic](/mitchtorkelson/assets/img/for_posts/mosaic_masonboro_chl_single.png)  
*Satellite-derived Chl a concentration in the study region for each sensor type on May 7, 2023. Parallel red lines indicate the path of in-situ data collection. A) Aqua-MODIS, B) SeaHawk-HawkEye, C) S3A-OLCI, D) S3B-OLCI.*

Utilizing a 3D in-situ dataset for satellite matchup analysis can enhance satellite analysis since satellite sensors often provide a surface-level perspective, which can limit understanding of vertical variations within water bodies. Our 3D approach captures data across different depths, providing a comprehensive view that is essential for accurately interpreting satellite imagery. This depth-resolved data enables enhanced calibration and validation of satellite sensors, leading to improved accuracy in mapping and monitoring aquatic environments. The 3D dataset not only aids in understanding the spatial distribution of water quality parameters but also supports the development of models that predict ecological changes within these complex systems.

![In-Situ Chl a](/mitchtorkelson/assets/img/for_posts/chl.gif)  
*In-situ Chl a concentration along the 7 transects, collected using the Acrobat instrument on May 5, 2023.*

### Preliminary Results

During the study period from May 5 to May 7, we observed variations in environmental factors like wind speed, Chl a concentration, and tidal changes. These factors influenced water quality metrics, highlighting the dynamic nature of the study area. Our in-situ data collection revealed detailed profiles of various water quality parameters, including chlorophyll a, turbidity, temperature, salinity, density, and dissolved oxygen. We observed increasing Chl a concentrations from transect 1 to transect 7 and with depth. Temperature showed a slight thermal divide with depth, while density, salinity, turbidity, and dissolved oxygen displayed minor variations.

The analysis of satellite imagery provided a comprehensive view of the study site. The SeaHawk-HawkEye sensor offered high spatial resolution, revealing detailed patterns in water quality parameters. Our matchup analysis showed notable discrepancies between in-situ and satellite-derived Chl a data, primarily due to differences in sensor resolution, environmental variability, and the temporal gap between data acquisition between in-situ and satellite-derived datasets. Low R-squared scores indicate poor model fit between the sensors, suggesting the water column had significantly changed over the 48-hour window.

![matchup metric comparison](/mitchtorkelson/assets/img/for_posts/metric_mosaic.png)
*Figure: Statistical metric comparison across satellite sensor types at different in-situ depth ranges for 1x1 pixel size windows.*

### Research Findings
The integration of in-situ measurements with satellite imagery revealed several key findings:
- **Three-Dimensional Phytoplankton Plumes**: The detection of three-dimensional phytoplankton plumes showcases the effective integration of in-situ and satellite data.
- **Data Discrepancies**: Notable discrepancies between in-situ and satellite-derived chlorophyll-a data were observed, attributed to differences in sensor resolution, atmospheric correction effectiveness, vertical heterogeneity in the water column, and proximity to land/benthos.
- **Enhanced Accuracy**: The multi-sensor strategy proved crucial in providing a more comprehensive understanding of coastal dynamics, demonstrating variability and complexity in coastal water quality monitoring.

### Implications and Future Work
The preliminary findings from this study underscore the potential of advanced satellite sensors like HawkEye in improving our understanding of complex coastal waters. By providing more accurate and timely data, HawkEye can significantly aid in the management and conservation of aquatic resources. Ongoing research will focus on further integrating these insights into broader marine management practices and continuing to validate and refine our findings.

### Collaboration and Resources
This research is part of a collaborative effort with the COAST Lab at UNCW. For more detailed information on methodologies and ongoing updates, please visit our [GitHub Repository](https://github.com/COAST-Lab/HawkEye_Evaluation){:target="_blank"}.  

For a deeper dive into how we conduct in-situ measurements that complement our satellite data analysis, check out our detailed study on the Masonboro Inlet: [In-Situ Sampling in Masonboro](https://dinodiver.github.io/mitchtorkelson/waterquality-masonboro/).  

### Thesis Defense Video
Watch the detailed presentation of this research in my thesis defense video below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/n_ooO1NqXgc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

*This research was presented at several conferences and gatherings, including:*  
·	*Cape Fear Astronomical Society - May 2024, UNCW, Wilmington, NC*  
·	*NC Water Resources Research Institute (WRRI) Annual Conference - March 2024, NC State Campus, Raleigh, NC*  
·	*CMS Research Showcase - February 2024, UNCW, Wilmington, NC*  
·	*CMS Research Showcase - April 2023, UNCW, Wilmington, NC*  
