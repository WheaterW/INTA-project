Creating a U-BFD Echo Session
=============================

A BFD session can be established on a BFD-enabled device to rapidly detect faults in a direct link.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create a U-BFD Echo session.
   
   Run either of the following commands to create a U-BFD echo session based on the IPv4 or IPv6 network and enter the BFD session view:
   * For an IPv4 network, run the [**bfd**](cmdqueryname=bfd) *sessname-value* **bind** **peer-ip** *ip-address* [ **vpn-instance** *vpn-instance-name* ] **interface** *ifType* *ifNum* [ **source-ip** *ip-address* ] **one-arm-echo** [ **destination-ip** *ip-address* ] command.
   * For an IPv6 network, run the [**bfd**](cmdqueryname=bfd) *sessname-value* **bind peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **interface** *ifType* *ifNum* [ **source-ipv6** *source-ipv6* ] **one-arm-echo** [ **destination-ipv6** *ipv6-address* ] command.
   
   In active-active networking, you must set **destination-ip** as the destination address of outgoing BFD packets. As shown in [Figure 1](#EN-US_TASK_0172361640__fig16404105413314), DeviceA and DeviceB are Layer 3 centralized gateways and work in active-active mode. DeviceA and DeviceB use the BDIF interface to establish a Layer 2 tunnel with the remote DeviceC using the same virtual address to implement network connectivity. To improve reliability, configure a U-BFD session on DeviceA and DeviceB to detect the status of the service links to DeviceC. Because the BDIF interface addresses of DeviceA and DeviceB are the same and the routes of BFD packets are the same, BFD response packets may return to the other device and are discarded. As a result, U-BFD cannot take effect. Therefore, you must set **destination-ip** to specify the IP address of interface 1 on the local device to ensure that BFD response packets can be sent back to the correct initiating device.
   
   **Figure 1** U-BFD for active-active networking  
   ![](figure/en-us_image_0000001239181465.png)  
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   U-BFD echo sessions can apply to single-hop detection only.
3. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
   
   
   
   A local discriminator is configured for the BFD session.
   
   U-BFD echo can be configured only on the device that supports BFD at one end of a link. Therefore, you need to configure only a local discriminator for a U-BFD echo session.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.