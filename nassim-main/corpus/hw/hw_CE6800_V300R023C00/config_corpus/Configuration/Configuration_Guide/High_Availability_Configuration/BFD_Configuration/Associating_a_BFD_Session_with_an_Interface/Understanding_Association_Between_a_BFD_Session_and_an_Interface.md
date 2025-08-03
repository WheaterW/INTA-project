Understanding Association Between a BFD Session and an Interface
================================================================

Understanding Association Between a BFD Session and an Interface

#### Context

To enable a BFD session to transmit fault notification messages to an interface, associate the BFD session with the interface. In [Figure 1](#EN-US_CONCEPT_0000001362599030__fig13691737183016), DeviceA is directed connected with DeviceE, and DeviceB is directed connected with DeviceF. A BFD session is configured on DeviceA and DeviceB. When the link between DeviceA and DeviceB fails, DeviceE and DeviceF are required to detect the failure to ensure reliable service transmission. You can associate BFD sessions with interfaces. When BFD detects a fault on the link between DeviceA and DeviceB, the BFD sessions on the devices send fault notification messages to the OAM module. This triggers the physical status of interface 1 on each device to become down. DeviceE and DeviceF can then detect the fault and switch traffic to a secondary link, thereby ensuring reliable service transmission.

**Figure 1** Network diagram of associating a BFD session with an interface  
![](figure/en-us_image_0000001413281897.png)