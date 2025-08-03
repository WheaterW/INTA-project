Typical Networking
==================

Typical Networking

#### Chain Topology

As shown in [Figure 1](#EN-US_CONCEPT_0000001564119917__fig1718316114521), DeviceA, DeviceB, DeviceC, and DeviceD are connected through Ethernet links to form a chain topology. DeviceB functions as the master clock to connect to the grandmaster clock. DeviceA and DeviceC function as slave clocks to synchronize with the clock of DeviceB.

**Figure 1** Chain topology  
![](figure/en-us_image_0000001564119957.png)

DeviceA, DeviceB, DeviceC, and DeviceD synchronize the time with the external clock as follows:

1. DeviceB extracts clock information from the bit streams received by the external clock, embeds the clock information into Ethernet bit streams, and transmits the Ethernet bit streams to DeviceA and DeviceC.
2. DeviceA extracts clock information from the Ethernet bit streams received from the E-side interface as the local clock information.
3. DeviceC extracts clock information from the Ethernet bit streams received from the W-side interface, embeds the clock information into Ethernet bit streams, and transmits the Ethernet bit streams to DeviceD.
4. DeviceD extracts clock information from the Ethernet bit streams received from the W-side interface as the local clock information.