Understanding Data Collection
=============================

Understanding Data Collection

#### Data Collection Process

The data collection system can collect the data generated during device running, and then process and store that data in a unified manner. If the available memory on the storage medium becomes insufficient or the storage space of the device is limited, the data collection system will not store collected data.

When the size of collected data files reaches a certain value, a compressed file named **yyyy-MM-dd.HH-mm-ss.dat.zip** is automatically generated and is saved in **flash:/full\_kpi**.

[Figure 1](#EN-US_CONCEPT_0000001512688662__fig1755931012393) shows the flowchart of the data collection system.

**Figure 1** Flowchart of the data collection system  
![](figure/en-us_image_0000001564127889.png)

#### Collected Data Type

The data collected mainly includes system data and application data. [Table 1](#EN-US_CONCEPT_0000001512688662__table1525024411195) describes these data types in further detail.

**Table 1** Common data types
| Data Type | Data Example |
| --- | --- |
| System data | CPU usage and memory usage |
| Application data | Number of discarded incoming packets and number of incoming multicast packets |