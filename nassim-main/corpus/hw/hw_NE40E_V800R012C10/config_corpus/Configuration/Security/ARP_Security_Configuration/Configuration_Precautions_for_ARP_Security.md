Configuration Precautions for ARP Security
==========================================

Configuration Precautions for ARP Security

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The function to filter out invalid ARP packets ("arp filter" and "arp check-destination-ip enable") is mutually exclusive with the BAS function.  Impact:  1. When the function to filter out invalid ARP packets is configured before the BAS function, the following message is displayed: Error: This interface has the configurations of other services, and cannot be configured as an access interface  2. If the BAS function is configured first, the command used to filter out invalid ARP packets cannot be associated with the interface. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |