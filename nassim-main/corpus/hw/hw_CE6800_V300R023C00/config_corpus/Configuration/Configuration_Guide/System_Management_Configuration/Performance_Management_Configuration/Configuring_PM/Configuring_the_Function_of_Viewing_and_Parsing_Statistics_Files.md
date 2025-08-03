Configuring the Function of Viewing and Parsing Statistics Files
================================================================

Configuring the Function of Viewing and Parsing Statistics Files

#### Context

By default, statistics files are saved to flash:/pmdata. Statistics files can be in text or xml format Statistics files are named in the format of *tasknameyyyymmddhhmmindexnum.***xxx**, where *xxx* represents either **txt** or **xml** depending on the file type. You can view and parse statistics files to analyze statistics and learn about a device's running status.


#### Procedure

1. View the list of generated statistics files.
   
   
   ```
   [display pm statistics-file](cmdqueryname=display+pm+statistics-file) [ task-name ]
   ```
2. Set the current working directory to **pmdata**.
   
   
   ```
   [cd pmdata](cmdqueryname=cd+pmdata) 
   ```
3. View a statistics file's content.
   
   
   ```
   [more](cmdqueryname=more) filename [offset]
   ```
4. Parse the content of a statistics file.
   
   The following is an example of a statistics file:
   ```
   2020-02-21 14:08:25.371                                                         
   FileFormatVersion=1.0                                                           
   SysName=HUAWEI                                                                  
   Release_Number=V300R023C00                                                    
   Start_Time=2020-02-21 13:00,2020-02-21 13:05,2020-02-21 13:10                   
   Statics_Interval=5                                                              
   Resource_type=6                                                                 
   Total_rows=3                                                                    
   Index List:                                                                     
   Index_rows=1                                                                    
   100GE1/0/1                                                                       
   Indicator List:                                                                 
   Indicator_rows=41                                                               
   393217                                                                          
   393218                                                                          
   393219                                                                          
   393220                                                                          
   393221                                                                          
   393222                                                                          
   393223                                                                          
   393224                                                                          
   393225                                                                          
   393226                                                                          
   393227                                                                          
   393228                                                                          
   393229                                                                          
   393230                                                                          
   393232                                                                          
   393233                                                                          
   393234                                                                          
   393235                                                                          
   393236                                                                          
   393237                                                                          
   393238                                                                          
   393239                                                                          
   393240                                                                          
   393241                                                                          
   393242                                                                          
   393243                                                                          
   393244                                                                          
   393245                                                                          
   393246                                                                          
   393247                                                                          
   393248                                                                          
   393249                                                                          
   393250                                                                          
   393251                                                                          
   393256                                                                          
   393257                                                                          
   393258                                                                          
   393252                                                                          
   393253                                                                          
   393254                                                                          
   393255                                                                          
   Value:                                                                          
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1410065408,2,1,0,0,0,0,0,0,0,0,0,0
   ,0,E3,E3,E3,E3                                                                  
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1410065408,2,1,0,0,0,0,0,0,0,0,0,0
   ,0,E3,E3,E3,E3                                                                  
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1410065408,2,1,0,0,0,0,0,0,0,0,0,0
   ,0,E3,E3,E3,E3   
   ```
   
   [Table 1](#EN-US_TASK_0000001513034098__tab_dc_vrp_logs_cfg_202401) describes the format of a statistics file.
   
   **Table 1** Format of a statistics file
   | Item | Description |
   | --- | --- |
   | 2020-02-21 14:08:25.371 | Date and time when the statistics file was generated. |
   | FileFormatVersion | Version number of the statistics file. |
   | SysName | Device name. |
   | Release\_Number | Version number. |
   | Start\_Time | Time when statistics were collected. |
   | Statics\_Interval | Performance statistics collection interval, in minutes. |
   | Resource\_type | ID of a statistics object type. |
   | Total\_rows | Number of performance statistics collection intervals x Number of performance statistics instances. |
   | Index List | List of statistics instances. |
   | Index\_rows | Number of statistics instances. |
   | Indicator List | List of statistics indicators. |
   | Indicator\_rows | Number of statistics indicators. |
   | Value | Statistics indicator data. |