Suppressing the Advertisement of Interface IP Addresses
=======================================================

Suppressing the Advertisement of Interface IP Addresses

#### Prerequisites

Before suppressing the advertisement of interface IP addresses, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

On an OSPF network, if a device only requires an interface to establish a neighbor relationship with another device, and you want to hide the IP address of the interface from external devices, you can suppress the advertisement of the interface IP address. This allows an interface of an external device to use the same IP address.


#### Procedure

* Suppress the advertisement of all interface IP addresses in the OSPF process.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the OSPF view.
     
     
     ```
     [ospf](cmdqueryname=ospf) [ process-id ]
     ```
     
     The *process-id* parameter specifies the ID of a process, and the default value is 1.
  3. Suppress the advertisement of all interface IP addresses in the OSPF process.
     
     
     ```
     [suppress-reachability](cmdqueryname=suppress-reachability)
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Suppress the advertisement of the IP address of a specified interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Suppress the advertisement of the IP address of the specified interface.
     
     
     ```
     [ospf suppress-reachability](cmdqueryname=ospf+suppress-reachability)
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **verbose** ] command to check OSPF interface information.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command to check OSPF routing table information.