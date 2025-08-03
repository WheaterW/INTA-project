Understanding PADS
==================

Understanding PADS

#### PADS Functions

PADS simulates experts to monitor the service status in real time. It also proactively detects faults, and automatically diagnoses and rectifies them.

PADS provides the following functions:

* Self-diagnosis and self-recovery in specific fault modes
* Service health checks and self-recovery upon poor check results

The service health checks include:

* Abnormal service status check: Diagnostic logs are generated. The status of the recent abnormal services can be queried using the CLI.
* Ongoing service status check: Diagnostic information is generated in the PADS O&M file on the PADS-dedicated flash, which helps restore services.


#### Implementation

**Figure 1** Implementation of PADS  
![](figure/en-us_image_0000001563761069.png)

1. The status of each service is saved in real time to the PADS O&M file on the flash memory, and key information is backed up.
2. The intelligent fault analysis/prevention unit monitors the running status of each service in real time.
3. The intelligent fault diagnosis unit automatically starts end-to-end diagnosis when detecting an exception. You can also run diagnostic commands to start end-to-end fault analysis.
4. During fault diagnosis, the inter-component and inter-device communication units can be used to collect information across components and devices for analysis.
5. Diagnosis results can be queried using the CLI at any time. PADS automatically restores services if faults are detected in the diagnosis result.