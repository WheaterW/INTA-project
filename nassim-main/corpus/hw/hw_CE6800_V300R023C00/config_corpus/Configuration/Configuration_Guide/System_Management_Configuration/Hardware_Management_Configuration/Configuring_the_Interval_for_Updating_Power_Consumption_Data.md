Configuring the Interval for Updating Power Consumption Data
============================================================

Configuring the Interval for Updating Power Consumption Data

#### Context

The system calculates the average power consumption at a specified interval. If real-time power consumption is required, configure a short interval for updating power consumption data.


#### Procedure

1. (Optional) Check the interval for updating power consumption data.
   
   
   ```
   [display device power system](cmdqueryname=display+device+power+system)
   ```
2. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
3. Configure an interval for updating power consumption data.
   
   
   ```
   [device power manage cycle](cmdqueryname=device+power+manage+cycle) cycle-value
   ```
   
   By default, the interval for updating power consumption data is 1 hour.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display device power system**](cmdqueryname=display+device+power+system) command to check the **Power manage cycle** field, which indicates the interval for updating power consumption data.