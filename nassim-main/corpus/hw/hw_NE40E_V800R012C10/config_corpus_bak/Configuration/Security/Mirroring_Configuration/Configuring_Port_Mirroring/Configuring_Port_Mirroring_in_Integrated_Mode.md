Configuring Port Mirroring in Integrated Mode
=============================================

Configuring_Port_Mirroring_in_Integrated_Mode

#### Context

To simplify port mirroring configuration, you can configure port mirroring in integrated mode.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You can configure port mirroring in either of the following ways:

* [Configure port mirroring in integrated mode](dc_ne_portmirror_cfg_0035.html).
* Configure [an observing port](dc_ne_portmirror_cfg_0005.html) and [a mirrored port](dc_ne_portmirror_cfg_0025.html), and [specify the observing port for mirroring](dc_ne_portmirror_cfg_0026.html).
  
  Although you can configure an observing port, configure a mirrored port, and specify the observing port for mirroring in any sequence, you need to perform all these operations. Otherwise, port mirroring cannot take effect. When the mirroring function is not required, you are advised to disable it so that it does not adversely affect other services.

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
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**port-mirroring to**](cmdqueryname=port-mirroring+to) { **null0** | **interface** *interface-type* *interface-number* **observe-index** *observe-index* } { **inbound** | **cpu-packet** | **outbound** } [ **user-defined-filter** *user-defined-filter-id* ]
   
   
   
   Port mirroring is configured in integrated mode.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.