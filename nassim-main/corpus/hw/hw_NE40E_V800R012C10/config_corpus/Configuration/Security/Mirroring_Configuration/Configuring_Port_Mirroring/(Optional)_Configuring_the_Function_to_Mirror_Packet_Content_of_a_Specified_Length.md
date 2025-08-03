(Optional) Configuring the Function to Mirror Packet Content of a Specified Length
==================================================================================

You can specify the length of packet content to be mirrored. This configuration reduces the bandwidth consumed by the observing port and improves service performance.

#### Context

The mirrored port and observing port required for mirroring must be configured before you configure the function to mirror packet content of a specified length.

**Table 1** Interfaces supporting local mirroring
| Interface Type | Mirrored Port | Observing Port |
| --- | --- | --- |
| Layer 3 Ethernet main interfaces (including Eth-Trunk interfaces) | Supported | Supported |
| BAS interfaces | Supported  NOTE:  A VE interface functioning as a BAS interface only supports local flow mirroring in loopback scenarios. | Not supported |
| Ethernet sub-interfaces (including Eth-Trunk sub-interfaces) | Supported NOTE:  A sub-interface supports the mirroring function even when configured as a dot1q, EVC, BAS, dot1q VLAN tag termination, or QinQ VLAN tag termination sub-interface. | Supported  NOTE:  A sub-interface functioning as a BAS, dot1q VLAN tag termination or QinQ VLAN tag termination sub-interface does not support observing port configuration.  An EVC sub-interface can be configured as an observing port only when it adopts the untag or dot1q encapsulation mode.  If an Eth-Trunk interface is configured as an observing port, downstream mirroring is performed, and packets are mirrored from their Layer 3 headers, the mirroring starts from the first member interface. Other traffic is mirrored among member interfaces in load balancing mode, which depends on the configured load balancing mode and hash factors. |
| POS interfaces | Supported | Supported |
| IP-Trunk interfaces | Supported | Supported |
| Serial interfaces | Supported | Not supported |
| ATM main interfaces | Supported | Not supported |
| ATM sub-interfaces | Supported | Not supported |
| MP-Group interfaces | Supported | Not supported |



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* if the mirrored port is not an EVC Layer 2 sub-interface
   
   
   
   The interface view is displayed.
   
   
   
   To configure the function to mirror packet content of a specified length in a scenario where the mirrored port is an EVC Layer 2 sub-interface or a BD, enter the corresponding view to implement the configuration. The view varies according to the scenario.
   * If the mirrored port is configured in common mode, run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number**.subnum* **mode** **l2** command to enter the EVC Layer 2 sub-interface view.
   * If the mirrored port is configured in mirroring instance mode, run the [**mirror instance**](cmdqueryname=mirror+instance) *instance-name* **location** command to enter the mirroring instance view.
3. Run [**port-mirroring slice-size**](cmdqueryname=port-mirroring+slice-size) *slice-size-value*
   
   
   
   The length of packet content to be mirrored is specified.