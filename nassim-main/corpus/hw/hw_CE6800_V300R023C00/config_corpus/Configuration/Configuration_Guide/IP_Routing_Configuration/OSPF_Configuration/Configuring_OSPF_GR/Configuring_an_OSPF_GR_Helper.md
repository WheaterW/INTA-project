Configuring an OSPF GR Helper
=============================

Configuring an OSPF GR Helper

#### Prerequisites

Before configuring an OSPF GR helper, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

Graceful restart (GR) is a high availability (HA) technology used to ensure normal traffic forwarding and non-stop forwarding of key services during the restart of routing protocols. HA comprises of a comprehensive set of techniques, such as fault-tolerant redundancy, link protection, faulty node recovery, and traffic engineering. As a fault-tolerant redundancy technology, GR is widely used to ensure non-stop forwarding of key data during the active/standby switchover and system upgrade.

![](../public_sys-resources/note_3.0-en-us.png) 

GR involves two roles: GR restarter and GR helper. Currently, a device can only function as a GR helper.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
   
   The *process-id* parameter specifies the ID of a process, and the default value is 1.
3. Enable the opaque LSA capability.
   
   
   ```
   [opaque-capability enable](cmdqueryname=opaque-capability+enable)
   ```
   
   OSPF supports OSPF GR by transmitting Type 9 LSAs (opaque LSAs). As such, before configuring OSPF GR, run the [**opaque-capability enable**](cmdqueryname=opaque-capability+enable) command to enable the opaque LSA capability.
4. Configure the device as a GR helper and specify a filtering policy so that the device functions as the GR helper only for the OSPF neighbors that match the filtering policy. Select either of the following filtering methods based on actual conditions:
   
   
   * Based on an ACL
     1. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
        ```
     2. Create an ACL and enter the ACL view.
        ```
        [acl](cmdqueryname=acl) { name basic-acl-name { basic | [ number ] basic-acl-number } | [ number ] basic-acl-number }
        ```
     3. Configure an ACL rule.
        ```
        [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } [ fragment-type fragment | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
        ```
        
        When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
     4. Enter the OSPF view.
        ```
        [ospf](cmdqueryname=ospf) [ process-id ]
        ```
     5. Implement filtering based on the ACL.
        ```
        [graceful-restart](cmdqueryname=graceful-restart) [ helper-role { { acl-number acl-number | acl-name acl-name } * | never } ]
        ```
   * Based on an IP prefix list
     ```
     [graceful-restart](cmdqueryname=graceful-restart) [ helper-role { { ip-prefix  ip-prefix-name * } | never } ]
     ```
5. (Optional) Disable the device from checking AS external LSAs when it functions as a GR helper.
   
   
   ```
   [graceful-restart](cmdqueryname=graceful-restart) helper-role ignore-external-lsa
   ```
   
   By default, a GR helper checks AS external LSAs.
6. (Optional) Configure the device to support only planned GR when it functions as a GR helper.
   
   
   ```
   [graceful-restart](cmdqueryname=graceful-restart) helper-role planned-only
   ```
   
   By default, a GR helper supports both planned GR and unplanned GR.
7. (Optional) Enable the non-IETF mode.
   
   
   ```
   [graceful-restart](cmdqueryname=graceful-restart) non-ietf
   ```
   
   By default, the device uses the IETF standard mode. When the neighbor restarter uses the non-IETF mode, the non-IETF mode must also be enabled on the local device. As the IETF mode and non-IETF mode are mutually exclusive, only one of them can be enabled on a device.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf+graceful-restart) [ *process-id* ] **graceful-restart** [ **verbose** ] command to check the OSPF GR configuration.