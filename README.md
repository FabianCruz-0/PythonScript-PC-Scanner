# PythonScript-PC-Scanner
Python script wich detect all your installed software on your machine and generate a PDF file with a list of them.

It will also scan your hardware, and will append it in the PDF file.

# Info that will be scaned
- NAME OF PC
- MAC ADDRESS
- IPV4 ADDRESS
- PROCESSOR MODEL
- OPERATING SYSTEM
- RAM MEMORY
- HARD DISK MEMORY
  - Total
  - Used
  - Free
- SOFTWARE INSTALLED


# Requieriments 

Have Python installed (realized with Python 3.9.2).

## Libraries instalation

• In the project folder, open the terminal and run the following commands to install the necessary modules:

- pip install py-cpuinfo
- pip install psutil
- pip install fpdf
- pip install getmac

# Run the script
- Double click on the script to execute it.
- It will open a cmd window and generate a PDF file.
