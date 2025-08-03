Enabling OSPFv3 on an Interface
===============================

For an interface with multiple instances, you need to specify which instance on the interface is enabled in the OSPFv3 process when enabling OSPFv3 on the interface.

#### Context

After enabling OSPFv3 in the system view, you need to enable OSPFv3 on the interface.

Because an interface may have multiple instances, you need to specify which instance of the interface is enabled in the OSPFv3 process when OSPFv3 is enabled on the interface. If no instance ID is specified, the value defaults to 0. The same instance must be enabled on the interfaces between which the neighbor relationship is set up.

Perform the following steps on the Router that runs OSPFv3.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospfv3**](cmdqueryname=ospfv3) *process-id* **area** *area-id* [ **instance** *instance-id* ]
   
   
   
   OSPFv3 is enabled on the interface.
   
   
   
   The specified area ID can be a decimal integer or in the IPv4 address format. Regardless of the specified format, the area ID is displayed as an IPv4 address.
4. (Optional) Run [**ospfv3 network-type**](cmdqueryname=ospfv3+network-type) { **broadcast** | **nbma** | **p2mp** [ **non-broadcast** ] | **p2p** } [ **instance** *instance-id* ]
   
   
   
   A network type is configured for the interface.
   
   
   
   When an interface supports multi-instance, specify *instance-id* when enabling OSPFv3 on the interface. If *instance-id* is not specified, the default value 0 is adopted. In this case, the configured network type of the interface is different from the actual network type. This step is mandatory in such a case.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.