Disabling OSPFv3 Interface Flapping Suppression
===============================================

Disabling OSPFv3 Interface Flapping Suppression

#### Prerequisites

Before disabling OSPFv3 interface flapping suppression, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

OSPF packets are exchanged frequently in cases where an interface carrying OSPFv3 services alternates between up and down, and this compromises the stability of existing interfaces, OSPFv3 services, and other OSPFv3-dependent services. Interface flapping suppression can address this issue by allowing a device to delay a flapping interface from going up.

OSPFv3 interface flapping suppression is enabled globally by default. However, you can disable this function if it is not required.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable OSPFv3 interface flapping suppression.
   
   
   ```
   [ospfv3 suppress-flapping interface disable](cmdqueryname=ospfv3+suppress-flapping+interface+disable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration configuration ospfv3**](cmdqueryname=display+current-configuration+configuration+ospfv3) command to check the status of OSPFv3 interface flapping suppression.