import sys
import tanzil_xml_parser as tp
import morphology as mor

if __name__ == "__main__":
    # Check if arguments were provided
    if len(sys.argv) > 1:
        # Create a dictionary of keyword arguments
        kwargs = {}
        
        if sys.argv[1] == 'mushaf':
            print ("Loading Mushaf Data")
            for arg in sys.argv[2:]:
                key, value = arg.split("=")
                kwargs[key] = value
            tp.process_command(**kwargs)
        elif sys.argv[1] == 'mor':
            for arg in sys.argv[2:]:
                key, value = arg.split("=")
                kwargs[key] = value
            mor.process_command(**kwargs)
        else:
            print ("invalid processor")
        
    else:
        print("No arguments provided.")