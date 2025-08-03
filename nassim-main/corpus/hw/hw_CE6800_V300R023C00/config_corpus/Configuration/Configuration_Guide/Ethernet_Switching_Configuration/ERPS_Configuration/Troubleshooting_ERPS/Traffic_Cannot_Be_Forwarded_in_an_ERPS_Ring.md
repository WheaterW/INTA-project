Traffic Cannot Be Forwarded in an ERPS Ring
===========================================

Traffic Cannot Be Forwarded in an ERPS Ring

#### Fault Symptom

After ERPS is configured, service traffic cannot be forwarded because the ERPS ring status is abnormal.


#### Procedure

1. Check ERPS ring information on the local device in any view.
   
   
   ```
   [display erps](cmdqueryname=display+erps) [ ring ring-id ] verbose
   ```
   
   
   
   Under normal circumstances, an ERPS ring has only one RPL owner port, other ports are common ports or RPL neighbour ports, and **Ring State** of each node on the ring is **Idle** in the command output.
   
   
   
   If the ERPS ring is incomplete or abnormal:
   
   1. Check whether all devices on the ERPS ring are added to the ERPS ring.
   2. Check whether devices on the ERPS ring have the same ERPS ring configuration, including the ERPS version, major ring, and sub-ring configurations.
   3. Check whether port roles, control VLANs, and ERP instances are correctly configured on all devices on the ERPS ring.
   4. Check whether ports are configured to allow packets from the specified data VLAN to pass through.