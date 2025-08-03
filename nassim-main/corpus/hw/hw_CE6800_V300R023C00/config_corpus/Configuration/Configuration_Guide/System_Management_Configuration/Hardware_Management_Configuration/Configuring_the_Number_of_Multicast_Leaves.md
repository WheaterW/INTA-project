Configuring the Number of Multicast Leaves
==========================================

Configuring the Number of Multicast Leaves

#### Context

The AIB table and ELB table share forwarding table resources of a chip. Specifically, entries related to the ARP, ND, VXLAN, and IP tunnel services are stored in the AIB table, while entries of multicast services, such as VLAN, Layer 3 multicast, and VXLAN, are stored in the ELB table. You can configure the number of multicast leaves in the ELB table to meet the requirements for multicast leaves in different scenarios.

![](public_sys-resources/note_3.0-en-us.png) 

This configuration is supported only by the following: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.



#### Procedure

1. Enter the system view.
   
   
   ```
   system-view
   ```
2. Configure the number of multicast leaves.
   
   
   ```
   [assign forward multicast-leaf](cmdqueryname=assign+forward+multicast-leaf) { 64 | 80 | 96 | 112 | 128 }
   ```
   
   The number of multicast leaves is defaulted to 64K.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
4. Exit the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Restart the device for the configuration to take effect.
   
   
   ```
   [reboot](cmdqueryname=reboot)
   ```

#### Verifying the Configuration

Run the [**display forward multicast-leaf**](cmdqueryname=display+forward+multicast-leaf) command to check the number of multicast leaves.