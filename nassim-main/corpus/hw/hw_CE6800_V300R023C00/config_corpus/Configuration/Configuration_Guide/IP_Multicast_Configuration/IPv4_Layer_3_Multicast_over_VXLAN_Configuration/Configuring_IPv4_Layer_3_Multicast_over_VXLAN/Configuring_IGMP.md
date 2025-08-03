Configuring IGMP
================

Configuring IGMP

#### Context

To forward multicast data based on local Layer 2 multicast entries after VXLAN decapsulation, a VXLAN gateway must be capable of forwarding both Layer 2 and Layer 3 multicast traffic. In this case, IGMP and related parameters must be configured on the corresponding VBDIF interface.

![](public_sys-resources/note_3.0-en-us.png) 

After IGMP is configured on a VBDIF interface, IGMP snooping is automatically enabled in the corresponding BD. To check IGMP snooping information, run the [**display igmp snooping**](cmdqueryname=display+igmp+snooping) **bridge-domain** *bd-id* command. If you manually modify IGMP snooping configurations in the BD view, the modification does not take effect. Instead, the configurations inherited from the VBDIF interface still take effect.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VBDIF interface view.
   
   
   ```
   [interface vbdif](cmdqueryname=interface+vbdif) bd-id
   ```
3. Enable PIM-SM.
   
   
   ```
   [pim sm](cmdqueryname=pim+sm)
   ```
4. Enable IGMP.
   
   
   ```
   [igmp enable](cmdqueryname=igmp+enable)
   ```
   
   By default, IGMP is not enabled on interfaces.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

Configure IGMP-related functions as needed. Perform interface configurations in the VBDIF interface view. For details, see [IGMP Configuration](vrp_igmp_cfg_0001.html). The following configuration tasks are not supported:

* Configure IGMP static-group join.
* Configure IGMP host tracking.
* Configure IGMP on-demand.