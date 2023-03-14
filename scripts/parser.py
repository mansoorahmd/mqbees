import sys
import tanzil_xml_parser as tp


if __name__ == "__main__":
    # Check if arguments were provided
    if len(sys.argv) > 1:
        # Create a dictionary of keyword arguments
        kwargs = {}
        for arg in sys.argv[1:]:
            key, value = arg.split("=")
            kwargs[key] = value
            
        # Process the keyword arguments
        tp.process_command(**kwargs)
    else:
        print("No arguments provided.")