(Optional) Configuring an iNOF Host Access Interface Whitelist
==============================================================

(Optional) Configuring an iNOF Host Access Interface Whitelist

#### Context

In the iNOF system, you can configure an iNOF host access interface whitelist and one or more exception interfaces to allow access only from authorized hosts.

* If you do not enable the iNOF host access interface whitelist function, the configured whitelist and exception interfaces do not take effect.
* If you enable the iNOF host access interface whitelist function, host access to iNOF is controlled as follows:
  + Access through an exception interface: A host can access the iNOF through such an interface without being restricted by the whitelist.
  + Access through a non-exception interface:
    - If a host and its access interface are configured in the whitelist, the host can access the iNOF only through the specified interface.
    - If a host is not configured in the whitelist, the host is denied access to the iNOF.

![](public_sys-resources/note_3.0-en-us.png) 

The iNOF host access interface whitelist and exception interfaces can be configured and the iNOF host access interface whitelist function can be enabled on both the reflector and client. The whitelist information, exception interface information, and whether the function is enabled on a device only come from the related configuration on this device, and cannot be synchronized from other devices.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the AI service and enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
   
   By default, the AI service is disabled.
3. Enable iNOF and enter the iNOF view.
   
   
   ```
   [inof](cmdqueryname=inof)
   ```
   
   By default, iNOF is disabled.
4. Enter the iNOF host access interface whitelist view.
   
   
   ```
   [access-filter](cmdqueryname=access-filter)
   ```
5. Configure a whitelist of interfaces through which hosts access the iNOF.
   
   
   ```
   [host](cmdqueryname=host) ip-address [ to ip-address ] interface { interface-name | interface-type interface-number }
   ```
   
   By default, no such interface whitelist is configured.
6. Configure exception interfaces for the iNOF host access interface whitelist.
   
   
   ```
   [exclude interface](cmdqueryname=exclude+interface) { interface-name | interface-type interface-number } [ to { interface-name | interface-type interface-number } ]
   ```
   
   By default, no exception interface is configured for the iNOF host access interface whitelist.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * Only physical interfaces and Eth-Trunk interfaces can be configured as host access interfaces in the iNOF host access interface whitelist. If the configured host access interface is an Eth-Trunk interface, the specified host can access the iNOF through any member interface of the Eth-Trunk interface.
   * Only physical interfaces can be configured as exception interfaces of the iNOF host access interface whitelist.
   * An interface cannot be added to the iNOF host access interface whitelist while being configured as an exception interface of the iNOF host access interface whitelist.
   * When a host needs to connect to two devices in the M-LAG and the iNOF host access interface whitelist function is enabled on the two M-LAG devices, perform either of the following operations on both M-LAG devices:
     + Run the **host interface** command to configure the host with the specified IP address to access the iNOF through the M-LAG member interface of the local M-LAG device.
     + Run the **exclude interface** command to specify the M-LAG member interface as an exception interface of the iNOF host access interface whitelist.
7. Exit the iNOF host access interface whitelist view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Enable the iNOF host access interface whitelist function.
   
   
   ```
   [access-filter enable](cmdqueryname=access-filter+enable)
   ```
   
   By default, the iNOF host access interface whitelist function is disabled.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```