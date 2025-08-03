Configuring DCBX
================

Configuring DCBX

#### Context

DCBX encapsulates DCB configurations into LLDP TLVs so that devices at both ends of a link can exchange DCB configurations using LLDP.

When the device connects to a non-Huawei device, the service priorities in the App TLVs must be the same.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support the DCBX function.



#### Prerequisites

Before configuring DCBX, you have completed the following task:

Configure a link layer protocol so that interfaces at both ends of a link are up.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable LLDP globally.
   
   
   ```
   [lldp enable](cmdqueryname=lldp+enable)
   ```
   
   By default, LLDP is disabled globally.
3. Enter the view of the interface for which the function of sending DCBX TLVs is to be enabled.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Enable the function of sending DCBX TLVs.
   
   
   ```
   [lldp tlv-enable dcbx](cmdqueryname=lldp+tlv-enable+dcbx)
   ```
5. (Optional) Set the version number in the DCBX TLVs to be sent.
   
   
   ```
   [dcb compliance](cmdqueryname=dcb+compliance) intel-oui
   ```
   
   Two standards are available for DCBX: IEEE DCBX and Intel DCBX.
   
   By default, an interface sends DCBX TLVs of the IEEE standard version.
6. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. (Optional) Create an App profile and enter the App profile view.
   
   
   ```
   [dcb app-profile](cmdqueryname=dcb+app-profile) profile-name
   ```
   
   By default, no App profile is configured.
8. (Optional) Specify the service priority in the App TLV of DCB packets.
   
   
   ```
   [application](cmdqueryname=application) { fcoe | fip | iscsi | ethtype ethtype-value | [ tcp | udp ] port port } priority priority-value
   ```
   
   By default, the priorities of FCoE and Fibre channel Initialization Protocol (FIP) services are both 3, and the priority of the Internet Small Computer Systems Interface (iSCSI) service is 4.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   PFC must be enabled for the FCoE service priority; otherwise, DCB negotiation may fail.
9. (Optional) Exit the App profile view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
10. (Optional) Enter the view of the interface to which the App profile is to be applied.
    
    
    ```
    [interface](cmdqueryname=interface) interface-type interface-number
    ```
11. (Optional) Apply the App profile to the interface.
    
    
    ```
    [dcb app-profile enable](cmdqueryname=dcb+app-profile+enable) appprofile
    ```
    
    
    
    By default, no App profile is applied to an interface.
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display lldp tlv-config**](cmdqueryname=display+lldp+tlv-config) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command to check TLV types supported by the system or an interface.
* Run the [**display dcb app-profile**](cmdqueryname=display+dcb+app-profile) [ *profile-name* ] command to check the App profile configuration.