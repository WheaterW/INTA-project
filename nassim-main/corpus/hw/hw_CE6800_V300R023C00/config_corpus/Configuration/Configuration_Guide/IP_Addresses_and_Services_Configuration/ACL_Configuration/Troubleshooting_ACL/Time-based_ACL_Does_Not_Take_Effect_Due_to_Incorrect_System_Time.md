Time-based ACL Does Not Take Effect Due to Incorrect System Time
================================================================

Time-based ACL Does Not Take Effect Due to Incorrect System Time

#### Fault Symptom

The system time on the device is incorrect, making the time-based ACL ineffective.


#### Procedure

1. Check ACL rules in the system view.
   
   
   ```
   [display acl all](cmdqueryname=display+acl+all)
   ```
   
   The following time-based ACL rule is included:
   
   ```
   rule 10 deny ip source 192.168.1.1 0 time-range time1 //Reject the packets from 192.168.1.1 within the time range time1.
   ```
2. Check the configuration of the time range **time1** in the system view.
   
   
   ```
   [display time-range time1](cmdqueryname=display+time-range+time1)
   ```
   
   The following information is displayed:
   
   ```
   Current time is 14:53:17 1-18-2019 Friday                                       
   
   Time-range: time1 ( Inactive )                                                  
   from 00:00 2020/1/1 to 23:59 2020/12/31                                         
   Total time-range number is 1 
   ```
   
   The time range **time1** starts at 00:00 on January 1, 2020 and ends at 23:59 on December 31, 2020. However, the system time is 14:53:17 on January 18, 2019, which is not the actual date (January 18, 2020) and is not within the time range **time1**. Therefore, the ACL associated with **time1** does not take effect, and packets from 192.168.1.1 are not discarded.
3. Change the system date and time.
   
   
   * Run the **clock datetime** command in the user view to change the system date and time to the actual ones.
     
     ```
     clock datetime 14:53:17 2020-02-10 //Change the date to 2020-02-10.
     ```
   * Configure NTP to enable automatic clock synchronization on the device, so that the device can synchronize its clock with a trusted device (which has been synchronized with an authoritative clock through the network).
     
     1. On the trusted device, configure the local clock as the NTP master clock and set a clock stratum for it. For details, see "NTP Configuration" in Configuration Guide > System Management Configuration.
     2. On the device that needs to synchronize its clock with the trusted device, configure an NTP working mode. For details, see "NTP Configuration" in Configuration Guide > System Management Configuration.