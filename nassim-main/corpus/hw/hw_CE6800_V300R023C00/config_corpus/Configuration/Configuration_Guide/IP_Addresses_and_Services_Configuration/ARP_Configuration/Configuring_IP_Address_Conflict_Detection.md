Configuring IP Address Conflict Detection
=========================================

Configuring IP Address Conflict Detection

#### Prerequisites

Before configuring IP address conflict detection, you have completed the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is up.

#### Context

IP address conflicts cause problems such as route flapping and traffic interruptions, affecting user services. IP address conflicts are often caused by incorrect networking or configurations. Customers expect that devices can automatically detect IP address conflicts on a network and immediately notify them of conflict reasons, so they can rapidly eliminate the conflicts and minimize adverse impacts on services.

IP address conflict detection helps you quickly locate and modify conflicting IP addresses and instructs you on how to properly configure and manage the IP addresses of devices.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable IP address conflict detection.
   
   
   ```
   [arp ip-conflict-detect enable](cmdqueryname=arp+ip-conflict-detect+enable)
   ```
3. (Optional) Configure host IP address conflict detection options.
   
   
   ```
   [arp host ip-conflict-check](cmdqueryname=arp+host+ip-conflict-check) period period-value retry-times retry-times-value
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This function is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, and CE6863E-48S8CQ.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display arp**](cmdqueryname=display+arp) [ **network** *network-address* [ *network-mask* | *mask-length* ] ] [ **dynamic** | **static** ] command to check specified ARP entries.
* Run the [**display arp vpn-instance**](cmdqueryname=display+arp+vpn-instance) *vpn-instance-name* [ **dynamic** | **static** ] command to check ARP entries of a VPN instance.