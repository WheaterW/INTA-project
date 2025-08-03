Configuring a DiffServ Domain
=============================

Configuring a DiffServ Domain

#### Context

When the device is used as an edge node connecting the DiffServ domain and another network, you need to configure mappings between internal and external priorities.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a DiffServ domain and enter the DiffServ domain view, or enter the view of an existing DiffServ domain.
   
   
   ```
   [diffserv domain](cmdqueryname=diffserv+domain) ds-domain-name
   ```
   
   
   
   The domain **default** defines default mappings between external priorities and internal or drop priorities. You can modify the mappings defined in the domain **default**, but you cannot delete this domain.
3. Run the following commands as required.
   
   
   
   | Operation | Command |
   | --- | --- |
   | Map the 802.1p value of an incoming VLAN packet to an internal priority and color the packet. | [**8021p-inbound**](cmdqueryname=8021p-inbound) *8021p-value* **phb** *service-class* [ *color* ] |
   | Map the internal priority or drop priority to the 802.1p value of VLAN packets in the outbound direction. | [**8021p-outbound**](cmdqueryname=8021p-outbound) *service-class* *color* **map** *8021p-value* |
   | Map DSCP values of incoming IP packets to internal priorities and color the packets. | [**ip-dscp-inbound**](cmdqueryname=ip-dscp-inbound) *dscp-value* **phb** *service-class* [ *color* ] |
   | Map the internal priority or drop priority to the DSCP value of IP packets in the outbound direction. | [**ip-dscp-outbound**](cmdqueryname=ip-dscp-outbound) *service-class* *color* **map** *dscp-value* |
   
   For details about the default priority mappings, see [Default Settings for Priority Mapping](galaxy_qos_priority_mapping_cfg_0005.html).
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```