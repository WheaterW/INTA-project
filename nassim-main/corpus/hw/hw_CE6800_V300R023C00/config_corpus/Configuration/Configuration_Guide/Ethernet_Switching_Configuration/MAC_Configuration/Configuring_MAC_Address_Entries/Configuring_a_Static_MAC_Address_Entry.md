Configuring a Static MAC Address Entry
======================================

Configuring a Static MAC Address Entry

#### Context

A device cannot distinguish packets from authorized and unauthorized users when it learns source MAC addresses of packets to maintain the MAC address table. This causes network risks. If an unauthorized user uses the MAC address of an authorized user as the source MAC address of attack packets and connects to another interface of the device, the device learns an incorrect MAC address entry. As a result, packets destined for the authorized user are forwarded to the unauthorized user. For security purposes, you can create static MAC address entries to bind MAC addresses of authorized users to specified interfaces. This prevents unauthorized users from intercepting the data of authorized users.

Static MAC address entries have the following characteristics:

* A static MAC address entry will not age out, and will not be lost after a system restart, and can only be deleted manually.
* The VLAN specified in a static MAC address entry must have been created and the interface bound to the entry must have been added to the VLAN.
* The MAC address in a static MAC address entry must be a unicast MAC address, and cannot be a multicast or broadcast MAC address.
* Static MAC address entries take precedence over dynamic MAC address entries. The system discards packets with flapping static MAC addresses.![](public_sys-resources/note_3.0-en-us.png) 
  
  The CE6885-LL (low latency mode) does not support this function.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a static MAC address entry.
   
   
   * Configure a static MAC address entry with a VLAN specified.
     ```
     [mac-address static](cmdqueryname=mac-address+static) mac-address interface-type interface-number vlan vlan-id
     ```
   * Configure a static MAC address entry with a BD specified.
     ```
     [mac-address static](cmdqueryname=mac-address+static) mac-address interface-type interface-number bridge-domain bd-id [ vid pe-vid ]
     ```
     
     This command is supported only by the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM and CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display mac-address static**](cmdqueryname=display+mac-address+static) **vlan** *vlan-id* [ **verbose** ] command to check static MAC address entries configured based on a specified VLAN.
* Run the [**display mac-address static**](cmdqueryname=display+mac-address+static) **bridge-domain** *bd-id* [ **verbose** ] command to check static MAC address entries configured based on a specified BD.
  
  This command is supported only by the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM and CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.