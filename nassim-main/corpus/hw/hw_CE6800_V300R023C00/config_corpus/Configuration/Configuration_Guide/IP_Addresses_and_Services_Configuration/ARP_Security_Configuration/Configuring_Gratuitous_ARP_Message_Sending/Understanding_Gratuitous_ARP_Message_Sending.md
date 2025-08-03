Understanding Gratuitous ARP Message Sending
============================================

Understanding Gratuitous ARP Message Sending

#### Fundamentals

As shown in [Figure 1](#EN-US_CONCEPT_0000001130622086__fig15461627114112), an attacker forges the Device address to send a bogus ARP message to HostA. HostA then records an incorrect ARP entry for Device. As a result, Device cannot receive messages from HostA.

**Figure 1** Bogus device attack  
![](figure/en-us_image_0000001130622100.png)

To avoid the preceding issue, configure gratuitous ARP message sending on Device. Device then sends gratuitous ARP messages at intervals to update the ARP entries of authorized users so that the entries contain the correct MAC address of Device.