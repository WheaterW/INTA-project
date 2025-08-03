Disabling OSPF Interface Flapping Suppression
=============================================

Disabling OSPF Interface Flapping Suppression

#### Prerequisites

Before disabling OSPF interface flapping suppression, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

OSPF packets are exchanged frequently in cases where an interface carrying OSPF services alternates between up and down, and this compromises the stability of existing interfaces, OSPF services, and other OSPF-dependent services. Interface flapping suppression can address this issue by allowing a device to delay a flapping interface from going up.

OSPF interface flapping suppression is enabled globally by default. However, you can disable this function if it is not required.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable OSPF interface flapping suppression.
   
   
   ```
   [ospf suppress-flapping interface disable](cmdqueryname=ospf+suppress-flapping+interface+disable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration configuration ospf**](cmdqueryname=display+current-configuration+configuration+ospf) command to check the configuration status of OSPF interface flapping suppression.