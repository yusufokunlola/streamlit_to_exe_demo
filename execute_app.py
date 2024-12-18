# Import libraries
import streamlit
import streamlit.web.cli as stcli
import streamlit.runtime.scriptrunner.magic_funcs
import os, sys 

# Check if this script is being run as the main program
if __name__ == "__main__":
    # Change directory to the current script's location
    os.chdir(os.path.dirname(__file__))
    
    
    # Set up command-line arguments for Streamlit
    sys.argv = [
        # Specify Streamlit command to run the app
        "streamlit",
        # Specify the Python file containing the app code
        "run",
        # Specify the app filename
        "streamlit_app.py",
        # Configure server settings
        "--server.port=8080",             # Tweak the port to a choice of yours (8080), default is 8501
        "--server.maxUploadSize=1024",    # Tweak the upload size to a choice of yours (1024MB = 1GB), default is 200MB
        "--global.developmentMode=false",
        # Set theme colors
        "--theme.base=light",
        "--theme.primaryColor=#10475a",
        "--theme.secondaryBackgroundColor=#f2f9f2"
    ]
    
    # Run Streamlit CLI
    stcli.main()