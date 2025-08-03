(Optional) Configuring a Cost for IS-IS Interfaces (IPv4)
=========================================================

Configuring IS-IS interface costs can control IS-IS route selection. Set interface costs based on network planning.

#### Context

The costs of IS-IS interfaces can be determined in the following modes (in descending order of priority):

* The interface cost takes effect only on a specified interface.
* The global cost takes effect only on all interfaces.
* The automatically calculated cost is a cost automatically calculated based on the interface bandwidth.

The default cost of an IS-IS interface is 10, and the default cost style is narrow.


#### Procedure

* Configure an IS-IS cost style.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**cost-style**](cmdqueryname=cost-style) { **narrow** | **wide** | **wide-compatible** | { **compatible** | **narrow-compatible** } [ **relax-spf-limit** ] }
     
     
     
     An IS-IS cost style is configured.
     
     
     
     The cost value range of an interface and the cost value range of the routes that can be accepted by the interface vary with the cost style.
     
     + If the cost style is narrow, the cost of an interface ranges from 1 to 63. The maximum cost of the routes accepted by the device is 1023.
     + If the cost style is narrow-compatible or compatible, the cost of an interface ranges from 1 to 63. The cost of the routes accepted by the device is related to **relax-spf-limit**.
       
       - If the **relax-spf-limit** parameter is not set:
         
         If the cost of a route is not greater than 1023 and the costs of all the interfaces through which the route passes are not greater than 63, the actual cost of the route is used.
         
         If the cost of a route is less than or equal to 1023 and the link cost of an interface through which the route passes is greater than 63, an IS-IS device can learn only the routes of the network segment where the interface resides and the routes imported by the interface. The actual cost of the route is used, and subsequent routes forwarded through the interface are discarded.
         
         If the cost of a route is greater than 1023 and the link cost of each interface through which the route passes before the route reaches an interface with the link cost greater than 1023 is not greater than 63, the IS-IS device can learn only the routes of this interface. The local device can learn routes to the network segment where the interface resides and the routes imported by the interface. The route cost is considered as 1023, and subsequent routes forwarded through the interface are discarded.
       - If the **relax-spf-limit** parameter is set:
         
         There is no limit on the link costs of interfaces or route costs. The route is received according to the actual cost.
     + If the cost style is **wide** or **wide-compatible**, the cost of an interface ranges from 1 to 16777214 or the maximum value (16777215). If **maximum** is configured, the neighbor TLV (with the cost 16777215) generated on the link cannot be used for route calculation; instead, it is used only for transmitting TE information. The maximum cost of the routes accepted by the device is 0xFFFFFF.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a cost for the IS-IS interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis**](cmdqueryname=isis) [ **topology** *topology-name* ] **cost** *cost* [ **level-1** | **level-2** ]
     
     
     
     A cost is configured for the IS-IS interface.
     
     The cost set using this command takes effect only on this interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the global IS-IS cost.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**circuit-cost**](cmdqueryname=circuit-cost) { *cost* } [ **level-1** | **level-2** ]
     
     
     
     The global IS-IS cost is configured.
     
     
     
     The cost set using this command takes effect on all interfaces.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable IS-IS to automatically calculate interface costs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**bandwidth-reference**](cmdqueryname=bandwidth-reference) *value*
     
     
     
     The reference value of the bandwidth is configured.
  4. Run [**auto-cost enable**](cmdqueryname=auto-cost+enable) [ **compatible** ]
     
     
     
     The device is enabled to automatically calculate the interface cost.
     
     
     
     + If the cost style of the system is wide or wide-compatible, when [**auto-cost enable**](cmdqueryname=auto-cost+enable) command is configured, Interface cost = (Bandwidth-reference/Interface bandwidth) x 10, and when [**auto-cost enable**](cmdqueryname=auto-cost+enable) **compatible** command is configured, Interface cost = (Bandwidth-reference/Interface bandwidth).![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the interface cost calculated through this formula is greater than 16777214, 16777214 is used as the interface cost for route calculation. That is, the interface cost will never be greater than 16777214.
       
       The [**auto-cost enable**](cmdqueryname=auto-cost+enable) command can be run on Eth-Trunk interfaces as same with on physical interfaces. If the command is run on an Eth-Trunk interface, the bandwidth of the Eth-Trunk interface is equal to the total bandwidth of all its member interfaces.
     + If the cost-style is narrow, narrow-compatible, or compatible, the cost of each interface is determined by the interface bandwidth range. [Table 1](#EN-US_TASK_0172365975__tab_dc_vrp_isis_cfg_100301) lists the interface costs corresponding to different interface bandwidth ranges.
       
       **Table 1** Mapping between IS-IS interface costs and interface bandwidth
       | Cost | Bandwidth Range |
       | --- | --- |
       | 60 | Interface bandwidth â¤ 10 Mbit/s |
       | 50 | 10 Mbit/s < interface bandwidth â¤ 100 Mbit/s |
       | 40 | 100 Mbit/s < interface bandwidth â¤ 155 Mbit/s |
       | 30 | 155 Mbit/s < interface bandwidth â¤ 622 Mbit/s |
       | 20 | 622 Mbit/s < Interface bandwidth â¤ 2.5 Gbit/s |
       | 10 | Interface bandwidth > 2.5 Gbit/s |![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To change the cost of a loopback interface, run the [**isis cost**](cmdqueryname=isis+cost) command only in the loopback interface view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Associate the remaining bandwidth of an IS-IS interface with the link cost.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis**](cmdqueryname=isis) [ **process-id** *process-id-value* ] **cost** *cost-value* { **higher-bandwidth** *higher-bandwidth-value* **cost** *better-cost-value* | **lower-bandwidth** *lower-bandwidth-value* **cost** *worse-cost-value* } \* [ **level-1** | **level-2** ]
     
     
     
     The remaining bandwidth of the IS-IS interface is associated with the link cost.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.