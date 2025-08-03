Configuring an OSPFv3 GR Helper
===============================

Configuring an OSPFv3 GR Helper

#### Prerequisites

Before configuring an OSPFv3 GR helper, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

Graceful restart (GR) is a high availability (HA) technology used to ensure normal traffic forwarding and non-stop forwarding of key services during the restart of routing protocols. HA comprises of a comprehensive set of techniques, such as fault-tolerant redundancy, link protection, faulty node recovery, and traffic engineering. As a fault-tolerant redundancy technology, GR is also widely used to ensure non-stop forwarding of key services during a master/slave main control board switchover or system upgrade.

![](../public_sys-resources/note_3.0-en-us.png) 

GR involves two roles: GR restarter and GR helper. Currently, a device can only function as a GR helper.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Configure the device as a GR helper and specify a filtering policy so that the device functions as the GR helper only for the OSPFv3 neighbors that match the filtering policy. Select either of the following filtering methods based on actual conditions:
   
   
   * Based on an ACL
     1. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
        ```
     2. Create an ACL and enter the ACL view.
        ```
        [acl ipv6](cmdqueryname=acl+ipv6) { name basic-acl6-name basic | [ number ] basic-acl6-number }
        ```
     3. Configure an ACL rule.
        ```
        [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment | source { source-ipv6-address { prefix-length | source-wildcard } | source-ipv6-address/prefix-length | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
        ```
        
        When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
     4. Enter the OSPFv3 view.
        ```
        [ospfv3](cmdqueryname=ospfv3) [ process-id ]
        ```
     5. Implement filtering based on the ACL.
        ```
        [helper-role](cmdqueryname=helper-role) [ acl-number acl-number | acl-name acl-name ]
        ```
   * Based on an IP prefix list
     ```
     [helper-role](cmdqueryname=helper-role) [ ip-prefix ip-prefix-name ]
     ```
4. (Optional) Disable the device from checking LSAs when it functions as a GR helper.
   
   
   ```
   [helper-role](cmdqueryname=helper-role) lsa-checking-ignore
   ```
   
   By default, a device performs strict check on all types of received LSAs.
5. (Optional) Configure the device to support only planned GR when it functions as a GR helper.
   
   
   ```
   [helper-role](cmdqueryname=helper-role) planned-only 
   ```
   
   By default, a GR helper supports both planned GR and unplanned GR.
6. (Optional) Set the maximum restart period allowed by the GR helper.
   
   
   ```
   [helper-role](cmdqueryname=helper-role) max-grace-period period
   ```
   
   By default, the maximum restart period allowed by a GR helper is 120 seconds.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the following command to check the previous configuration:

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **graceful-restart-information** command to check the OSPFv3 GR helper status.