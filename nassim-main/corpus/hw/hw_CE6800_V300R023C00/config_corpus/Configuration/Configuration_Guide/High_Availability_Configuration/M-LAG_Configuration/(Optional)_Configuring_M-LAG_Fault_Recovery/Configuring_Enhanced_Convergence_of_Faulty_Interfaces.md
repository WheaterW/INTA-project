Configuring Enhanced Convergence of Faulty Interfaces
=====================================================

Configuring Enhanced Convergence of Faulty Interfaces

#### Context

To ensure switchback performance, you can set the delay and automatic recovery interval for an M-LAG member interface to report its up state if an M-LAG member device fails, a card resets, or the peer-link recovers from a fault. M-LAG member interfaces will automatically go up in ascending order of their M-LAG IDs, ensuring that M-LAG member interfaces go up at different time points, and that entries of each service are delivered without affecting each other.

To improve device performance when a device is single-homed to the M-LAG and the connected M-LAG member interface is down or when an M-LAG single-homing interface is changed to a dual-homing interface and there are a large number of M-LAG interfaces on the entire network, configure the local or peer M-LAG member device not to delete the corresponding MAC address on its peer-link interface.


#### Procedure

* Configure the delay for the M-LAG member interface to report the up state and the automatic recovery interval.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the DFS group view.
     
     
     ```
     [dfs-group](cmdqueryname=dfs-group) dfs-group-id
     ```
  3. Configure the delay for the M-LAG member interface to report the up state and the automatic recovery interval.
     
     
     ```
     [m-lag up-delay](cmdqueryname=m-lag+up-delay) updelay [ auto-recovery interval intervaltime ]
     ```
     
     By default, the delay for the M-LAG member interface to report the up state is 240 seconds, and the automatic recovery interval is 0 seconds.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     If you need to change the default configuration, you are advised to set the delay for an M-LAG member interface to report the up state to 30 seconds or longer.
     
     If the **[**set up-delay**](cmdqueryname=set+up-delay)** command is also configured on a physical member interface of the M-LAG member interface, the delay configured using the **[**m-lag up-delay**](cmdqueryname=m-lag+up-delay)** command takes effect.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the local or peer M-LAG member device not to delete the corresponding MAC address on its peer-link interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the DFS group view.
     
     
     ```
     [dfs-group](cmdqueryname=dfs-group) dfs-group-id
     ```
  3. Configure the device not to delete the corresponding MAC address on its peer-link interface.
     
     
     ```
     [peer-link mac-address remain enable](cmdqueryname=peer-link+mac-address+remain+enable) { paired-port | unpaired-port }
     ```
     
     By default, the local or peer M-LAG member device is not triggered to delete the corresponding MAC address on its peer-link interface under certain conditions.