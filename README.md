# emergencyVehicle

Windows system installation 

You can get SUMO on Windows either by running the official MSI installer (or extracting the portable ZIP), then setting up your PATH and SUMO_HOME. OMNeT++ ships as a self-contained ZIP with MinGW/MSYS and a ready-to-run shell—just extract it to a path without spaces, launch `mingwenv.cmd`, and run the familiar `./configure` → `make`. Finally, INET can be pulled straight into the IDE via **Help → Install Simulation Models**, or you can clone the Git repo and build it by hand in the same MSYS shell. Below are step-by-step instructions.

## Prerequisites

- **Windows version**: 64-bit Windows 10 or newer, with administrator privileges.  
- **Java JDK 8**: Required by the OMNeT++ IDE (Eclipse Neon).  
- **MSYS2/MinGW64**: OMNeT++ includes MinGW, but if you prefer a standalone environment (or need updated tools), install MSYS2 first:  
  1. Download `msys2-x86_64-*.exe` and run the installer.  
  2. Follow prompts to install to a short, no-spaces path (e.g., `C:\msys64`).  ([MSYS2](https://www.msys2.org/?utm_source=chatgpt.com))  
- **Git**: To clone INET manually (optional).  
- **7-Zip or WinRAR**: To extract ZIP archives (SUMO, OMNeT++, INET).

## Step 1: Install SUMO 1.22 on Windows

1. **Download** the Windows binaries from the official SUMO site:  
   - MSI installer: `sumo-win64-1.22.0.msi`  
   - ZIP archive: `sumo-win64-1.22.0.zip`  
   - “Extra” GPL versions also available as `.msi` or `.zip`.  
2. **Install or extract**:  
   - With admin rights, run the MSI.  
   - Without admin rights, extract the ZIP to a folder of your choice using 7-Zip.  ([Installing - SUMO Documentation - DLR]
  
3. **Set environment variables**:  
   1. Open **System Properties → Advanced → Environment Variables**.  
   2. Edit your **Path** user variable and append:  
      ```
      C:\Program Files\sumo-1.22.0\bin
      ```  
   3. Create a new user variable **SUMO_HOME** pointing to:  
      ```
      C:\Program Files\sumo-1.22.0
      ```  
   4. Close and reopen any command prompts.  
  
4. **Verify** by opening `cmd.exe` and running:  
   ```bash
   sumo --version
   ```  
   You should see “SUMO Version 1.22.0”.

## Step 2: Install OMNeT++ 5.6.2 on Windows

1. **Download** the Windows source+IDE+MinGW bundle:  
   ```
   https://github.com/omnetpp/omnetpp/releases/download/omnetpp-5.6.2/omnetpp-5.6.2-src-windows.zip
   ```    
2. **Extract** the ZIP to a folder without spaces, e.g., `C:\omnetpp-5.6.2`.  ([[PDF] Installation Guide - Version 4.6 - Index of - OMNeT++](https://doc.omnetpp.org/omnetpp4/InstallGuide.pdf?utm_source=chatgpt.com))  
3. **Launch the MSYS shell** by double-clicking `mingwenv.cmd` in that folder. This shell comes pre-configured with MinGW gcc and Unix tools.  ([OMNeT++ - Simulation Manual - Index of](https://doc.omnetpp.org/omnetpp/manual/?utm_source=chatgpt.com))  
4. In the MSYS prompt, initialize the environment and build:  
   ```bash
   ./setenv
   ./configure
   make
   ```  
      
5. **Run the IDE** by typing:  
   ```bash
   omnetpp
   ```  
   The Eclipse-based IDE should open without errors.

> **Note**: If you ever need newer GNU tools, you can install MSYS2 first and then use its shell instead of the bundled one.

## Step 3: Add the INET Framework

### 3.1 IDE “Install Simulation Models” Method

1. In the OMNeT++ IDE, select **Help → Install Simulation Models**.  
2. Choose **INET**, then follow the prompts. The IDE will download, unpack, and build INET automatically.  ([Installing INET - INET Framework - OMNeT++]  

### 3.2 Manual Clone & Build Method (Optional)

1. From your MSYS or MSYS2 shell, clone the INET repository:  
   ```bash
   git clone https://github.com/inet-framework/inet.git
   cd inet
   ```  
      
2. (Optional) Install Python requirements if you plan to use Python tools:  
   ```bash
   pip install -r python/requirements.txt
   ```  
3. Generate makefiles and build:  
   ```bash
   make makefiles
   make
   ```  
4. Import the `inet` project into the OMNeT++ IDE (File → Import → Existing Projects).

## Verification

- **SUMO**: `sumo --version` returns 1.22.0.  
- **OMNeT++**: Launching `omnetpp` opens the IDE, and sample simulations in `samples/` run without errors.  
- **INET**: The **INET** project builds cleanly in the IDE (green checkmarks) and you can run examples like **aloha**.

You now have a fully functioning Windows setup with SUMO 1.22, OMNeT++ 5.6.2, and the INET framework—ready for traffic and network simulations!


Ubuntu system installation.

You can install SUMO 1.22 on Ubuntu either via the official PPA or by building from source with CMake; OMNeT++ 5.6.2 requires installing a set of development tools (C/C++ compiler, Java JDK 8, Qt, etc.), downloading the appropriate source archive, running `./configure` and `make`, then launching the IDE; finally, the INET framework can be added either through the OMNeT++ IDE’s “Install Simulation Models” dialog or manually by cloning the GitHub repository and building it with `make makefiles` and `make`.  

## Prerequisites

### System and Compiler  
- **Linux distribution**: Ubuntu 20.04 or later (or Debian-based) is recommended.  
- **C++11 compiler**: g++ 4.8+ or clang++ enabled for C++11 support .  
- **CMake**: version 3.5 or higher to configure SUMO builds.
- **Python 3**: Python 3 headers and pip for SUMO tools and INET’s Python requirements.  

### Java and Qt for OMNeT++  
- **Java**: JDK 8 (Java SE 8) is required by the OMNeT++ IDE  ([How to install OMNET++ 5.6.2](https://omnet-manual.com/omnet-5-6-2-installation-steps/?utm_source=chatgpt.com)).  
- **Qt5**: Qt5 development packages (e.g., `qt5-default`, `libqt5opengl5-dev`) for the OMNeT++ GUI  ([Install Omnet++ on debian/ubuntu - GitHub Gist](https://gist.github.com/mido3ds/cfff3d58042e8b728031cd9333305392?utm_source=chatgpt.com)).  

### Other Development Libraries  
Install OMNeT++ build dependencies in one line on Ubuntu:  
```bash
sudo apt update && sudo apt install -y build-essential gcc g++ bison flex \
  perl python3 python3-pip qt5-default libqt5opengl5-dev tcl-dev tk-dev \
  libxml2-dev zlib1g-dev default-jre doxygen graphviz wget tar qtbase5-dev \
  qt5-qmake libopenscenegraph-dev libosgearth-dev
```    

## Step 1: Install SUMO 1.22

### 1.1 Ubuntu Binary via PPA  
1. Add the SUMO stable PPA and update:  
   ```bash
   sudo add-apt-repository ppa:sumo/stable
   sudo apt-get update
   ```  
2. Install SUMO and its tools/docs:  
   ```bash
   sudo apt-get install sumo sumo-tools sumo-doc
   ```    

### 1.2 Build from Source  
1. Install build tools and libraries:  
   ```bash
   sudo apt-get install git
   git clone --recursive https://github.com/eclipse-sumo/sumo
   cd sumo
   export SUMO_HOME="$PWD"
   sudo apt-get install $(cat build_config/build_req_deb.txt build_config/tools_req_deb.txt)
   ```  
2. Configure and build:  
   ```bash
   cmake -B build .
   cmake --build build -j$(nproc)
   ```  
3. (Optional) Install into your system:  
   ```bash
   sudo cmake --install build
   export SUMO_HOME=/usr/local/share/sumo
   ```  
   

## Step 2: Install OMNeT++ 5.6.2

### 2.1 Download and Extract  
```bash
wget -c https://github.com/omnetpp/omnetpp/releases/download/omnetpp-5.6.2/omnetpp-5.6.2-src-linux.tgz
tar xzf omnetpp-5.6.2-src-linux.tgz
cd omnetpp-5.6.2
```  
   

### 2.2 Configure and Build  
1. Source the OMNeT++ environment:  
   ```bash
   source setenv
   ```  
2. Run the configuration script:  
   ```bash
   ./configure
   ```  
3. Compile OMNeT++:  
   ```bash
   make
   ```  
4. Launch the OMNeT++ IDE:  
   ```bash
   omnetpp
   ```  
   

## Step 3: Install the INET Framework

### 3.1 Using the OMNeT++ IDE  
1. Open the OMNeT++ IDE (`omnetpp`).  
2. Go to **Help → Install Simulation Models**.  
3. Select **INET**, then follow the prompts.  
4. The IDE will download, unpack, and build INET automatically.  
   

### 3.2 Manual Installation  
1. Clone the INET repository and change directory:  
   ```bash
   git clone https://github.com/inet-framework/inet.git
   cd inet
   source setenv
   ```  
2. Install Python requirements:  
   ```bash
   pip install -r python/requirements.txt
   ```  
3. Generate makefiles and build:  
   ```bash
   make makefiles
   make
   ```  
## Verification

- **SUMO version**:  
  ```bash
  sumo --version
  ```  
  Should display “SUMO Version 1.22.0”.    

- **OMNeT++ launch**:  
  Typing `omnetpp` should open the IDE without errors.    

- **INET build**:  
  No errors should occur when running `make` in the INET directory, and you’ll find compiled libraries in `src/`.  



To run the simulation :


To run your co‐simulation, you must first start SUMO (or SUMO-GUI) configured to accept two TraCI clients on port 9999. Next, launch your OMNeT++ simulation so its TraCI client connects as the first client. Then, execute your Python script—which uses the TraCI API—to connect as the second client and drive additional logic. Finally, you can observe and analyze the integrated simulation in both SUMO-GUI and the OMNeT++ runtime (Qtenv or Cmdenv).  

## 1. Launch SUMO on port 9999 for two clients

### Windows & Linux (Ubuntu)

1. **Open a terminal** (Windows CMD/PowerShell or Ubuntu shell).  
2. **Navigate** to the directory containing the SUMO executables (or ensure `sumo`/`sumo-gui` is in your `PATH`).  
3. **Run** SUMO (headless) or SUMO-GUI with the remote‐port and client count flags:  
   ```bash
   sumo-gui -c path/to/yourConfig.sumocfg \
            --remote-port 9999 \
            --num-clients 2
   ```
   Or, for headless:
   ```bash
   sumo -c path/to/yourConfig.sumocfg \
        --remote-port 9999 \
        --num-clients 2
   ```  
     
4. **Wait** until SUMO reports it’s listening (you’ll see “listening on port 9999” in the console).

## 2. Start your OMNeT++ simulation (first TraCI client)

1. **Open** the OMNeT++ IDE (or an MSYS2 shell on Windows):  
   ```bash
   omnetpp       # launches the IDE GUI
   ```
2. **Configure** your simulation’s TraCI manager (e.g., in Veins’ `TraCIScenarioManager.ned` or your `omnetpp.ini`):
   ```ini
   *.manager.configFile = "path/to/yourConfig.sumocfg"
   *.manager.tcpPort     = 9999
   *.manager.numClients  = 2
   ```
3. **Build** and **run** your simulation from the IDE or CLI.  
   - **CLI** example (Cmdenv):
     ```bash
     opp_run -u Cmdenv -f omnetpp.ini
     ```
        
4. OMNeT++ will connect to SUMO on port 9999 as **client 1**, send its initialization commands, and block on `simulationStep` until all clients are connected.

## 3. Run your Python TraCI code (second TraCI client)

1. **Ensure** `SUMO_HOME` is set (e.g., via your environment variables):  
   ```bash
   export SUMO_HOME=/path/to/sumo
   ```
  
2. **Run** the script in your IDE or terminal:  
   ```bash
   python my_traci_script.py
   ```
   It will connect as **client 2**, synchronize on each `simulationStep()`, and then close.

## 4. Observe and study the integrated simulation

- **SUMO-GUI**: Watch vehicle movements, traffic lights, and any dynamic changes in real time.  
- **OMNeT++ Qtenv**: See packet exchanges, node mobility, and network-layer events synchronized with SUMO time.  
- **Cmdenv logs**: Examine console output or log files for scalar/vector results.  
- **Post-processing**: Use Python or MATLAB/R to parse output vector and scalar files for in-depth analysis.  

By following these steps—starting SUMO with `--num-clients 2`, launching OMNeT++ as client 1, running your Python TraCI script as client 2, and then exploring both GUIs and log outputs—you’ll achieve a fully synchronized co-simulation ready for study and further experimentation.
